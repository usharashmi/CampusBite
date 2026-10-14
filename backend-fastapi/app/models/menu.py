from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import Boolean
from app.database.connection import Base


class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    category = Column(String(100))
    price = Column(Float)
    image = Column(String(500))
    is_available = Column(Boolean, default=True)