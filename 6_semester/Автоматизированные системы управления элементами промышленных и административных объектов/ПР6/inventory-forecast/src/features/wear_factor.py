"""Расчет коэффициента износа лыжного инвентаря."""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, Optional
from loguru import logger
from sqlalchemy import text


class SkiWearCalculator:
    """
    Калькулятор износа лыжного инвентаря.

    Учитывает:
    - Нормативный срок службы (из карточки номенклатуры)
    - Интенсивность использования (количество выдач)
    - Сезонность использования
    - Плановую замену инвентаря
    """

    def __init__(self, db_manager):
        self.db_manager = db_manager

    def calculate_wear_rate(
            self,
            nomenclature_id: int,
            forecast_horizon_days: int
    ) -> float:
        """
        Расчет ожидаемого процента износа за период прогноза.

        Returns:
            Коэффициент износа (0-1) - доля инвентаря, требующая замены
        """
        info = self.db_manager.get_nomenclature_info(nomenclature_id)
        if not info:
            logger.warning(f"Номенклатура {nomenclature_id} не найдена")
            return 0.05  # Значение по умолчанию 5% в квартал

        standard_life_months = info.get('standard_service_life_months', 24)

        # Запрос среднего возраста инвентаря
        query = """
        SELECT 
            AVG(EXTRACT(DAY FROM NOW() - commissioning_date)) / 30.0 as avg_age_months,
            COUNT(*) as total_items,
            COUNT(CASE 
                WHEN EXTRACT(MONTH FROM AGE(NOW(), commissioning_date)) > :standard_life_months 
                THEN 1 
            END) as expired_items
        FROM inventory_items
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

                # Прогнозируемый износ за период
                forecast_months = forecast_horizon_days / 30.0
                forecast_wear = (avg_age_months + forecast_months) / standard_life_months
                forecast_wear = np.clip(forecast_wear, 0.05, 0.5)  # Минимум 5%, максимум 50%

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
        """
        Расчет полной потребности в закупке с учетом износа.

        Returns:
            Словарь с компонентами потребности:
            - base_demand: базовый спрос
            - wear_replacement: замена изношенного инвентаря
            - safety_stock: страховой запас
            - total_need: итоговая потребность
        """
        current_stock = self.db_manager.get_current_stock(nomenclature_id)
        wear_rate = self.calculate_wear_rate(nomenclature_id, forecast_horizon_days)

        # Оценка общего количества инвентаря в обращении
        query = """
        SELECT COUNT(*) as total_active
        FROM inventory_items
        WHERE nomenclature_id = :nomenclature_id
            AND status IN ('AVAILABLE', 'ISSUED', 'RESERVED')
        """
        with self.db_manager.engine.connect() as conn:
            result = conn.execute(text(query), {"nomenclature_id": nomenclature_id})
            total_active = result.scalar() or 0

        # Расчет компонентов
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