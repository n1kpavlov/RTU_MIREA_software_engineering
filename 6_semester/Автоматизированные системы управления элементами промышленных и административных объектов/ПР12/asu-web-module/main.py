from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
from datetime import date, datetime

from database import DatabaseManager
from config import config

app = FastAPI(title="АСУ МТО Web API", version="2.0.0")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

db = DatabaseManager()


# ==================== Pydantic-схемы ====================

class AthleteResponse(BaseModel):
    athlete_id: int
    full_name: str
    sports_category: Optional[str]
    birth_year: Optional[int]
    group_name: Optional[str]
    coach_name: Optional[str]
    has_active_debt: bool

class IssueRequest(BaseModel):
    athlete_id: int
    inventory_item_id: int
    planned_return_date: date

class ReturnRequest(BaseModel):
    issuance_id: int

class MessageResponse(BaseModel):
    status: str
    message: str


# ==================== ДАШБОРД ====================

@app.get("/api/dashboard")
async def get_dashboard():
    """Ключевые метрики, последние выдачи, топ-должники."""
    with db.engine.connect() as conn:
        from sqlalchemy import text

        athletes_count = conn.execute(text("SELECT COUNT(*) FROM athlete")).scalar()
        available_items = conn.execute(text(
            "SELECT COUNT(*) FROM inventory_item WHERE inventory_status = 'AVAILABLE'"
        )).scalar()
        active_issuances = conn.execute(text(
            "SELECT COUNT(*) FROM issuance_document WHERE issuance_document_status IN ('ACTIVE', 'EXTENDED', 'OVERDUE')"
        )).scalar()
        overdue_count = conn.execute(text("""
            SELECT COUNT(*) FROM issuance_document
            WHERE planned_return_date < CURRENT_DATE
            AND issuance_document_status IN ('ACTIVE', 'OVERDUE')
        """)).scalar()
        debtors = conn.execute(text(
            "SELECT COUNT(*) FROM athlete WHERE has_active_debt = TRUE"
        )).scalar()

        categories = conn.execute(text("""
            SELECT n.nomenclature_category, COUNT(*) as cnt
            FROM inventory_item i
            JOIN nomenclature n ON i.inventory_item_nomenclature_id = n.nomenclature_id
            WHERE i.inventory_status = 'AVAILABLE'
            GROUP BY n.nomenclature_category ORDER BY cnt DESC
        """)).fetchall()

        recent_issuances = conn.execute(text("""
            SELECT u.full_name AS athlete_name, n.nomenclature_name AS product_name,
                   d.issuance_date, d.planned_return_date,
                   CASE WHEN d.planned_return_date < CURRENT_DATE THEN 'OVERDUE' ELSE 'ACTIVE' END AS effective_status
            FROM issuance_document d
            JOIN athlete a ON d.issuance_document_athlete_id = a.athlete_id
            JOIN "user" u ON a.athlete_user_id = u.user_id
            JOIN inventory_item i ON d.issuance_document_inventory_item_id = i.inventory_item_id
            JOIN nomenclature n ON i.inventory_item_nomenclature_id = n.nomenclature_id
            WHERE d.issuance_document_status IN ('ACTIVE', 'EXTENDED', 'OVERDUE')
            ORDER BY d.issuance_date DESC LIMIT 5
        """)).fetchall()

        top_debtors = conn.execute(text("""
            SELECT u.full_name AS athlete_name, a.sports_category,
                   COUNT(d.issuance_document_id) AS overdue_items,
                   MAX(CURRENT_DATE - d.planned_return_date) AS max_days
            FROM athlete a
            JOIN "user" u ON a.athlete_user_id = u.user_id
            JOIN issuance_document d ON a.athlete_id = d.issuance_document_athlete_id
            WHERE d.planned_return_date < CURRENT_DATE
              AND d.issuance_document_status IN ('ACTIVE', 'OVERDUE')
            GROUP BY u.full_name, a.sports_category
            ORDER BY overdue_items DESC LIMIT 5
        """)).fetchall()

        return {
            "athletes_count": athletes_count,
            "available_items": available_items,
            "active_issuances": active_issuances,
            "overdue_count": overdue_count,
            "debtors": debtors,
            "categories": [{"category": r[0], "count": r[1]} for r in categories],
            "recent_issuances": [dict(r._mapping) for r in recent_issuances],
            "top_debtors": [dict(r._mapping) for r in top_debtors]
        }


# ==================== СПОРТСМЕНЫ ====================

