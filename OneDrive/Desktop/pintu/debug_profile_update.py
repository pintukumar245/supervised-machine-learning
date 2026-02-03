import urllib.request
import json

BASE_URL = "http://localhost:8001/api/auth/"

def run_debug():
    # 1. Generate OTP
    print("1. Generating OTP...")
    req = urllib.request.Request(
        f"{BASE_URL}generate-otp/", 
        data=json.dumps({"phone_number": "9876543210", "role": "CUSTOMER"}).encode('utf-8'), 
        headers={'Content-Type': 'application/json'}
    )
    with urllib.request.urlopen(req) as res:
        otp_data = json.loads(res.read().decode('utf-8'))
        print(f"   OTP Response: {otp_data}")
        otp = otp_data['otp']

    # 2. Verify OTP to get Token
    print(f"\n2. Verifying OTP {otp}...")
    req = urllib.request.Request(
        f"{BASE_URL}verify-otp/", 
        data=json.dumps({"phone_number": "9876543210", "otp": otp}).encode('utf-8'), 
        headers={'Content-Type': 'application/json'}
    )
    access_token = None
    with urllib.request.urlopen(req) as res:
        token_data = json.loads(res.read().decode('utf-8'))
        print(f"   Token Response: obtained")
        access_token = token_data['access']

    # 3. Update Profile
    print("\n3. Updating Profile (Address & Name)...")
    update_data = {
        "first_name": "Debug",
        "last_name": "User",
        "email": "debug@example.com",
        "address": "123 Debug Lane"
    }
    req = urllib.request.Request(
        f"{BASE_URL}me/", 
        data=json.dumps(update_data).encode('utf-8'), 
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}'
        },
        method='PATCH'
    )
    try:
        with urllib.request.urlopen(req) as res:
            updated_profile = json.loads(res.read().decode('utf-8'))
            print(f"   Update Response Code: {res.getcode()}")
            print(f"   Updated Profile: {json.dumps(updated_profile, indent=2)}")
    except urllib.error.HTTPError as e:
        print(f"   Update Failed: {e.code}")
        print(f"   Response: {e.read().decode('utf-8')}")

if __name__ == "__main__":
    try:
        run_debug()
    except Exception as e:
        print(f"Script Error: {e}")
