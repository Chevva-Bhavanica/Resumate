# app/controllers/ai_controller.py

from fastapi import UploadFile
from sqlalchemy.orm import Session
from typing import List
import shutil
import os
import uuid

from app.models.resume_model import Resume
from app.models.job_model import Job
from app.models.user_model import User
from app.utils.file_handler import save_file
from app.services.resume_parser import parse_resume_file
from app.services.summary_generator import generate_summary
from app.services.recommendation_engine import recommend_jobs

# --------------------------------------------------
# Parse Resume
# --------------------------------------------------
def parse_resume(file: UploadFile, user: User, db: Session):
    # Save uploaded file
    saved_path = save_file(file)
    
    # Parse resume using service
    parsed_data = parse_resume_file(saved_path)
    
    # Save resume record in DB
    resume_record = Resume(
        user_id=user.id,
        file_path=saved_path,
        extracted_data=parsed_data
    )
    db.add(resume_record)
    db.commit()
    db.refresh(resume_record)
    return resume_record

# --------------------------------------------------
# Generate Resume Summary
# --------------------------------------------------
def generate_resume_summary(file: UploadFile, user: User, db: Session):
    saved_path = save_file(file)
    
    summary_text = generate_summary(saved_path)
    
    # Optionally save summary in DB
    resume_summary_record = Resume(
        user_id=user.id,
        file_path=saved_path,
        summary=summary_text
    )
    db.add(resume_summary_record)
    db.commit()
    db.refresh(resume_summary_record)
    
    return resume_summary_record

# --------------------------------------------------
# Recommend Jobs
# --------------------------------------------------
def recommend_jobs_for_candidate(user: User, db: Session) -> List[Job]:
    # Fetch user resumes
    resumes = db.query(Resume).filter(Resume.user_id == user.id).all()
    
    # Pass resumes or skills to recommendation engine
    recommended_job_ids = recommend_jobs(resumes, db)
    
    jobs = db.query(Job).filter(Job.id.in_(recommended_job_ids)).all()
    return jobs
