
"""
PROBLEM: Event Log Session Analysis and Ledger Reconciliation

Input:
    events: A list of dictionaries, each containing:
        - user: str
        - action: str ("login", "logout", or "action")
        - ts: int (timestamp)

    ledgers: A list of dictionaries, each containing:
        - user: str
        - timestamp: int
        - amount: float

PART 1 — Session Summary
    Process events in timestamp order and calculate, for each user:
        - active_sessions: Number of sessions started by a login.
        - active_time: Total duration across the user's sessions.

    Rules:
        1. Events may arrive in any order; sort them by timestamp.
        2. A login starts a session.
        3. An action during an active session updates its last-event time.
        4. A logout closes an active session at the logout timestamp.
        5. If a new login occurs while a session is open, close the old
           session at its last-event timestamp, then start a new session.
        6. If no logout occurs, the session ends at its last-event
           timestamp. A login with no subsequent events has duration 0.
        7. Ignore actions and logouts that occur without an open session.

PART 2 — Ledger Reconciliation
    Match each ledger charge to a session when:
        - The user matches, AND
        - session.start <= charge.timestamp <= session.end

    Return:
        - orphaned_charges: Charges that match no session.
        - unbilled_sessions: Sessions that match no charge.

    Assumption:
        Multiple charges may match the same session. A session is
        considered billed if at least one charge matches.

Complexity:
    Part 1: O(E log E) time, O(E) space.
    Part 2: O(E log E + L*S) time, O(E + L) space.
    E = number of events, L = number of ledger charges,
    S = number of sessions.
"""

from typing import TypedDict
from collections import defaultdict


class Event(TypedDict):
    user: str
    action: str
    ts: int


class Session(TypedDict):
    user: str
    start: int
    end: int


class Charge(TypedDict):
    user: str
    timestamp: int
    amount: float


def build_sessions(events: list[Event]) -> list[Session]:
    """Convert unordered events into session intervals."""
    events = sorted(events, key=lambda event: event["ts"])

    sessions: list[Session] = []
    # user -> {"start": login timestamp, "last_event": latest activity}
    state = {}

    for event in events:
        user = event["user"]
        ts = event["ts"]
        action = event["action"]

        if action == "login":
            # Close an existing session if the user logs in again.
            if user in state:
                sessions.append({
                    "user": user,
                    "start": state[user]["start"],
                    "end": state[user]["last_event"],
                })

            state[user] = {
                "start": ts,
                "last_event": ts,
            }

        elif action == "action":
            # Ignore actions outside an active session.
            if user in state:
                state[user]["last_event"] = ts

        elif action == "logout":
            # Ignore logouts outside an active session.
            if user in state:
                sessions.append({
                    "user": user,
                    "start": state[user]["start"],
                    "end": ts,
                })
                del state[user]

    # Close remaining sessions at their last observed event.
    for user, info in state.items():
        sessions.append({
            "user": user,
            "start": info["start"],
            "end": info["last_event"],
        })

    return sessions


def session_summary(events: list[Event]) -> dict:
    """Part 1: Return session count and total active time per user."""
    sessions = build_sessions(events)

    summary = defaultdict(lambda: {
        "active_sessions": 0,
        "active_time": 0,
    })

    for session in sessions:
        user = session["user"]
        summary[user]["active_sessions"] += 1
        summary[user]["active_time"] += (
            session["end"] - session["start"]
        )

    return dict(summary)


def reconcile_events(
    events: list[Event],
    ledgers: list[Charge],
) -> dict:
    """Part 2: Find orphaned charges and unbilled sessions."""
    sessions = build_sessions(events)

    matched_sessions = set()
    orphaned_charges = []

    for charge in ledgers:
        matched = False

        for session_idx, session in enumerate(sessions):
            if (
                charge["user"] == session["user"]
                and session["start"]
                <= charge["timestamp"]
                <= session["end"]
            ):
                matched = True
                matched_sessions.add(session_idx)

        if not matched:
            orphaned_charges.append(charge)

    unbilled_sessions = [
        session
        for session_idx, session in enumerate(sessions)
        if session_idx not in matched_sessions
    ]

    return {
        "orphaned_charges": orphaned_charges,
        "unbilled_sessions": unbilled_sessions,
    }


if __name__ == "__main__":
    events: list[Event] = [
        {"user": "u1", "ts": 100, "action": "login"},
        {"user": "u1", "ts": 180, "action": "action"},
        {"user": "u1", "ts": 300, "action": "login"},
        {"user": "u1", "ts": 350, "action": "logout"},
        {"user": "u2", "ts": 200, "action": "login"},
    ]

    print("Part 1:")
    print(session_summary(events))

    ledgers: list[Charge] = [
        {"user": "u1", "timestamp": 150, "amount": 10.0},
        {"user": "u1", "timestamp": 320, "amount": 20.0},
        {"user": "u2", "timestamp": 250, "amount": 5.0},
        {"user": "u3", "timestamp": 400, "amount": 15.0},
    ]

    print("\nPart 2:")
    print(reconcile_events(events, ledgers))
