from fastapi import FastAPI
from app.models.rca import RCA
from app.api.router import api_router
from fastapi.middleware.cors import CORSMiddleware 

from app.db.database import engine
from app.models.incident import Incident
from app.db.database import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Incident Management System",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)

@app.get("/")
def root():
    return {
        "message": "IMS Backend Running 🚀"
    }