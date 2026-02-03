# Payment Method Selector - Quick Testing Guide

## ⚡ Quick Start Testing

### Step 1: Ensure Backend is Running
```powershell
# Terminal 1 - Backend
cd backend
python manage.py runserver 0.0.0.0:8001
# Wait for "Starting development server at http://127.0.0.1:8001/"
```

### Step 2: Ensure Frontend is Running
```powershell
# Terminal 2 - Frontend
cd frontend
npm run dev
# Visit http://localhost:3000
```

### Step 3: Login as Customer
1. Go to http://localhost:3000/login
2. Enter phone: `9876543210` (test customer)
3. Enter OTP: `123456` (or use actual OTP)
4. Click "Login"
5. Should redirect to `/dashboard/customer`

---

## 🧪 Test Scenarios

### Test 1: Payment Method Selection Opens
```
✅ Expected:
1. Navigate to customer dashboard
2. Click any "Pay" button on a job
3. Beautiful bottom sheet modal opens
4. Shows 4 payment options: UPI, PhonePe, Google Pay, Paytm
5. Shows amount to pay

❌ If not working:
- Check browser console for errors
- Verify PaymentMethodSelector component imported
- Check if CSS animations work
```

### Test 2: Select UPI Payment
```
✅ Expected:
1. Click on "UPI Payment" option
2. It shows checkmark (selected)
3. Below shows UPI details:
   - UPI ID: pintuk33621@okhdfcbank
   - Copy button
   - QR code instructions
4. "Proceed to Upload Proof" button enabled

❌ If not working:
- Check state is updating (dev tools)
- Verify UPI ID is correct
- Check copy button functionality
```

### Test 3: Copy UPI ID
```
✅ Expected:
1. Click copy button next to UPI ID
2. Toast notification: "✅ UPI ID copied to clipboard!"
3. Can paste (Ctrl+V) elsewhere to verify

❌ If not working:
- May require HTTPS (clipboard API requirement)
- Check browser permissions
- Look for console errors
```

### Test 4: Proceed to Proof Upload
```
✅ Expected:
1. Click "Proceed to Upload Proof" button
2. Modal changes to show:
   - UPI Payment component (static display)
   - PaymentProofUpload form
   - Proof Type dropdown
   - UTR input field
   - File upload area
   - Step-by-step instructions

❌ If not working:
- Verify PaymentProofUpload component loaded
- Check if form displays correctly
- Look for React component errors
```

### Test 5: Upload Payment Proof
```
✅ Expected:
1. Select proof type from dropdown
2. Enter UTR number (e.g., "123456789")
3. Upload screenshot file (JPG/PNG)
4. Click "Upload" button
5. Shows loading spinner
6. After 2-3 seconds: Toast "✅ Payment proof uploaded!"
7. Modal changes to success screen

❌ If not working:
- Check API endpoint: POST /api/payments/proof/
- Verify backend is running
- Check network tab for request/response
- Look for validation errors
```

### Test 6: Success Screen
```
✅ Expected:
1. Shows ✅ checkmark
2. Title: "Payment Proof Submitted!"
3. Message about admin verification
4. "Continue Browsing" button

❌ If not working:
- Check success screen HTML rendering
- Verify animations work
- Check "Continue Browsing" link works
```

---

## 🐛 Debugging Checklist

### Frontend Issues
```
□ Check browser console (F12) for errors
□ Check Network tab for API requests
□ Verify all imports are correct in customer/page.tsx
□ Verify PaymentMethodSelector component file exists
□ Check if Tailwind CSS classes render
□ Verify animations work (fade-in, slide-in, etc.)
```

### Backend Issues
```
□ Backend running on port 8001? (netstat -ano | findstr 8001)
□ API endpoint exists? /api/payments/proof/
□ Permissions class set correctly?
□ File upload working?
□ CORS headers allowing frontend?
```

### Common Errors

**Error**: "PaymentMethodSelector is not defined"
```
Solution: Check import at top of customer/page.tsx
import PaymentMethodSelector from '@/components/PaymentMethodSelector';
```

**Error**: "Cannot read property 'clipboard'"
```
Solution: HTTPS required for clipboard in prod. In dev, may work with localhost.
Workaround: Use manual copy text selection
```

**Error**: "Payment proof upload failed"
```
Solution: 
1. Check backend is running
2. Verify /api/payments/proof/ endpoint exists
3. Check file size not too large
4. Check browser has permission to upload files
```

