"""Offline vector-clock simulation for three processes."""

import csv
from collections import defaultdict
from pathlib import Path


CSV_FILE = Path(__file__).resolve().parent / "vector_events_68.csv"
EXPECTED_COLUMNS = ["event_id", "process_id", "event_action", "target_process"]


def read_events():
    with CSV_FILE.open("r", encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != EXPECTED_COLUMNS:
            raise ValueError(f"Expected columns {EXPECTED_COLUMNS}, got {reader.fieldnames}")
        return list(reader)


def happens_before(first, second):
    return all(a <= b for a, b in zip(first, second)) and any(
        a < b for a, b in zip(first, second)
    )


def main():
    events = read_events()
    process_names = sorted({event["process_id"] for event in events})
    if process_names != ["P1", "P2", "P3"]:
        raise ValueError("This chit demonstration expects processes P1, P2, and P3")
    index = {process: position for position, process in enumerate(process_names)}
    clocks = {process: [0, 0, 0] for process in process_names}
    messages = defaultdict(list)
    event_vectors = {}

    for event in events:
        event_id = event["event_id"]
        process = event["process_id"]
        action = event["event_action"].upper()
        target = event["target_process"]
        if action == "RECEIVE":
            # Merge the queued sender snapshot before the receiver increments.
            queue = messages[(target, process)]
            if not queue:
                raise ValueError(f"No pending {target}->{process} message for {event_id}")
            incoming = queue.pop(0)
            clocks[process] = [
                max(local, received)
                for local, received in zip(clocks[process], incoming)
            ]
            clocks[process][index[process]] += 1
        elif action in {"SEND", "INTERNAL"}:
            clocks[process][index[process]] += 1
            if action == "SEND":
                messages[(process, target)].append(clocks[process].copy())
        else:
            raise ValueError(f"Unknown action {action}")
        event_vectors[event_id] = clocks[process].copy()
        print(f"[EVENT] {event_id} {process} {action} {target} -> {clocks[process]}")

    print("[PAIR RELATIONS]")
    # Comparable vectors are causal; incomparable vectors are concurrent.
    event_ids = list(event_vectors)
    for left_index, left_id in enumerate(event_ids):
        for right_id in event_ids[left_index + 1 :]:
            left = event_vectors[left_id]
            right = event_vectors[right_id]
            if happens_before(left, right):
                print(f"Causally Preceding: {left_id} < {right_id}")
            elif happens_before(right, left):
                print(f"Causally Preceding: {right_id} < {left_id}")
            else:
                print(f"Concurrent: {left_id} || {right_id}")


if __name__ == "__main__":
    main()
