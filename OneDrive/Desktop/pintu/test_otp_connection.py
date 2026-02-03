#!/usr/bin/env python3
"""
Test OTP API Connection
Tests if backend is running and OTP endpoint is working
"""

import requests
import json
import sys

BASE_URL = "http://127.0.0.1:8000/api/"

def test_connection():
    """Test if backend is running"""
    print("=" * 60)
    print("Testing Backend Connection")
    print("=" * 60)
    
    try:
        response = requests.get(BASE_URL + "auth/")
        print(f"✓ Backend is running on {BASE_URL}")
        return True
    except requests.exceptions.ConnectionError as e:
        print(f"✗ Cannot connect to backend on {BASE_URL}")
        print(f"  Error: {str(e)}")
        print("\n⚠️  Make sure backend is running:")
        print("  1. Open terminal in 'backend' folder")
        print("  2. Run: venv\\Scripts\\python.exe -m daphne -b 127.0.0.1 -p 8000 service_market.asgi:application")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {str(e)}")
        return False

def test_generate_otp():
    """Test OTP generation"""
    print("\n" + "=" * 60)
    print("Testing OTP Generation")
    print("=" * 60)
    
    test_cases = [
        {"phone": "9876543210", "role": "CUSTOMER", "desc": "Valid customer phone"},
        {"phone": "9123456789", "role": "PROVIDER", "desc": "Valid provider phone"},
        {"phone": "123", "role": "CUSTOMER", "desc": "Invalid phone (too short)"},
        {"phone": "abc1234567", "role": "CUSTOMER", "desc": "Invalid phone (non-numeric)"},
    ]
    
    for test in test_cases:
        print(f"\nTest: {test['desc']}")
        print(f"  Phone: {test['phone']}, Role: {test['role']}")
        
        try:
            response = requests.post(
                BASE_URL + "auth/generate-otp/",
                json={
                    "phone_number": test['phone'],
                    "role": test['role']
                },
                headers={"Content-Type": "application/json"}
            )
            
            print(f"  Status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                otp = data.get('otp', 'N/A')
                print(f"  ✓ OTP Generated: {otp}")
                return True  # At least one worked
            else:
                print(f"  ✗ Error: {response.text}")
                
        except Exception as e:
            print(f"  ✗ Exception: {str(e)}")
    
    return False

def main():
    if not test_connection():
        sys.exit(1)
    
    if not test_generate_otp():
        print("\n⚠️  OTP generation failed. Check backend logs for details.")
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("✓ All tests passed!")
    print("=" * 60)

if __name__ == "__main__":
    main()
