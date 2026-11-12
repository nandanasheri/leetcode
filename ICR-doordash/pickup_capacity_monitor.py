from dataclasses import dataclass
from typing import List, Dict, Optional, Any


@dataclass
class PickupReservation:
    reservation_id: str
    start_min: int
    end_min: int


@dataclass
class PickupReservationsResponse:
    status_code: int
    reservations: List[PickupReservation]


class PickupReservationsApiService:
    def __init__(self, responses_by_store: Dict[str, PickupReservationsResponse]):
        self.responses_by_store = responses_by_store

    def get_reservations(self, store_id: str) -> PickupReservationsResponse:
        return self.responses_by_store.get(
            store_id, PickupReservationsResponse(404, [])
        )


class PickupCapacityMonitor:
    def __init__(self, reservations_api: PickupReservationsApiService):
        self.reservations_api = reservations_api

    def analyze_capacity(
        self, store_id: str, capacity: int
    ) -> Optional[Dict[str, Any]]:
        if (not isinstance(capacity, int) or isinstance(capacity, bool)
                or capacity < 0):
            return None

        response = self.reservations_api.get_reservations(store_id)
        if response.status_code != 200:
            return None

        seen_ids = set()
        events = []
        for reservation in response.reservations:
            rid = reservation.reservation_id
            start, end = reservation.start_min, reservation.end_min
            if not isinstance(rid, str) or not rid or rid in seen_ids:
                continue
            if (not isinstance(start, int) or isinstance(start, bool)
                    or not isinstance(end, int) or isinstance(end, bool)):
                continue
            if end <= start:
                continue
            seen_ids.add(rid)
            events.append((start, 1))
            events.append((end, -1))

        if not events:
            return {
                "peak_count": 0,
                "peak_start_min": None,
                "over_capacity_ranges": [],
            }

        events.sort()
        active = peak_count = 0
        peak_start = None
        over_start = None
        over_ranges = []
        i = 0

        while i < len(events):
            minute = events[i][0]
            delta = 0
            while i < len(events) and events[i][0] == minute:
                delta += events[i][1]
                i += 1
            active += delta
            next_minute = events[i][0] if i < len(events) else minute
            has_interval = next_minute > minute
            is_over = has_interval and active > capacity

            if has_interval and active > peak_count:
                peak_count = active
                peak_start = minute

            if is_over and over_start is None:
                over_start = minute
            elif not is_over and over_start is not None:
                over_ranges.append({
                    "start_min": over_start,
                    "end_min": minute,
                })
                over_start = None

        return {
            "peak_count": peak_count,
            "peak_start_min": peak_start,
            "over_capacity_ranges": over_ranges,
        }


def run_test_case(name, monitor, store_id, capacity, expected):
    actual = monitor.analyze_capacity(store_id, capacity)
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
        "main": PickupReservationsResponse(200, [
            PickupReservation("A", 10, 40),
            PickupReservation("B", 20, 50),
            PickupReservation("C", 30, 45),
            PickupReservation("D", 40, 60),
            PickupReservation("E", 45, 55),
            PickupReservation("F", 70, 80),
        ]),
        "adjacent": PickupReservationsResponse(200, [
            PickupReservation("A", 0, 10),
            PickupReservation("B", 10, 20),
        ]),
        "invalid": PickupReservationsResponse(200, [
            PickupReservation("bad", 10, 10),
            PickupReservation("", 0, 20),
            PickupReservation("valid", 5, 15),
            PickupReservation("valid", 0, 100),
        ]),
        "empty": PickupReservationsResponse(200, []),
        "error": PickupReservationsResponse(503, [
            PickupReservation("A", 0, 10),
        ]),
    }
    monitor = PickupCapacityMonitor(PickupReservationsApiService(responses))
    cases = [
        ("Overlapping reservations", "main", 2, {
            "peak_count": 3, "peak_start_min": 30,
            "over_capacity_ranges": [{"start_min": 30, "end_min": 50}],
        }),
        ("Adjacent reservations do not overlap", "adjacent", 1, {
            "peak_count": 1, "peak_start_min": 0,
            "over_capacity_ranges": [],
        }),
        ("Invalid and duplicate reservations ignored", "invalid", 1, {
            "peak_count": 1, "peak_start_min": 5,
            "over_capacity_ranges": [],
        }),
        ("Empty reservation list", "empty", 2, {
            "peak_count": 0, "peak_start_min": None,
            "over_capacity_ranges": [],
        }),
        ("Downstream API failure", "error", 2, None),
        ("Invalid capacity", "main", -1, None),
    ]

    passed = 0
    for name, store_id, capacity, expected in cases:
        passed += run_test_case(name, monitor, store_id, capacity, expected)
    print(f"\\nSummary: {passed}/{len(cases)} test cases passed.")
    if passed != len(cases):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
