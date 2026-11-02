# Q161 - CLOCK SYNCHRONIZATION - VECTOR CLOCKS

Project: Stock Market Exchange Order Matching

## Aim

Implement Vector Clocks [V1, V2, V3] in the terminal to track event vectors from a CSV and determine whether event pairs are causally related or concurrent for the application domain 'Stock Market Exchange Order Matching'.

## Run

Open this folder in VS Code, open a terminal in this same folder, and run:

```text
python solution.py
```

Python 3 and its standard library are enough. On Windows, `py solution.py` also works.
The code reads `vector_events_161.csv` directly, like the sample program you supplied.

## Working

Vector clocks track causal history. Each event increments its process component. A receive first merges the message vector by componentwise maximum. Ordered vectors identify causal precedence; incomparable vectors identify concurrency.

1. Initialize P1, P2 and P3 to [0, 0, 0].
2. For RECEIVE, merge the oldest matching message vector.
3. Increment the local component for every event. SEND queues a vector copy.
4. Compare every pair of recorded vectors and print causal precedence or concurrency.

## Files

- `solution.py`: short program for this experiment.
- `vector_events_161.csv`: input data, including the manual's sample row.
- `sample_output.txt`: actual output from a run with this CSV.
- `README.md`: these instructions and a short explanation.

## Notes

- CSV rows are clean execution-trace events for P1, P2 and P3, in that vector order.
- event_action is LOCAL, SEND or RECEIVE. LOCAL has an empty target_process.
- On SEND target_process names the destination; on RECEIVE it names the source.
- The schema has no message ID. Each directed sender/receiver channel therefore pairs messages FIFO.
- Every receive has a preceding matching send. Unreceived sends are allowed and counted as pending.
- Additional rows are illustrative demonstration events.
- Extra CSV rows are illustrative examples. Use the same column names and input conventions when editing them.


Source question: DC SAMPLE LAB MANUAL.pdf, Q161.
