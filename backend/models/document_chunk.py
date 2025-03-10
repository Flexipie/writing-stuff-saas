from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float
from sqlalchemy.orm import relationship

from models.base import Base

class DocumentChunk(Base):
    """
    Model for storing document chunks for vector search
    """
    __tablename__ = "document_chunks"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id", ondelete="CASCADE"))
    chunk_id = Column(String, index=True, nullable=False)  # Unique ID for the chunk
    content = Column(Text, nullable=False)  # Text content of the chunk
    page_number = Column(Integer, nullable=True)  # Page number where the chunk is from
    chunk_index = Column(Integer, nullable=False)  # Index of the chunk within the document
    vector_id = Column(String, nullable=True)  # ID for retrieval from vector DB
    
    # Define relationship with Document
    document = relationship("Document", backref="chunks")
    
    @classmethod
    def create(cls, db, document_id, chunk_id, content, page_number, chunk_index, vector_id=None):
        """
        Create a new document chunk record
        """
        chunk = cls(
            document_id=document_id,
            chunk_id=chunk_id,
            content=content,
            page_number=page_number,
            chunk_index=chunk_index,
            vector_id=vector_id
        )
        db.add(chunk)
        db.commit()
        db.refresh(chunk)
        return chunk
    
    @classmethod
    def get_by_document_id(cls, db, document_id, skip=0, limit=100):
        """
        Get all chunks for a document
        """
        return db.query(cls).filter(cls.document_id == document_id).offset(skip).limit(limit).all()
