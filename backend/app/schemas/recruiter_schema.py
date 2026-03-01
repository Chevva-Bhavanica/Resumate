# app/schemas/recruiter_schema.py

from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

# --------------------------------------------------
# Base Recruiter Schema
# --------------------------------------------------
class RecruiterBase(BaseModel):
    company_name: Optional[str] = Field(None, max_length=150)
    phone: Optional[str] = Field(None, max_length=20)
    location: Optional[str] = Field(None, max_length=100)
    bio: Optional[str] = Field(None, max_length=1000)

# --------------------------------------------------
# Create Recruiter Profile
# --------------------------------------------------
class RecruiterCreate(RecruiterBase):
    user_id: str

# --------------------------------------------------
# Update Recruiter Profile
# --------------------------------------------------
class RecruiterUpdate(RecruiterBase):
    pass  # All optional for partial updates

# --------------------------------------------------
# Recruiter Response
# --------------------------------------------------
class RecruiterResponse(RecruiterBase):
    id: str
    user_id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
