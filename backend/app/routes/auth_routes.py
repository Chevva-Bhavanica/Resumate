# app/routes/auth_routes.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.auth_schema import RegisterRequest, LoginRequest
from app.controllers.auth_controller import register_user, login_user
from app.dependencies import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])


# --------------------------------------------------
# Register Endpoint
# --------------------------------------------------

@router.post("/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    return register_user(data, db)


# --------------------------------------------------
# Login Endpoint
# --------------------------------------------------

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    return login_user(data, db)
