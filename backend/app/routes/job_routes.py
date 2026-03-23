# app/routes/job_routes.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.controllers.job_controller import create_job, update_job, get_job, get_all_jobs
from app.schemas.job_schema import JobCreate, JobUpdate, JobResponse
from app.dependencies import get_db
from app.dependencies import get_current_user, require_role

router = APIRouter(prefix="/jobs", tags=["Jobs"])


# --------------------------------------------------
# Create Job (Recruiter only)
# --------------------------------------------------
@router.post("/", response_model=JobResponse)
def post_job(
    data: JobCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("recruiter"))
):
    data.recruiter_id = str(current_user.id)
    return create_job(data, db)


# --------------------------------------------------
# Update Job
# --------------------------------------------------
@router.put("/{job_id}", response_model=JobResponse)
def edit_job(
    job_id: str,
    data: JobUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("recruiter"))
):
    return update_job(job_id, data, db)


# --------------------------------------------------
# Get Job by ID
# --------------------------------------------------
@router.get("/{job_id}", response_model=JobResponse)
def get_job_detail(
    job_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_job(job_id, db)

# --------------------------------------------------
# Get All Jobs
# --------------------------------------------------
@router.get("/", response_model=List[JobResponse])
def list_jobs(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_all_jobs(db, skip=skip, limit=limit)
