from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.incident import Incident

router = APIRouter()

@router.get("/incidents")
def get_incidents(
    db: Session = Depends(get_db)
):

    incidents = db.query(Incident).all()

    return incidents