**Error**: "Modal doesn't show"
```
Solution:
1. Check if paymentMethodOpen state is true
2. Check if z-index overlaps with other elements
3. Try clearing CSS cache (Ctrl+Shift+Delete in browser)
```

---

## 📊 Expected Test Results

| Test | Status | Evidence |
|------|--------|----------|
| Method selector opens | ✅/❌ | Modal visible? |
| UPI option selectable | ✅/❌ | Checkmark appears? |
| Copy button works | ✅/❌ | Toast notification? |
| Proof upload opens | ✅/❌ | Form visible? |
| File upload works | ✅/❌ | No validation errors? |
| API request sent | ✅/❌ | Network tab shows POST? |
| Success screen shows | ✅/❌ | ✅ emoji visible? |
| Continues browsing | ✅/❌ | Back to dashboard? |

---

## 📝 Manual Testing Flow

### Test Case 1: Complete Happy Path
```
1. Customer logs in ✓
2. Views available jobs ✓
3. Clicks "Pay" on any job ✓
4. Payment method selector opens ✓
5. Selects "UPI Payment" ✓
6. Sees UPI ID: pintuk33621@okhdfcbank ✓
7. Copies UPI ID ✓
8. Clicks "Proceed to Upload Proof" ✓
9. Uploads payment screenshot ✓
10. Enters UTR number ✓
11. Clicks "Upload" ✓
12. Sees success message ✓
13. Clicks "Continue Browsing" ✓
14. Back on dashboard ✓

Expected: All steps successful, no errors
```

### Test Case 2: Cancel Payment
```
1. Payment method selector opens ✓
2. Clicks "Cancel" button ✓

Expected: Modal closes, back to jobs list
```

### Test Case 3: Change Payment Method
```
1. Method selector opens ✓
2. Selects "UPI Payment" ✓
3. Sees proof upload form ✓
4. Clicks "Back to Payment Method" ✓
5. Back to method selector ✓
6. Selects different method ✓

Expected: Can change method without issues
```

### Test Case 4: File Validation
```
1. Tries uploading without selecting proof type ✓
2. Should show error ✓
3. Tries uploading without UTR ✓
4. Should show error ✓
5. Tries uploading wrong file type ✓
6. Should show file type error ✓

Expected: All validations work
```

---

## 🔧 Configuration

### To Change UPI ID
**File**: `frontend/src/components/PaymentMethodSelector.tsx`
```tsx
// Line ~14
const upiId = 'pintuk33621@okhdfcbank';
// Change to your UPI ID
```

### To Change App Deep Links
**File**: `frontend/src/components/PaymentMethodSelector.tsx`
```tsx
// Add more handlers in handleOpenUPIApp() function
// Example: Google Pay UPI link format:
// googlepay://upi/pay?pa=UPI_ID&am=AMOUNT
```

### To Change Colors
**File**: `frontend/src/components/PaymentMethodSelector.tsx`
```tsx
// All color classes are Tailwind CSS
// Change bg-blue-600 to any Tailwind color
// Examples: bg-green-600, bg-purple-600, etc.
```

---

## 📞 Support

### If Payment Method Selector Doesn't Open
1. Check if `PaymentMethodSelector` imported correctly
2. Check if `paymentMethodOpen` state is being set
3. Look at console for TypeScript errors

### If Upload Fails
1. Check backend running on port 8001
2. Check `/api/payments/proof/` endpoint exists
3. Verify user is authenticated (token in cookies)
4. Check file size < 10MB

### If No Toast Notifications
1. Check if `react-hot-toast` is installed
2. Verify Toaster component in layout.tsx
3. Check browser console for errors

---

## ✅ Final Verification

Before declaring complete, verify:
- [ ] Payment method selector opens on Pay button click
- [ ] All 4 payment methods display correctly
- [ ] UPI copy button works and shows toast
- [ ] Proof upload form displays
- [ ] File upload validation works
- [ ] Success message shows after upload
- [ ] Proof appears in admin dashboard
- [ ] No console errors
- [ ] No network errors in browser dev tools
- [ ] Mobile responsive (test on phone if possible)

---

## 📱 Mobile Testing

The payment method selector is designed to be mobile-first.

```
Test on mobile:
1. Open http://192.168.1.X:3000 (your local IP)
2. Click Pay button
3. Bottom sheet should slide up nicely
4. All buttons should be easily tappable
5. Text should be readable
6. File upload should work

Expected: Smooth experience on mobile
```

---

**Testing Date**: January 29, 2026
**Tester**: You
**Status**: Ready for QA Testing
**Version**: v1.0
