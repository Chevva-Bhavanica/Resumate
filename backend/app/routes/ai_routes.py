# app/routes/ai_routes.py

from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from typing import List

from app.controllers.ai_controller import (
    parse_resume,
    generate_resume_summary,
    recommend_jobs_for_candidate
)
from app.schemas.resume_schema import ResumeResponse, ResumeSummaryResponse
from app.schemas.job_schema import JobResponse
from app.dependencies import get_db
from app.middleware.auth_middleware import require_role

router = APIRouter(prefix="/ai", tags=["AI"])

# --------------------------------------------------
# Upload & Parse Resume (Candidate only)
# --------------------------------------------------
@router.post("/parse_resume", response_model=ResumeResponse)
def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user = Depends(require_role("candidate"))
):
    return parse_resume(file, current_user, db)

# --------------------------------------------------
# Generate Resume Summary (Candidate only)
# --------------------------------------------------
@router.post("/summary", response_model=ResumeSummaryResponse)
def resume_summary(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user = Depends(require_role("candidate"))
):
    return generate_resume_summary(file, current_user, db)

# --------------------------------------------------
# Job Recommendations (Candidate only)
# --------------------------------------------------
@router.get("/recommendations", response_model=List[JobResponse])
def job_recommendations(
    db: Session = Depends(get_db),
    current_user = Depends(require_role("candidate"))
):
    return recommend_jobs_for_candidate(current_user, db)
