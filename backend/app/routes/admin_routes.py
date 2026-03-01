# app/routes/admin_routes.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.controllers.admin_controller import (
    get_all_users,
    get_user_by_id,
    delete_user,
    get_all_jobs,
)
from app.schemas.user_schema import UserResponse
from app.schemas.job_schema import JobResponse
from app.dependencies import get_db
from app.middleware.auth_middleware import require_role

router = APIRouter(prefix="/admin", tags=["Admin"])

# --------------------------------------------------
# Get all users (Admin only)
# --------------------------------------------------
@router.get("/users", response_model=List[UserResponse])
def list_users(
    db: Session = Depends(get_db),
    current_user = Depends(require_role("admin"))
):
    return get_all_users(db)

# --------------------------------------------------
# Get single user by ID (Admin only)
# --------------------------------------------------
@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(
    user_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("admin"))
):
    user = get_user_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

# --------------------------------------------------
# Delete user (Admin only)
# --------------------------------------------------
@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_user(
    user_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(require_role("admin"))
):
    delete_user(user_id, db)
    return {"detail": "User deleted successfully"}

# --------------------------------------------------
# Get all jobs (Admin dashboard)
# --------------------------------------------------
@router.get("/jobs", response_model=List[JobResponse])
def list_jobs(
    db: Session = Depends(get_db),
    current_user = Depends(require_role("admin"))
):
    return get_all_jobs(db)
