from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.db import session
# CORRECTED IMPORTS: Import the specific classes we need
from app.schemas.user import User, UserCreate

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = session.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CORRECTED CODE: Removed 'schemas.' prefix
@router.post("/", response_model=User)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)
