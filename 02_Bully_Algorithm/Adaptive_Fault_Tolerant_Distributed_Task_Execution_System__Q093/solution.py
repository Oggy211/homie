# Q093 - Adaptive Fault-Tolerant Distributed Task Execution System
import csv

with open('bully_cluster_93.csv', newline="") as file:
    nodes = {int(row["node_id"]): row for row in csv.DictReader(file)}
alive = sorted(n for n in nodes if nodes[n]["is_alive"].upper() == "TRUE")
coordinator = next((n for n in nodes
                    if nodes[n]["is_current_coordinator"].upper() == "TRUE"), None)

if not alive:
    print("No live nodes: no leader can be elected.")
elif coordinator in alive:
    print("Coordinator", coordinator, "is alive; no election is needed.")
else:
    print("Coordinator", coordinator, "failed or is missing.")
    candidate = alive[0]
    while True:
        print("Node", candidate, "starts an election.")
        responders = []
        for higher in sorted(n for n in nodes if n > candidate):
            print(f"ELECTION: {candidate} -> {higher}")
            if higher in alive:
                print(f"OK: {higher} -> {candidate}")
                responders.append(higher)
            else:
                print("No response from", higher)
        if not responders:
            break
        candidate = min(responders)
    print("COORDINATOR:", candidate, "broadcasts its election.")
    for node in alive:
        if node != candidate:
            print(f"COORDINATOR: {candidate} -> {node}")
    print("Final leader:", candidate)
