# DoorDash ICR Mock Interview: Pickup Capacity Monitor

**Duration:** 60 minutes · **Language:** Python · **Difficulty:** Medium  
**Built-in sorting:** Allowed

## Problem

A merchant has a limited number of pickup slots available at any moment. DoorDash receives pickup reservations from a downstream service. Implement `PickupCapacityMonitor.analyze_capacity(store_id, capacity)` to determine when the store is over capacity.

Each reservation contains:
- `reservation_id`: unique identifier
- `start_min`: pickup window start, in minutes
- `end_min`: pickup window end, in minutes

Treat reservations as half-open intervals: `[start_min, end_min)`. A reservation is active at its start, but not at its end.

### Requirements

1. Fetch reservations for the requested store using the mocked API.
2. Ignore invalid reservations: empty IDs, non-integer start/end values (booleans are not valid integers), and intervals where `end_min <= start_min`.
3. Deduplicate by `reservation_id`. Keep the first valid occurrence and ignore later occurrences with the same ID.
4. Calculate the maximum number of simultaneously active reservations (`peak_count`).
5. Calculate the earliest minute at which that peak first occurs (`peak_start_min`).
6. Return all ranges during which active reservations are strictly greater than `capacity`. Merge adjacent overloaded ranges.
7. If the API response is not successful, return `None`.
8. If there are no valid reservations, return `peak_count = 0`, `peak_start_min = None`, and an empty range list.

Return:

```python
{
    "peak_count": 3,
    "peak_start_min": 30,
    "over_capacity_ranges": [{"start_min": 30, "end_min": 50}]
}
```

## Example

For capacity `2`:

| Reservation | Start | End |
|---|---:|---:|
| A | 10 | 40 |
| B | 20 | 50 |
| C | 30 | 45 |
| D | 40 | 60 |
| E | 45 | 55 |
| F | 70 | 80 |

Expected result:

```python
{
    "peak_count": 3,
    "peak_start_min": 30,
    "over_capacity_ranges": [{"start_min": 30, "end_min": 50}]
}
```

At minute 30, A, B, and C are active. At minute 40, A ends as D starts, so the active count remains 3. The count falls to 2 at minute 50.

## Mocked API contract

`PickupReservationsApiService.get_reservations(store_id)` returns an object with `status_code` and `reservations`.

The companion Python file contains data models, the mocked service, a reference implementation, and runnable tests.

Run:

```bash
python pickup_capacity_monitor.py
```

Each test prints expected output, actual output, and `TEST CASE PASSED` or `TEST CASE FAILED`.

## Follow-up prompts

1. **Large input:** The service may return millions of reservations. Discuss time and memory complexity.
2. **Live updates:** Reservations can be added or cancelled while the monitor runs. How would you update results without recomputing everything?
3. **Multiple stores:** Analyze capacity for many stores in one request.
4. **Cancellation events:** A reservation may be cancelled after creation. Define how cancellation affects its interval.
5. **Changing capacity:** The store's capacity may vary over time. Extend the input model.

## Interviewer notes

- The central technique is a sweep line over start/end events.
- For half-open intervals, end events take effect before starts at the same timestamp.
- Adjacent overloaded segments should be merged.
- Expected complexity for `R` valid reservations: `O(R log R)` time and `O(R)` space.
