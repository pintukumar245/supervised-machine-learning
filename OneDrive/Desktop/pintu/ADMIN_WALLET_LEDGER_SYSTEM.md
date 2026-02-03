# 💰 Admin Wallet + Provider Ledger + Settlement System

## 🎯 System Overview

आपके लिए एक complete **Virtual Wallet System** बनाया गया है जहां:
- ✅ पैसा असल में **SBI Account** में जाता है
- ✅ लेकिन App में **Tracking & Proof** के लिए dashboard है
- ✅ हर transaction का **Complete Ledger** रहता है
- ✅ Settlement के लिए **Payment Proof** store होता है

---

## 📊 System Architecture

```
┌─────────────────────────────────────────┐
│         CUSTOMER PAYMENT                │
│         (SBI Account में)               │
└────────────────┬────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│     DATABASE TRACKING SYSTEM            │
├─────────────────────────────────────────┤
│                                         │
│  1. PROVIDER LEDGER (per booking)      │
│     ├─ Booking Amount                  │
│     ├─ Commission (10% default)        │
│     ├─ Payout Amount                   │
│     └─ Status (Pending/Approved/Paid)  │
│                                         │
│  2. SETTLEMENT (period-based)          │
│     ├─ Total for period                │
│     ├─ Transaction count               │
│     ├─ Bank details                    │
│     └─ Status (Initiated/Processing)   │
│                                         │
│  3. PAYMENT PROOF (attachment)         │
│     ├─ UTR/Screenshot                  │
│     ├─ Transaction date                │
│     └─ Verification                    │
│                                         │
│  4. ADMIN WALLET LOG (audit trail)     │
│     └─ All activities                  │
│                                         │
└─────────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────────┐
│      ADMIN DASHBOARD                    │
│  • View all providers                   │
│  • Track earnings                       │
│  • Manage settlements                   │
│  • Upload/verify proofs                 │
└─────────────────────────────────────────┘
```

---

## 🗄️ Database Models

### 1️⃣ ProviderLedger
**Purpose:** हर booking के लिए provider की earnings track करता है

```python
class ProviderLedger(models.Model):
    provider         # जो provider है
    job              # किस job का booking है (optional)
    booking_amount   # कितना amount booking हुआ (e.g., 500)
    commission_percentage  # कितना commission (default 10%)
    commission_amount      # auto-calculated (e.g., 50)
    payout_amount    # provider को देना है (e.g., 450)
    status           # PENDING/APPROVED/PAID/CANCELLED
    booking_date     # कब booking हुई
    approved_date    # कब approved हुई
    payout_date      # कब payment दी गई
```

**Example:**
```
Provider: John (ID: 5)
Booking Amount: ₹1000
Commission: 10% = ₹100
Payout Amount: ₹900
Status: PENDING
```

### 2️⃣ Settlement
**Purpose:** एक specific period के लिए सभी payouts को combine करता है

```python
class Settlement(models.Model):
    provider         # किस provider को payment
    settlement_period_start  # 01-Jan-2026
    settlement_period_end    # 31-Jan-2026
    total_amount     # इस period में total payout
    transaction_count # कितने bookings
    status           # INITIATED/PROCESSING/COMPLETED
    transaction_reference  # Bank UTR number
```

**Example:**
```
Provider: John
Period: Jan 1-31, 2026
Total: ₹9000 (10 bookings x ₹900 each)
Status: INITIATED
```

### 3️⃣ PaymentProof
**Purpose:** Settlement के proof को store करता है (UTR, screenshot, etc.)

```python
class PaymentProof(models.Model):
    settlement   # कौन सा settlement
    proof_type   # BANK_SLIP / SCREENSHOT / UTR_PROOF
    file         # uploaded file
    utr_number   # UTR/RRN number
    transaction_date  # कब payment हुई
    verified_by_admin  # verified या नहीं
```

### 4️⃣ AdminWalletLog
**Purpose:** सभी wallet activities का audit trail

```python
class AdminWalletLog(models.Model):
    activity_type    # BOOKING_RECEIVED / PAYOUT_INITIATED / etc.
    provider         # किस provider के लिए
    amount           # कितना amount
    related_ledger   # किस ledger entry से related
    related_settlement  # किस settlement से related
    created_at       # कब हुआ
```

---

## 🔌 API Endpoints

### Admin Dashboard
```
GET /api/payments/admin/dashboard/
```
**Response:**
```json
{
    "total_bookings": 50000,
    "total_commission": 5000,
    "total_payouts": 45000,
    "pending_payouts": 5000,
    "total_providers": 25,
    "completed_settlements": 10,
    "pending_settlements": 2
}
```

