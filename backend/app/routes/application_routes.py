# app/routes/application_routes.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.controllers.application_controller import (
    create_application, update_application, get_application
)
from app.schemas.application_schema import ApplicationCreate, ApplicationUpdate, ApplicationResponse
from app.dependencies import get_db
from app.dependencies import get_current_user, require_role

router = APIRouter(prefix="/applications", tags=["Applications"])


# --------------------------------------------------
# Apply to a Job (Candidate only)
# --------------------------------------------------
@router.post("/", response_model=ApplicationResponse)
def apply_job(
    data: ApplicationCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("candidate"))
):
    # Ensure candidate_id is current user
    data.candidate_id = str(current_user.candidate_profile[0].id)
    return create_application(data, db)


# --------------------------------------------------
# Update Application Status (Recruiter/Admin)
# --------------------------------------------------
@router.put("/{application_id}", response_model=ApplicationResponse)
def update_status(
    application_id: str,
    data: ApplicationUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    # Only recruiter or admin can update
    if current_user.role not in ["recruiter", "admin"]:
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied"
        )
    return update_application(application_id, data, db)


# --------------------------------------------------
# Get Application by ID
# --------------------------------------------------
@router.get("/{application_id}", response_model=ApplicationResponse)
def get_application_detail(
    application_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_application(application_id, db)
