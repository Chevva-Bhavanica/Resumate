# app/models/candidate_model.py

from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.database.base import Base


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Link to User table
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True, nullable=False)

    phone = Column(String(20), nullable=True)
    location = Column(String(100), nullable=True)
    bio = Column(Text, nullable=True)
    skills = Column(Text, nullable=True)  # Can store comma-separated or JSON later

    # Relationships
    user = relationship("User", backref="candidate_profile")
    applications = relationship("Application", back_populates="candidate")
