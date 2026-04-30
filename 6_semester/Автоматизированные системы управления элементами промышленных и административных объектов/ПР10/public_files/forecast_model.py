"""Модель прогнозирования потребности в лыжном инвентаре (statsmodels)."""
import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from loguru import logger
import joblib
import os
from typing import Optional, Dict, Any
from datetime import datetime, timedelta

from config import config


class SkiInventoryForecastModel:
    """Модель прогнозирования на основе экспоненциального сглаживания."""

    def __init__(self, model_name: str = "ski_forecast"):
        self.model_name = model_name
        self.model = None
        self.training_metrics: Dict[str, float] = {}
        self._simple_mean = None
        self._simple_std = None
        self._seasonal_periods = 7

    def prepare_data(self, df: pd.DataFrame):
        """Подготовка данных."""
        df = df.copy()
        df['ds'] = pd.to_datetime(df['ds'])
        df = df.set_index('ds')
        df = df.asfreq('D', fill_value=0)
        series = df['y'].astype(float)
        logger.info(f"Данные подготовлены: {len(series)} точек")
        return series

    def fit(self, df: pd.DataFrame) -> 'SkiInventoryForecastModel':
        """Обучение модели."""
        logger.info(f"Обучение модели {self.model_name}...")
        series = self.prepare_data(df)

        if len(series) < config.forecast.min_train_days:
            logger.warning(f"Мало данных: {len(series)} точек. Использую среднее.")
            self._simple_mean = series.mean()
            self._simple_std = series.std()
            return self

        # Определяем seasonal_periods на основе длины ряда
        data_len = len(series)
        if data_len < 14:
            self._seasonal_periods = 3
            use_seasonal = False
            use_trend = False
        elif data_len < 30:
            self._seasonal_periods = 5
            use_seasonal = True
            use_trend = False
        elif data_len < 60:
            self._seasonal_periods = 7
            use_seasonal = True
            use_trend = False
        else:
            self._seasonal_periods = 7
            use_seasonal = True
            use_trend = True

        logger.info(f"Параметры: seasonal_periods={self._seasonal_periods}, "
                    f"seasonal={use_seasonal}, trend={use_trend}")

        try:
            if use_seasonal:
                self.model = ExponentialSmoothing(
                    series,
                    seasonal_periods=self._seasonal_periods,
                    trend='add' if use_trend else None,
                    seasonal='add',
                    damped_trend=True,
                    initialization_method='estimated'
                ).fit()
            else:
                self.model = ExponentialSmoothing(
                    series,
                    trend=None,
                    seasonal=None,
                    initialization_method='estimated'
                ).fit()

            fitted = self.model.fittedvalues
            valid_idx = ~np.isnan(fitted)
            if valid_idx.sum() > 0:
                mae = np.mean(np.abs(series[valid_idx] - fitted[valid_idx]))
                mape = np.mean(np.abs((series[valid_idx] - fitted[valid_idx]) /
                                      np.where(series[valid_idx] == 0, 1, series[valid_idx]))) * 100
                self.training_metrics = {'mae': round(mae, 2), 'mape': round(mape, 1)}
                logger.info(f"Модель обучена. MAE={mae:.2f}, MAPE={mape:.1f}%")
        except Exception as e:
            logger.error(f"Ошибка обучения: {e}. Использую среднее.")
            self.model = None
            self._simple_mean = series.mean()
            self._simple_std = series.std()

        return self

    def predict(self, periods: int = None) -> pd.DataFrame:
        """Прогноз."""
        if periods is None:
            periods = config.forecast.forecast_days

        start_date = datetime.now().date()
        dates = [start_date + timedelta(days=i) for i in range(periods)]

        if self.model is not None:
            try:
                forecast_values = self.model.forecast(steps=periods)
                forecast_values = np.maximum(forecast_values, 0)

                # Ограничиваем рост: не больше максимума из исторических данных
                max_historical = self._simple_mean * 3 if self._simple_mean else 5
                forecast_values = np.minimum(forecast_values, max_historical)

                return pd.DataFrame({
                    'ds': dates,
                    'yhat': forecast_values,
                    'yhat_lower': np.maximum(forecast_values * 0.6, 0),
                    'yhat_upper': np.minimum(forecast_values * 1.5, max_historical * 1.5)
                })
            except Exception as e:
                logger.error(f"Ошибка прогноза: {e}")

        # Запасной вариант: простое среднее
        mean_val = self._simple_mean or 0
        std_val = self._simple_std or 0
        values = np.full(periods, mean_val)
        return pd.DataFrame({
            'ds': dates,
            'yhat': values,
            'yhat_lower': np.maximum(values - 2 * std_val, 0),
            'yhat_upper': values + 2 * std_val
        })

    def save(self, path: Optional[str] = None):
        if path is None:
            path = os.path.join(config.models_dir, f"{self.model_name}.pkl")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        joblib.dump({
            'model': self.model,
            'model_name': self.model_name,
            'training_metrics': self.training_metrics,
            '_simple_mean': self._simple_mean,
            '_simple_std': self._simple_std,
            '_seasonal_periods': self._seasonal_periods
        }, path)
        logger.info(f"Модель сохранена: {path}")

    @classmethod
    def load(cls, path: str) -> 'SkiInventoryForecastModel':
        data = joblib.load(path)
        instance = cls(model_name=data['model_name'])
        instance.model = data['model']
        instance.training_metrics = data['training_metrics']
        instance._simple_mean = data.get('_simple_mean')
        instance._simple_std = data.get('_simple_std')
        instance._seasonal_periods = data.get('_seasonal_periods', 7)
        logger.info(f"Модель загружена: {path}")
        return instance