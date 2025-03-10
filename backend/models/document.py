from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from models.base import Base

class Document(Base):
    """
    Document model for storing uploaded documents (PDFs, text files, etc.)
    """
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text, nullable=True)
    file_path = Column(String, nullable=False)  # Path to the file in storage
    file_type = Column(String, nullable=False)  # PDF, TXT, etc.
    file_size = Column(Integer, nullable=False)  # Size in bytes
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Define relationship with User
    user = relationship("User", backref="documents")

    @classmethod
    def create(cls, db, title, description, file_path, file_type, file_size, user_id):
        """
        Create a new document record
        """
        document = cls(
            title=title,
            description=description,
            file_path=file_path,
            file_type=file_type,
            file_size=file_size,
            user_id=user_id
        )
        db.add(document)
        db.commit()
        db.refresh(document)
        return document
