from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def read_root():
    return {"message":"Hello from my first FASTAPI"}

@app.get("/stocks/{symbol}") 

def getStocks(symbol:str):
    return {"symbol":symbol,"price":"fetch coming soon"}