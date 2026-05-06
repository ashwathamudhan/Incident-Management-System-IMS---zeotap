from fastapi import APIRouter, Depends
from datetime import datetime
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.incident import Incident
from app.models.status import StatusUpdate

from app.models.rca import RCA
from app.models.rca_request import RCARequest

router = APIRouter()


# =========================
# GET ALL INCIDENTS
# =========================
@router.get("/incidents")
def get_incidents(
    db: Session = Depends(get_db)
):

    incidents = db.query(Incident).all()

    return incidents


# =========================
# UPDATE INCIDENT STATUS
# =========================
@router.put("/incidents/{incident_id}/status")
def update_incident_status(
    incident_id: int,
    status_update: StatusUpdate,
    db: Session = Depends(get_db)
):

    incident = db.query(Incident).filter(
        Incident.id == incident_id
    ).first()

    if not incident:
        return {
            "error": "Incident not found"
        }

    # RCA validation before closing
    if status_update.status == "CLOSED":

        existing_rca = db.query(RCA).filter(
            RCA.incident_id == incident_id
        ).first()

        if not existing_rca:
            return {
                "error": "Cannot close incident without RCA"
            }

    incident.status = status_update.status

    if status_update.status == "CLOSED":

        incident.resolved_at = datetime.utcnow()

        mttr = incident.resolved_at - incident.created_at

        incident.mttr_minutes = int(
        mttr.total_seconds() / 60
    )

    db.commit()

    db.refresh(incident)

    return {
        "message": "Incident status updated",
        "incident_id": incident.id,
        "new_status": incident.status
    }


# =========================
# CREATE RCA
# =========================
@router.post("/incidents/{incident_id}/rca")
def create_rca(
    incident_id: int,
    rca_data: RCARequest,
    db: Session = Depends(get_db)
):

    incident = db.query(Incident).filter(
        Incident.id == incident_id
    ).first()

    if not incident:
        return {
            "error": "Incident not found"
        }

    new_rca = RCA(
        incident_id=incident_id,
        root_cause=rca_data.root_cause,
        fix_applied=rca_data.fix_applied,
        prevention_steps=rca_data.prevention_steps
    )

    db.add(new_rca)

    db.commit()

    return {
        "message": "RCA added successfully"
    }