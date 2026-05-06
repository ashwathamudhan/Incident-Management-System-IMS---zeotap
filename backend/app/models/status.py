from pydantic import BaseModel
from pydantic import StrictStr

class StatusUpdate(BaseModel):
    status: StrictStr