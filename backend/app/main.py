from fastapi import FastAPI

from app.database.database import engine
from app.database.base import Base
from app.models.url import URL
from app.api.urls import router as url_router




app = FastAPI(
    title="ZipLink API",
    version="1.0.0"
)

app.include_router(url_router)

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