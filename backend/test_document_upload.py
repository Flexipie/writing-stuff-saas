"""Test script for document upload and processing"""
import os
import sys
import json
import requests
from pprint import pprint

# URL of the API
API_URL = "http://localhost:8000"

# Test user credentials (same as in test_auth.py)
test_user = {
    "email": "test@example.com",
    "username": "testuser",
    "password": "Test1234!"
}

def get_access_token():
    """Get access token for authentication"""
    url = f"{API_URL}/api/v1/auth/login"
    login_data = {
        "username": test_user["email"],  # OAuth2 form uses username field for email
        "password": test_user["password"]
    }
    
    response = requests.post(url, data=login_data)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("access_token")
    else:
        print(f"Failed to get access token. Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        return None

def upload_sample_pdf(token):
    """Upload a sample PDF file"""
    print("\n--- Testing Document Upload ---")
    
    if not token:
        print("No access token available. Skipping test.")
        return None
    
    # Create a simple test text file for upload
    test_file_path = "test_document.txt"
    try:
        with open(test_file_path, "w") as f:
            f.write("This is a test document.\n")
            f.write("It contains some text for testing the document processing functionality.\n")
            f.write("The system should extract this text and split it into chunks.\n")
            f.write("Each chunk should be stored in the database for later retrieval.\n\n")
            
            # Add more text to ensure we have enough for multiple chunks
            for i in range(20):
                f.write(f"This is line {i+1} of the test document. " * 3 + "\n")
                
        print(f"Created test text file at {test_file_path}")
    except Exception as e:
        print(f"Failed to create test file: {str(e)}")
        return None
    
    # Upload the text file
    url = f"{API_URL}/api/v1/documents"
    headers = {"Authorization": f"Bearer {token}"}
    
    with open(test_file_path, "rb") as f:
        files = {"file": (os.path.basename(test_file_path), f, "text/plain")}
        data = {"title": "Test Document", "description": "A test document for text processing"}
        
        response = requests.post(url, headers=headers, files=files, data=data)
        
        print(f"Status Code: {response.status_code}")
        try:
            result = response.json()
            print("Response:")
            pprint(result)
            return result.get("id")
        except Exception as e:
            print(f"Error: {e}")
            print(f"Response: {response.text}")
            return None

def get_document_details(token, document_id):
    """Get document details"""
    print("\n--- Getting Document Details ---")
    
    if not token or not document_id:
        print("Missing token or document ID. Skipping test.")
        return
    
    url = f"{API_URL}/api/v1/documents/{document_id}"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers)
    
    print(f"Status Code: {response.status_code}")
    try:
        print("Response:")
        pprint(response.json())
    except Exception as e:
        print(f"Error: {e}")
        print(f"Response: {response.text}")

if __name__ == "__main__":
    # Get access token
    token = get_access_token()
    
    if not token:
        print("Failed to get access token. Exiting.")
        sys.exit(1)
    
    # Upload a test document
    document_id = upload_sample_pdf(token)
    
    if document_id:
        # Get document details
        get_document_details(token, document_id)
        print("\n✅ Document upload test completed!")
    else:
        print("\n❌ Document upload test failed!")
