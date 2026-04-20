"""Расчет сезонных коэффициентов для лыжного спорта."""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
from loguru import logger


class SkiSeasonalityCalculator:
    """
    Калькулятор сезонности для лыжного спорта.

    Учитывает:
    - Подготовительный период (август-октябрь): закупка инвентаря
    - Соревновательный сезон (ноябрь-март): пиковое использование
    - Межсезонье (апрель-июль): обслуживание и ремонт
    """

    MONTHLY_FACTORS = {
        1: 1.2,   # Январь - пик сезона
        2: 1.3,   # Февраль - пик сезона
        3: 1.1,   # Март - завершение сезона
        4: 0.4,   # Апрель - межсезонье
        5: 0.2,   # Май - межсезонье
        6: 0.1,   # Июнь - минимум
        7: 0.1,   # Июль - минимум
        8: 0.5,   # Август - начало подготовки
        9: 0.8,   # Сентябрь - активная подготовка
        10: 1.0,  # Октябрь - предсезонные сборы
        11: 1.1,  # Ноябрь - начало соревнований
        12: 1.2   # Декабрь - разгар сезона
    }

    @classmethod
    def get_monthly_factor(cls, month: int) -> float:
        return cls.MONTHLY_FACTORS.get(month, 1.0)

    @classmethod
    def create_seasonality_features(cls, dates: pd.DatetimeIndex) -> pd.DataFrame:
        df = pd.DataFrame(index=dates)
        df['month'] = dates.month
        df['month_factor'] = df['month'].map(cls.MONTHLY_FACTORS)
        df['is_winter_season'] = df['month'].isin([11, 12, 1, 2, 3]).astype(int)
        df['is_preparation_period'] = df['month'].isin([8, 9, 10]).astype(int)
        df['is_off_season'] = df['month'].isin([4, 5, 6, 7]).astype(int)
        df['day_of_week'] = dates.dayofweek
        df['is_weekend'] = (df['day_of_week'] >= 5).astype(int)
        return df

    @classmethod
    def adjust_forecast_by_seasonality(
        cls,
        forecast: pd.DataFrame,
        seasonality_multiplier: float = 1.0
    ) -> pd.DataFrame:
        forecast = forecast.copy()
        forecast['month'] = pd.to_datetime(forecast['ds']).dt.month
        forecast['seasonality_factor'] = forecast['month'].map(cls.MONTHLY_FACTORS)
        mean_factor = np.mean(list(cls.MONTHLY_FACTORS.values()))
        forecast['seasonality_factor'] = forecast['seasonality_factor'] / mean_factor

        forecast['yhat'] = forecast['yhat'] * (1 + (forecast['seasonality_factor'] - 1) * seasonality_multiplier)
        forecast['yhat_lower'] = forecast['yhat_lower'] * (1 + (forecast['seasonality_factor'] - 1) * seasonality_multiplier)
        forecast['yhat_upper'] = forecast['yhat_upper'] * (1 + (forecast['seasonality_factor'] - 1) * seasonality_multiplier)

        return forecast