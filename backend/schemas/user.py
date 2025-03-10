from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    """Base model for user data"""
    email: EmailStr
    username: str
    is_active: Optional[bool] = True


class UserCreate(UserBase):
    """Model for creating a new user"""
    password: str = Field(..., min_length=8)


class UserUpdate(BaseModel):
    """Model for updating a user"""
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None


class UserInDBBase(UserBase):
    """Base model for a user in the database"""
    id: int

    class Config:
        from_attributes = True


class User(UserInDBBase):
    """Model for user response data"""
    pass


class UserInDB(UserInDBBase):
    """Model for a user in the database (internal use)"""
    hashed_password: str
