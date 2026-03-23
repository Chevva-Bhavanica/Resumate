# app/controllers/job_controller.py

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import List

from app.models.job_model import Job
from app.schemas.job_schema import JobCreate, JobUpdate, JobResponse

# --------------------------------------------------
# Create Job
# --------------------------------------------------
def create_job(data: JobCreate, db: Session) -> JobResponse:
    job = Job(
        recruiter_id=data.recruiter_id,
        title=data.title,
        description=data.description,
        required_skills=",".join(data.required_skills) if data.required_skills else None,
        location=data.location,
        is_active=data.is_active
    )
    db.add(job)
    db.commit()
    db.refresh(job)
    return job

# --------------------------------------------------
# Update Job
# --------------------------------------------------
def update_job(job_id: str, data: JobUpdate, db: Session) -> JobResponse:
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")

    for field, value in data.dict(exclude_unset=True).items():
        if field == "required_skills" and value is not None:
            setattr(job, field, ",".join(value))
        else:
            setattr(job, field, value)

    db.commit()
    db.refresh(job)
    return job

# --------------------------------------------------
# Get Job by ID
# --------------------------------------------------
def get_job(job_id: str, db: Session) -> JobResponse:
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    return job

# --------------------------------------------------
# Get All Jobs
# --------------------------------------------------
def get_all_jobs(db: Session, skip: int = 0, limit: int = 100) -> List[Job]:
    return db.query(Job).filter(Job.is_active == True).offset(skip).limit(limit).all()
