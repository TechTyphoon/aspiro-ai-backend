from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.config import settings
from app.db.base_class import Base
from app.db.session import engine

# This line creates the database table if it doesn't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint for the ASPIRO AI Backend.
    """
    return {"status": "ok", "message": "Welcome to ASPIRO AI Backend"}

app.include_router(api_router, prefix=settings.API_V1_STR)
