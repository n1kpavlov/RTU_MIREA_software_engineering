"""Расчет коэффициента износа лыжного инвентаря."""
import pandas as pd
import numpy as np
from typing import Dict
from loguru import logger
from sqlalchemy import text

from src.utils.config import config


class SkiWearCalculator:
    """Калькулятор износа лыжного инвентаря."""

    def __init__(self, db_manager):
        self.db_manager = db_manager

    def calculate_wear_rate(
        self,
        nomenclature_id: int,
        forecast_horizon_days: int
    ) -> float:
        """Расчет ожидаемого процента износа за период прогноза."""
        info = self.db_manager.get_nomenclature_info(nomenclature_id)
        if not info:
            logger.warning(f"Номенклатура {nomenclature_id} не найдена")
            return 0.05

        standard_life_months = info.get('standard_service_life', 24)

        query = f"""
        SELECT 
            AVG(EXTRACT(DAY FROM NOW() - receipt_date)) / 30.0 as avg_age_months,
            COUNT(*) as total_items,
            COUNT(CASE 
                WHEN EXTRACT(MONTH FROM AGE(NOW(), receipt_date)) > :standard_life_months 
                THEN 1 
            END) as expired_items
        FROM {config.db.schema}.inventory_items
        WHERE nomenclature_id = :nomenclature_id
            AND status NOT IN ('WRITTEN_OFF', 'DEFECTIVE')
        """

        with self.db_manager.engine.connect() as conn:
            result = conn.execute(
                text(query),
                {"nomenclature_id": nomenclature_id, "standard_life_months": standard_life_months}
            )
            row = result.fetchone()

            if row and row.total_items > 0:
                avg_age_months = row.avg_age_months or 0
                expired_ratio = row.expired_items / row.total_items
                forecast_months = forecast_horizon_days / 30.0
                forecast_wear = (avg_age_months + forecast_months) / standard_life_months
                forecast_wear = np.clip(forecast_wear, 0.05, 0.5)

                logger.info(f"Средний возраст: {avg_age_months:.1f} мес, "
                          f"просрочено: {expired_ratio:.1%}, "
                          f"прогноз износа: {forecast_wear:.1%}")

                return max(forecast_wear, expired_ratio)

        return 0.05

    def calculate_replacement_need(
        self,
        nomenclature_id: int,
        forecasted_demand: float,
        forecast_horizon_days: int
    ) -> Dict[str, float]:
        """Расчет полной потребности в закупке с учетом износа."""
        current_stock = self.db_manager.get_current_stock(nomenclature_id)
        wear_rate = self.calculate_wear_rate(nomenclature_id, forecast_horizon_days)

        query = f"""
        SELECT COUNT(*) as total_active
        FROM {config.db.schema}.inventory_items
        WHERE nomenclature_id = :nomenclature_id
            AND status IN ('AVAILABLE', 'ISSUED', 'RESERVED')
        """
        with self.db_manager.engine.connect() as conn:
            result = conn.execute(text(query), {"nomenclature_id": nomenclature_id})
            total_active = result.scalar() or 0

        base_demand = forecasted_demand
        wear_replacement = total_active * wear_rate

        info = self.db_manager.get_nomenclature_info(nomenclature_id)
        min_stock_level = info.get('min_stock_level', 5)
        safety_stock = max(min_stock_level - current_stock, 0)

        total_need = base_demand + wear_replacement + safety_stock
        total_need = max(total_need, 0)

        return {
            'base_demand': round(base_demand, 1),
            'wear_replacement': round(wear_replacement, 1),
            'safety_stock': round(safety_stock, 1),
            'current_stock': current_stock,
            'total_active': total_active,
            'wear_rate': round(wear_rate, 3),
            'total_need': round(total_need, 1)
        }