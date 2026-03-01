# app/database/db_connection.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from app.config import settings

# --------------------------------------------------
# SQLAlchemy Engine
# --------------------------------------------------
engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in settings.SQLALCHEMY_DATABASE_URL else {}
)

# --------------------------------------------------
# SessionLocal for Dependency Injection
# --------------------------------------------------
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# --------------------------------------------------
# Base class for models
# --------------------------------------------------
Base = declarative_base()

# --------------------------------------------------
# Dependency for FastAPI routes
# --------------------------------------------------
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
