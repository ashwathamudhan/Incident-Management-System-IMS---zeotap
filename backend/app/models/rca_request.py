from pydantic import BaseModel
from pydantic import StrictStr

class RCARequest(BaseModel):

    root_cause: StrictStr

    fix_applied: StrictStr

    prevention_steps: StrictStr