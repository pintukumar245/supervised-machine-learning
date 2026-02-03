# Sub-Admin Management System - Complete Guide

## Feature Overview

This system allows the **Main Admin** to assign specific city/state combinations to **Sub-Admins**. Once assigned, a Sub-Admin can manage all providers and customers within their assigned city/state.

### Role Hierarchy:
1. **Main Admin** (role='ADMIN', is_superuser=True)
   - Can create, view, edit, and delete sub-admin assignments
   - Has complete access to all users and cities
   - Manages all pricing, payments, and system-wide operations

2. **Sub-Admin** (role='SUB_ADMIN')
   - Can only view and manage users in their assigned city/state
   - Can verify providers in their city
   - Can handle customer complaints and jobs
   - Cannot create other sub-admins

3. **Customer & Provider**
   - Regular users with their specific roles

## Backend Implementation

### 1. Database Models

#### User Model Changes
- Added `city` field (CharField, nullable)
- Added `state` field (CharField, nullable)
- Added `SUB_ADMIN` role choice to Role enum

#### New SubAdminAssignment Model
```python
class SubAdminAssignment(models.Model):
    sub_admin = ForeignKey(User, role=SUB_ADMIN)
    city = CharField(max_length=100)
    state = CharField(max_length=100)
    assigned_by = ForeignKey(User, role=ADMIN)
    created_at = DateTimeField(auto_now_add=True)
    is_active = BooleanField(default=True)
    
    class Meta:
        unique_together = ('sub_admin', 'city', 'state')
```

### 2. API Endpoints

#### Assign Sub-Admin
**POST** `/api/auth/admin/assign-sub-admin/`

**Required:** Main Admin access

**Request Body:**
```json
{
    "user_id": 123,
    "city": "Mumbai",
    "state": "Maharashtra"
}
```

**Response:**
```json
{
    "id": 1,
    "sub_admin": 123,
    "sub_admin_name": "john_doe",
    "sub_admin_phone": "9876543210",
    "city": "Mumbai",
    "state": "Maharashtra",
    "assigned_by_name": "admin",
    "created_at": "2026-01-28T22:55:36Z",
    "is_active": true
}
```

#### List Sub-Admins
**GET** `/api/auth/admin/sub-admins/`

**Required:** Admin or Sub-Admin access

**Response:** Array of SubAdminAssignment objects

#### Remove Sub-Admin
**DELETE** `/api/auth/admin/remove-sub-admin/`

**Required:** Main Admin access

**Request Body:**
```json
{
    "assignment_id": 1
}
```

### 3. Permissions

**IsSubAdminOrAdmin** permission class:
- Main Admin: Full access to all resources
- Sub-Admin: Access only to users in their assigned city
- Other users: No access

## Frontend Implementation

### SubAdminManager Component

Located at: `src/components/SubAdminManager.tsx`

**Features:**
- List all sub-admin assignments
- Assign new sub-admin (with state selector for all Indian states)
- Remove sub-admin assignments
- Display sub-admin details with contact info

**UI Components:**
- Assignment form with user selector, state dropdown, and city input
- Table displaying all active sub-admin assignments
- Delete button with confirmation

**Props:** None (component fetches its own data)

### Integration in Admin Dashboard

The SubAdminManager component is included in the Admin Dashboard at:
`src/app/dashboard/admin/page.tsx`

## How to Use

### For Main Admin:

1. **Navigate to Admin Dashboard** → `/dashboard/admin`
2. **Scroll to "Sub-Admin Management"** section
3. **Click "Assign Sub-Admin"** button
4. **Fill in the form:**
   - Select User (dropdown lists all customers/providers)
   - Select State (dropdown with all Indian states)
   - Enter City name
5. **Click "Assign"** button
6. **Sub-admin will be activated** with role changed to SUB_ADMIN
7. **To remove:** Click trash icon and confirm

### For Sub-Admin:

