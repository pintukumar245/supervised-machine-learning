# 🔧 Code Changes - Indian Phone Validation

## File 1: Frontend Login Page
**Location:** `frontend/src/app/login/page.tsx`

### Change 1: Import Statements
**Status:** ✅ Already correct (no changes needed)

### Change 2: Add phoneError State
```typescript
// NEW - Add this line with other state declarations
const [phoneError, setPhoneError] = useState(''); // Phone validation error
```

### Change 3: Add Validation Function
```typescript
// NEW - Add this function after state declarations
const validateIndianPhone = (phoneNumber: string): string => {
    """Validate Indian phone number format - exactly 10 digits, starts with 6-9"""
    // Remove whitespace
    const cleanPhone = phoneNumber.trim();
    
    // Check if empty
    if (!cleanPhone) {
        return "Phone number is required";
    }
    
    // Check if it contains only digits
    if (!/^\d+$/.test(cleanPhone)) {
        return "Phone number must contain only digits. No letters or special characters allowed.";
    }
    
    // Check if it's exactly 10 digits
    if (cleanPhone.length !== 10) {
        return "Invalid phone number. Indian phone numbers must be exactly 10 digits.";
    }
    
    // Check if it starts with 6-9 (valid Indian mobile numbers)
    if (!/^[6-9]/.test(cleanPhone)) {
        return "Invalid Indian phone number. Must start with 6, 7, 8, or 9.";
    }
    
    return ""; // No error
};
```

### Change 4: Add Phone Change Handler
```typescript
// NEW - Add this function after validateIndianPhone
const handlePhoneChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    setPhone(value);
    
    // Only validate if user has started typing
    if (value) {
        const error = validateIndianPhone(value);
        setPhoneError(error);
    } else {
        setPhoneError("");
    }
};
```

### Change 5: Update handlePhoneSubmit Function
**BEFORE:**
```typescript
const handlePhoneSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (phone.length < 10) {
        alert("Phone number must be at least 10 digits");
        return;
    }
    try {
        const gOtp = await generateOtp(phone, role, referralCode);
        setGeneratedOtp(gOtp);
        setStep('OTP');
    } catch (error: any) {
        console.error(error);
        alert('Failed to send OTP: ' + (error.response?.data?.error || error.message));
    }
};
```

**AFTER:**
```typescript
const handlePhoneSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    // Validate phone number
    const error = validateIndianPhone(phone);
    if (error) {
        setPhoneError(error);
        alert(error);
        return;
    }
    
    setPhoneError(""); // Clear error if validation passes
    
    try {
        const gOtp = await generateOtp(phone, role, referralCode);
        setGeneratedOtp(gOtp);
        setStep('OTP');
    } catch (error: any) {
        console.error(error);
        const errorMsg = error.response?.data?.error || error.message || 'Failed to send OTP';
        setPhoneError(errorMsg);
        alert('Failed to send OTP: ' + errorMsg);
    }
};
```

### Change 6: Update Phone Input Field in JSX
**BEFORE:**
```tsx
<div>
    <label className="mb-1 block text-sm font-medium text-gray-700">Phone Number</label>
    <div className="relative">
        <Phone className="absolute left-3 top-3 h-5 w-5 text-gray-400" />
        <input
            type="tel"
            className="block w-full rounded-lg border border-gray-300 p-2.5 pl-10 text-gray-900 focus:border-blue-500 focus:ring-blue-500"
            placeholder="9876543210"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
            required
        />
    </div>
</div>
```

