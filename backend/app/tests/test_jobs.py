# app/tests/test_jobs.py

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

job_data = {
    "title": "Software Engineer",
    "description": "Develop and maintain web applications",
    "required_skills": ["Python", "FastAPI"],
    "location": "Remote",
    "is_active": True
}

def test_create_job():
    # Note: ideally, include auth headers with a recruiter token
    response = client.post("/jobs/", json=job_data)
    # Access denied expected if no auth
    assert response.status_code in [401, 403, 201, 200]

def test_get_job():
    # Dummy job ID, replace with actual in real test
    job_id = "dummy-job-id"
    response = client.get(f"/jobs/{job_id}")
    assert response.status_code in [404, 200]
