"""Offline Ring leader-election simulation."""

import csv
from pathlib import Path


CSV_FILE = Path(__file__).resolve().parent / "ring_nodes_83.csv"
EXPECTED_COLUMNS = ["node_id", "next_node_id", "is_active", "priority_rank"]


def as_bool(value):
    return value.strip().upper() == "TRUE"


def read_nodes():
    with CSV_FILE.open("r", encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != EXPECTED_COLUMNS:
            raise ValueError(f"Expected columns {EXPECTED_COLUMNS}, got {reader.fieldnames}")
        rows = list(reader)
    return {
        int(row["node_id"]): {
            "next_node_id": int(row["next_node_id"]),
            "is_active": as_bool(row["is_active"]),
            "priority_rank": int(row["priority_rank"]),
        }
        for row in rows
    }


def main():
    nodes = read_nodes()
    if not nodes:
        raise ValueError("The ring dataset is empty")
    if any(node["next_node_id"] not in nodes for node in nodes.values()):
        raise ValueError("A next_node_id does not exist in the ring")
    previous_coordinator = max(nodes)
    # The source schema lacks a coordinator flag; the documented demo uses max ID.
    if nodes[previous_coordinator]["is_active"]:
        print(f"[STATUS] Coordinator Node {previous_coordinator} is active")
        return
    print(f"[DETECT] Coordinator Node {previous_coordinator} has failed")
    active_ids = sorted(node_id for node_id, node in nodes.items() if node["is_active"])
    if not active_ids:
        raise ValueError("No active nodes can participate")
    start = active_ids[0]
    print(f"[ELECTION START] Node {start}")
    token_nodes = [start]
    visited = {start}
    current = start
    while True:
        # Follow next_node_id and bypass every inactive ring member.
        candidate = nodes[current]["next_node_id"]
        skipped = []
        for _ in range(len(nodes)):
            if nodes[candidate]["is_active"]:
                break
            skipped.append(candidate)
            candidate = nodes[candidate]["next_node_id"]
        else:
            raise ValueError("The ring has no reachable active successor")
        suffix = f" (skipped inactive: {','.join(map(str, skipped))})" if skipped else ""
        print(f"[TOKEN] Node {current} -> Node {candidate}{suffix}")
        if candidate == start:
            break
        if candidate in visited:
            raise ValueError("Ring traversal entered a cycle before returning to start")
        visited.add(candidate)
        token_nodes.append(candidate)
        current = candidate
    leader = max(token_nodes)
    print(f"[ELECTED COORDINATOR] Node {leader} (highest active node ID)")
    for node_id in active_ids:
        if node_id != leader:
            print(f"[ANNOUNCE] Node {leader} -> Node {node_id}")


if __name__ == "__main__":
    main()
