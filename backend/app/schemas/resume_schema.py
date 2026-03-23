# app/schemas/resume_schema.py

from pydantic import BaseModel
from typing import Optional, Dict
from uuid import UUID


# ----------------------------
# Resume Base Schema
# ----------------------------
class ResumeBase(BaseModel):
    user_id: UUID
    file_path: str
    extracted_data: Optional[Dict] = None
    summary: Optional[str] = None


# ----------------------------
# Resume Create Schema
# ----------------------------
class ResumeCreate(ResumeBase):
    pass  # all fields required for creation


# ----------------------------
# Resume Update Schema
# ----------------------------
class ResumeUpdate(BaseModel):
    extracted_data: Optional[Dict] = None
    summary: Optional[str] = None


# ----------------------------
# Resume Response Schema
# ----------------------------
class ResumeResponse(ResumeBase):
    id: UUID

    class Config:
        orm_mode = True


# ----------------------------
# Resume Summary Response Schema
# ----------------------------
class ResumeSummaryResponse(BaseModel):
    summary: str

    class Config:
        orm_mode = True

# ----------------------------
# Resume Builder Request
# ----------------------------
class ResumeBuilderRequest(BaseModel):
    skills: str
    projects: str
    experience: str
