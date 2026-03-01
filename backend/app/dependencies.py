# app/dependencies.py

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from bson import ObjectId

from app.config import settings
from app.database.db_connection import get_database

# OAuth2 scheme for JWT extraction
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


# -------------------------------------------------
# Get Current User from JWT
# -------------------------------------------------

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db=Depends(get_database)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        user_id: str = payload.get("sub")

        if user_id is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = await db["users"].find_one({"_id": ObjectId(user_id)})

    if user is None:
        raise credentials_exception

    user["id"] = str(user["_id"])
    return user


# -------------------------------------------------
# Role-Based Dependency
# -------------------------------------------------

def require_role(required_role: str):
    async def role_checker(current_user=Depends(get_current_user)):
        if current_user["role"] != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied: insufficient permissions"
            )
        return current_user

    return role_checker


# -------------------------------------------------
# Database Dependency
# -------------------------------------------------

async def get_db():
    db = await get_database()
    return db
