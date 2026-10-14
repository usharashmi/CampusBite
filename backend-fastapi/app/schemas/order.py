from pydantic import BaseModel
from typing import List


class OrderItem(BaseModel):
    menu_id: int
    quantity: int


class OrderCreate(BaseModel):
    items: List[OrderItem]
    payment_method: str