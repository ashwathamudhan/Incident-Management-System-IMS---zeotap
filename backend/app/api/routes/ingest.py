from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.signal import Signal
from app.models.incident import Incident

from app.db.database import get_db

router = APIRouter()

@router.post("/ingest")
def ingest_signal(
    signal: Signal,
    db: Session = Depends(get_db)
):

    new_incident = Incident(
        component_id=signal.component_id,
        severity=signal.severity,
        message=signal.message
    )

    db.add(new_incident)

    db.commit()

    db.refresh(new_incident)

    return {
        "message": "Incident created successfully",
        "incident_id": new_incident.id,
        "status": new_incident.status
    }