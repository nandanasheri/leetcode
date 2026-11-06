# DoorDash ICR Mock Interview 3: Delivery Quote Selector

**Format:** 60 minutes · **Language:** Python · **Difficulty:** Medium  
**Built-in sorting:** Allowed (though a single-pass solution is sufficient).

## Problem

A DoorDash order can receive delivery quotes from several providers. Each quote has:
- `provider_id`: provider identifier
- `fee_cents`: delivery fee in cents
- `eta_minutes`: estimated delivery time
- `available`: whether the provider can fulfill the delivery

Implement `DeliveryQuoteSelector.select_quote(order_id, max_eta_minutes)`.

### Eligibility
A quote is eligible only if:
1. `provider_id` is a non-empty string.
2. `fee_cents` is a non-negative integer.
3. `eta_minutes` is a positive integer.
4. `available` is exactly `True`.
5. `eta_minutes <= max_eta_minutes`.

Ignore malformed/ineligible quotes. In Python, explicitly reject booleans for numeric fields (`bool` is a subclass of `int`).

### Selection / tie-breaking
Choose the eligible quote with:
1. Lowest `fee_cents`.
2. If tied, lowest `eta_minutes`.
3. If still tied, lexicographically smallest `provider_id`.

Return `{"provider_id": ..., "fee_cents": ..., "eta_minutes": ...}` or `None` if there is no eligible quote. If the downstream API returns a non-200 status, return `None`.

## Example

For `order_id="order-123"` and `max_eta_minutes=40`:

| Provider | Fee (cents) | ETA (minutes) | Available |
|---|---:|---:|---|
| alpha | 499 | 35 | true |
| bravo | 399 | 45 | true |
| charlie | 399 | 30 | true |
| delta | 399 | 30 | true |
| echo | 250 | 20 | false |
| foxtrot | -1 | 15 | true |
| golf | 300 | 0 | true |

Expected result:

```python
{"provider_id": "charlie", "fee_cents": 399, "eta_minutes": 30}
```

`bravo` is too slow; `echo` is unavailable; `foxtrot` and `golf` have invalid values. `charlie` wins the final tie-break over `delta`.

## Mocked API contract

`DeliveryQuotesApiService.get_quotes(order_id)` returns a response with `status_code` and `quotes`. The companion Python file provides the mock classes and a runnable test harness.

Run:

```bash
python delivery_quote_selector.py
```

The harness prints the **expected output**, **actual output**, and `TEST CASE PASSED` or `TEST CASE FAILED` for every test.

## Suggested interview progression

- **0–10 min:** Clarify eligibility, tie-breaking, and API failure behavior.
- **10–25 min:** Implement validation and filtering.
- **25–35 min:** Implement deterministic selection.
- **35–40 min:** Run tests and add edge cases.
- **40–50 min:** Discuss duplicate quotes from one provider.
- **50–60 min:** Discuss quote expiration, caching, and explainability.

## Follow-up questions

1. If one provider returns multiple eligible quotes, should all be considered, or should only its cheapest quote be kept?
2. Add an `expires_at` field and ignore expired quotes. How would you test time-dependent behavior reliably?
3. Distinguish “no eligible quote” from “the quote service failed.” What should the caller receive?
4. Return a reason for each rejected quote, without changing the selected quote.
5. Add configurable ranking that trades off fee and ETA. Why might explicit tie-breaking be easier to reason about than a weighted score?

## Expected complexity

Let `Q` be the number of returned quotes:
- Time: `O(Q)` using a single pass.
- Auxiliary space: `O(1)` beyond the returned result.

You do not need to sort the quotes.
