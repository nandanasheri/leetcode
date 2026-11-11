# DoorDash AI Code Craft Mock Interview: Merchant Order Management System

**Format:** AI-assisted coding / AI Code Craft  
**Suggested duration:** 60 minutes  
**Language:** Candidate's choice (Python is a convenient default)  
**Difficulty:** Medium

## 1. Product context

A restaurant merchant uses a DoorDash merchant dashboard to manage incoming delivery orders. When a customer places an order, the merchant needs to review it, accept or reject it, and update its preparation progress.

Build a simplified **Merchant Order Management System**. Implement a small service/API layer that can receive orders and apply merchant actions. A graphical UI is not required.

The goal is a reliable, understandable working feature—not a production-scale distributed system.

## 2. Initial requirements

### A. Receive an order

Accept an order containing:
- `order_id`: unique order identifier
- `merchant_id`: merchant responsible for the order
- `customer_id`: customer who placed the order
- `items`: list of items, each with item ID, name, quantity, and unit price
- `created_at`: creation timestamp

On valid input:
- Store the order.
- Set status to `PENDING`.
- Make it retrievable by `order_id`.

Validation:
- IDs must be non-empty strings.
- `items` must contain at least one item.
- Each item needs a non-empty name, positive integer quantity, and non-negative unit price.
- Reject duplicate `order_id` values; do not overwrite existing orders.

An in-memory data store is sufficient.

### B. Retrieve orders

Support:
- Retrieving one order by `order_id`.
- Listing all orders for a `merchant_id`.

List orders newest first by `created_at`. Define a deterministic tie-breaker for equal timestamps.

### C. Accept or reject an order

A merchant can accept or reject a pending order:
- Accept: `PENDING` → `ACCEPTED`.
- Reject: `PENDING` → `REJECTED`.
- Rejection requires a non-empty reason.
- Only the owning merchant may modify the order.
- Missing orders return a not-found result.
- Orders that are no longer `PENDING` cannot be accepted or rejected again.

### D. Update preparation status

After acceptance, the merchant can update:
- `ACCEPTED` → `PREPARING`
- `PREPARING` → `READY_FOR_PICKUP`

Reject invalid or backwards transitions. For example, `REJECTED` cannot become `PREPARING`, and `READY_FOR_PICKUP` cannot return to `PREPARING`.

Record a timestamp for each successful status change and retain status history.