1. **Login with credentials**
2. **Access dashboard** → `/dashboard/admin` (role-based)
3. **View only users** in their assigned city/state
4. **Cannot:**
   - Create new sub-admins
   - Access users from other cities
   - Access main admin settings

## Database Migration

The following migrations were created:
- `users/migrations/0017_user_city_user_state_alter_user_role_and_more.py`

**Applied changes:**
- Added `city` and `state` fields to User model
- Updated Role choices to include SUB_ADMIN
- Created SubAdminAssignment model

**To apply migrations:**
```bash
python manage.py migrate users
```

## Admin Panel (Django Admin)

Sub-Admin assignments can also be managed via Django admin at:
`/admin/users/subadminassignment/`

**Features:**
- Create/edit/delete assignments
- Filter by state, city, active status
- Search by sub-admin username or city

## Security Features

1. **Role-based Access Control (RBAC)**
   - Only Main Admin can assign sub-admins
   - Sub-Admins have limited scope

2. **City/State Validation**
   - Sub-Admin can only see users in their assigned city
   - Prevents cross-city access

3. **Assignment Tracking**
   - Records which admin created the assignment
   - Stores creation timestamp
   - Can be deactivated without deleting

4. **Cascading Updates**
   - If sub-admin removed from all assignments, role reverts to CUSTOMER
   - User data is preserved

## Testing

### Manual Testing Checklist:

1. ✅ Main admin can assign a user as sub-admin
2. ✅ Sub-admin role is set correctly
3. ✅ Sub-admin can only see users in their city
4. ✅ Multiple assignments for same user in different cities
5. ✅ Main admin can remove assignments
6. ✅ Role reverts when all assignments removed
7. ✅ State dropdown shows all Indian states
8. ✅ Unique constraint prevents duplicate assignments
9. ✅ Created/updated timestamps are accurate
10. ✅ Django admin CRUD operations work

### API Testing:

```bash
# Assign sub-admin (requires admin token)
POST /api/auth/admin/assign-sub-admin/
{
    "user_id": 5,
    "city": "Bangalore",
    "state": "Karnataka"
}

# List sub-admins
GET /api/auth/admin/sub-admins/

# Remove assignment
DELETE /api/auth/admin/remove-sub-admin/
{
    "assignment_id": 1
}
```

## Troubleshooting

### Issue: Sub-admin cannot see users
- **Solution:** Verify user's city field matches assignment city
- Update user profile with correct city/state

### Issue: Sub-admin role not changed
- **Solution:** Restart the server
- Clear browser cache and login again

### Issue: Cannot remove sub-admin
- **Solution:** Ensure you're using Main Admin account
- Check if assignment exists

### Issue: "Access Denied" errors
- **Solution:** Verify your role in `/api/auth/me/`
- Check token expiration in browser DevTools

## Files Modified/Created

### Backend Files:
- `users/models.py` - Added city, state fields and SubAdminAssignment model
- `users/serializers.py` - Added SubAdminAssignmentSerializer
- `users/views.py` - Added sub-admin management actions
- `users/urls.py` - Added new endpoints
- `users/admin.py` - Registered SubAdminAssignment in Django admin
- `users/permissions.py` - Added IsSubAdminOrAdmin permission
- `users/migrations/0017_*.py` - Migration file

### Frontend Files:
- `src/components/SubAdminManager.tsx` - New component
- `src/app/dashboard/admin/page.tsx` - Added SubAdminManager import

## Future Enhancements

1. **Multi-city assignments** - Allow one sub-admin multiple cities
2. **Sub-admin hierarchy** - Zone-wise sub-admins over regional sub-admins
3. **Performance metrics** - Track sub-admin performance
4. **Notifications** - Alert main admin of sub-admin activities
5. **Audit logs** - Track all sub-admin actions
6. **Bulk operations** - Assign multiple users at once

## Support

For issues or questions, check:
- Backend logs: `manage.py runserver` output
- Browser console: F12 → Console tab
- Network tab: F12 → Network tab (check API responses)
