# app.py (임시 확인용)
from fastapi import FastAPI
from sqlalchemy import create_engine, text
import os

app = FastAPI()
engine = create_engine(os.getenv("DATABASE_URL"), pool_pre_ping=True)

@app.get("/dbcheck")
def dbcheck():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1")).scalar()
        return {"db_ok": bool(result)}