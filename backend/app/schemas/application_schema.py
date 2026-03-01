# app/schemas/application_schema.py

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

# --------------------------------------------------
# Base Application Schema
# --------------------------------------------------
class ApplicationBase(BaseModel):
    status: Optional[str] = Field("applied", description="applied | shortlisted | rejected | hired")

# --------------------------------------------------
# Create Application
# --------------------------------------------------
class ApplicationCreate(ApplicationBase):
    candidate_id: str
    job_id: str

# --------------------------------------------------
# Update Application (status change)
# --------------------------------------------------
class ApplicationUpdate(ApplicationBase):
    pass  # Partial updates allowed

# --------------------------------------------------
# Application Response
# --------------------------------------------------
class ApplicationResponse(ApplicationBase):
    id: str
    candidate_id: str
    job_id: str
    applied_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
