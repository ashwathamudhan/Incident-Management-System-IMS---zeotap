from pydantic import BaseModel, StrictStr
from datetime import datetime

class Signal(BaseModel):
    component_id: StrictStr
    severity: StrictStr
    message: StrictStr
    timestamp: datetime = datetime.utcnow()