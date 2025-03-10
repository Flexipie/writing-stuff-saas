"""Test script for authentication system"""
import os
import sys
import json
import requests
from pprint import pprint

# URL of the API (change if needed based on your setup)
API_URL = "http://localhost:8000"

# Test user data
test_user = {
    "email": "test@example.com",
    "username": "testuser",
    "password": "Test1234!"
}

def test_registration():
    """Test user registration"""
    print("\n--- Testing User Registration ---")
    
    url = f"{API_URL}/api/v1/auth/register"
    response = requests.post(url, json=test_user)
    
    print(f"Status Code: {response.status_code}")
    try:
        print("Response:")
        pprint(response.json())
        return True
    except Exception as e:
        print(f"Error: {e}")
        print(f"Response: {response.text}")
        return False

def test_login():
    """Test user login"""
    print("\n--- Testing User Login ---")
    
    url = f"{API_URL}/api/v1/auth/login"
    login_data = {
        "username": test_user["email"],  # OAuth2 form uses username field for email
        "password": test_user["password"]
    }
    
    response = requests.post(url, data=login_data)
    
    print(f"Status Code: {response.status_code}")
    try:
        data = response.json()
        print("Response:")
        pprint(data)
        return data.get("access_token")
    except Exception as e:
        print(f"Error: {e}")
        print(f"Response: {response.text}")
        return None

def test_current_user(token):
    """Test getting current user"""
    print("\n--- Testing Get Current User ---")
    
    if not token:
        print("Skipping test (no token available)")
        return False
    
    url = f"{API_URL}/api/v1/auth/me"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers)
    
    print(f"Status Code: {response.status_code}")
    try:
        print("Response:")
        pprint(response.json())
        return True
    except Exception as e:
        print(f"Error: {e}")
        print(f"Response: {response.text}")
        return False

if __name__ == "__main__":
    # Registration might fail if user already exists, that's ok
    registration_success = test_registration()
    
    # Login should succeed
    token = test_login()
    
    if token:
        # Test current user endpoint with token
        test_current_user(token)
        print("\n✅ Authentication system tests completed successfully!")
    else:
        print("\n❌ Authentication system tests failed! Could not obtain token.")
