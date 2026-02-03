# 🎯 Provider Dashboard - Quick Start Guide

## How Everything Works (ہندی میں سمجھیے)

---

## 👨‍💼 **Provider (Service Provider) के लिए**

### **Dashboard में क्या दिखता है:**

```
┌─────────────────────────────────────────┐
│  Provider Dashboard                     │
├─────────────────────────────────────────┤
│                                         │
│  📊 Quick Stats                        │
│  ├─ Today Jobs: 5                      │
│  ├─ Completed: 23                      │
│  ├─ Verified: ✅                       │
│  └─ Base Rate: ₹100/visit              │
│                                         │
│  📬 New Job Requests (Grid View)      │
│  ├─ Job Card 1 [Electrical]           │
│  │  ├─ Customer: Rajesh Kumar          │
│  │  ├─ ⏳ Status: PENDING               │
│  │  ├─ 💰 ₹500                         │
│  │  └─ Buttons:                        │
│  │     ✅ Accept | ❌ Reject           │
│  │                                     │
│  └─ Job Card 2 [Plumbing]             │
│                                         │
│  📅 Manage Schedule (Tab)              │
│                                         │
└─────────────────────────────────────────┘
```

### **Jobs की Life Cycle:**

```
1. ⏳ PENDING (नया request आया)
   ├─ ✅ ACCEPT करो या ❌ REJECT करो
   
2. 🎯 ASSIGNED (Customer accept हो गया)
   ├─ 📍 GPS से location देखो
   ├─ 💬 Chat करो customer से
   ├─ 📞 Call करो customer को
   ├─ 🚀 "Start Work" button दबाओ
   
3. 🔧 IN_PROGRESS (काम चल रहा है)
   ├─ 💬 Chat/Call रखो customer से
   ├─ ✨ "Complete Job" दबाओ जब काम हो जाए
   
4. ✅ COMPLETED (काम हो गया)
   ├─ 📄 Invoice download करो
   ├─ 💳 Payment गई customer को
   └─ ⭐ Waiting for rating
```

### **हर Job Card पर क्या मिलता है:**

```
┌──────────────────────────────────────┐
│ ⏳ PENDING          📅 Jan 29, 2025  │
│                                      │
│ Electrical Installation              │
│ Install ceiling fan in bedroom      │
│                                      │
│ 👤 Rajesh Kumar                     │
│    🌟 4.5 rating (50 reviews)       │
│                                      │
│ 📍 Sector 5, Delhi                  │
│ 💰 ₹500                             │
│                                      │
│ Buttons:                            │
│ ┌──────────────────────────────┐   │
│ │ ✅ Accept  |  ❌ Reject      │   │
│ ├──────────────────────────────┤   │
│ │ 💬 Chat  | 📞 Call  | 🗺️ GPS │   │
│ └──────────────────────────────┘   │
└──────────────────────────────────────┘
```

### **Settings/Setup करना:**

**Step 1️⃣: Skills चुनो**
```
🔧 Skills Tab
├─ ⚡ Electrical Work
├─ 🔧 Plumbing
├─ 💄 Beauty Parlor
├─ 🧹 Cleaning
└─ ₹100/visit (Base Price)
```

**Step 2️⃣: Portfolio Upload करो**
```
🖼️ Portfolio Tab
├─ Photo 1: AC repair (Description)
├─ Photo 2: Ceiling fan installation
├─ Photo 3: Before/After
└─ ➕ Add More Photos
```

**Step 3️⃣: KYC करो (ID verification)**
```
📋 Verification Tab
├─ Upload ID (Aadhar/PAN)
├─ Upload Photo
├─ Submit
└─ ✅ Verified (Badge मिलेगा)
```

---

## 👨‍👩‍👧 **Customer (Service Lेने वाले) के लिए**

### **Provider को कैसे खोजते हैं:**

