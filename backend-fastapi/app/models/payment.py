from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from app.database.connection import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)

    order_id = Column(Integer, ForeignKey("orders.id"))

    amount = Column(Float, nullable=False)

    payment_method = Column(String(30))   # upi / cash

    transaction_id = Column(String(120), nullable=True)

    status = Column(String(30), default="pending")
    # pending / paid / failed

    created_at = Column(DateTime, default=datetime.utcnow)