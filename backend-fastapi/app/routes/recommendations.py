from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.database.connection import get_db
from app.models.menu import Menu
from app.services.recommendation_service import (
    get_time_based_category,
    get_popular_keywords
)

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)


@router.get("/time-based")
def time_based_recommendations(db: Session = Depends(get_db)):
    category = get_time_based_category()

    items = db.query(Menu).filter(
        Menu.category == category,
        Menu.is_available == True
    ).all()

    return {
        "recommended_category": category,
        "items": items
    }


@router.get("/popular")
def popular_items(db: Session = Depends(get_db)):
    keywords = get_popular_keywords()

    conditions = []
    for word in keywords:
        conditions.append(Menu.name.ilike(f"%{word}%"))

    items = db.query(Menu).filter(
        or_(*conditions),
        Menu.is_available == True
    ).limit(10).all()

    return items


@router.get("/personalized/{user_id}")
def personalized(user_id: int, db: Session = Depends(get_db)):
    # basic starter logic
    category = get_time_based_category()

    items = db.query(Menu).filter(
        Menu.category == category,
        Menu.is_available == True
    ).limit(5).all()

    return {
        "user_id": user_id,
        "message": "Personalized suggestions",
        "items": items
    }