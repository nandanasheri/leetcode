# DoorDash ICR Mock Interview: Dasher Availability Matcher

**Time limit:** 60 minutes  
**Language:** Python  
**Difficulty:** Medium  
**Allowed:** Built-in sorting functions  
**Focus:** Intervals, filtering, greedy algorithms, service integration, and error handling

> This is an original mock-interview exercise inspired by the format of DoorDash's sample ICR question. It is not an official DoorDash interview question.

## Problem Statement

### Overview

You're building a scheduling helper for DoorDash's Dasher logistics platform.

When an order is ready for pickup, DoorDash needs to identify Dashers whose availability overlaps with the order's pickup window. A downstream service provides the availability windows for each Dasher.

Your task is to implement a service that identifies eligible Dashers and returns them in a predictable order.

### Requirements

Given an order's pickup window and a list of Dashers, implement a service that:

1. Fetches availability windows for each Dasher from a mocked downstream API.
2. Ignores invalid availability windows.
3. Determines which Dashers have availability that overlaps the order's pickup window.
4. Returns the eligible Dashers sorted by their earliest available start time.

For this exercise, assume each Dasher can have multiple availability windows.

### Overlap Definition

Represent time intervals as half-open intervals: `[start_min, end_min)`.

A Dasher is eligible if **at least one valid availability window overlaps the order's pickup window**.

Two intervals overlap if:

```python
max(start_a, start_b) < min(end_a, end_b)
```

Intervals that merely touch at an endpoint do not overlap. For example, `[60, 120)` and `[120, 180)` do not overlap.

### Response Format

Return a list of dictionaries:

```python
[
    {
        "dasher_id": 101,
        "earliest_available_min": 90
    },
    {
        "dasher_id": 205,
        "earliest_available_min": 100
    }
]
```

The results should be sorted by `earliest_available_min` in ascending order. If two Dashers have the same earliest available time, sort by `dasher_id` in ascending order.

For this exercise, `earliest_available_min` means the earliest start time among that Dasher's valid availability windows that overlap the requested pickup window. In other words, report the start of the overlapping portion: `max(window.start_min, pickup_start_min)`.

## Provided Starter Code

The accompanying `dasher_availability_matcher.py` file contains the data models, mocked downstream API, and the method to implement.

Implement `DasherAvailabilityMatcher.find_eligible_dashers(...)`.

### Method Contract

```python
def find_eligible_dashers(
    self,
    dashers: List[Dasher],
    pickup_start_min: int,
    pickup_end_min: int,
) -> List[Dict]:
    ...
```

Rules:

- The pickup window is `[pickup_start_min, pickup_end_min)`.
- Availability windows are `[start_min, end_min)`.
- Ignore invalid availability windows where `end_min <= start_min`.
- A Dasher is eligible if at least one valid window overlaps the pickup window.
- If a Dasher has multiple overlapping windows, return them once.
- Report the earliest overlapping start time for each Dasher.
- Sort results by `(earliest_available_min, dasher_id)`.
- You may use Python's built-in `sorted()` or `.sort()`.

## Test Case 1: Basic Matching

Use this test case to check the implementation:

```python
availability_by_dasher = {
    101: ListAvailabilityResponse([
        AvailabilityWindow(60, 120),
        AvailabilityWindow(130, 180),
    ]),
    205: ListAvailabilityResponse([
        AvailabilityWindow(100, 150),
    ]),
    309: ListAvailabilityResponse([
        AvailabilityWindow(180, 240),
    ]),
    412: ListAvailabilityResponse([
        AvailabilityWindow(90, 90),  # Invalid
        AvailabilityWindow(110, 140),
    ]),
}

api = DasherAvailabilityApiService(availability_by_dasher)
matcher = DasherAvailabilityMatcher(api)

dashers = [
    Dasher(101),
    Dasher(205),
    Dasher(309),
    Dasher(412),
]

result = matcher.find_eligible_dashers(
    dashers,
    pickup_start_min=100,
    pickup_end_min=160,
)

print(result)
```