### Provider Ledger Management
```
GET    /api/payments/ledger/              # सभी ledger entries देखें
POST   /api/payments/ledger/              # नई entry बनाएं
GET    /api/payments/ledger/{id}/         # एक entry देखें
PATCH  /api/payments/ledger/{id}/approve/ # approve करें
PATCH  /api/payments/ledger/{id}/mark_paid/  # paid mark करें
GET    /api/payments/ledger/by_provider/?provider_id=5  # specific provider
```

**Create Ledger Entry:**
```
POST /api/payments/ledger/
{
    "provider": 5,
    "booking_amount": 1000,
    "commission_percentage": 10
}
```

**Response:**
```json
{
    "id": 1,
    "provider": 5,
    "provider_name": "John",
    "provider_phone": "9876543210",
    "booking_amount": "1000.00",
    "commission_percentage": "10.00",
    "commission_amount": "100.00",
    "payout_amount": "900.00",
    "status": "PENDING",
    "booking_date": "2026-01-29T10:00:00Z",
    "approved_date": null,
    "payout_date": null
}
```

### Settlement Management
```
GET    /api/payments/settlement/         # सभी settlements
POST   /api/payments/settlement/         # नया settlement बनाएं
GET    /api/payments/settlement/{id}/    # एक settlement देखें
PATCH  /api/payments/settlement/{id}/mark_processing/  # processing mark करें
PATCH  /api/payments/settlement/{id}/mark_completed/   # completed mark करें
```

**Create Settlement:**
```
POST /api/payments/settlement/
{
    "provider": 5,
    "settlement_period_start": "2026-01-01",
    "settlement_period_end": "2026-01-31",
    "bank_account_number": "1234567890",
    "bank_ifsc": "SBIN0001234"
}
```

**Mark as Completed:**
```
PATCH /api/payments/settlement/1/mark_completed/
{
    "transaction_reference": "UTR123456789"
}
```

### Payment Proof Management
```
GET    /api/payments/proof/              # सभी proofs
POST   /api/payments/proof/              # नया proof upload करें
GET    /api/payments/proof/{id}/         # एक proof देखें
PATCH  /api/payments/proof/{id}/verify/  # verify करें
```

**Upload Proof:**
```
POST /api/payments/proof/
{
    "settlement": 1,
    "proof_type": "UTR_PROOF",
    "file": <file>,
    "utr_number": "UTR123456789",
    "transaction_date": "2026-01-29"
}
```

### Wallet Activity Log
```
GET /api/payments/wallet-log/            # सभी activities
GET /api/payments/wallet-log/?provider=5 # specific provider की activities
GET /api/payments/wallet-log/?activity_type=PAYOUT_COMPLETED  # specific type
```

---

## 🚀 Workflow Example

### Step 1: Customer Books a Service
```
Customer pays ₹1000 to SBI Account
```

### Step 2: Admin Creates Ledger Entry
```
POST /api/payments/ledger/
{
    "provider": 5,
    "booking_amount": 1000,
    "commission_percentage": 10
}

Response:
✅ Ledger created
   Provider (John): ₹1000
   Commission: ₹100 (10%)
   Payout: ₹900
   Status: PENDING
```

### Step 3: Admin Approves Payout
```
PATCH /api/payments/ledger/1/approve/

Status changed to APPROVED
Approved date recorded
```

### Step 4: Create Settlement (Monthly)
```
POST /api/payments/settlement/
{
    "provider": 5,
    "settlement_period_start": "2026-01-01",
    "settlement_period_end": "2026-01-31"
}

Response:
✅ Settlement created
   Provider: John
   Total Payout: ₹9000 (10 bookings)
   Transaction Count: 10
   Status: INITIATED
```

### Step 5: Process Settlement
```
PATCH /api/payments/settlement/1/mark_processing/

Status: PROCESSING
Processing date recorded
(Admin transfers money to provider's bank)
```

### Step 6: Upload Payment Proof
```
POST /api/payments/proof/
{
    "settlement": 1,
    "proof_type": "UTR_PROOF",
    "file": bank_slip.pdf,
    "utr_number": "UTR2026012912345",
    "transaction_date": "2026-01-29"
}

✅ Proof uploaded
```

### Step 7: Verify & Complete
```
PATCH /api/payments/proof/1/verify/
{
    "notes": "Verified with bank slip"
}

Then mark settlement as completed:

PATCH /api/payments/settlement/1/mark_completed/
{
    "transaction_reference": "UTR2026012912345"
}

Status: COMPLETED
✅ Provider paid successfully
```

---

## 🎯 Use Cases

### For Admin
✅ Track all provider earnings  
✅ Monitor commission collected  
✅ Manage monthly settlements  
✅ Upload & verify payment proofs  
✅ View complete audit trail  

