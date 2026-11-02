"""Offline Bully leader-election simulation."""

import csv
from pathlib import Path


CSV_FILE = Path(__file__).resolve().parent / "bully_cluster_312.csv"
EXPECTED_COLUMNS = ["node_id", "is_alive", "is_current_coordinator"]


def as_bool(value):
    return value.strip().upper() == "TRUE"


def read_nodes():
    with CSV_FILE.open("r", encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != EXPECTED_COLUMNS:
            raise ValueError(f"Expected columns {EXPECTED_COLUMNS}, got {reader.fieldnames}")
        nodes = [
            {
                "node_id": int(row["node_id"]),
                "is_alive": as_bool(row["is_alive"]),
                "is_current_coordinator": as_bool(row["is_current_coordinator"]),
            }
            for row in reader
        ]
    return sorted(nodes, key=lambda node: node["node_id"])


def main():
    nodes = read_nodes()
    # The CSV explicitly identifies the current coordinator and live nodes.
    coordinators = [node for node in nodes if node["is_current_coordinator"]]
    alive = [node for node in nodes if node["is_alive"]]
    if len(coordinators) != 1 or not alive:
        raise ValueError("Dataset needs exactly one current coordinator and one live node")

    coordinator = coordinators[0]
    if coordinator["is_alive"]:
        print(f"[STATUS] Coordinator Node {coordinator['node_id']} is alive; no election needed")
        return

    print(f"[DETECT] Coordinator Node {coordinator['node_id']} has failed")
    initiator = min(alive, key=lambda node: node["node_id"])
    print(f"[INITIATOR] Node {initiator['node_id']} starts the election")
    # In Bully election, the initiator contacts every higher live node.
    higher_nodes = [node for node in alive if node["node_id"] > initiator["node_id"]]
    for node in higher_nodes:
        print(f"[ELECTION] Node {initiator['node_id']} -> Node {node['node_id']}")
        print(f"[OK] Node {node['node_id']} -> Node {initiator['node_id']}")

    leader = max(alive, key=lambda node: node["node_id"])
    print(f"[WINNER] Highest alive node is Node {leader['node_id']}")
    for node in alive:
        if node["node_id"] != leader["node_id"]:
            print(f"[COORDINATOR] Node {leader['node_id']} -> Node {node['node_id']}")


if __name__ == "__main__":
    main()
