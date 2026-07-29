from fastapi import FastAPI

from app.database.database import engine
from app.database.base import Base
from app.models.url import URL


app = FastAPI(
    title="ZipLink API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "message": "Welcome to ZipLink 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }