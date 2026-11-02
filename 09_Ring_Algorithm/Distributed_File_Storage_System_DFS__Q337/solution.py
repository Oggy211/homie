# Q337 - Distributed File Storage System (DFS)
import csv

with open('ring_nodes_337.csv', newline="") as file:
    nodes = {int(row["node_id"]): row for row in csv.DictReader(file)}
active = sorted(n for n in nodes if nodes[n]["is_active"].upper() == "TRUE")

def next_active(node):
    node = int(nodes[node]["next_node_id"])
    while node not in active:
        print("Bypassing inactive node", node)
        node = int(nodes[node]["next_node_id"])
    return node

previous = max(nodes) if nodes else None
if not active:
    print("No active nodes: no leader can be elected.")
elif previous in active:
    print("Coordinator", previous, "is active; no election is needed.")
else:
    print("Previous coordinator", previous, "failed.")
    start = active[0]
    current = start
    token = [start]
    while True:
        successor = next_active(current)
        print(f"TOKEN: {current} -> {successor}; candidates = {token}")
        if successor == start:
            break
        token.append(successor)
        current = successor
    winner = max(token)
    print("COORDINATOR:", winner, "has the highest active ID.")
    current = winner
    while True:
        successor = next_active(current)
        print(f"COORDINATOR: {current} -> {successor}; leader = {winner}")
        current = successor
        if current == winner:
            break
    print("Final leader:", winner)
