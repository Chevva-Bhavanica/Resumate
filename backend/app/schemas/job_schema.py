# app/schemas/job_schema.py

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# --------------------------------------------------
# Base Job Schema
# --------------------------------------------------
class JobBase(BaseModel):
    title: str = Field(..., max_length=255)
    description: str = Field(..., max_length=5000)
    required_skills: Optional[List[str]] = Field(default_factory=list)
    location: Optional[str] = Field(None, max_length=100)
    is_active: Optional[bool] = True

# --------------------------------------------------
# Create Job
# --------------------------------------------------
class JobCreate(JobBase):
    recruiter_id: str

# --------------------------------------------------
# Update Job
# --------------------------------------------------
class JobUpdate(JobBase):
    pass  # Partial update

# --------------------------------------------------
# Job Response
# --------------------------------------------------
class JobResponse(JobBase):
    id: str
    recruiter_id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
