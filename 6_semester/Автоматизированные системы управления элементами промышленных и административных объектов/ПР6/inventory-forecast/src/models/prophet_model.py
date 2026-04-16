"""Модель прогнозирования на основе Facebook Prophet."""
import pandas as pd
import numpy as np
from prophet import Prophet
from loguru import logger
import joblib
from typing import Optional, Dict, Any, Tuple
from datetime import datetime, timedelta

from src.utils.config import config
from src.features.seasonality import SkiSeasonalityCalculator


class SkiInventoryForecastModel:
    """
    Модель прогнозирования потребности в лыжном инвентаре.

    Использует Prophet с дополнительными настройками для учета:
    - Сезонности лыжного спорта
    - Российских праздников
    - Предстоящих соревнований
    """

    def __init__(self, model_name: str = "ski_forecast"):
        self.model_name = model_name
        self.model: Optional[Prophet] = None
        self.seasonality_calculator = SkiSeasonalityCalculator()
        self.training_metrics: Dict[str, float] = {}

    def _create_model(self) -> Prophet:
        """Создание и настройка модели Prophet."""
        model = Prophet(
            growth='linear',
            seasonality_mode=config.forecast.seasonality_mode,
            yearly_seasonality=config.forecast.yearly_seasonality,
            weekly_seasonality=config.forecast.weekly_seasonality,
            daily_seasonality=config.forecast.daily_seasonality,
            changepoint_prior_scale=config.forecast.changepoint_prior_scale,
            seasonality_prior_scale=config.forecast.seasonality_prior_scale,
            interval_width=0.95  # 95% доверительный интервал
        )

        # Добавление российских праздников
        model.add_country_holidays(country_name='RU')

        # Добавление специфичной сезонности для лыжного спорта
        model.add_seasonality(
            name='winter_season',
            period=365.25,
            fourier_order=5,
            prior_scale=15.0,
            condition_name='is_winter_season'
        )

        model.add_seasonality(
            name='preparation_period',
            period=365.25,
            fourier_order=3,
            prior_scale=10.0,
            condition_name='is_preparation_period'
        )

        return model

    def prepare_data(
            self,
            df: pd.DataFrame,
            include_seasonality_features: bool = True
    ) -> pd.DataFrame:
        """
        Подготовка данных для обучения.

        Args:
            df: DataFrame с колонками ds (дата) и y (значение)
            include_seasonality_features: Добавлять ли признаки сезонности

        Returns:
            Подготовленный DataFrame
        """
        df = df.copy()
        df['ds'] = pd.to_datetime(df['ds'])

        if include_seasonality_features:
            features = self.seasonality_calculator.create_seasonality_features(df['ds'])
            df = pd.concat([df, features], axis=1)

        # Удаление выбросов (метод IQR)
        Q1 = df['y'].quantile(0.25)
        Q3 = df['y'].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df['y'] >= lower_bound) & (df['y'] <= upper_bound)]

        logger.info(f"Данные подготовлены: {len(df)} записей")
        return df

    def fit(self, df: pd.DataFrame, **kwargs) -> 'SkiInventoryForecastModel':
        """
        Обучение модели на исторических данных.

        Args:
            df: DataFrame с колонками ds и y
            **kwargs: Дополнительные параметры для Prophet.fit()

        Returns:
            self
        """
        logger.info(f"Начало обучения модели {self.model_name}")

        df = self.prepare_data(df)

        if len(df) < 30:
            logger.warning(f"Недостаточно данных для обучения: {len(df)} записей")
            # Используем простую скользящую среднюю
            self._create_simple_model(df)
            return self

        self.model = self._create_model()
        self.model.fit(df, **kwargs)

        # Расчет метрик на обучающей выборке
        forecast = self.model.predict(df)
        self._calculate_metrics(df['y'].values, forecast['yhat'].values[:len(df)])

        logger.info(f"Модель обучена. MAE: {self.training_metrics.get('mae', 0):.2f}")
        return self

    def _create_simple_model(self, df: pd.DataFrame):
        """Создание простой модели при недостатке данных."""
        self.model = None
        self._simple_mean = df['y'].mean()
        self._simple_std = df['y'].std()
        logger.info(f"Создана простая модель: mean={self._simple_mean:.2f}, std={self._simple_std:.2f}")

    def predict(self, periods: int = 90) -> pd.DataFrame:
        """
        Прогнозирование на будущие периоды.

        Args:
            periods: Количество дней для прогноза

        Returns:
            DataFrame с прогнозом: ds, yhat, yhat_lower, yhat_upper
        """
        if self.model is None:
            # Используем простую модель
            future_dates = pd.date_range(
                start=datetime.now(),
                periods=periods,
                freq='D'
            )
            return pd.DataFrame({
                'ds': future_dates,
                'yhat': self._simple_mean,
                'yhat_lower': max(0, self._simple_mean - 2 * self._simple_std),
                'yhat_upper': self._simple_mean + 2 * self._simple_std
            })

        future = self.model.make_future_dataframe(periods=periods)

        # Добавление признаков сезонности
        features = self.seasonality_calculator.create_seasonality_features(future['ds'])
        future = pd.concat([future, features], axis=1)

        forecast = self.model.predict(future)

        # Корректировка с учетом сезонности лыжного спорта
        forecast = self.seasonality_calculator.adjust_forecast_by_seasonality(
            forecast, seasonality_multiplier=1.2
        )

        # Отрицательные значения заменяем на 0
        forecast['yhat'] = forecast['yhat'].clip(lower=0)
        forecast['yhat_lower'] = forecast['yhat_lower'].clip(lower=0)
        forecast['yhat_upper'] = forecast['yhat_upper'].clip(lower=0)

        return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

    def predict_demand(
            self,
            periods: int = 90
    ) -> Dict[str, Any]:
        """
        Прогнозирование суммарного спроса на период.

        Returns:
            Словарь с суммарным прогнозом и доверительными интервалами
        """
        forecast = self.predict(periods)

        total_demand = forecast['yhat'].sum()
        total_lower = forecast['yhat_lower'].sum()
        total_upper = forecast['yhat_upper'].sum()

        return {
            'forecast_period_days': periods,
            'total_demand': round(total_demand, 1),
            'confidence_interval': {
                'lower': round(total_lower, 1),
                'upper': round(total_upper, 1)
            },
            'daily_forecast': forecast.to_dict('records')
        }

    def _calculate_metrics(self, y_true: np.ndarray, y_pred: np.ndarray):
        """Расчет метрик качества прогноза."""
        from sklearn.metrics import mean_absolute_error, mean_squared_error

        mae = mean_absolute_error(y_true, y_pred)
        rmse = np.sqrt(mean_squared_error(y_true, y_pred))

        # MAPE (Mean Absolute Percentage Error)
        mape = np.mean(np.abs((y_true - y_pred) / np.where(y_true == 0, 1, y_true))) * 100

        self.training_metrics = {
            'mae': mae,
            'rmse': rmse,
            'mape': mape
        }

    def save(self, path: Optional[str] = None):
        """Сохранение модели."""
        import os
        if path is None:
            path = os.path.join(config.models_dir, f"{self.model_name}.pkl")

        os.makedirs(os.path.dirname(path), exist_ok=True)

        model_data = {
            'model': self.model,
            'model_name': self.model_name,
            'training_metrics': self.training_metrics,
            'config': config.forecast
        }
        joblib.dump(model_data, path)
        logger.info(f"Модель сохранена: {path}")

    @classmethod
    def load(cls, path: str) -> 'SkiInventoryForecastModel':
        """Загрузка модели."""
        model_data = joblib.load(path)

        instance = cls(model_name=model_data['model_name'])
        instance.model = model_data['model']
        instance.training_metrics = model_data['training_metrics']

        logger.info(f"Модель загружена: {path}")
        return instance