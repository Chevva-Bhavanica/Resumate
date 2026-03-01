# app/models/application_model.py

from sqlalchemy import Column, ForeignKey, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from app.database.base import Base


class Application(Base):
    __tablename__ = "applications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    candidate_id = Column(UUID(as_uuid=True), ForeignKey("candidates.id"), nullable=False)
    job_id = Column(UUID(as_uuid=True), ForeignKey("jobs.id"), nullable=False)

    status = Column(String(50), default="applied")  # applied | shortlisted | rejected | hired

    applied_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    candidate = relationship("Candidate", back_populates="applications")
    job = relationship("Job", back_populates="applications")
