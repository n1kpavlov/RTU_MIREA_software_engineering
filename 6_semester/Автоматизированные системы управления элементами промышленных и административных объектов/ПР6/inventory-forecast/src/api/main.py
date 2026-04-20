"""REST API для модуля прогнозирования (без events)."""
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime, timedelta
from loguru import logger
import uvicorn

from src.data.database import DatabaseManager
from src.models.prophet_model import SkiInventoryForecastModel
from src.features.wear_factor import SkiWearCalculator
from src.utils.config import config


# Pydantic схемы
class ForecastRequest(BaseModel):
    nomenclature_id: int = Field(..., description="ID номенклатуры")
    forecast_days: int = Field(90, ge=7, le=365, description="Горизонт прогноза в днях")
    include_wear: bool = Field(True, description="Учитывать износ инвентаря")

    class Config:
        json_schema_extra = {
            "example": {
                "nomenclature_id": 1,  # ID из таблицы nomenclature (SKI-001)
                "forecast_days": 90,
                "include_wear": True
            }
        }


class ForecastResponse(BaseModel):
    nomenclature_id: int
    nomenclature_name: str
    forecast_period_days: int
    forecast_start_date: str
    forecast_end_date: str
    base_demand: float
    wear_replacement: float
    safety_stock: float
    current_stock: int
    total_need: float
    recommended_order: float
    confidence_interval: Dict[str, float]
    daily_forecast: List[Dict[str, Any]]
    model_metrics: Dict[str, float]
    created_at: str


class ModelInfoResponse(BaseModel):
    model_name: str
    is_trained: bool
    training_metrics: Dict[str, float]
    last_trained: Optional[str]


class TrainRequest(BaseModel):
    nomenclature_id: int = Field(..., description="ID номенклатуры")
    historical_days: int = Field(365, ge=90, le=1095, description="Дней истории для обучения")


# Создание приложения
app = FastAPI(
    title="ASU Ski Inventory Forecast API",
    description="API для прогнозирования потребности в лыжном инвентаре",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db_manager = DatabaseManager()
wear_calculator = SkiWearCalculator(db_manager)
models_cache: Dict[int, SkiInventoryForecastModel] = {}


def get_or_train_model(nomenclature_id: int, force_retrain: bool = False) -> SkiInventoryForecastModel:
    import os
    model_path = os.path.join(config.models_dir, f"model_{nomenclature_id}.pkl")

    if not force_retrain and os.path.exists(model_path):
        return SkiInventoryForecastModel.load(model_path)

    start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
    df = db_manager.get_historical_consumption(nomenclature_id, start_date)

    if df.empty:
        raise HTTPException(status_code=404, detail=f"Нет исторических данных для номенклатуры {nomenclature_id}")

    model = SkiInventoryForecastModel(model_name=f"ski_forecast_{nomenclature_id}")
    model.fit(df)
    model.save(model_path)

    models_cache[nomenclature_id] = model
    return model


@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}


@app.post("/forecast", response_model=ForecastResponse)
async def create_forecast(request: ForecastRequest):
    logger.info(f"Запрос прогноза: nomenclature_id={request.nomenclature_id}, days={request.forecast_days}")

    try:
        info = db_manager.get_nomenclature_info(request.nomenclature_id)
        if not info:
            raise HTTPException(status_code=404, detail=f"Номенклатура {request.nomenclature_id} не найдена")

        model = get_or_train_model(request.nomenclature_id)
        demand_forecast = model.predict_demand(periods=request.forecast_days)
        base_demand = demand_forecast['total_demand']

        if request.include_wear:
            replacement_need = wear_calculator.calculate_replacement_need(
                request.nomenclature_id,
                base_demand,
                request.forecast_days
            )
        else:
            current_stock = db_manager.get_current_stock(request.nomenclature_id)
            replacement_need = {
                'base_demand': base_demand,
                'wear_replacement': 0,
                'safety_stock': max(0, info.get('min_stock_level', 5) - current_stock),
                'current_stock': current_stock,
                'total_active': 0,
                'wear_rate': 0,
                'total_need': base_demand + max(0, info.get('min_stock_level', 5) - current_stock)
            }

        recommended_order = max(0, replacement_need['total_need'] - replacement_need['current_stock'])

        start_date = datetime.now().date()
        end_date = start_date + timedelta(days=request.forecast_days)

        return ForecastResponse(
            nomenclature_id=request.nomenclature_id,
            nomenclature_name=info.get('name', 'Unknown'),
            forecast_period_days=request.forecast_days,
            forecast_start_date=start_date.isoformat(),
            forecast_end_date=end_date.isoformat(),
            base_demand=round(replacement_need['base_demand'], 1),
            wear_replacement=round(replacement_need['wear_replacement'], 1),
            safety_stock=round(replacement_need['safety_stock'], 1),
            current_stock=replacement_need['current_stock'],
            total_need=round(replacement_need['total_need'], 1),
            recommended_order=round(recommended_order, 1),
            confidence_interval=demand_forecast['confidence_interval'],
            daily_forecast=demand_forecast['daily_forecast'][-request.forecast_days:],
            model_metrics=model.training_metrics,
            created_at=datetime.now().isoformat()
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Ошибка при создании прогноза: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/train", response_model=ModelInfoResponse)
async def train_model(request: TrainRequest):
    logger.info(f"Запрос обучения модели: nomenclature_id={request.nomenclature_id}")

    try:
        start_date = (datetime.now() - timedelta(days=request.historical_days)).strftime('%Y-%m-%d')
        df = db_manager.get_historical_consumption(request.nomenclature_id, start_date)

        if df.empty:
            raise HTTPException(status_code=404, detail="Нет данных для обучения")

        model = SkiInventoryForecastModel(model_name=f"ski_forecast_{request.nomenclature_id}")
        model.fit(df)

        import os
        model_path = os.path.join(config.models_dir, f"model_{request.nomenclature_id}.pkl")
        model.save(model_path)
        models_cache[request.nomenclature_id] = model

        return ModelInfoResponse(
            model_name=model.model_name,
            is_trained=True,
            training_metrics=model.training_metrics,
            last_trained=datetime.now().isoformat()
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Ошибка при обучении модели: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/model/{nomenclature_id}", response_model=ModelInfoResponse)
async def get_model_info(nomenclature_id: int):
    import os
    model_path = os.path.join(config.models_dir, f"model_{nomenclature_id}.pkl")

    if os.path.exists(model_path):
        try:
            model = SkiInventoryForecastModel.load(model_path)
            mtime = os.path.getmtime(model_path)
            last_trained = datetime.fromtimestamp(mtime).isoformat()

            return ModelInfoResponse(
                model_name=model.model_name,
                is_trained=True,
                training_metrics=model.training_metrics,
                last_trained=last_trained
            )
        except Exception as e:
            logger.error(f"Ошибка загрузки модели: {e}")

    return ModelInfoResponse(
        model_name=f"ski_forecast_{nomenclature_id}",
        is_trained=False,
        training_metrics={},
        last_trained=None
    )


@app.get("/nomenclature/{nomenclature_id}/history")
async def get_historical_data(
    nomenclature_id: int,
    days: int = Query(365, ge=30, le=1095)
):
    start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
    df = db_manager.get_historical_consumption(nomenclature_id, start_date)

    return {
        "nomenclature_id": nomenclature_id,
        "days": days,
        "data": df.to_dict('records') if not df.empty else []
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level=config.log_level.lower()
    )