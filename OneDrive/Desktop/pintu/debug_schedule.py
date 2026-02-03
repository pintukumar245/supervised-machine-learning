import requests
import json

BASE_URL = "http://127.0.0.1:8001/api"

# 1. Login as Customer
def login(username, password):
    res = requests.post(f"{BASE_URL}/auth/token/", data={'username': username, 'password': password})
    if res.status_code == 200:
        return res.json()['access']
    print("Login Failed", res.text)
    return None

token = login('customer', 'password123') # Ensure this user exists
if not token:
    exit()

headers = {'Authorization': f'Bearer {token}'}

# 2. Get a category and provider
cats = requests.get(f"{BASE_URL}/services/categories/", headers=headers).json()
if not cats:
    print("No categories")
    exit()
cat_id = cats[0]['id']

providers = requests.get(f"{BASE_URL}/auth/providers/?category={cat_id}", headers=headers).json()
if not providers:
    print("No providers")
    exit()
provider_id = providers[0]['id']

# 3. Create Scheduled Job
data = {
    "category": cat_id,
    "provider_id": provider_id,
    "description": "Debug Scheduled Job",
    "address": "123 Debug Lane",
    "scheduled_time": "2026-02-01T10:00:00Z"
}

print("Sending Data:", data)
res = requests.post(f"{BASE_URL}/services/jobs/", json=data, headers=headers)
print("Response Status:", res.status_code)
print("Response Data:", res.json())

if res.status_code == 201:
    job = res.json()
    print(f"Job Created. Scheduled Time: {job.get('scheduled_time')}")
    if job.get('scheduled_time'):
        print("SUCCESS! Backend is saving scheduled_time.")
    else:
        print("FAILURE! Backend did NOT save scheduled_time.")
else:
    print("Failed to create job")
