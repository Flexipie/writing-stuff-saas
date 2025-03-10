from models.base import Base, get_db
from models.user import User
from models.document import Document

# Export all models for easy importing
__all__ = ["Base", "get_db", "User", "Document"]
