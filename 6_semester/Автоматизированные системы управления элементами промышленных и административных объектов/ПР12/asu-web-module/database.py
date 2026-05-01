from sqlalchemy import create_engine
from loguru import logger
from config import config


class DatabaseManager:
    def __init__(self):
        self.engine = create_engine(
            config.db.connection_string,
            pool_size=5,
            max_overflow=10,
            echo=False,
            connect_args={'options': f'-c search_path={config.db.schema},public'}
        )
        logger.info(f"Подключение к БД: {config.db.host}:{config.db.port}/{config.db.database}")