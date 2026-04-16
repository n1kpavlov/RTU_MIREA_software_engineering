"""Конфигурация модуля прогнозирования."""
import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class DatabaseConfig:
    """Настройки подключения к PostgreSQL."""
    host: str = os.getenv("DB_HOST", "localhost")
    port: int = int(os.getenv("DB_PORT", "5432"))
    database: str = os.getenv("DB_NAME", "asu_inventory")
    username: str = os.getenv("DB_USERNAME", "asu_user")
    password: str = os.getenv("DB_PASSWORD", "secure_password")

    @property
    def connection_string(self) -> str:
        return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"


@dataclass
class ForecastConfig:
    """Настройки модели прогнозирования."""
    forecast_horizon_days: int = 90  # Прогноз на 3 месяца
    seasonality_mode: str = "multiplicative"  # Мультипликативная сезонность для спорта
    yearly_seasonality: bool = True
    weekly_seasonality: bool = True
    daily_seasonality: bool = False
    changepoint_prior_scale: float = 0.05  # Гибкость тренда
    seasonality_prior_scale: float = 10.0  # Сила сезонности

    # Специфичные для лыжного спорта
    ski_wear_factor_enabled: bool = True  # Учет износа лыж
    min_stock_days: int = 14  # Минимальный страховой запас в днях


@dataclass
class AppConfig:
    """Общая конфигурация приложения."""
    db: DatabaseConfig = DatabaseConfig()
    forecast: ForecastConfig = ForecastConfig()
    models_dir: str = os.getenv("MODELS_DIR", "./models")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")


config = AppConfig()