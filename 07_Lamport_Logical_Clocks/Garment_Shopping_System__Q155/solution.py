# Q155 - Garment Shopping System
import csv
from collections import defaultdict, deque

print('Lamport logical clocks')
with open('events_155.csv', newline="") as file:
    rows = list(csv.DictReader(file))

clocks = {}
messages = defaultdict(deque)
events = []

for row in rows:
    event, process = row["event_id"], row["process_id"]
    action, peer = row["event_type"], row["message_to"]
    # The first row for a process sets its initial clock; later rows do not reset it.
    clocks.setdefault(process, int(row["initial_clock"]))
    old = clocks[process]
    if action == "RECEIVE":
        # For RECEIVE, peer is the source; take its oldest pending message.
        incoming = messages[(peer, process)].popleft()
        clocks[process] = max(old, incoming) + 1
        print(event, process, "RECEIVE: max(", old, ",", incoming, ") + 1 =", clocks[process])
    else:
        clocks[process] += 1
        print(event, process, action, ":", old, "+ 1 =", clocks[process])
        if action == "SEND":
            messages[(process, peer)].append(clocks[process])
            print("Message:", process, "->", peer, "timestamp:", clocks[process])
    events.append((clocks[process], process, event))

print("Total order consistent with causality:")
for timestamp, process, event in sorted(events):
    print(event, process, "timestamp:", timestamp)
print("Pending messages:", sum(len(queue) for queue in messages.values()))
