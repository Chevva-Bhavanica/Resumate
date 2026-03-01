# app/schemas/recruiter_schema.py

from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID


# ----------------------------
# Recruiter Base Schema (common fields)
# ----------------------------
class RecruiterBase(BaseModel):
    company: Optional[str]
    phone: Optional[str]
    location: Optional[str]
    bio: Optional[str]


# ----------------------------
# Recruiter Create Schema
# ----------------------------
class RecruiterCreate(RecruiterBase):
    user_id: UUID  # Must be linked to existing user


# ----------------------------
# Recruiter Update Schema
# ----------------------------
class RecruiterUpdate(RecruiterBase):
    pass  # Optional fields can be updated


# ----------------------------
# Recruiter Response Schema
# ----------------------------
class RecruiterResponse(RecruiterBase):
    id: UUID
    user_id: UUID

    class Config:
        orm_mode = True
