# app/services/job_matcher.py

from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --------------------------------------------------
# Simple Job Matching
# --------------------------------------------------
def match_candidate_to_job(candidate_skills: List[str], job_description: str) -> float:
    candidate_text = " ".join(candidate_skills)
    corpus = [candidate_text, job_description]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(float(score), 2)
