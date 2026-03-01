# app/config.py

from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # ----------------------------
    # Application Settings
    # ----------------------------
    APP_NAME: str = "Resumate API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # ----------------------------
    # MongoDB Settings
    # ----------------------------
    MONGODB_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "resumate_db"

    # ----------------------------
    # JWT Authentication Settings
    # ----------------------------
    SECRET_KEY: str = "your-super-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # ----------------------------
    # CORS Settings
    # ----------------------------
    ALLOWED_ORIGINS: List[str] = ["*"]  # Change in production

    # ----------------------------
    # File Upload Settings
    # ----------------------------
    MAX_FILE_SIZE_MB: int = 5
    ALLOWED_FILE_TYPES: List[str] = ["application/pdf"]

    class Config:
        env_file = ".env"
        case_sensitive = True


# Create a single settings object
settings = Settings()
