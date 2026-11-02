# Q045 - CLOCK SYNCHRONIZATION - LAMPORT'S LOGICAL CLOCK

Project: Scalable Distributed Learning Management System (LMS)

## Aim

Implement Lamport's Logical Clock in the terminal to assign timestamps to a sequence of events from a CSV and print their total causal order for the application domain 'Scalable Distributed Learning Management System (LMS)'.

## Run

Open this folder in VS Code, open a terminal in this same folder, and run:

```text
python solution.py
```

Python 3 and its standard library are enough. On Windows, `py solution.py` also works.
The code reads `events_45.csv` directly, like the sample program you supplied.

## Working

Lamport clocks increment at local/send events. A receive uses max(local clock, message timestamp) + 1. Sorting by timestamp, process, and event gives a deterministic total order consistent with causality.

1. Initialize each process once from its first CSV initial_clock value.
2. Increment for LOCAL or SEND; SEND queues the timestamp.
3. For RECEIVE, take the oldest matching message and apply max(local, received) + 1.
4. Sort recorded (timestamp, process, event) tuples and print the total order.

## Files

- `solution.py`: short program for this experiment.
- `events_45.csv`: input data, including the manual's sample row.
- `sample_output.txt`: actual output from a run with this CSV.
- `README.md`: these instructions and a short explanation.

## Notes

- Rows are clean events with event_type LOCAL, SEND or RECEIVE.
- On SEND message_to is the destination; on RECEIVE it is interpreted as the source because the CSV has no message_from.
- Each directed channel pairs messages FIFO. Every receive has a preceding matching send.
- initial_clock is used only when a process first appears. Later rows do not reset its clock.
- Timestamp order is consistent with happened-before but cannot prove a causal relationship between arbitrary events.
- Additional rows are illustrative. P2 starts at 5 to show max(local, received) + 1.
- Extra CSV rows are illustrative examples. Use the same column names and input conventions when editing them.


Source question: DC SAMPLE LAB MANUAL.pdf, Q45.
