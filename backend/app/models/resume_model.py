# app/models/resume_model.py

from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
import uuid

from app.database.base import Base

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Link to User
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    # File path
    file_path = Column(String(300), nullable=False)

    # Parsed resume data (JSON)
    extracted_data = Column(JSONB, nullable=True)

    # Generated summary text
    summary = Column(Text, nullable=True)

    # Relationships
    user = relationship("User", backref="resumes")
