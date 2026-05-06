from fastapi import APIRouter

from app.models.signal import Signal

router = APIRouter()

@router.post("/ingest")
def ingest_signal(signal: Signal):

    print("Received Signal:")
    print(signal)

    return {
        "message": "Signal received successfully",
        "data": signal
    }