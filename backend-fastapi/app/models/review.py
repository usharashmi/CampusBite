from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.connection import Base


class Review(Base):

    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)

    menu_id = Column(Integer, ForeignKey("menu.id"))

    username = Column(String(100))

    rating = Column(Integer)

    comment = Column(String(500))