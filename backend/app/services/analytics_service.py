# app/services/analytics_service.py

from sqlalchemy.orm import Session
from app.models.user_model import User
from app.models.job_model import Job
from app.models.application_model import Application

# --------------------------------------------------
# Get Admin Dashboard Statistics
# --------------------------------------------------
def get_dashboard_stats(db: Session) -> dict:
    total_candidates = db.query(User).filter(User.role == "candidate").count()
    total_recruiters = db.query(User).filter(User.role == "recruiter").count()
    total_jobs = db.query(Job).count()
    total_applications = db.query(Application).count()
    
    application_status_counts = {
        status: db.query(Application).filter(Application.status == status).count()
        for status in ["applied", "shortlisted", "rejected", "hired"]
    }

    return {
        "total_candidates": total_candidates,
        "total_recruiters": total_recruiters,
        "total_jobs": total_jobs,
        "total_applications": total_applications,
        "application_status_counts": application_status_counts
    }
