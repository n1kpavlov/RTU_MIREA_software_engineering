"""Конфигурация модуля прогнозирования."""
import os
from dataclasses import dataclass, field


@dataclass
class DatabaseConfig:
    """Настройки подключения к PostgreSQL."""
    host: str = field(default_factory=lambda: os.getenv("DB_HOST", "localhost"))
    port: int = field(default_factory=lambda: int(os.getenv("DB_PORT", "5432")))
    database: str = field(default_factory=lambda: os.getenv("DB_NAME", "postgres"))
    schema: str = field(default_factory=lambda: os.getenv("DB_SCHEMA", "asu_inventory"))
    username: str = field(default_factory=lambda: os.getenv("DB_USERNAME", "postgres"))
    password: str = field(default_factory=lambda: os.getenv("DB_PASSWORD", "CKu9LmMo"))

    @property
    def connection_string(self) -> str:
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"


@dataclass
class ForecastConfig:
    """Настройки модели прогнозирования."""
    forecast_days: int = 90
    seasonality_mode: str = "multiplicative"
    yearly_seasonality: bool = True
    weekly_seasonality: bool = True
    min_train_days: int = 30


@dataclass
class AppConfig:
    """Общая конфигурация приложения."""
    db: DatabaseConfig = field(default_factory=DatabaseConfig)
    forecast: ForecastConfig = field(default_factory=ForecastConfig)
    models_dir: str = field(default_factory=lambda: os.getenv("MODELS_DIR", "./models"))


config = AppConfig()