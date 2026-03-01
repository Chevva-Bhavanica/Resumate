# app/constants.py

# -------------------------------------------------
# User Roles
# -------------------------------------------------

ROLE_CANDIDATE = "candidate"
ROLE_RECRUITER = "recruiter"
ROLE_ADMIN = "admin"

VALID_ROLES = [
    ROLE_CANDIDATE,
    ROLE_RECRUITER,
    ROLE_ADMIN
]


# -------------------------------------------------
# Application Status
# -------------------------------------------------

STATUS_APPLIED = "applied"
STATUS_SHORTLISTED = "shortlisted"
STATUS_REJECTED = "rejected"

VALID_APPLICATION_STATUSES = [
    STATUS_APPLIED,
    STATUS_SHORTLISTED,
    STATUS_REJECTED
]


# -------------------------------------------------
# Job Status
# -------------------------------------------------

JOB_STATUS_OPEN = "open"
JOB_STATUS_CLOSED = "closed"

VALID_JOB_STATUSES = [
    JOB_STATUS_OPEN,
    JOB_STATUS_CLOSED
]


# -------------------------------------------------
# Matching Algorithm Weights
# -------------------------------------------------
# You can tune these later

SKILL_MATCH_WEIGHT = 0.7
EXPERIENCE_MATCH_WEIGHT = 0.2
EDUCATION_MATCH_WEIGHT = 0.1


# -------------------------------------------------
# Pagination Defaults
# -------------------------------------------------

DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 10
MAX_PAGE_SIZE = 100


# -------------------------------------------------
# File Upload Constraints
# -------------------------------------------------

MAX_RESUME_FILE_SIZE_MB = 5
ALLOWED_RESUME_EXTENSIONS = ["pdf"]


# -------------------------------------------------
# AI / Recommendation Settings
# -------------------------------------------------

TOP_N_RECOMMENDATIONS = 5


# -------------------------------------------------
# Collection Names (MongoDB)
# -------------------------------------------------
# Avoid hardcoding collection names everywhere

COLLECTION_USERS = "users"
COLLECTION_CANDIDATES = "candidate_profiles"
COLLECTION_RECRUITERS = "recruiter_profiles"
COLLECTION_JOBS = "jobs"
COLLECTION_APPLICATIONS = "applications"
COLLECTION_RESUME_ANALYSIS = "resume_analysis"
