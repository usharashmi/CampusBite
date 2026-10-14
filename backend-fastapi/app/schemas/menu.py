from pydantic import BaseModel

class MenuCreate(BaseModel):
    name: str
    category: str
    price: float
    image: str
    is_available: bool = True


class MenuResponse(MenuCreate):
    id: int

    class Config:
        from_attributes = True