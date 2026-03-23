# app/routes/candidate_routes.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.controllers.candidate_controller import (
    create_candidate, update_candidate, get_candidate, get_dashboard_stats
)
from app.schemas.candidate_schema import CandidateCreate, CandidateUpdate, CandidateResponse, CandidateDashboardStats
from app.dependencies import get_db
from app.dependencies import get_current_user, require_role

router = APIRouter(prefix="/candidates", tags=["Candidates"])


# --------------------------------------------------
# Create Candidate Profile (Candidate only)
# --------------------------------------------------
@router.post("/", response_model=CandidateResponse)
def create_profile(
    data: CandidateCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("candidate"))
):
    # Override user_id to current user for safety
    data.user_id = str(current_user.id)
    return create_candidate(data, db)


# --------------------------------------------------
# Update Candidate Profile
# --------------------------------------------------
@router.put("/{candidate_id}", response_model=CandidateResponse)
def update_profile(
    candidate_id: str,
    data: CandidateUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("candidate"))
):
    return update_candidate(candidate_id, data, db)


# --------------------------------------------------
# Get Candidate Profile (Admin or Owner)
# --------------------------------------------------
@router.get("/{candidate_id}", response_model=CandidateResponse)
def get_profile(
    candidate_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_candidate(candidate_id, db)

# --------------------------------------------------
# Get Dashboard Stats
# --------------------------------------------------
@router.get("/me/dashboard/stats", response_model=CandidateDashboardStats)
def get_stats(
    db: Session = Depends(get_db),
    current_user = Depends(require_role("candidate"))
):
    return get_dashboard_stats(str(current_user.id), db)

# --------------------------------------------------
# Build Resume PDF
# --------------------------------------------------
from fastapi.responses import FileResponse
from app.utils.pdf_generator import generate_resume_pdf
from app.schemas.resume_schema import ResumeBuilderRequest

@router.post("/me/resume/build", response_class=FileResponse)
def build_resume_pdf(
    data: ResumeBuilderRequest,
    current_user = Depends(require_role("candidate"))
):
    pdf_path = generate_resume_pdf(data.dict(), current_user.name)
    return FileResponse(pdf_path, media_type="application/pdf", filename=f"{current_user.name}_Resume.pdf")
