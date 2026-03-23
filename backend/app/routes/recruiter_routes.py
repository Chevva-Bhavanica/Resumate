# app/routes/recruiter_routes.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controllers.recruiter_controller import (
    create_recruiter, update_recruiter, get_recruiter
)
from app.schemas.recruiter_schema import RecruiterCreate, RecruiterUpdate, RecruiterResponse
from app.dependencies import get_db
from app.dependencies import get_current_user, require_role

router = APIRouter(prefix="/recruiters", tags=["Recruiters"])


# --------------------------------------------------
# Create Recruiter Profile (Recruiter only)
# --------------------------------------------------
@router.post("/", response_model=RecruiterResponse)
def create_profile(
    data: RecruiterCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("recruiter"))
):
    data.user_id = str(current_user.id)
    return create_recruiter(data, db)


# --------------------------------------------------
# Update Recruiter Profile
# --------------------------------------------------
@router.put("/{recruiter_id}", response_model=RecruiterResponse)
def update_profile(
    recruiter_id: str,
    data: RecruiterUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("recruiter"))
):
    return update_recruiter(recruiter_id, data, db)


# --------------------------------------------------
# Get Recruiter Profile
# --------------------------------------------------
@router.get("/{recruiter_id}", response_model=RecruiterResponse)
def get_profile(
    recruiter_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_recruiter(recruiter_id, db)
