# app/schemas/user_schema.py

from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


# --------------------------------------------------
# Base User Schema (Shared Fields)
# --------------------------------------------------

class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    role: str = Field(..., description="Role: candidate | recruiter | admin")


# --------------------------------------------------
# Create User (Used during registration)
# --------------------------------------------------

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)


# --------------------------------------------------
# Update User
# --------------------------------------------------

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=6)


# --------------------------------------------------
# User Response (Safe for API return)
# --------------------------------------------------

class UserResponse(UserBase):
    id: str
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True


# --------------------------------------------------
# Public User Profile (No Sensitive Data)
# --------------------------------------------------

class PublicUserProfile(BaseModel):
    id: str
    name: str
    role: str


# --------------------------------------------------
# Admin View User Schema
# --------------------------------------------------

class AdminUserView(UserResponse):
    updated_at: Optional[datetime] = None
