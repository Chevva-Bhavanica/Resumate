# app/tests/test_ai.py

import pytest
from app.services import resume_parser, job_matcher, recommendation_engine, summary_generator

def test_resume_parser_text_extraction():
    sample_text = "John Doe has 3 years experience in Python and FastAPI."
    skills = ["Python", "FastAPI", "JavaScript"]
    extracted_skills = resume_parser.parse_skills(sample_text, skills)
    assert "Python" in extracted_skills
    assert "FastAPI" in extracted_skills

def test_job_matcher():
    candidate_skills = ["Python", "FastAPI"]
    job_desc = "Looking for a backend developer with Python and FastAPI experience."
    score = job_matcher.match_candidate_to_job(candidate_skills, job_desc)
    assert score > 0.5

def test_recommendation_engine():
    candidate_skills = ["Python", "FastAPI"]
    jobs = [
        {"id": "1", "title": "Backend Dev", "description": "Python backend work"},
        {"id": "2", "title": "Frontend Dev", "description": "React developer"}
    ]
    recommended = recommendation_engine.recommend_jobs(candidate_skills, jobs)
    assert recommended[0]["id"] == "1"
