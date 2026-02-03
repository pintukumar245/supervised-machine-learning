# 🔧 Provider Dashboard - Troubleshooting Guide

## समस्या: Provider Login के बाद Dashboard नहीं दिख रहा है

### ✅ समाधान:

---

## 1️⃣ **Backend Server Check करो**

```bash
# Backend running है या नहीं check करो
# पोर्ट 8001 पर होना चाहिए

http://127.0.0.1:8001/api/auth/me/

# अगर यह काम करता है तो backend ठीक है
```

---

## 2️⃣ **Frontend Environment Variables**

**File:** `frontend/.env.local`

```
NEXT_PUBLIC_API_URL=http://127.0.0.1:8001/api/
NEXT_PUBLIC_WS_URL=ws://127.0.0.1:8001/ws/notifications/
NEXT_PUBLIC_MEDIA_BASE_URL=http://127.0.0.1:8001
```

✅ ये file create हो चुकी है

---

## 3️⃣ **Token Check करो**

Browser console में चलाओ:
```javascript
// Cookies में access_token है या नहीं
document.cookie

// या
localStorage.getItem('access_token')
```

अगर token नहीं है तो login करना पड़ेगा

---

## 4️⃣ **API Connection Test करो**

```bash
# Terminal से test करो
curl http://127.0.0.1:8001/api/services/jobs/

# या browser console में:
fetch('http://127.0.0.1:8001/api/services/jobs/', {
  headers: {
    'Authorization': `Bearer YOUR_TOKEN`
  }
}).then(r => r.json()).then(d => console.log(d))
```

---

## 5️⃣ **Browser Console में Errors देखो**

```
F12 दबाओ → Console tab → देखो क्या error हैं
```

**Common Errors:**

| Error | Solution |
|-------|----------|
| `Cannot read property 'role' of undefined` | Auth context load नहीं हुआ - wait करो |
| `WebSocket connection failed` | Backend WebSocket नहीं चल रहा - ignore करो |
| `404 not found on /services/jobs/` | Backend endpoint नहीं है |
| `401 Unauthorized` | Token invalid है - login करो फिर से |
| `Network error` | Backend server नहीं चल रहा |

---

## 6️⃣ **Fixes Applied** ✅

हमने ये fixes किये हैं:

✅ WebSocket error handling जोड़ी (अब fail होने पर भी dashboard show होगा)  
✅ API error handling improve की  
✅ Loading state बेहतर बनाई  
✅ Role-based redirect जोड़ा  
✅ Environment variables set किये  
✅ Better error messages add किये  

---

## 7️⃣ **Step-by-Step Fix करो**

### **Backend को शुरू करो:**
```bash
cd backend
python manage.py runserver
# Should show: http://127.0.0.1:8000/
```

### **Frontend को शुरू करो:**
```bash
cd frontend
npm run dev
# Should show: http://localhost:3000
```

### **Login करो:**
```
1. http://localhost:3000/login
2. Phone number डालो
3. OTP डालो
4. Role: Provider select करो
5. Dashboard खुल जाएगा!
```

---

## 8️⃣ **Check करो कि सब काम कर रहा है**

```javascript
// Browser Console में:
console.log(document.cookie) // Token होना चाहिए
console.log(localStorage) // user info होना चाहिए
```

---

## 9️⃣ **अगर फिर भी काम नहीं कर रहा है:**

```bash
# 1. Cache clear करो
npm run build
npm run dev

# 2. Browser cache clear करो
# Ctrl+Shift+Delete

# 3. Hard refresh करो
# Ctrl+Shift+R

# 4. Backend database check करो
python manage.py shell
>>> from users.models import User
>>> User.objects.filter(role='PROVIDER').count()
```

---

## 🔟 **File Changes Made**

```
✅ /frontend/src/app/dashboard/provider/page.tsx
   - Better WebSocket error handling
   - Improved loading state
   - Role-based redirect
   - Better error messages

✅ /frontend/.env.local (NEW)
   - Environment variables set
```

---

## ⚡ **Quick Fixes**

```bash
# Browser में:
1. F12 दबाओ
2. Console check करो
3. Refresh करो (Ctrl+R)
4. आधा मिनट wait करो
```

---

## 📞 **Still Not Working?**

यह check करो:

1. ✅ Backend चल रहा है?
   ```
   http://127.0.0.1:8001/api/
   ```

2. ✅ Frontend serve हो रहा है?
   ```
   http://localhost:3000
   ```

3. ✅ User का role PROVIDER है?
   ```
   Backend में check करो: python manage.py shell
   >>> from users.models import User; User.objects.filter(username='your_user').first().role
   ```

4. ✅ Token valid है?
   ```
   Browser console: document.cookie
   ```

5. ✅ Jobs API काम कर रहा है?
   ```
   curl -H "Authorization: Bearer TOKEN" http://127.0.0.1:8001/api/services/jobs/
   ```

---

## 💡 **Pro Tips**

```bash
# Terminal में real-time logs देखो:
tail -f backend/server_output.txt

# या Backend को verbose mode में चलाओ:
python manage.py runserver --verbosity 3

# Frontend में हर change को watch करो:
npm run dev
```

---

**अगर अभी भी issue है तो सब console errors screenshot भेजो! 📸**
