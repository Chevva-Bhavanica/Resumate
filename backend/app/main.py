# app/main.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.database.db_connection import create_tables


from app.routes import (
    auth_routes,
    candidate_routes,
    recruiter_routes,
    job_routes,
    application_routes
)
from app.middleware.error_handler import (
    generic_exception_handler,
    sqlalchemy_exception_handler,
    validation_exception_handler
)
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError
from app.database.db_connection import engine, Base, get_db
from sqlalchemy.orm import Session

# --------------------------------------------------
# FastAPI app
# --------------------------------------------------
app = FastAPI(
    title="Resumate - AI-Based Resume Screening & Job Recommendation",
    description="Automated resume evaluation, job matching, and analytics",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# --------------------------------------------------
# CORS Middleware
# --------------------------------------------------
origins = [
    "http://localhost",
    "http://localhost:3000",  # frontend port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# Include Routers
# --------------------------------------------------
app.include_router(auth_routes.router)
app.include_router(candidate_routes.router)
app.include_router(recruiter_routes.router)
app.include_router(job_routes.router)
app.include_router(application_routes.router)

# --------------------------------------------------
# Exception Handlers
# --------------------------------------------------
app.add_exception_handler(Exception, generic_exception_handler)
app.add_exception_handler(SQLAlchemyError, sqlalchemy_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

# --------------------------------------------------
# Startup / Shutdown Events
# --------------------------------------------------
@app.on_event("startup")
def startup_event():
    # Create tables if not exists (for SQLAlchemy)
    create_tables()
    Base.metadata.create_all(bind=engine)
    print("Application Startup: Database tables ready.")


@app.on_event("shutdown")
def shutdown_event():
    print("Application Shutdown: Goodbye!")


# --------------------------------------------------
# Health Check
# --------------------------------------------------
@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "Resumate backend is running!"}
