#!/bin/bash
# This script will stop if any command fails
set -e

# Define the project directory
PROJECT_DIR="/home/reddy/aspiro_ai_backend"
echo "--- Generating all code for Phase 2 ---"

# 1. Update config.py to load the DATABASE_URL
echo "Updating app/core/config.py..."
cat <<EOT > $PROJECT_DIR/app/core/config.py
import os
from pydantic import BaseSettings
from dotenv import load_dotenv

# Load .env file variables
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "ASPIRO AI"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    class Config:
        case_sensitive = True

settings = Settings()
EOT

# 2. Create the database session handler
echo "Creating app/db/session.py..."
cat <<EOT > $PROJECT_DIR/app/db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
EOT

# 3. Create the Base class for DB models
echo "Creating app/db/base_class.py..."
cat <<EOT > $PROJECT_DIR/app/db/base_class.py
from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    id: any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
EOT

# 4. Define the User database model
echo "Creating app/models/user.py..."
cat <<EOT > $PROJECT_DIR/app/models/user.py
from sqlalchemy import Column, Integer, String, Boolean
from app.db.base_class import Base

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
EOT

# 5. Define the User Pydantic schemas for API validation
echo "Creating app/schemas/user.py..."
cat <<EOT > $PROJECT_DIR/app/schemas/user.py
from pydantic import BaseModel, EmailStr

# Shared properties
class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None
    is_active: bool = True

# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str

# Properties to return to client
class User(UserBase):
    id: int

    class Config:
        orm_mode = True
EOT

# 6. Create the CRUD (Create, Read, Update, Delete) functions
echo "Creating app/crud.py..."
cat <<EOT > $PROJECT_DIR/app/crud.py
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

# For this example, we will just store passwords as plain text.
# In a real application, YOU MUST HASH THE PASSWORDS.
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    # In a real app, hash the password here: fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=user.password # Replace with hashed password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
EOT

# 7. Create the User API endpoint
echo "Creating app/api/v1/endpoints/users.py..."
touch $PROJECT_DIR/app/api/v1/api.py # Ensure api.py exists
cat <<EOT > $PROJECT_DIR/app/api/v1/endpoints/users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db import session

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = session.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)
EOT

# 8. Create the API router and include the new endpoint in main.py
echo "Creating app/api/v1/api.py..."
cat <<EOT > $PROJECT_DIR/app/api/v1/api.py
from fastapi import APIRouter
from app.api.v1.endpoints import users

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
EOT

echo "Updating app/main.py to include the new API router..."
cat <<EOT > $PROJECT_DIR/app/main.py
from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.config import settings
from app.db.base_class import Base
from app.db.session import engine

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

@app.get("/", tags=["Root"])
def read_root():
    return {"status": "ok", "message": "Welcome to ASPIRO AI Backend"}

app.include_router(api_router, prefix=settings.API_V1_STR)
EOT

echo "--- All code for Phase 2 has been generated successfully. ---"
