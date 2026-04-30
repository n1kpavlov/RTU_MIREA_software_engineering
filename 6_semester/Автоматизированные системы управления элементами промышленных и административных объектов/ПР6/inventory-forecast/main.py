"""Главный скрипт запуска модуля прогнозирования."""
import os
from datetime import datetime
from loguru import logger

from config import config
from database import DatabaseManager
from forecast_model import SkiInventoryForecastModel


def print_header(title: str):
    """Вывод заголовка раздела."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def main():
    """Основная функция."""
    print_header("МОДУЛЬ ПРОГНОЗИРОВАНИЯ ПОТРЕБНОСТИ В ЛЫЖНОМ ИНВЕНТАРЕ")

    # 1. Подключение к БД
    print_header("1. ПОДКЛЮЧЕНИЕ К БАЗЕ ДАННЫХ")
    db = DatabaseManager()

    # 2. Загрузка списка номенклатуры
    print_header("2. ДОСТУПНАЯ НОМЕНКЛАТУРА")
    nomenclature_df = db.get_all_nomenclature()
    print(nomenclature_df.to_string(index=False))

    # 3. Выбор номенклатуры для прогноза
    print_header("3. ВЫБОР НОМЕНКЛАТУРЫ")
    nomenclature_id = 1
    info = db.get_nomenclature_info(nomenclature_id)
    print(f"Выбрана номенклатура: ID={nomenclature_id}")
    print(f"  Наименование:   {info.get('nomenclature_name', '—')}")
    print(f"  Категория:      {info.get('nomenclature_category', '—')}")
    print(f"  Производитель:  {info.get('manufacturer', '—')}")
    print(f"  Мин. остаток:   {info.get('min_stock_level', '—')} шт.")
    print(f"  Срок службы:    {info.get('standard_service_life', '—')} мес.")

    # 4. Загрузка исторических данных
    print_header("4. ЗАГРУЗКА ИСТОРИЧЕСКИХ ДАННЫХ")
    start_date = '2024-01-01'
    df = db.get_historical_consumption(nomenclature_id, start_date)
    print(f"Загружено {len(df)} записей (с {df['ds'].min().date() if not df.empty else '—'} "
          f"по {df['ds'].max().date() if not df.empty else '—'})")

    if len(df) > 0:
        print("\nПервые 5 записей:")
        print(df.head().to_string(index=False))
        print(f"\nСтатистика: среднее={df['y'].mean():.1f} шт./день, "
              f"максимум={df['y'].max():.0f} шт./день")

    # 5. Обучение модели
    print_header("5. ОБУЧЕНИЕ МОДЕЛИ")
    model = SkiInventoryForecastModel(model_name=f"forecast_nomenclature_{nomenclature_id}")
    model.fit(df)
    print(f"Метрики качества:")
    if model.training_metrics:
        print(f"  MAE  (средняя абсолютная ошибка): {model.training_metrics['mae']} шт.")
        print(f"  MAPE (средняя процентная ошибка): {model.training_metrics['mape']}%")

    # 6. Прогноз
    print_header("6. ПРОГНОЗ НА 90 ДНЕЙ")
    forecast = model.predict(periods=90)

    forecast['month'] = forecast['ds'].apply(lambda x: x.month)
    month_names = {5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь'}
    forecast['month_name'] = forecast['month'].map(month_names)
    monthly = forecast.groupby('month_name')['yhat'].sum().round(1)

    print("\nПрогноз потребности по месяцам:")
    for month, value in monthly.items():
        bar = "█" * max(1, int(value))
        print(f"  {month:10}: {value:6.1f} шт.  {bar}")

    total_demand = forecast['yhat'].sum()
    total_lower = forecast['yhat_lower'].sum()
    total_upper = forecast['yhat_upper'].sum()

    print(f"\nСуммарный прогноз на 90 дней:")
    print(f"  Ожидаемый спрос:     {total_demand:.1f} шт.")
    print(f"  Доверительный интервал: [{total_lower:.1f} — {total_upper:.1f}] шт.")

    # 7. Сравнение с текущим остатком
    print_header("7. РЕКОМЕНДАЦИИ ПО ЗАКУПКЕ")
    current_stock = db.get_current_stock(nomenclature_id)
    min_stock = info.get('min_stock_level', 5)

    print(f"  Текущий остаток:     {current_stock} шт.")
    print(f"  Минимальный запас:   {min_stock} шт.")
    print(f"  Прогноз спроса:      {total_demand:.1f} шт.")

    if current_stock >= total_demand + min_stock:
        print(f"\n  ✓ Запас достаточен. Закупка не требуется.")
    else:
        need = total_demand + min_stock - current_stock
        print(f"\n  ! Рекомендуется закупить: {need:.1f} шт.")

    # 8. Сохранение модели
    print_header("8. СОХРАНЕНИЕ МОДЕЛИ")
    model_path = os.path.join(config.models_dir, f"model_nomenclature_{nomenclature_id}.pkl")
    model.save(model_path)
    print(f"Модель сохранена в: {model_path}")

    print_header("РАБОТА МОДУЛЯ ЗАВЕРШЕНА")


if __name__ == "__main__":
    main()