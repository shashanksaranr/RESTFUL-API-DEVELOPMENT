# models.py (SQLAlchemy Model)
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class Item(Base):  # This is your database table model
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float)
    quantity = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
