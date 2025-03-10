from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from sqlalchemy.orm import Session

from core.config import settings
from models.base import get_db
from models.user import User
from routers.auth import get_current_user

# Create router with tags for OpenAPI documentation
router = APIRouter(tags=["ai"])

# Define Pydantic models for request/response validation
class TextImprovement(BaseModel):
    original_text: str
    improved_text: Optional[str] = None
    suggestions: Optional[List[str]] = None
    
class TextRewriteRequest(BaseModel):
    text: str
    style: Optional[str] = None  # e.g., "formal", "casual", "academic"
    tone: Optional[str] = None  # e.g., "friendly", "professional", "persuasive"
    length: Optional[str] = None  # e.g., "shorter", "longer", "same"
    
class TextRewriteResponse(BaseModel):
    rewritten_text: str
    
class TextSummarizeRequest(BaseModel):
    text: str
    length: Optional[int] = 3  # Number of sentences or paragraphs
    format: Optional[str] = "paragraph"  # paragraph, bullets, key_points

class TextSummarizeResponse(BaseModel):
    summary: str

# OpenAI helper function (placeholder - will implement with actual OpenAI API)
async def generate_openai_response(prompt: str, max_tokens: int = 500) -> str:
    """Generate text using OpenAI API (placeholder implementation)"""
    # Check if OpenAI API key is configured
    if not settings.OPENAI_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="OpenAI API key not configured. Please set OPENAI_API_KEY in environment variables."
        )
    
    # TODO: Implement actual OpenAI API call
    # For now, return a simple echo response
    return f"AI response for: {prompt[:50]}... (placeholder)"

# Routes with authentication
@router.post("/improve_text", response_model=TextImprovement)
async def improve_text(
    text: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Improve text grammar and style (requires authentication)"""
    # Generate prompt for text improvement
    prompt = f"Improve the grammar and style of the following text:\n\n{text}\n\nImproved version:"
    
    # Call OpenAI API (placeholder)
    improved_text = await generate_openai_response(prompt)
    
    # Return response
    return {
        "original_text": text,
        "improved_text": improved_text,
        "suggestions": [
            "Consider using more active voice",
            "Check for consistent tense usage",
            "Review paragraph structure for clarity"
        ]
    }

@router.post("/rewrite", response_model=TextRewriteResponse)
async def rewrite_text(
    request: TextRewriteRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Rewrite text according to specified style and tone (requires authentication)"""
    # Build prompt based on request parameters
    prompt = f"Rewrite the following text"
    
    if request.style:
        prompt += f" in a {request.style} style"
    
    if request.tone:
        prompt += f" with a {request.tone} tone"
        
    if request.length:
        prompt += f" and make it {request.length}"
    
    prompt += f":\n\n{request.text}\n\nRewritten text:"
    
    # Call OpenAI API (placeholder)
    rewritten_text = await generate_openai_response(prompt)
    
    # Return response
    return {"rewritten_text": rewritten_text}

@router.post("/summarize", response_model=TextSummarizeResponse)
async def summarize_text(
    request: TextSummarizeRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Summarize text with AI (requires authentication)"""
    # Build prompt based on request parameters
    format_instruction = ""
    if request.format == "bullets":
        format_instruction = "in bullet points"
    elif request.format == "key_points":
        format_instruction = "highlighting only the key points"
    else:
        format_instruction = "in a concise paragraph"
    
    prompt = f"Summarize the following text in about {request.length} sentences {format_instruction}:\n\n{request.text}\n\nSummary:"
    
    # Call OpenAI API (placeholder)
    summary = await generate_openai_response(prompt)
    
    # Return response
    return {"summary": summary}
