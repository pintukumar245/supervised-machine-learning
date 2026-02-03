# Admin Wallet System - API Testing Guide

## 🚀 Quick Start

Test data has been populated with:
- **8 Providers** (provider_1 to provider_8)
- **40 Ledger Entries** (bookings with earnings)
- **3 Settlements** (grouped payouts)
- **Financial Summary**:
  - Total Bookings: ₹47,000
  - Total Commission: ₹7,275
  - Total Payouts: ₹27,787.50
  - Pending Payouts: ₹11,937.50

---

## 📊 API Endpoints

### 1. Admin Dashboard (Summary)

**Endpoint:** `GET /api/payments/admin/dashboard/`

**Description:** Get complete financial overview

**Example Response:**
```json
{
  "total_bookings": 47000,
  "total_commission": 7275,
  "total_payouts": 27787.50,
  "pending_payouts": 11937.50,
  "total_providers": 8,
  "completed_settlements": 2,
  "pending_settlements": 1,
  "dashboard_summary": {
    "by_status": {
      "PENDING": 5,
      "APPROVED": 6,
      "PAID": 29,
      "CANCELLED": 0
    },
    "top_providers": [...],
    "recent_transactions": [...]
  }
}
```

**cURL:**
```bash
curl -H "Authorization: Bearer YOUR_ADMIN_TOKEN" \
  http://localhost:8000/api/payments/admin/dashboard/
```

---

### 2. Provider Ledger (Individual Earnings)

**Endpoint:** `GET /api/payments/ledger/`

**Description:** View all provider earnings with filtering

**Query Parameters:**
- `provider` - Filter by provider ID
- `status` - Filter by PENDING, APPROVED, PAID, CANCELLED
- `date_from` - Filter from date (YYYY-MM-DD)
- `date_to` - Filter to date (YYYY-MM-DD)
- `ordering` - Sort by field (e.g., `-booking_date`)

**Example:**
```bash
# Get all approved entries for provider_1
curl -H "Authorization: Bearer YOUR_TOKEN" \
  "http://localhost:8000/api/payments/ledger/?provider=1&status=APPROVED"

# Get paid entries in January 2026
curl -H "Authorization: Bearer YOUR_TOKEN" \
  "http://localhost:8000/api/payments/ledger/?status=PAID&date_from=2026-01-01&date_to=2026-01-31"
```

**Response Sample:**
```json
{
  "count": 40,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "provider": {
        "id": 2,
        "name": "provider_2",
        "phone": "9876543210"
      },
      "booking_amount": "1000.00",
      "commission_percentage": "10.00",
      "commission_amount": "100.00",
      "payout_amount": "900.00",
      "status": "APPROVED",
      "booking_date": "2026-01-28",
      "approved_date": "2026-01-29",
      "payout_date": null
    }
  ]
}
```

---

### 3. Custom Ledger Actions

**Approve Pending Entry:**
```bash
# POST /api/payments/ledger/{id}/approve/
curl -X POST -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:8000/api/payments/ledger/1/approve/
```

**Mark as Paid:**
```bash
# POST /api/payments/ledger/{id}/mark_paid/
curl -X POST -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"payout_date": "2026-02-01"}' \
  http://localhost:8000/api/payments/ledger/1/mark_paid/
```

**Filter by Provider:**
```bash
# GET /api/payments/ledger/{provider_id}/by_provider/
curl -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:8000/api/payments/ledger/1/by_provider/
```

---

### 4. Settlement Management

**Endpoint:** `GET /api/payments/settlement/`

**Description:** View all settlement records

**Example:**
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:8000/api/payments/settlement/
```

**Response Sample:**
```json
{
  "count": 3,
  "results": [
    {
      "id": 1,
      "provider": {
        "id": 1,
        "name": "provider_1"
      },
      "settlement_period_start": "2025-12-29",
      "settlement_period_end": "2026-01-28",
      "total_amount": "900.00",
      "transaction_count": 2,
      "status": "COMPLETED",
      "bank_account_number": "12345678900",
      "bank_ifsc": "SBIN0001234",
      "utr_number": null,
      "created_date": "2026-01-28T15:58:46.950213Z"
    }
  ]
}
```

---

### 5. Settlement Actions

**Create Settlement:**
```bash
curl -X POST -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "provider": 1,
    "settlement_period_start": "2025-12-29",
    "settlement_period_end": "2026-01-28",
    "total_amount": "900.00",
    "transaction_count": 2,
    "bank_account_number": "12345678901",
    "bank_ifsc": "SBIN0001234"
  }' \
  http://localhost:8000/api/payments/settlement/
```

**Mark as Processing:**
```bash
curl -X POST -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:8000/api/payments/settlement/1/mark_processing/
```

**Mark as Completed (with UTR):**
```bash
curl -X POST -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"utr_number": "202601280001234"}' \
  http://localhost:8000/api/payments/settlement/1/mark_completed/
