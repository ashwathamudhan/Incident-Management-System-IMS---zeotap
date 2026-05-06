from fastapi import FastAPI

from app.api.router import api_router

from app.db.database import engine
from app.models.incident import Incident
from app.db.database import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Incident Management System",
    version="1.0.0"
)

app.include_router(api_router)

@app.get("/")
def root():
    return {
        "message": "IMS Backend Running 🚀"
    }