@app.get("/api/athletes")
async def get_athletes(
    search: str = Query("", description="Поиск по фамилии"),
    has_debt: Optional[str] = Query(None, description="Фильтр по задолженности")
):
    query = """
    SELECT
        a.athlete_id, u.full_name, a.sports_category, a.birth_year,
        g.group_name, cu.full_name AS coach_name, a.has_active_debt,
        (SELECT COUNT(*) FROM issuance_document d
         WHERE d.issuance_document_athlete_id = a.athlete_id
         AND d.issuance_document_status IN ('ACTIVE','EXTENDED','OVERDUE')) AS active_items
    FROM athlete a
    JOIN "user" u ON a.athlete_user_id = u.user_id
    LEFT JOIN "group" g ON a.athlete_group_id = g.group_id
    LEFT JOIN coach c ON a.athlete_coach_id = c.coach_id
    LEFT JOIN "user" cu ON c.coach_user_id = cu.user_id
    WHERE 1=1
    """
    params = {}
    if search:
        query += " AND u.full_name ILIKE :search"
        params["search"] = f"%{search}%"
    if has_debt == "true":
        query += " AND a.has_active_debt = TRUE"
    elif has_debt == "false":
        query += " AND a.has_active_debt = FALSE"
    query += " ORDER BY u.full_name"

    with db.engine.connect() as conn:
        from sqlalchemy import text
        result = conn.execute(text(query), params)
        return [dict(row._mapping) for row in result]


@app.get("/api/athletes/{athlete_id}")
async def get_athlete_detail(athlete_id: int):
    """Детальная информация о спортсмене."""
    query = """
    SELECT
        a.athlete_id, u.full_name, u.email, u.phone,
        a.sports_category, a.birth_year, a.has_active_debt,
        g.group_name, cu.full_name AS coach_name,
        (SELECT COUNT(*) FROM issuance_document d
         WHERE d.issuance_document_athlete_id = a.athlete_id
         AND d.issuance_document_status IN ('ACTIVE','EXTENDED','OVERDUE')) AS active_items,
        (SELECT COUNT(*) FROM issuance_document d
         WHERE d.issuance_document_athlete_id = a.athlete_id
         AND d.issuance_document_status = 'RETURNED') AS returned_items
    FROM athlete a
    JOIN "user" u ON a.athlete_user_id = u.user_id
    LEFT JOIN "group" g ON a.athlete_group_id = g.group_id
    LEFT JOIN coach c ON a.athlete_coach_id = c.coach_id
    LEFT JOIN "user" cu ON c.coach_user_id = cu.user_id
    WHERE a.athlete_id = :athlete_id
    """
    with db.engine.connect() as conn:
        from sqlalchemy import text
        result = conn.execute(text(query), {"athlete_id": athlete_id})
        row = result.fetchone()
        if row:
            return dict(row._mapping)
        raise HTTPException(status_code=404, detail="Спортсмен не найден")


# ==================== ИНВЕНТАРЬ ====================

@app.get("/api/inventory/available")
async def get_available_inventory():
    query = """
    SELECT
        i.inventory_item_id, i.barcode, i.size,
        n.nomenclature_name, n.nomenclature_category
    FROM inventory_item i
    JOIN nomenclature n ON i.inventory_item_nomenclature_id = n.nomenclature_id
    WHERE i.inventory_status = 'AVAILABLE'
    ORDER BY n.nomenclature_name, i.size
    """
    with db.engine.connect() as conn:
        from sqlalchemy import text
        result = conn.execute(text(query))
        return [dict(row._mapping) for row in result]


@app.get("/api/inventory/statistics")
async def get_inventory_statistics():
    query = """
    SELECT
        n.nomenclature_category,
        COUNT(*) FILTER (WHERE i.inventory_status = 'AVAILABLE') AS available,
        COUNT(*) FILTER (WHERE i.inventory_status = 'ISSUED') AS issued,
        COUNT(*) FILTER (WHERE i.inventory_status IN ('DEFECTIVE','UNDER_REPAIR')) AS problems,
        COUNT(*) AS total
    FROM inventory_item i
    JOIN nomenclature n ON i.inventory_item_nomenclature_id = n.nomenclature_id
    GROUP BY n.nomenclature_category ORDER BY total DESC
    """
    with db.engine.connect() as conn:
        from sqlalchemy import text
        result = conn.execute(text(query))
        return [dict(row._mapping) for row in result]


# ==================== ВЫДАЧА ====================

