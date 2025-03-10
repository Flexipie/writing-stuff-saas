from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func
from passlib.context import CryptContext

from models.base import Base

# Password context for hashing and verification
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    """
    User model for authentication and user management
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    @classmethod
    def create(cls, db, email, username, password):
        """
        Create a new user with hashed password
        """
        hashed_password = pwd_context.hash(password)
        user = cls(
            email=email,
            username=username,
            hashed_password=hashed_password
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def verify_password(plain_password, hashed_password):
        """
        Verify a plain password against a hashed password
        """
        return pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def authenticate(cls, db, email, password):
        """
        Authenticate a user with email and password
        """
        user = db.query(cls).filter(cls.email == email).first()
        if not user:
            return None
        if not cls.verify_password(password, user.hashed_password):
            return None
        return user
