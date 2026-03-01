# app/controllers/application_controller.py

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.application_model import Application
from app.models.candidate_model import Candidate
from app.models.job_model import Job
from app.schemas.application_schema import ApplicationCreate, ApplicationUpdate, ApplicationResponse

# --------------------------------------------------
# Apply to Job
# --------------------------------------------------
def create_application(data: ApplicationCreate, db: Session) -> ApplicationResponse:
    candidate = db.query(Candidate).filter(Candidate.id == data.candidate_id).first()
    if not candidate:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Candidate not found")

    job = db.query(Job).filter(Job.id == data.job_id).first()
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")

    # Optional: Prevent duplicate application
    existing = db.query(Application).filter(
        Application.candidate_id == data.candidate_id,
        Application.job_id == data.job_id
    ).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Already applied")

    application = Application(
        candidate_id=data.candidate_id,
        job_id=data.job_id,
        status=data.status
    )
    db.add(application)
    db.commit()
    db.refresh(application)
    return application

# --------------------------------------------------
# Update Application Status
# --------------------------------------------------
def update_application(application_id: str, data: ApplicationUpdate, db: Session) -> ApplicationResponse:
    application = db.query(Application).filter(Application.id == application_id).first()
    if not application:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found")

    if data.status:
        application.status = data.status

    db.commit()
    db.refresh(application)
    return application

# --------------------------------------------------
# Get Application by ID
# --------------------------------------------------
def get_application(application_id: str, db: Session) -> ApplicationResponse:
    application = db.query(Application).filter(Application.id == application_id).first()
    if not application:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Application not found")
    return application
