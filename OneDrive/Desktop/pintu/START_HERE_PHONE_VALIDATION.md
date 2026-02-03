# 🚀 Quick Start - Indian Phone Validation

## ✅ What's Done?

Your app now validates **only Indian phone numbers** (10 digits) during login. Invalid entries show **red error messages**.

---

## ⚡ Quick Test (2 Minutes)

### Step 1: Start Servers

**Terminal 1:**
```powershell
cd backend
python manage.py runserver 0.0.0.0:8001
```

**Terminal 2:**
```powershell
cd frontend
npm run dev
```

### Step 2: Open Browser
```
http://localhost:3000/login
```

### Step 3: Test Invalid Number
```
Enter: 987654321 (9 digits)
See: Red error → "must be exactly 10 digits"
```

### Step 4: Test Valid Number
```
Enter: 9876543210 (10 digits)
See: No error, can click "Send OTP"
```

---

## ✨ What You'll See

### Invalid Number ❌
```
Phone Number: [987654321̶]  ← RED BORDER
❌ Invalid phone number. Indian phone numbers 
   must be exactly 10 digits.
```

### Valid Number ✅
```
Phone Number: [9876543210]  ← NORMAL BORDER
💡 Indian phone numbers must be exactly 10 digits
```

---

## 📋 Test Cases

### Invalid (Will Show Error) ❌
- `987654321` (9 digits)
- `98765432101` (11 digits)
- `9876543a10` (has letter)
- `9876-543210` (has dash)
- `5876543210` (starts with 5)

### Valid (Will Work) ✅
- `9876543210` (starts with 9)
- `8765432109` (starts with 8)
- `7654321098` (starts with 7)
- `6543210987` (starts with 6)

---

## 📁 Files Changed

1. **frontend/src/app/login/page.tsx** - Added validation UI
2. **backend/users/serializers.py** - Added backend validation

---

## 📚 Documentation

**Start Here:**
→ `README_PHONE_VALIDATION.md`

**Quick Reference:**
→ `PHONE_VALIDATION_QUICK_REFERENCE.md`

**Visual Guide:**
→ `PHONE_VALIDATION_VISUAL_GUIDE.md`

---

## ✅ Rules

Phone numbers must:
1. ✅ Be **exactly 10 digits**
2. ✅ Contain **only numbers** (no letters or special chars)
3. ✅ Start with **6, 7, 8, or 9** (Indian standard)

---

## 🎯 That's It!

Implementation complete and ready to use.

**Start testing now:** http://localhost:3000/login

