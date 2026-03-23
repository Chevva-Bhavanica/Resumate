# app/services/resume_parser.py

import re
from typing import List, Dict
from pdfminer.high_level import extract_text
import docx
import spacy
import json

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import spacy.cli
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

SKILL_ONTOLOGY = {
    "software engineering": {"python", "java", "c++", "c#", "javascript", "typescript", "ruby", "go", "rust", "php"},
    "web development": {"html", "css", "react", "angular", "vue", "node.js", "django", "flask", "fastapi", "spring boot"},
    "data science": {"machine learning", "deep learning", "nlp", "computer vision", "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch"},
    "devops": {"docker", "kubernetes", "aws", "azure", "gcp", "ci/cd", "jenkins", "terraform"},
    "databases": {"sql", "mysql", "postgresql", "mongodb", "redis", "elasticsearch", "cassandra"}
}

ALL_SKILLS = set()
for skills in SKILL_ONTOLOGY.values():
    ALL_SKILLS.update(skills)

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
# Parse skills (using Skill Ontology)
# --------------------------------------------------
def parse_skills(text: str) -> List[str]:
    text_lower = text.lower()
    found_skills = set()
    for skill in ALL_SKILLS:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.add(skill.title())
    return list(found_skills)

# --------------------------------------------------
# Extract Organizations and Dates using spaCy NER
# --------------------------------------------------
def extract_ner_entities(text: str) -> Dict[str, List[str]]:
    doc = nlp(text)
    organizations = set()
    dates = set()
    for ent in doc.ents:
        if ent.label_ == "ORG":
            organizations.add(ent.text)
        elif ent.label_ == "DATE":
            dates.add(ent.text)
    return {
        "organizations": list(organizations),
        "dates": list(dates)
    }

# --------------------------------------------------
# Main Parse Function
# --------------------------------------------------
def parse_resume_file(file_path: str) -> dict:
    text = extract_resume_text(file_path)
    skills = parse_skills(text)
    entities = extract_ner_entities(text)
    
    # Return a structured dictionary
    return {
        "text": text[:500] + "...",  # Store a snippet
        "skills": skills,
        "organizations": entities["organizations"],
        "dates": entities["dates"]
    }
