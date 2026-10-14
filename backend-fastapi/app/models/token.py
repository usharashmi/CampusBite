from sqlalchemy import Column, Integer, String
from app.database.connection import Base

class Token(Base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True)
    token_number = Column(String(20))