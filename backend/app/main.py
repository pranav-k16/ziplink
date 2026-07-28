from fastapi import FastAPI

app = FastAPI(
    title="ZipLink API",
    version="1.0.0"
)


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