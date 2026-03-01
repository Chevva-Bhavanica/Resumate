# app/services/recommendation_engine.py

from typing import List, Dict
from app.services.job_matcher import match_candidate_to_job

# --------------------------------------------------
# Recommend Jobs
# --------------------------------------------------
def recommend_jobs(candidate_skills: List[str], jobs: List[Dict]) -> List[Dict]:
    """
    jobs: list of dicts with 'id', 'title', 'description'
    Returns sorted jobs by match_score
    """
    recommendations = []
    for job in jobs:
        score = match_candidate_to_job(candidate_skills, job['description'])
        job_copy = job.copy()
        job_copy['match_score'] = score
        recommendations.append(job_copy)

    recommendations.sort(key=lambda x: x['match_score'], reverse=True)
    return recommendations
