from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connection string — like a connection handle in Pro*C
DATABASE_URL = "postgresql://fastapi_user:password123@localhost/fastapi_stocks"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency — gives us a DB session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()