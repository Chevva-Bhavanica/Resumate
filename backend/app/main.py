# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database.db_connection import connect_to_mongo, close_mongo_connection

# Routers
from app.routes.auth_routes import router as auth_router
from app.routes.candidate_routes import router as candidate_router
from app.routes.recruiter_routes import router as recruiter_router
from app.routes.admin_routes import router as admin_router
from app.routes.ai_routes import router as ai_router

# Global error handler
from app.middleware.error_handler import add_exception_handlers



# Create FastAPI App


app = FastAPI(
    title="Resumate API",
    description="AI-Based Resume Screening & Job Recommendation System",
    version="1.0.0"
)

# CORS Configuration

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database Events


@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()
    print("Connected to MongoDB")

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()
    print("Disconnected from MongoDB")
# Health Check Route
@app.get("/", tags=["Health"])
async def health_check():
    return {
        "status": "success",
        "message": "Resumate Backend is running "
    }
# Register Routers
app.include_router(auth_router, prefix="/api/auth")
app.include_router(candidate_router, prefix="/api/candidate")
app.include_router(recruiter_router, prefix="/api/recruiter")
app.include_router(admin_router, prefix="/api/admin")
app.include_router(ai_router, prefix="/api/ai")
# Global Exception Handlers
add_exception_handlers(app)
