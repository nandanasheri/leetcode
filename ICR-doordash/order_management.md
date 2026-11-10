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

## 3. Suggested data model

You may adapt this model, but keep the concepts distinct.

### Order

| Field | Description |
|---|---|
| `order_id` | Unique order ID |
| `merchant_id` | Owning merchant |
| `customer_id` | Customer who placed the order |
| `items` | Ordered line items |
| `status` | Current order status |
| `created_at` | Creation timestamp |
| `updated_at` | Most recent successful update |
| `rejection_reason` | Optional rejection reason |
| `status_history` | Ordered record of successful status changes |

### Order item

| Field | Description |
|---|---|
| `item_id` | Item identifier |
| `name` | Display name |
| `quantity` | Positive integer |
| `unit_price_cents` | Non-negative integer price |

### Status history entry

| Field | Description |
|---|---|
| `status` | Status after the transition |
| `changed_at` | Timestamp of transition |
| `reason` | Optional reason, such as rejection reason |

Use integer cents for prices to avoid floating-point currency calculations.

## 4. Interface / API expectations

You may implement ordinary functions, a class-based service, or HTTP endpoints. A service interface should provide equivalents of:

```text
create_order(order_data)
get_order(order_id)
list_orders_for_merchant(merchant_id)
accept_order(order_id, merchant_id)
reject_order(order_id, merchant_id, reason)
update_preparation_status(order_id, merchant_id, new_status)
```

Return clear success and failure results. Keep these cases distinguishable:
- Invalid input
- Duplicate order
- Order not found
- Merchant does not own order
- Invalid status transition

If you build HTTP endpoints, choose appropriate status codes and document request/response shapes. A web framework is not required.

## 5. Example workflow

A merchant receives:

```json
{
  "order_id": "ord-101",
  "merchant_id": "merchant-7",
  "customer_id": "customer-42",
  "created_at": "2026-11-06T18:00:00Z",
  "items": [
    {
      "item_id": "item-1",
      "name": "Chicken bowl",
      "quantity": 2,
      "unit_price_cents": 1299
    }
  ]
}
```

Expected lifecycle:

```text
PENDING
  | merchant accepts
  v
ACCEPTED
  | merchant starts preparing
  v
PREPARING
  | merchant marks ready
  v
READY_FOR_PICKUP
```

Alternatively:

```text
PENDING -- merchant rejects with reason --> REJECTED
```

Invalid transitions must be rejected.

## 6. Testing expectations

Demonstrate at least these cases:
1. A valid order is created with `PENDING` status.
2. A duplicate order ID is rejected.
3. Invalid order data is rejected.
4. A merchant retrieves its orders newest first.
5. A merchant can accept a pending order.
6. A merchant can reject a pending order only with a reason.
7. A merchant cannot modify another merchant's order.
8. A nonexistent order returns not found.
9. A valid preparation transition succeeds.
10. An invalid/backwards transition is rejected.
11. Status history records successful transitions in order.
12. A failed operation does not partially mutate the order.

Use fixed timestamps or an injectable clock in tests. Avoid sleeping or relying on the real current time.

## 7. AI collaboration expectations

This is an AI-assisted coding exercise. Use the AI coding assistant as a partner, but remain responsible for the implementation.

A strong workflow:
1. **Understand before prompting:** restate requirements and identify ambiguity.
2. **Plan:** choose data structures, service boundaries, and error handling before generating lots of code.
3. **Work in vertical slices:** create/retrieve orders, then merchant actions, then lifecycle transitions.
4. **Review generated code:** verify ownership checks, validation, and transition rules.
5. **Run frequently:** use tests to catch integration errors; do not trust generated code without checking it.
6. **Debug deliberately:** give the AI the smallest relevant failure and code context, then verify its suggested fix.
7. **Explain tradeoffs:** be ready to explain invariants, failure modes, and concurrency behavior.

Do not accept a large generated implementation without understanding it. You should be able to explain every important part of the final solution.

## 8. Progressive interviewer extensions

Introduce these one at a time after the core workflow works. Do not reveal every extension at the beginning.

### Extension 1 — Duplicate delivery of the same order event

The upstream system may send the same order-created event more than once. Add an `event_id` and make creation idempotent:
- Reprocessing the same event must not create a second order.
- Reusing an event ID with conflicting order data must be handled explicitly.
- Explain event deduplication versus duplicate `order_id` rejection.

### Extension 2 — Merchant action retries

A client may retry an accept/reject request because it did not receive the first response. Add an idempotency key:
- Same key and same request returns the original result.
- Same key with a different action or payload returns a conflict.
- Do not apply a state transition twice.

### Extension 3 — Concurrent merchant actions

Two requests may try to accept and reject the same pending order at nearly the same time.
- Ensure only one valid transition wins.
- For an in-memory implementation, a lock around the relevant operation is acceptable.
- Explain what changes with a database-backed implementation.

### Extension 4 — Order cancellation

Add customer cancellation:
- A customer may cancel only while status is `PENDING` or `ACCEPTED`.
- Cancellation after preparation starts is not allowed in this simplified version.
- Record cancellation in status history.
- Merchant actions must not move a cancelled order forward.

### Extension 5 — Merchant queue filters

Add merchant-list filters:
- Filter by one or more statuses.
- Limit the number of returned orders.
- Support cursor or offset pagination.

Explain how to keep pagination stable when new orders arrive during paging.

## 9. Suggested 60-minute pacing

| Time | Goal |
|---|---|
| 0–5 min | Read prompt, clarify assumptions, identify core entities |
| 5–10 min | Agree on a small plan and interfaces |
| 10–25 min | Implement order creation and retrieval |
| 25–40 min | Implement accept/reject and preparation transitions |
| 40–48 min | Add tests, run them, fix failures |
| 48–55 min | Implement one interviewer extension |
| 55–60 min | Review design, explain tradeoffs, identify next steps |

If the core workflow is incomplete, do not rush into extensions. If moving quickly, prioritize idempotency or concurrent actions.

## 10. What a strong performance demonstrates

- Turns product requirements into a coherent working implementation.
- Clarifies ambiguous rules instead of guessing.
- Models state transitions explicitly and prevents invalid transitions.
- Validates input at a sensible boundary.
- Enforces merchant ownership on every modifying operation.
- Prevents failed operations from leaving partially updated state.
- Uses AI to accelerate work while independently reviewing and testing it.
- Explains how an in-memory design could evolve into a persistent, concurrent service.

## Out of scope

Do not spend time on authentication infrastructure, payment processing, real restaurant integrations, deployment, a polished frontend, or distributed-system infrastructure. Keep the first version small and correct.
