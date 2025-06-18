from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=user.password, # In a real app, hash this!
        is_active=True
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

