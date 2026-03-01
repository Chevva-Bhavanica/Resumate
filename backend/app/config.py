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
    # SQLAlchemy / Relational DB Settings
    # ----------------------------
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./resumate.db"  # SQLite for dev, change to PostgreSQL in prod

    # ----------------------------
    # JWT Authentication Settings
    # ----------------------------
    SECRET_KEY: str = "your-super-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # ----------------------------
    # CORS Settings
    # ----------------------------
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]  # Add frontend URLs

    # ----------------------------
    # File Upload Settings
    # ----------------------------
    MAX_FILE_SIZE_MB: int = 5
    ALLOWED_FILE_TYPES: List[str] = ["application/pdf"]

    class Config:
        env_file = ".env"
        case_sensitive = True

# Single settings object
settings = Settings()