### For Provider (Future Frontend)
✅ View their ledger entries  
✅ See pending payouts  
✅ Check settlement history  
✅ Download payment proofs  

### For Finance Team
✅ Generate settlement reports  
✅ Track UTR numbers  
✅ Reconcile bank statements  
✅ Audit all transactions  

---

## 💡 Key Features

### ✅ Auto-Commission Calculation
```python
commission_amount = (booking_amount * commission_percentage) / 100
payout_amount = booking_amount - commission_amount
```

### ✅ Complete Audit Trail
Every action is logged in AdminWalletLog:
- Booking received
- Payout initiated
- Payout completed
- etc.

### ✅ Settlement Period Tracking
- Automatic grouping by date range
- No duplicate settlements for same period
- Transaction count tracking

### ✅ Payment Proof System
- Multiple proof types (UTR, Bank Slip, Screenshot, etc.)
- Admin verification workflow
- Timestamp tracking

### ✅ Status Management
```
Ledger Status:
PENDING → APPROVED → PAID → (CANCELLED option)

Settlement Status:
INITIATED → PROCESSING → COMPLETED → (FAILED/CANCELLED options)
```

---

## 📱 Admin Dashboard Views (Frontend)

### Dashboard Summary
```
┌─────────────────────────────────────────┐
│       ADMIN WALLET DASHBOARD            │
├─────────────────────────────────────────┤
│                                         │
│  Total Bookings:        ₹50,000        │
│  Total Commission:      ₹5,000         │
│  Total Payouts:         ₹45,000        │
│  Pending Payouts:       ₹5,000         │
│                                         │
│  Active Providers:      25              │
│  Completed Settlements: 10              │
│  Pending Settlements:   2               │
│                                         │
└─────────────────────────────────────────┘
```

### Provider Ledger Table
```
┌─────┬─────────┬────────┬────┬─────┬────────┐
│ ID  │Provider │Booking │Com │Pay  │Status  │
├─────┼─────────┼────────┼────┼─────┼────────┤
│ 1   │ John    │ ₹1000  │₹100│₹900│PENDING │
│ 2   │ Jane    │ ₹1500  │₹150│1350│APPROVED│
│ 3   │ Mike    │ ₹800   │₹80 │₹720│ PAID   │
└─────┴─────────┴────────┴────┴─────┴────────┘
```

### Settlement Records
```
┌───┬────────┬────────┬──────────┬────────┐
│ ID│Provider│Amount  │Period    │Status  │
├───┼────────┼────────┼──────────┼────────┤
│ 1 │ John   │₹9000   │Jan 1-31  │COMPLETED
│ 2 │ Jane   │₹8500   │Jan 1-31  │PROCESSING
└───┴────────┴────────┴──────────┴────────┘
```

---

## 🔒 Security & Permissions

- Only admins can:
  - Create/modify ledger entries
  - Create settlements
  - Upload/verify proofs
  - View wallet logs

- Providers can (future):
  - View their own ledger entries
  - View their settlements
  - Download proofs

---

## 📚 Example Curl Requests

### Create Ledger Entry
```bash
curl -X POST http://localhost:8001/api/payments/ledger/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{
    "provider": 5,
    "booking_amount": "1000.00",
    "commission_percentage": "10.00"
  }'
```

### Get Dashboard
```bash
curl -X GET http://localhost:8001/api/payments/admin/dashboard/ \
  -H "Authorization: Bearer <token>"
```

### Create Settlement
```bash
curl -X POST http://localhost:8001/api/payments/settlement/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{
    "provider": 5,
    "settlement_period_start": "2026-01-01",
    "settlement_period_end": "2026-01-31"
  }'
```

---

## ✅ Implementation Checklist

- [x] Models created (ProviderLedger, Settlement, PaymentProof, AdminWalletLog)
- [x] Serializers created
- [x] ViewSets created with filters and actions
- [x] URLs configured
- [x] Migrations created and applied
- [x] Auto-calculation logic added
- [ ] Frontend dashboard (Next.js) - TODO
- [ ] Provider views (Next.js) - TODO
- [ ] Email notifications - TODO
- [ ] PDF reports - TODO

---

## 🎓 Next Steps

1. **Create Admin Dashboard Frontend** (React/Next.js)
2. **Create Provider Views** (Next.js)
3. **Add Email Notifications**
4. **Generate PDF Reports**
5. **Add Data Export (CSV/Excel)**
6. **Integration with Bank API**

---

## 📞 Support

All endpoints are documented and ready to use!

Test करने के लिए:
1. Backend start करें
2. Postman/Curl से API calls करें
3. Dashboard देखें

हो गया! 🎉

