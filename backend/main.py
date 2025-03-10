from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    title="WritingStuff API",
    description="API for AI-powered writing assistant and PDF research summarizer",
    version="0.1.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to WritingStuff API", "status": "online"}

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Import and include routers
# Will be implemented in phase B and beyond
# app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
# app.include_router(documents_router, prefix="/documents", tags=["Documents"])
# app.include_router(ai_router, prefix="/ai", tags=["AI Services"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
