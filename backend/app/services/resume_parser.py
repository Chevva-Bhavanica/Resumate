# app/services/resume_parser.py

import re
from typing import List, Dict
from pdfminer.high_level import extract_text
import docx

# --------------------------------------------------
# Extract text from file
# --------------------------------------------------
def extract_resume_text(file_path: str) -> str:
    if file_path.endswith(".pdf"):
        text = extract_text(file_path)
    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        text = "\n".join([p.text for p in doc.paragraphs])
    else:
        raise ValueError("Unsupported file type")
    return text

# --------------------------------------------------
# Parse skills (example using regex / simple keywords)
# --------------------------------------------------
def parse_skills(text: str, skill_keywords: List[str]) -> List[str]:
    text_lower = text.lower()
    found_skills = [skill for skill in skill_keywords if skill.lower() in text_lower]
    return found_skills

# --------------------------------------------------
# Parse education (simplified)
# --------------------------------------------------
def parse_education(text: str) -> List[str]:
    patterns = [
        r"(bachelor[s]?\s+of\s+\w+)",
        r"(master[s]?\s+of\s+\w+)",
        r"(ph\.d\.?\s+in\s+\w+)"
    ]
    results = []
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        results.extend(matches)
    return results

# --------------------------------------------------
# Parse experience (simplified)
# --------------------------------------------------
def parse_experience(text: str) -> List[str]:
    # This can be enhanced with NLP later
    exp_pattern = r"(\d+\s+years?\s+experience)"
    matches = re.findall(exp_pattern, text, re.IGNORECASE)
    return matches
