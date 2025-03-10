"""Test script to check imports and database connection"""
import os
import sys

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    # Test imports
    from core.config import settings
    from models.base import engine, Base, get_db
    from models.user import User
    from models.document import Document
    from routers import auth, documents, ai
    
    # Print success message
    print("✅ Imports working correctly!")
    
    # Try to connect to the database
    try:
        # Create a test connection
        connection = engine.connect()
        connection.close()
        print(f"✅ Successfully connected to database at {settings.DATABASE_URL}")
        
        # Create tables if they don't exist
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully")
        
    except Exception as e:
        print(f"❌ Database connection error: {e}")
        
except Exception as e:
    print(f"❌ Import error: {e}")
