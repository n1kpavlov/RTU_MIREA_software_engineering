"""Модуль для работы с базой данных PostgreSQL."""
import pandas as pd
from sqlalchemy import create_engine, text
from loguru import logger
from typing import Optional, Dict, Any

from config import config


class DatabaseManager:
    """Менеджер для работы с БД АСУ."""

    def __init__(self):
        self.engine = create_engine(
            config.db.connection_string,
            connect_args={'options': f'-c search_path={config.db.schema},public'}
        )
        logger.info(f"Подключение к БД: {config.db.host}:{config.db.port}/{config.db.database}")
        logger.info(f"Схема: {config.db.schema}")

    def get_historical_consumption(self, nomenclature_id: int, start_date: str, end_date: Optional[str] = None) -> pd.DataFrame:
        """Загрузка исторических данных по расходу инвентаря."""
        query = f"""
        SELECT 
            DATE(d.issuance_date) as ds,
            COUNT(*) as y
        FROM issuance_document d
        JOIN inventory_item i ON d.issuance_document_inventory_item_id = i.inventory_item_id
        WHERE i.inventory_item_nomenclature_id = :nomenclature_id
            AND d.issuance_date >= :start_date
        """
        params = {"nomenclature_id": nomenclature_id, "start_date": start_date}

        if end_date:
            query += " AND d.issuance_date <= :end_date"
            params["end_date"] = end_date

        query += " GROUP BY DATE(d.issuance_date) ORDER BY ds"

        logger.info(f"Загрузка данных для номенклатуры ID={nomenclature_id}")

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
        FROM inventory_item
        WHERE inventory_item_nomenclature_id = :nomenclature_id
            AND inventory_status = 'AVAILABLE'
        """
        with self.engine.connect() as conn:
            result = conn.execute(text(query), {"nomenclature_id": nomenclature_id})
            return result.scalar() or 0

    def get_nomenclature_info(self, nomenclature_id: int) -> Dict[str, Any]:
        """Получение информации о номенклатуре."""
        query = f"""
        SELECT 
            nomenclature_id,
            nomenclature_name,
            nomenclature_category,
            min_stock_level,
            standard_service_life,
            manufacturer
        FROM nomenclature
        WHERE nomenclature_id = :nomenclature_id
        """
        with self.engine.connect() as conn:
            result = conn.execute(text(query), {"nomenclature_id": nomenclature_id})
            row = result.fetchone()
            if row:
                return dict(row._mapping)
        return {}

    def get_all_nomenclature(self) -> pd.DataFrame:
        """Получение списка всей номенклатуры."""
        query = f"""
        SELECT 
            nomenclature_id,
            nomenclature_name,
            nomenclature_category,
            min_stock_level,
            manufacturer
        FROM nomenclature
        ORDER BY nomenclature_id
        """
        with self.engine.connect() as conn:
            return pd.read_sql(text(query), conn)