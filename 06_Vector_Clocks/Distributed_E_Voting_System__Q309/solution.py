# Q309 - Distributed E-Voting System
import csv
from collections import defaultdict, deque
from itertools import combinations

print('Vector clocks')
with open('vector_events_309.csv', newline="") as file:
    rows = list(csv.DictReader(file))

processes = ["P1", "P2", "P3"]
clocks = {p: [0, 0, 0] for p in processes}
messages = defaultdict(deque)
events = []

for row in rows:
    event, process = row["event_id"], row["process_id"]
    action, peer = row["event_action"], row["target_process"]
    if action == "RECEIVE":
        # For RECEIVE, peer names the source. Each channel is FIFO.
        incoming = messages[(peer, process)].popleft()
        clocks[process] = [max(a, b) for a, b in zip(clocks[process], incoming)]
    clocks[process][processes.index(process)] += 1
    if action == "SEND":
        messages[(process, peer)].append(clocks[process].copy())
    vector = clocks[process].copy()
    events.append((event, vector))
    print(event, process, action, peer, "vector:", vector)

for (a, va), (b, vb) in combinations(events, 2):
    before = all(x <= y for x, y in zip(va, vb)) and va != vb
    after = all(y <= x for x, y in zip(va, vb)) and va != vb
    if before:
        print("Causally preceding:", a, "<", b)
    elif after:
        print("Causally preceding:", b, "<", a)
    else:
        print("Concurrent:", a, "||", b)
print("Pending messages:", sum(len(queue) for queue in messages.values()))
