from pydantic import BaseModel, EmailStr

# Shared properties
class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None
    is_active: bool | None = True

# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str

# Properties stored in DB
class UserInDB(UserBase):
    hashed_password: str

# Properties to return to client
class User(UserBase):
    id: int

    class Config:
        from_attributes = True # <-- THIS LINE IS CHANGED from orm_mode
