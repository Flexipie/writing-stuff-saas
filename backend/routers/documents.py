import os
from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
from sqlalchemy.orm import Session

from models.base import get_db
from models.document import Document
from models.user import User
from routers.auth import get_current_user
from schemas.document import Document as DocumentSchema, DocumentCreate

# Create router with tags for OpenAPI documentation
router = APIRouter(tags=["documents"])

# Define schemas for search results
from pydantic import BaseModel

class SearchResult(BaseModel):
    chunk_id: str
    text: str
    page_number: int
    relevance_score: float
    
    class Config:
        from_attributes = True

# Document routes
@router.post("/", response_model=DocumentSchema, status_code=status.HTTP_201_CREATED)
async def upload_document(
    file: UploadFile = File(...),
    title: Optional[str] = None,
    description: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Upload a document (requires authentication)"""
    
    # Validate file type
    file_extension = os.path.splitext(file.filename)[1].lower()
    if file_extension not in [".pdf", ".txt", ".md", ".docx"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported file type: {file_extension}. Only PDF, TXT, MD, and DOCX files are supported."
        )
    
    # Read file content
    file_content = await file.read()
    file_size = len(file_content)
    
    # Set title to filename if not provided
    if not title:
        title = os.path.splitext(file.filename)[0]
    
    # Save file to storage (placeholder - will implement S3 storage later)
    # For now, we'll just store the file path in the database
    file_path = f"uploads/{current_user.id}/{file.filename}"
    
    # Create document record in database
    document = Document.create(
        db=db,
        title=title,
        description=description,
        file_path=file_path,
        file_type=file_extension.replace(".", ""),
        file_size=file_size,
        user_id=current_user.id
    )
    
    return document

@router.get("/", response_model=List[DocumentSchema])
async def get_user_documents(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    skip: int = 0,
    limit: int = 100
):
    """Get all documents for the current user (requires authentication)"""
    documents = db.query(Document).filter(Document.user_id == current_user.id).offset(skip).limit(limit).all()
    return documents

@router.get("/{document_id}", response_model=DocumentSchema)
async def get_document(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get document metadata (requires authentication)"""
    # Get document from database and verify ownership
    document = db.query(Document).filter(Document.id == document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
        
    if document.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to access this document")
        
    return document

@router.get("/{document_id}/search", response_model=List[SearchResult])
async def search_document(document_id: int, query: str):
    """Search within a document using semantic search"""
    # Implementation will go here
    return [
        {
            "chunk_id": f"doc_{document_id}_chunk_1",
            "text": "This is a sample text chunk that matches the query.",
            "page_number": 1,
            "relevance_score": 0.95
        }
    ]

@router.post("/{document_id}/summarize")
async def summarize_document(document_id: int):
    """Generate an AI summary of the document"""
    # Implementation will go here
    return {"summary": "This is a placeholder for the document summary."}
