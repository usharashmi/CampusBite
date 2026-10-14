from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.connection import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    total_amount = Column(Float)

    payment_method = Column(String(50))

    status = Column(String(50), default="Pending")

    token_number = Column(String(20), unique=True)

    estimated_time = Column(Integer, default=15)

    created_at = Column(DateTime, default=datetime.utcnow)

    items = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete"
    )


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)

    order_id = Column(Integer, ForeignKey("orders.id"))

    menu_id = Column(Integer, ForeignKey("menu.id"))

    quantity = Column(Integer)

    order = relationship(
        "Order",
        back_populates="items"
    )