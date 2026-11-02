"""Offline Berkeley physical-clock synchronization simulation."""

import csv
from pathlib import Path


CSV_FILE = Path(__file__).resolve().parent / "node_clocks_274.csv"
EXPECTED_COLUMNS = ["node_id", "clock_time_sec", "is_faulty"]


def as_bool(value):
    return value.strip().upper() == "TRUE"


def read_clocks():
    with CSV_FILE.open("r", encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != EXPECTED_COLUMNS:
            raise ValueError(f"Expected columns {EXPECTED_COLUMNS}, got {reader.fieldnames}")
        return [
            {
                "node_id": row["node_id"],
                "clock": int(row["clock_time_sec"]),
                "faulty": as_bool(row["is_faulty"]),
            }
            for row in reader
        ]


def main():
    clocks = read_clocks()
    # First show every value returned by the polling phase.
    for node in clocks:
        print(
            f"[POLL] {node['node_id']} time={node['clock']} sec "
            f"faulty={str(node['faulty']).upper()}"
        )
    valid = [node for node in clocks if not node["faulty"]]
    faulty = [node for node in clocks if node["faulty"]]
    if not valid:
        raise ValueError("No non-faulty clocks are available")
    for node in faulty:
        print(f"[DISCARD] {node['node_id']} time={node['clock']} sec")
    # Berkeley synchronization averages only the non-faulty clocks.
    average = sum(node["clock"] for node in valid) / len(valid)
    print(f"[AVERAGE] synchronized_time={average:.1f} sec")
    for node in valid:
        adjustment = average - node["clock"]
        print(f"[ADJUST] {node['node_id']} {adjustment:+.1f} sec")


if __name__ == "__main__":
    main()