### Expected Output

```python
[
    {"dasher_id": 101, "earliest_available_min": 100},
    {"dasher_id": 205, "earliest_available_min": 100},
    {"dasher_id": 412, "earliest_available_min": 110},
]
```

Dasher `309` is excluded because their availability starts at minute 180, after the pickup window ends at minute 160.

Dasher `101`'s availability starts at minute 60, but the earliest overlapping start is minute 100, the beginning of the intersection between their availability and the pickup window.

## Interviewer-Only Follow-Ups

Do not give these extensions to the candidate at the start. Introduce them after the core implementation is working.

### Follow-up 1: Handle Downstream Failures

**Prompt:** What should happen if the availability API returns a 500 response for one Dasher?

Discuss assumptions before changing the code. Consider:

- Should one failed request prevent all other Dashers from being considered?
- How should a missing response differ from an empty availability list?
- Should the service retry failed requests?

For this mock, a reasonable initial choice is to exclude that Dasher while processing the remaining Dashers. The candidate should state the assumption explicitly.

### Follow-up 2: Prioritize Dashers With the Most Overlapping Availability

**Prompt:** Product now wants to prioritize Dashers who have the most available time overlapping the pickup window. Break ties using the earliest overlapping start time, then `dasher_id`.

Example:

```text
Pickup window: [100, 200)

Dasher 101: [90, 150)    -> 50 minutes overlap
Dasher 205: [120, 180)   -> 60 minutes overlap
Dasher 309: [160, 220)   -> 40 minutes overlap
```

Expected ranking:

```text
205 -> 60 minutes
101 -> 50 minutes
309 -> 40 minutes
```

For this mock, use the **total overlap duration across all valid availability windows** for each Dasher. Ask the candidate to update the ranking without breaking eligibility filtering.

### Follow-up 3: Deduplicate Dashers

**Prompt:** The incoming Dasher list may contain duplicate IDs. Ensure each Dasher is returned only once.

Example:

```python
dashers = [
    Dasher(101),
    Dasher(205),
    Dasher(101),
]
```

Expected: Dashers `101` and `205` appear at most once each.

In this starter model, a Dasher has only an ID, so duplicate IDs represent the same Dasher.

### Follow-up 4: Optimize API Usage

**Prompt:** The same Dasher can appear in multiple requests. How could you reduce unnecessary downstream API calls?

Discuss:

- Cache expiration.
- Stale availability data.
- What happens when availability changes.
- Whether cached results can be safely shared across requests.

The candidate does not need to implement a distributed caching system.

## Suggested 60-Minute Interview Structure

| Time | Activity | What to evaluate |
|---|---|---|
| 0–10 min | Clarify requirements and inspect starter code | Identifies interval boundaries and invalid-input behavior |
| 10–30 min | Implement matching and run the basic test | Correctness and integration with the mocked API |
| 30–40 min | Introduce downstream failures and edge cases | Reliability and testing |
| 40–50 min | Introduce availability-based ranking | Extensibility and reasoning |
| 50–60 min | Test, debug, and discuss complexity and trade-offs | Code quality and communication |

These timings are a mock-interview plan, not official DoorDash timing requirements.

## Evaluation Checklist

- [ ] Clarifies interval boundary semantics.
- [ ] Filters invalid availability windows.
- [ ] Correctly determines interval overlap.
- [ ] Calculates the earliest overlapping start time.
- [ ] Returns each Dasher at most once.
- [ ] Sorts by `(earliest_available_min, dasher_id)`.
- [ ] Handles empty responses and downstream failures thoughtfully.
- [ ] Tests empty inputs, invalid windows, touching intervals, and ties.
- [ ] Keeps downstream API access separate from matching logic.
- [ ] Explains assumptions and trade-offs.
