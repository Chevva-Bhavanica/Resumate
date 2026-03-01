from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # App
    APP_NAME: str = "Resumate API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # SQL Database
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./resumate.db"
    # For PostgreSQL: postgresql://user:password@localhost:5432/resumate_db

    # JWT
    SECRET_KEY: str = "your-super-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]

    # File Upload
    MAX_FILE_SIZE_MB: int = 5
    ALLOWED_FILE_TYPES: List[str] = ["application/pdf"]

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
