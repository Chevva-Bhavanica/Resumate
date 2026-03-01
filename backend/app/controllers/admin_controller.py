# app/controllers/admin_controller.py

from sqlalchemy.orm import Session
from app.models.user_model import User
from app.models.job_model import Job
from typing import List

# --------------------------------------------------
# Get all users
# --------------------------------------------------
def get_all_users(db: Session) -> List[User]:
    return db.query(User).all()


# --------------------------------------------------
# Get user by ID
# --------------------------------------------------
def get_user_by_id(user_id: str, db: Session) -> User:
    return db.query(User).filter(User.id == user_id).first()


# --------------------------------------------------
# Delete user by ID
# --------------------------------------------------
def delete_user(user_id: str, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()


# --------------------------------------------------
# Get all jobs (for admin dashboard)
# --------------------------------------------------
def get_all_jobs(db: Session) -> List[Job]:
    return db.query(Job).all()
