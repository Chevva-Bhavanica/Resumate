# app/middleware/role_middleware.py

from fastapi import HTTPException, status
from app.models.user_model import User

# --------------------------------------------------
# Check if user has one of allowed roles
# --------------------------------------------------
def has_roles(user: User, allowed_roles: list):
    if user.role not in allowed_roles:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Access denied. Allowed roles: {allowed_roles}"
        )
