# app/controllers/recruiter_controller.py

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.recruiter_model import Recruiter
from app.models.user_model import User
from app.schemas.recruiter_schema import RecruiterCreate, RecruiterUpdate, RecruiterResponse

# --------------------------------------------------
# Create Recruiter Profile
# --------------------------------------------------
def create_recruiter(data: RecruiterCreate, db: Session) -> RecruiterResponse:
    user = db.query(User).filter(User.id == data.user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    recruiter = Recruiter(
        user_id=data.user_id,
        company_name=data.company_name,
        phone=data.phone,
        location=data.location,
        bio=data.bio
    )
    db.add(recruiter)
    db.commit()
    db.refresh(recruiter)
    return recruiter

# --------------------------------------------------
# Update Recruiter Profile
# --------------------------------------------------
def update_recruiter(recruiter_id: str, data: RecruiterUpdate, db: Session) -> RecruiterResponse:
    recruiter = db.query(Recruiter).filter(Recruiter.id == recruiter_id).first()
    if not recruiter:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recruiter not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(recruiter, field, value)

    db.commit()
    db.refresh(recruiter)
    return recruiter

# --------------------------------------------------
# Get Recruiter by ID
# --------------------------------------------------
def get_recruiter(recruiter_id: str, db: Session) -> RecruiterResponse:
    recruiter = db.query(Recruiter).filter(Recruiter.id == recruiter_id).first()
    if not recruiter:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Recruiter not found")
    return recruiter
