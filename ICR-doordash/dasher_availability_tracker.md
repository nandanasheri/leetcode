# SAMPLE AI CODE CRAFT QUESTION

## Dasher Availability Tracker

### What to build

DoorDash needs a simple system to keep track of which Dashers are available to receive delivery offers.

Build a working system that continuously ingests a feed of Dasher status updates. Each update identifies a Dasher and includes their current status and the delivery zone they are in. The system should maintain the latest known state for each Dasher.

Anyone running the system should be able to look up a Dasher's current status and retrieve the Dashers who are currently available in a particular zone.

The system should keep running and process updates as they arrive, rather than execute once and exit, so we can observe it live.

### What we care about

- A working end-to-end system that ingests updates and supports live queries.
- Reasonable scope and design decisions under time pressure.
- Correct handling of duplicate updates and updates that arrive out of order.
- Correct results when multiple updates arrive close together.
- Effective use of Codex to plan, implement, test, and debug the system.

Use any language or framework you prefer. You must use Codex as your agentic coding environment.

---

### Interviewer extensions (share one at a time)

1. A Dasher may move between delivery zones while remaining available. Make sure queries reflect the latest zone.
2. The same update may be delivered more than once. Ensure it does not cause incorrect state.
3. Updates may arrive out of order. Decide how the system determines which update is newest.
4. Add a way to retrieve the number of available Dashers in each zone.
5. The system restarts. Discuss or implement how current Dasher state can be recovered.
