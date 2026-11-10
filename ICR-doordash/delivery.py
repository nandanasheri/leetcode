from dataclasses import dataclass
from typing import List, Optional, Dict, Any


@dataclass
class DeliveryQuote:
    provider_id: str
    fee_cents: int
    eta_minutes: int
    available: bool


@dataclass
class DeliveryQuotesResponse:
    status_code: int
    quotes: List[DeliveryQuote]


class DeliveryQuotesApiService:
    """Mock downstream service."""

    def __init__(self, responses_by_order: Dict[str, DeliveryQuotesResponse]):
        self.responses_by_order = responses_by_order

    def get_quotes(self, order_id: str) -> DeliveryQuotesResponse:
        return self.responses_by_order.get(
            order_id, DeliveryQuotesResponse(status_code=404, quotes=[])
        )


class DeliveryQuoteSelector:
    def __init__(self, quotes_api: DeliveryQuotesApiService):
        self.quotes_api = quotes_api

    def select_quote(
        self, order_id: str, max_eta_minutes: int
    ) -> Optional[Dict[str, Any]]:
        """Return the best eligible quote, or None."""
        if (not isinstance(max_eta_minutes, int)
                or isinstance(max_eta_minutes, bool)
                or max_eta_minutes <= 0):
            return None

        response = self.quotes_api.get_quotes(order_id)
        if response.status_code != 200:
            return None

        best = None
        for quote in response.quotes:
            if not isinstance(quote.provider_id, str) or not quote.provider_id:
                continue
            if (not isinstance(quote.fee_cents, int)
                    or isinstance(quote.fee_cents, bool)
                    or quote.fee_cents < 0):
                continue
            if (not isinstance(quote.eta_minutes, int)
                    or isinstance(quote.eta_minutes, bool)
                    or quote.eta_minutes <= 0):
                continue
            if quote.available is not True:
                continue
            if quote.eta_minutes > max_eta_minutes:
                continue

            key = (quote.fee_cents, quote.eta_minutes, quote.provider_id)
            if best is None or key < (
                best.fee_cents, best.eta_minutes, best.provider_id
            ):
                best = quote

        if best is None:
            return None
        return {
            "provider_id": best.provider_id,
            "fee_cents": best.fee_cents,
            "eta_minutes": best.eta_minutes,
        }


def run_test_case(name, selector, order_id, max_eta, expected):
    actual = selector.select_quote(order_id, max_eta)
    print(f"\\n{name}")
    print(f"Expected output: {expected}")
    print(f"Actual output:   {actual}")
    if actual == expected:
        print("TEST CASE PASSED")
        return True
    print("TEST CASE FAILED")
    return False


def main():
    responses = {
        "order-123": DeliveryQuotesResponse(200, [
            DeliveryQuote("alpha", 499, 35, True),
            DeliveryQuote("bravo", 399, 45, True),    # ETA too high
            DeliveryQuote("charlie", 399, 30, True),
            DeliveryQuote("delta", 399, 30, True),    # loses provider tie-break
            DeliveryQuote("echo", 250, 20, False),    # unavailable
            DeliveryQuote("foxtrot", -1, 15, True),   # invalid fee
            DeliveryQuote("golf", 300, 0, True),      # invalid ETA
            DeliveryQuote("", 100, 10, True),         # invalid provider ID
            DeliveryQuote("hotel", True, 10, True),   # bool is not a valid fee
        ]),
        "order-no-match": DeliveryQuotesResponse(200, [
            DeliveryQuote("alpha", 100, 50, True),
            DeliveryQuote("bravo", 200, 20, False),
        ]),
        "order-api-error": DeliveryQuotesResponse(
            503, [DeliveryQuote("alpha", 100, 10, True)]
        ),
        "order-empty": DeliveryQuotesResponse(200, []),
    }

    selector = DeliveryQuoteSelector(DeliveryQuotesApiService(responses))
    cases = [
        ("Main selection and tie-break", "order-123", 40,
         {"provider_id": "charlie", "fee_cents": 399, "eta_minutes": 30}),
        ("No eligible quote", "order-no-match", 30, None),
        ("Downstream API failure", "order-api-error", 30, None),
        ("Empty quote list", "order-empty", 30, None),
        ("Invalid maximum ETA", "order-123", 0, None),
    ]

    passed = 0
    for name, order_id, max_eta, expected in cases:
        passed += run_test_case(
            name, selector, order_id, max_eta, expected
        )

    print(f"\\nSummary: {passed}/{len(cases)} test cases passed.")
    if passed != len(cases):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
