# app/database/db_connection.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.database.base import Base

# Example: PostgreSQL URL
DATABASE_URL = settings.SQLALCHEMY_DATABASE_URL  # e.g., "postgresql+psycopg2://user:pass@localhost/resumate_db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Call this once at startup to create all tables automatically
def create_tables():
    Base.metadata.create_all(bind=engine)
