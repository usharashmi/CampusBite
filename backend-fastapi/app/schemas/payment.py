from pydantic import BaseModel


class PaymentCreate(BaseModel):
    order_id: int
    amount: float
    payment_method: str