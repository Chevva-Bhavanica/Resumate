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
    
    # Extract text before summarizing
    from app.services.resume_parser import extract_resume_text
    resume_text = extract_resume_text(saved_path)
    
    summary_text = generate_summary(resume_text)
    
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
    
    candidate_skills = []
    for r in resumes:
        if r.extracted_data and "skills" in r.extracted_data:
            candidate_skills.extend(r.extracted_data["skills"])
            
    # Also get skills from candidate profile if present
    from app.models.candidate_model import Candidate
    candidate = db.query(Candidate).filter(Candidate.user_id == user.id).first()
    if candidate and candidate.skills:
        candidate_skills.extend(candidate.skills.split(","))
        
    candidate_skills = list(set(candidate_skills))
    
    # Fetch all active jobs
    all_jobs = db.query(Job).filter(Job.is_active == True).all()
    jobs_dict = [
        {"id": str(job.id), "title": job.title, "description": job.description, "obj": job}
        for job in all_jobs
    ]
    
    # Recommend
    recommended_dicts = recommend_jobs(candidate_skills, jobs_dict)
    
    # Return sorted jobs
    # Only return top match score jobs
    sorted_jobs = []
    for rd in recommended_dicts:
        if rd.get("match_score", 0) > 0.1: # Threshold
            sorted_jobs.append(rd["obj"])
            
    return sorted_jobs
