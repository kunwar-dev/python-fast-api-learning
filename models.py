from sqlalchemy import Column, String, Float
from database import Base

# This is like a CREATE TABLE in SQL
class Stock(Base):
    __tablename__ = "stocks"

    symbol = Column(String, primary_key=True, index=True)
    company = Column(String, nullable=False)
    price = Column(Float, nullable=False)