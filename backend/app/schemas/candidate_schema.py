# app/schemas/candidate_schema.py

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


# --------------------------------------------------
# Base Candidate Schema
# --------------------------------------------------

class CandidateBase(BaseModel):
    phone: Optional[str] = Field(None, max_length=20)
    location: Optional[str] = Field(None, max_length=100)
    bio: Optional[str] = Field(None, max_length=1000)
    skills: Optional[List[str]] = Field(default_factory=list)


# --------------------------------------------------
# Create Candidate Profile
# --------------------------------------------------

class CandidateCreate(CandidateBase):
    user_id: str


# --------------------------------------------------
# Update Candidate Profile
# --------------------------------------------------

class CandidateUpdate(CandidateBase):
    pass  # Partial update allowed, all optional


# --------------------------------------------------
# Candidate Response Schema
# --------------------------------------------------

class CandidateResponse(CandidateBase):
    id: str
    user_id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


# --------------------------------------------------
# Public Candidate Profile (For Job Listing Views)
# --------------------------------------------------

class PublicCandidateProfile(BaseModel):
    id: str
    name: str  # From User table
    skills: List[str]
    location: Optional[str] = None
    bio: Optional[str] = None

# --------------------------------------------------
# Candidate Dashboard Stats
# --------------------------------------------------
class CandidateDashboardStats(BaseModel):
    profile_completion: int
    jobs_applied: int
    ai_matches: int