```
1. "Browse Providers" page पर जाओ
2. Filter करो:
   ├─ 🔍 Search: "Electrical work"
   ├─ 🎯 Skill: "Electrical"
   ├─ 📍 City: "Delhi"
   └─ ⭐ Sort: "Highest Rating"
3. Provider card देखो
4. ❤️ Favorite करो या booking करो
```

### **Provider Profile Card पर क्या दिखता है:**

```
┌─────────────────────────────────────┐
│ 🎨 Profile Banner (Color)          │
│                                     │
│  👤 Rajesh Kumar    ❤️              │
│  🎖️ Verified                        │
│                                     │
│  📍 Delhi, India                    │
│                                     │
│  ┌─────────────────────────────┐   │
│  │ 💼 23    ⭐ 4.5    💰 ₹100   │   │
│  │ Jobs   Rating      Base Rate│   │
│  └─────────────────────────────┘   │
│                                     │
│  Skills: ⚡ 🔧 💄                    │
│                                     │
│  Recent Work (Photos):             │
│  [Photo1] [Photo2] [Photo3]        │
│                                     │
│  ┌─────────────────────────────┐   │
│  │ 💬 Chat  |  📞 Call        │   │
│  ├─────────────────────────────┤   │
│  │ 📅 Book Service Now        │   │
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
```

### **Booking का Process:**

```
1. Provider Profile देखो
   ├─ Skills check करो
   ├─ Reviews पढ़ो
   └─ Portfolio देखो

2. Chat/Call करो (optional)
   ├─ सवाल पूछो
   └─ Price negotiate करो

3. "Book Service Now" दबाओ
   ├─ Address select करो
   ├─ Time select करो
   └─ Confirm करो

4. Provider को notification मिलेगा
   ├─ Accept/Reject कर सकता है
   └─ अगर accept करे तो confirmed

5. Job assignment हो जाएगी
   ├─ Chat/Call करना शुरू करो
   └─ Provider come करेगा work करने

6. काम हो जाने के बाद
   ├─ Rating दो
   ├─ Payment करो
   └─ Review लिखो
```

---

## 💬 **Chat और Call कैसे काम करते हैं**

### **Chat:**
```
Provider Dashboard में:
├─ हर Job card पर "💬 Chat" button है
├─ Click करो → Chat window खुल जाएगी
├─ Real-time messages मिलेंगे
├─ WebSocket से instant notifications
└─ Unread messages की red dot दिखेगी

Customer से:
├─ Provider के profile पर "Chat" button
├─ Provider से सीधे बात कर सकता है
└─ Job book करने से पहले भी chat कर सकता है
```

### **Call:**
```
Provider Dashboard में:
├─ हर Job card पर "📞 Call" button है
├─ Click करो → Dialer खुल जाएगा
├─ Customer का phone number automatically
└─ Phone call connect होगी (WhatsApp/Dial पर)

Customer से:
├─ Provider को direct call कर सकता है
└─ Provider's phone number दिखेगा
```

---

## 📍 **GPS Tracking**

```
Provider:
├─ Job card पर "🗺️ Track GPS" option
├─ Click करो → Google Maps खुलेगा
├─ Customer का exact location
└─ Turn-by-turn navigation मिलेगा

Customer:
├─ Provider का location real-time में देख सकता है
├─ ETA मिलेगा (कितनी देर में आएगा)
└─ Live tracking feature
```

---

## 💳 **Payment और Invoice**

```
After Job Completion:

Provider Side:
├─ Job को "Complete" करो
├─ Automatically invoice generate होगा
└─ ✅ Payment received notification

Customer Side:
├─ Completion confirmation मिलेगा
├─ "📄 Pay Now" button दिखेगी
├─ Secure payment portal खुलेगा
├─ Multiple payment options:
│  ├─ UPI
│  ├─ Credit/Debit Card
│  ├─ Net Banking
│  └─ Wallet
└─ ✅ Payment confirmation
```

