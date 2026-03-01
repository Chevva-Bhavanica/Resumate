# app/controllers/candidate_controller.py

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.candidate_model import Candidate
from app.models.user_model import User
from app.schemas.candidate_schema import CandidateCreate, CandidateUpdate, CandidateResponse

# --------------------------------------------------
# Create Candidate Profile
# --------------------------------------------------
def create_candidate(data: CandidateCreate, db: Session) -> CandidateResponse:
    user = db.query(User).filter(User.id == data.user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    candidate = Candidate(
        user_id=data.user_id,
        phone=data.phone,
        location=data.location,
        bio=data.bio,
        skills=",".join(data.skills) if data.skills else None
    )
    db.add(candidate)
    db.commit()
    db.refresh(candidate)
    return candidate

# --------------------------------------------------
# Update Candidate Profile
# --------------------------------------------------
def update_candidate(candidate_id: str, data: CandidateUpdate, db: Session) -> CandidateResponse:
    candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
    if not candidate:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Candidate not found")

    for field, value in data.dict(exclude_unset=True).items():
        if field == "skills" and value is not None:
            setattr(candidate, field, ",".join(value))
        else:
            setattr(candidate, field, value)

    db.commit()
    db.refresh(candidate)
    return candidate

# --------------------------------------------------
# Get Candidate by ID
# --------------------------------------------------
def get_candidate(candidate_id: str, db: Session) -> CandidateResponse:
    candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
    if not candidate:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Candidate not found")
    return candidate