@app.post("/api/issuance/issue", response_model=MessageResponse)
async def issue_inventory(request: IssueRequest):
    try:
        with db.engine.connect() as conn:
            from sqlalchemy import text

            result = conn.execute(
                text("SELECT has_active_debt FROM athlete WHERE athlete_id = :id"),
                {"id": request.athlete_id}
            )
            row = result.fetchone()
            if not row:
                raise HTTPException(status_code=404, detail="Спортсмен не найден")
            if row[0]:
                return MessageResponse(status="error", message="⚠️ Спортсмен имеет задолженность! Выдача невозможна.")

            result = conn.execute(
                text("SELECT inventory_status FROM inventory_item WHERE inventory_item_id = :id"),
                {"id": request.inventory_item_id}
            )
            row = result.fetchone()
            if not row or row[0] != 'AVAILABLE':
                return MessageResponse(status="error", message="⚠️ Инвентарь недоступен для выдачи.")

            result = conn.execute(
                text("""
                    INSERT INTO issuance_document
                    (issuance_document_inventory_item_id, issuance_document_athlete_id,
                     issuance_document_storekeeper_id, issuance_date, planned_return_date,
                     issuance_document_status, condition_on_issue)
                    VALUES (:inv_id, :ath_id, 1, CURRENT_DATE, :ret_date, 'ACTIVE', 'NEW')
                    RETURNING issuance_document_id
                """),
                {"inv_id": request.inventory_item_id, "ath_id": request.athlete_id, "ret_date": request.planned_return_date}
            )
            issuance_id = result.scalar()

            conn.execute(
                text("""
                    UPDATE inventory_item
                    SET inventory_status = 'ISSUED', current_holder_id = :ath_id
                    WHERE inventory_item_id = :inv_id
                """),
                {"ath_id": request.athlete_id, "inv_id": request.inventory_item_id}
            )
            conn.commit()

            return MessageResponse(status="success", message=f"✅ Инвентарь успешно выдан! Документ №{issuance_id}")

    except HTTPException:
        raise
    except Exception as e:
        return MessageResponse(status="error", message=str(e))


# ==================== АКТИВНЫЕ ВЫДАЧИ ====================

@app.get("/api/issuance/active")
async def get_active_issuances(filter_status: str = Query("all")):
    query = """
    SELECT
        d.issuance_document_id, u.full_name AS athlete_name,
        i.barcode, n.nomenclature_name AS product_name,
        i.size, d.issuance_date, d.planned_return_date,
        CASE
            WHEN d.planned_return_date < CURRENT_DATE AND d.issuance_document_status = 'ACTIVE'
            THEN 'OVERDUE'
            ELSE d.issuance_document_status
        END AS effective_status,
        CASE
            WHEN d.planned_return_date < CURRENT_DATE
            THEN (CURRENT_DATE - d.planned_return_date)
            ELSE 0
        END AS days_overdue
    FROM issuance_document d
    JOIN athlete a ON d.issuance_document_athlete_id = a.athlete_id
    JOIN "user" u ON a.athlete_user_id = u.user_id
    JOIN inventory_item i ON d.issuance_document_inventory_item_id = i.inventory_item_id
    JOIN nomenclature n ON i.inventory_item_nomenclature_id = n.nomenclature_id
    WHERE d.issuance_document_status IN ('ACTIVE', 'EXTENDED', 'OVERDUE')
    """
    params = {}
    if filter_status == "overdue":
        query += " AND d.planned_return_date < CURRENT_DATE"
    elif filter_status == "active":
        query += " AND d.planned_return_date >= CURRENT_DATE"
    query += " ORDER BY days_overdue DESC, d.issuance_date DESC"

    with db.engine.connect() as conn:
        from sqlalchemy import text
        result = conn.execute(text(query), params)
        return [dict(row._mapping) for row in result]


# ==================== ВОЗВРАТ ====================

@app.post("/api/issuance/return", response_model=MessageResponse)
async def return_inventory(request: ReturnRequest):
    try:
        with db.engine.connect() as conn:
            from sqlalchemy import text

            result = conn.execute(
                text("""
                    SELECT issuance_document_inventory_item_id, issuance_document_status
                    FROM issuance_document WHERE issuance_document_id = :id
                """),
                {"id": request.issuance_id}
            )
            row = result.fetchone()
            if not row:
                return MessageResponse(status="error", message="Документ выдачи не найден.")
            if row[1] == 'RETURNED':
                return MessageResponse(status="error", message="Инвентарь уже возвращён.")

            conn.execute(
                text("""
                    UPDATE issuance_document
                    SET actual_return_date = CURRENT_DATE,
                        issuance_document_status = 'RETURNED',
                        condition_on_return = 'GOOD'
                    WHERE issuance_document_id = :id
                """),
                {"id": request.issuance_id}
            )

            conn.execute(
                text("""
                    UPDATE inventory_item
                    SET inventory_status = 'AVAILABLE', current_holder_id = NULL
                    WHERE inventory_item_id = :inv_id
                """),
                {"inv_id": row[0]}
            )
            conn.commit()

            return MessageResponse(status="success", message="✅ Инвентарь успешно возвращён!")

    except Exception as e:
        return MessageResponse(status="error", message=str(e))


# ==================== СТАТИКА ====================

app.mount("/", StaticFiles(directory="static", html=True), name="static")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)