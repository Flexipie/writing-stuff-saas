from pydantic import BaseModel
from typing import Optional

class DocumentChunkBase(BaseModel):
    """Base model for document chunk data"""
    chunk_id: str
    content: str
    page_number: Optional[int] = None
    chunk_index: int

class DocumentChunkCreate(DocumentChunkBase):
    """Model for creating a new document chunk"""
    document_id: int
    vector_id: Optional[str] = None

class DocumentChunkInDB(DocumentChunkBase):
    """Base model for a document chunk in the database"""
    id: int
    document_id: int
    vector_id: Optional[str] = None

    class Config:
        from_attributes = True

class DocumentChunk(DocumentChunkInDB):
    """Model for document chunk response data"""
    pass
