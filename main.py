from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db, engine
from models import Stock, Base
from pydantic import BaseModel

Base.metadata.create_all(bind=engine)

app = FastAPI()

class StockCreate(BaseModel):
    symbol: str
    company: str
    price: float

@app.get("/stocks")
def get_all_stocks(db: Session = Depends(get_db)):
    return db.query(Stock).all()

@app.get("/stocks/{symbol}")
def get_stock(symbol: str, db: Session = Depends(get_db)):
    stock = db.query(Stock).filter(Stock.symbol == symbol).first()
    return stock

@app.post("/stocks")
def add_stock(stock: StockCreate, db: Session = Depends(get_db)):
    db_stock = Stock(symbol=stock.symbol, company=stock.company, price=stock.price)
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return {"message": "Stock saved to database!", "stock": db_stock}