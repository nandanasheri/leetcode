from typing import Dict, List


# --- Data Models ---


class AvailabilityWindow:
    def __init__(self, start_min: int, end_min: int):
        self.start_min = start_min
        self.end_min = end_min


class Dasher:
    def __init__(self, dasher_id: int):
        self.dasher_id = dasher_id


class HttpResponse:
    def __init__(self, status_code: int = 200):
        self.status_code = status_code


class ListAvailabilityResponse(HttpResponse):
    def __init__(
        self,
        windows: List[AvailabilityWindow] = None,
        status_code: int = 200,
    ):
        super().__init__(status_code)
        self.windows = windows if windows is not None else []


# --- Mocked Downstream Service ---


class DasherAvailabilityApiService:
    def __init__(
        self,
        availability_by_dasher: Dict[int, ListAvailabilityResponse],
    ):
        self.availability_by_dasher = availability_by_dasher

    def get_availability(self, dasher_id: int) -> ListAvailabilityResponse:
        return self.availability_by_dasher.get(
            dasher_id,
            ListAvailabilityResponse([], status_code=404),
        )


# --- Core Service (to implement) ---


class DasherAvailabilityMatcher:
    def __init__(self, availability_api: DasherAvailabilityApiService):
        self.availability_api = availability_api

    def find_eligible_dashers(
        self,
        dashers: List[Dasher],
        pickup_start_min: int,
        pickup_end_min: int,
    ) -> List[Dict]:
        """
        Return eligible Dashers sorted by their earliest overlapping
        availability start time, then by dasher_id.

        Rules:
        - Pickup window is [pickup_start_min, pickup_end_min).
        - Availability windows are [start_min, end_min).
        - Ignore invalid availability windows where end_min <= start_min.
        - A Dasher is eligible if at least one valid window overlaps
          the pickup window.
        - For each Dasher, report the earliest overlapping start time.
        - If a Dasher has multiple overlapping windows, return them once.
        - Sort results by (earliest_available_min, dasher_id).

        TODO: Implement the method.
        """
        # Candidate implementation goes here.
        raise NotImplementedError


# --- Test Harness ---


def test_basic_matching():
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

    actual = matcher.find_eligible_dashers(
        dashers,
        pickup_start_min=100,
        pickup_end_min=160,
    )

    expected = [
        {"dasher_id": 101, "earliest_available_min": 100},
        {"dasher_id": 205, "earliest_available_min": 100},
        {"dasher_id": 412, "earliest_available_min": 110},
    ]

    assert actual == expected, f"Expected {expected}, got {actual}"
    print("PASS: basic matching")


if __name__ == "__main__":
    test_basic_matching()
