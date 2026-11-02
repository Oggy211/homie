"""Offline Lamport logical-clock simulation."""

import csv
from collections import defaultdict
from pathlib import Path


CSV_FILE = Path(__file__).resolve().parent / "events_222.csv"
EXPECTED_COLUMNS = ["event_id", "process_id", "event_type", "message_to", "initial_clock"]


def read_events():
    with CSV_FILE.open("r", encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != EXPECTED_COLUMNS:
            raise ValueError(f"Expected columns {EXPECTED_COLUMNS}, got {reader.fieldnames}")
        return list(reader)


def main():
    events = read_events()
    process_names = sorted({event["process_id"] for event in events})
    clocks = {process: 0 for process in process_names}
    messages = defaultdict(list)
    timestamps = {}
    for event in events:
        event_id = event["event_id"]
        process = event["process_id"]
        event_type = event["event_type"].upper()
        peer = event["message_to"]
        local_before = max(clocks[process], int(event["initial_clock"]))
        if event_type == "RECEIVE":
            # A receive event incorporates the timestamp carried by the message.
            queue = messages[(peer, process)]
            if not queue:
                raise ValueError(f"No pending {peer}->{process} message for {event_id}")
            message_time = queue.pop(0)
            clocks[process] = max(local_before, message_time) + 1
            formula = f"L=max({local_before}, {message_time})+1={clocks[process]}"
        elif event_type in {"SEND", "INTERNAL"}:
            clocks[process] = local_before + 1
            formula = f"L={local_before}+1={clocks[process]}"
            if event_type == "SEND":
                messages[(process, peer)].append(clocks[process])
        else:
            raise ValueError(f"Unknown event type {event_type}")
        timestamps[event_id] = clocks[process]
        print(f"[EVENT] {event_id} {process} {event_type} {peer} | {formula}")

    total_order = sorted(timestamps, key=lambda event_id: (timestamps[event_id], event_id))
    # Event ID is a stable tie-breaker when two Lamport times are equal.
    print("[TOTAL CAUSAL ORDER]")
    print(" -> ".join(f"{event_id}@{timestamps[event_id]}" for event_id in total_order))


if __name__ == "__main__":
    main()
