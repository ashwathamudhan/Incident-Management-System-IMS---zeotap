from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.db.database import Base

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)

    component_id = Column(String, nullable=False)

    severity = Column(String, nullable=False)

    message = Column(String, nullable=False)

    status = Column(String, default="OPEN")

    created_at = Column(DateTime, default=datetime.utcnow)