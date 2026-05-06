from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base

class RCA(Base):
    __tablename__ = "rca"

    id = Column(Integer, primary_key=True, index=True)

    incident_id = Column(Integer, ForeignKey("incidents.id"))

    root_cause = Column(String, nullable=False)

    fix_applied = Column(String, nullable=False)

    prevention_steps = Column(String, nullable=False)