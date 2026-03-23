# app/models/recruiter_model.py

from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.database.base import Base

class Recruiter(Base):
    __tablename__ = "recruiters"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Link to User table
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True, nullable=False)

    company = Column(String(150), nullable=True)
    phone = Column(String(20), nullable=True)
    location = Column(String(100), nullable=True)
    bio = Column(Text, nullable=True)

    # Relationships
    user = relationship("User", backref="recruiter_profile")
