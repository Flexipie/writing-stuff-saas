from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class DocumentBase(BaseModel):
    """Base model for document data"""
    title: str
    description: Optional[str] = None
    file_type: str


class DocumentCreate(DocumentBase):
    """Model for creating a new document"""
    pass


class DocumentUpdate(BaseModel):
    """Model for updating a document"""
    title: Optional[str] = None
    description: Optional[str] = None


class DocumentInDBBase(DocumentBase):
    """Base model for a document in the database"""
    id: int
    file_path: str
    file_size: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class Document(DocumentInDBBase):
    """Model for document response data"""
    pass
