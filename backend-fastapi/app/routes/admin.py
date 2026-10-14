from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, date

from app.database.connection import get_db
from app.models.order import Order
from app.models.user_model import User
from app.models.menu import Menu
from app.models.payment import Payment

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    total_users = db.query(User).count()
    total_orders = db.query(Order).count()
    total_menu_items = db.query(Menu).count()

    paid_orders = db.query(Order).filter(
        Order.payment_status == "paid"
    ).all()

    total_revenue = sum(order.total_amount for order in paid_orders)

    pending_orders = db.query(Order).filter(
        Order.status.in_(["pending", "accepted", "preparing"])
    ).count()

    return {
        "total_users": total_users,
        "total_orders": total_orders,
        "total_menu_items": total_menu_items,
        "pending_orders": pending_orders,
        "total_revenue": total_revenue
    }


@router.get("/orders")
def all_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).order_by(Order.created_at.desc()).all()
    return orders


@router.put("/orders/{order_id}/{status}")
def update_order(order_id: int, status: str, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.status = status
    db.commit()

    return {"message": "Order status updated"}


@router.get("/users")
def all_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.put("/users/deactivate/{user_id}")
def deactivate_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.is_active = False
    db.commit()

    return {"message": "User deactivated"}


@router.get("/reports/daily-sales")
def daily_sales(db: Session = Depends(get_db)):
    today = date.today()

    orders = db.query(Order).filter(
        func.date(Order.created_at) == today,
        Order.payment_status == "paid"
    ).all()

    total_sales = sum(order.total_amount for order in orders)

    return {
        "date": str(today),
        "total_orders": len(orders),
        "total_sales": total_sales
    }