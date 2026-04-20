"""Модуль для работы с базой данных PostgreSQL (схема asu_inventory)."""
import pandas as pd
from sqlalchemy import create_engine, text
from loguru import logger
from typing import Optional, Dict, Any

from src.utils.config import config


class DatabaseManager:
    """Менеджер для работы с БД АСУ (схема asu_inventory)."""

    def __init__(self):
        # Подключение к БД с указанием схемы по умолчанию
        self.engine = create_engine(
            config.db.connection_string,
            pool_size=5,
            max_overflow=10,
            echo=False,
            connect_args={'options': f'-c search_path={config.db.schema},public'}
        )
        logger.info(f"Подключение к БД: {config.db.host}:{config.db.port}/{config.db.database} (схема: {config.db.schema})")

    def get_historical_consumption(
        self,
        nomenclature_id: int,
        start_date: str,
        end_date: Optional[str] = None
    ) -> pd.DataFrame:
        """
        Загрузка исторических данных по расходу инвентаря.
        """
        query = f"""
        SELECT 
            DATE(d.issuance_date) as ds,
            COUNT(*) as y
        FROM {config.db.schema}.issuance_documents d
        JOIN {config.db.schema}.inventory_items i ON d.inventory_item_id = i.id
        WHERE i.nomenclature_id = :nomenclature_id
            AND d.issuance_date >= :start_date
        """
        params = {"nomenclature_id": nomenclature_id, "start_date": start_date}

        if end_date:
            query += " AND d.issuance_date <= :end_date"
            params["end_date"] = end_date

        query += " GROUP BY DATE(d.issuance_date) ORDER BY ds"

        logger.info(f"Загрузка исторических данных для номенклатуры {nomenclature_id}")

        with self.engine.connect() as conn:
            df = pd.read_sql(text(query), conn, params=params)

        if not df.empty:
            df['ds'] = pd.to_datetime(df['ds'])
            date_range = pd.date_range(start=df['ds'].min(), end=df['ds'].max())
            df = df.set_index('ds').reindex(date_range, fill_value=0).reset_index()
            df.columns = ['ds', 'y']

        logger.info(f"Загружено {len(df)} записей")
        return df

    def get_current_stock(self, nomenclature_id: int) -> int:
        """Получение текущего остатка на складе."""
        query = f"""
        SELECT COUNT(*) as stock
        FROM {config.db.schema}.inventory_items
        WHERE nomenclature_id = :nomenclature_id
            AND status = 'AVAILABLE'
        """
        with self.engine.connect() as conn:
            result = conn.execute(text(query), {"nomenclature_id": nomenclature_id})
            return result.scalar() or 0

    def get_nomenclature_info(self, nomenclature_id: int) -> Dict[str, Any]:
        """Получение информации о номенклатуре."""
        query = f"""
        SELECT 
            id,
            name,
            category,
            min_stock_level,
            standard_service_life,
            manufacturer
        FROM {config.db.schema}.nomenclature
        WHERE id = :nomenclature_id
        """
        with self.engine.connect() as conn:
            result = conn.execute(text(query), {"nomenclature_id": nomenclature_id})
            row = result.fetchone()
            if row:
                return dict(row._mapping)
        return {}

    def get_athletes_count_by_size(self, nomenclature_id: int) -> pd.DataFrame:
        """Получение распределения спортсменов по размерам."""
        query = f"""
        SELECT 
            i.size,
            COUNT(DISTINCT a.id) as athletes_count
        FROM {config.db.schema}.athletes a
        CROSS JOIN {config.db.schema}.nomenclature n
        LEFT JOIN {config.db.schema}.inventory_items i ON i.nomenclature_id = n.id 
            AND i.status = 'ISSUED' 
            AND i.current_holder_id = a.id
        WHERE n.id = :nomenclature_id
        GROUP BY i.size
        """
        with self.engine.connect() as conn:
            return pd.read_sql(text(query), conn, params={"nomenclature_id": nomenclature_id})