**AFTER:**
```tsx
<div>
    <label className="mb-1 block text-sm font-medium text-gray-700">Phone Number</label>
    <div className="relative">
        <Phone className="absolute left-3 top-3 h-5 w-5 text-gray-400" />
        <input
            type="tel"
            className={`block w-full rounded-lg border p-2.5 pl-10 text-gray-900 focus:border-blue-500 focus:ring-blue-500 ${
                phoneError ? 'border-red-500 bg-red-50' : 'border-gray-300'
            }`}
            placeholder="9876543210"
            value={phone}
            onChange={handlePhoneChange}
            required
        />
    </div>
    {phoneError && (
        <p className="mt-1 text-sm text-red-600 font-medium">❌ {phoneError}</p>
    )}
    <p className="mt-1 text-xs text-gray-500">💡 Indian phone numbers must be exactly 10 digits</p>
</div>
```

---

## File 2: Backend Serializers
**Location:** `backend/users/serializers.py`

### Change 1: Add Import (if not already present)
```python
import re  # Add this to imports
```

### Change 2: Update GenerateOTPSerializer
**BEFORE:**
```python
class GenerateOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    role = serializers.ChoiceField(choices=['CUSTOMER', 'PROVIDER'], required=False)
    referral_code = serializers.CharField(max_length=10, required=False, allow_blank=True)
```

**AFTER:**
```python
class GenerateOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    role = serializers.ChoiceField(choices=['CUSTOMER', 'PROVIDER'], required=False)
    referral_code = serializers.CharField(max_length=10, required=False, allow_blank=True)
    
    def validate_phone_number(self, value):
        """Validate Indian phone number - exactly 10 digits, no special characters"""
        # Remove any whitespace
        phone = value.strip()
        
        # Check if it contains only digits
        if not phone.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits. No letters or special characters allowed.")
        
        # Check if it's exactly 10 digits
        if len(phone) != 10:
            raise serializers.ValidationError("Invalid phone number. Indian phone numbers must be exactly 10 digits.")
        
        # Optionally validate that it starts with 6-9 (Indian mobile numbers usually start with these)
        if phone[0] not in ['6', '7', '8', '9']:
            raise serializers.ValidationError("Invalid Indian phone number. Must start with 6, 7, 8, or 9.")
        
        return phone
```

### Change 3: Update VerifyOTPSerializer
**BEFORE:**
```python
class VerifyOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    otp = serializers.CharField(max_length=6)
```

**AFTER:**
```python
class VerifyOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    otp = serializers.CharField(max_length=6)
    
    def validate_phone_number(self, value):
        """Validate Indian phone number - exactly 10 digits, no special characters"""
        # Remove any whitespace
        phone = value.strip()
        
        # Check if it contains only digits
        if not phone.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits. No letters or special characters allowed.")
        
        # Check if it's exactly 10 digits
        if len(phone) != 10:
            raise serializers.ValidationError("Invalid phone number. Indian phone numbers must be exactly 10 digits.")
        
        # Validate that it starts with 6-9 (Indian mobile numbers usually start with these)
        if phone[0] not in ['6', '7', '8', '9']:
            raise serializers.ValidationError("Invalid Indian phone number. Must start with 6, 7, 8, or 9.")
        
        return phone
```

---

## Summary of Changes

### Frontend Changes:
1. ✅ Added `phoneError` state
2. ✅ Added `validateIndianPhone()` function
3. ✅ Added `handlePhoneChange()` function  
4. ✅ Updated `handlePhoneSubmit()` function
5. ✅ Updated phone input field with error styling
6. ✅ Added error message display
7. ✅ Added helpful hint text

### Backend Changes:
1. ✅ Added `validate_phone_number()` method to `GenerateOTPSerializer`
2. ✅ Added `validate_phone_number()` method to `VerifyOTPSerializer`

### New Files:
1. ✅ `backend/test_phone_validation.py` - Test file
2. ✅ `INDIAN_PHONE_VALIDATION_GUIDE.md` - Guide
3. ✅ `PHONE_VALIDATION_IMPLEMENTATION_COMPLETE.md` - Summary

---

## ✅ All Changes Applied Successfully!

Both frontend and backend are now validating Indian phone numbers correctly. Users will see clear error messages for invalid entries.