---

## 🎖️ **Verification और Trust Building**

### **Provider के लिए:**
```
Verified Badge पाने के लिए:

1. KYC Complete करो:
   ├─ Identity proof (Aadhar/PAN/Passport)
   ├─ Address proof (Utility bill/Lease)
   └─ Selfie with documents

2. Portfolio upload करो:
   ├─ कम से कम 3-5 work photos
   └─ Clear photos, good lighting

3. Skills select करो:
   ├─ कम से कम 1 skill
   └─ Honest capabilities बताओ

✅ Verified हो जाओ:
├─ Green badge दिखेगी
├─ ज्यादा job requests आएंगे
└─ Customer trust बढ़ेगा
```

### **Customer के लिए:**
```
Trust Signals:

1. 🎖️ Verified Badge
   └─ KYC complete है

2. ⭐ Ratings
   ├─ 4.5+ stars = अच्छा provider
   └─ 100+ reviews = experienced

3. 🖼️ Portfolio
   └─ Real work samples देखो

4. 💼 Completed Jobs
   ├─ ज्यादा jobs = more experience
   └─ Consistent quality

5. 💬 Reviews
   └─ पिछले customers के comments
```

---

## ⚡ **Quick Tips**

### **For Providers:**
```
✅ Do's:
├─ Quickly respond to chat messages
├─ Be polite and professional
├─ Take clear photos of your work
├─ Complete KYC verification ASAP
├─ Update portfolio regularly
└─ Maintain good ratings

❌ Don'ts:
├─ Ignore job requests
├─ Be rude in chat
├─ Accept jobs आप नहीं कर सकते
├─ Cancel jobs बिना reason के
└─ Over-charge customers
```

### **For Customers:**
```
✅ Do's:
├─ Read provider reviews carefully
├─ Chat before booking
├─ Provide clear instructions
├─ Be respectful and polite
├─ Pay on time
└─ Leave honest reviews

❌ Don'ts:
├─ Book without checking details
├─ Make late-night calls/messages
├─ Negotiate too much
├─ Cancel at last minute
└─ Give fake ratings
```

---

## 📱 **Responsive Design**

```
Mobile (< 640px):
├─ Single column grid
├─ Stacked buttons
├─ Touch-friendly sizes
└─ Vertical layout

Tablet (640px - 1024px):
├─ 2 column grid
├─ Better spacing
└─ Side-by-side buttons

Desktop (> 1024px):
├─ 3 column grid
├─ Full featured
└─ Optimized layout
```

---

## 🔔 **Notifications**

```
Providers को:
├─ New job request → Sound + Toast
├─ Customer message → Toast with preview
├─ Job accepted → Confirmation toast
├─ Payment received → Money notification
└─ New review → Alert

Customers को:
├─ Provider accepted → Confirmation
├─ Provider message → Chat notification
├─ Job completed → Payment alert
└─ New offer → Promotion notification
```

---

## 🆘 **Troubleshooting**

```
❓ Call button काम नहीं कर रहा?
✓ Check करो phone number saved है
✓ Browser default dialer supported है
✓ WhatsApp का use करो अगर fail हो

❓ Chat message नहीं जा रहा?
✓ Internet connection check करो
✓ WebSocket connection check करो
✓ Page refresh करो

❓ GPS location नहीं दिख रहा?
✓ Location permission enable करो
✓ GPS enabled है check करो
✓ Google Maps installled है verify करो

❓ Invoice download नहीं हो रहा?
✓ Job status "COMPLETED" है check करो
✓ Browser permissions check करो
✓ Internet connection verify करो
```

---

**Happy Using! 🎉**

अगर कोई problem हो तो support को contact करो। 

**Support Email:** support@servicemarket.in  
**WhatsApp:** +91-XXXX-XXXX-XX  
**Live Chat:** Available 24/7

---

*Last Updated: January 29, 2026*