```

---

### 6. Payment Proofs

**Endpoint:** `GET /api/payments/proof/`

**Description:** View uploaded payment proofs

**Upload Proof:**
```bash
curl -X POST -H "Authorization: Bearer YOUR_TOKEN" \
  -F "settlement=1" \
  -F "proof_type=BANK_SLIP" \
  -F "utr_number=202601280001234" \
  -F "file=@/path/to/proof.pdf" \
  http://localhost:8000/api/payments/proof/
```

**Verify Proof:**
```bash
curl -X POST -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:8000/api/payments/proof/1/verify/
```

---

### 7. Wallet Activity Log

**Endpoint:** `GET /api/payments/wallet-log/`

**Description:** View all wallet activities

**Example:**
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:8000/api/payments/wallet-log/
```

**Activity Types:**
- `BOOKING_RECEIVED` - When booking is created
- `COMMISSION_EARNED` - Commission calculated
- `PAYOUT_INITIATED` - Settlement started
- `PAYOUT_COMPLETED` - Settlement completed

---

## 🧪 Testing Workflow

### Step 1: View Dashboard
```bash
curl -H "Authorization: Bearer YOUR_ADMIN_TOKEN" \
  http://localhost:8000/api/payments/admin/dashboard/
```

### Step 2: View All Ledger Entries
```bash
curl -H "Authorization: Bearer YOUR_ADMIN_TOKEN" \
  http://localhost:8000/api/payments/ledger/
```

### Step 3: Filter by Status
```bash
curl -H "Authorization: Bearer YOUR_ADMIN_TOKEN" \
  http://localhost:8000/api/payments/ledger/?status=PENDING
```

### Step 4: Approve Pending Entry
```bash
curl -X POST -H "Authorization: Bearer YOUR_ADMIN_TOKEN" \
  http://localhost:8000/api/payments/ledger/1/approve/
```

### Step 5: Create Settlement
```bash
curl -X POST -H "Authorization: Bearer YOUR_ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "provider": 1,
    "settlement_period_start": "2025-12-29",
    "settlement_period_end": "2026-01-28",
    "total_amount": "900.00",
    "transaction_count": 2,
    "bank_account_number": "12345678901",
    "bank_ifsc": "SBIN0001234"
  }' \
  http://localhost:8000/api/payments/settlement/
```

### Step 6: Mark Settlement as Completed
```bash
curl -X POST -H "Authorization: Bearer YOUR_ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"utr_number": "202601280001234"}' \
  http://localhost:8000/api/payments/settlement/1/mark_completed/
```

### Step 7: View Activity Log
```bash
curl -H "Authorization: Bearer YOUR_ADMIN_TOKEN" \
  http://localhost:8000/api/payments/wallet-log/
```

---

## 🔑 Authentication

All API endpoints require admin token. Get token via:

```bash
# Login as admin
curl -X POST -H "Content-Type: application/json" \
  -d '{
    "phone_number": "YOUR_ADMIN_PHONE",
    "password": "YOUR_PASSWORD"
  }' \
  http://localhost:8000/api/auth/login/
```

Response will include `token`:
```json
{
  "token": "abc123...",
  "user": {
    "id": 1,
    "role": "ADMIN"
  }
}
```

---

## 📋 Data Summary

### Test Providers
```
provider_1: 2 approved entries (₹900 pending payout)
provider_2: 1 approved entry (₹1,350 pending payout)
provider_3: 1 approved entry (₹1,800 pending payout)
provider_4: 8 paid entries (₹5,625 completed)
provider_5: 5 mixed entries
provider_6: 4 mixed entries
provider_7: 3 mixed entries
provider_8: 12 mixed entries
```

### Status Distribution
```
PENDING:   5 entries
APPROVED:  6 entries
PAID:      29 entries
CANCELLED: 0 entries
```

---

## 🐛 Troubleshooting

### Issue: 403 Forbidden
- **Solution**: Ensure token is for admin user. Check user role is "ADMIN"

### Issue: 404 Not Found
- **Solution**: Verify ID exists. Get IDs from list endpoints first

### Issue: 400 Bad Request
- **Solution**: Check JSON format and required fields match API spec

### Issue: No data populated
- **Solution**: Run command again:
  ```bash
  python manage.py populate_wallet_data --providers=10 --bookings=50
  ```

---

## 📱 Provider-Facing Endpoints (Next Phase)

These will be implemented for providers to view their own data:

- `GET /api/payments/my-ledger/` - View own earnings
- `GET /api/payments/my-settlements/` - View own settlements
- `GET /api/payments/my-wallet/` - View wallet balance
- `GET /api/payments/my-proofs/` - View own payment proofs

---

## 🎯 Next Steps

1. ✅ Backend API Complete
2. 📊 Frontend Admin Dashboard (React/Next.js)
3. 📱 Provider-facing views
4. 📧 Email notifications
5. 📄 PDF report generation
6. 🏦 Bank API integration (optional)

---

**Documentation:** See [ADMIN_WALLET_LEDGER_SYSTEM.md](./ADMIN_WALLET_LEDGER_SYSTEM.md) for complete system design
