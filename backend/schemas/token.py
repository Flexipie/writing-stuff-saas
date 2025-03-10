from typing import Optional
from pydantic import BaseModel


class Token(BaseModel):
    """Model for token response"""
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    """Model for token payload"""
    sub: Optional[str] = None
