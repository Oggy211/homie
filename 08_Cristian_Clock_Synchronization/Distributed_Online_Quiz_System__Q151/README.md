# Q151 - CLOCK SYNCHRONIZATION - CRISTIAN'S ALGORITHM

Project: Distributed Online Quiz System

## Aim

Implement Cristian's Clock Synchronization in the terminal to calculate round- trip time (RTT), time server drift, and adjusted client time from CSV records for the application domain 'Distributed Online Quiz System'.

## Run

Open this folder in VS Code, open a terminal in this same folder, and run:

```text
python solution.py
```

Python 3 and its standard library are enough. On Windows, `py solution.py` also works.
The code reads `cristian_clocks_151.csv` directly, like the sample program you supplied.

## Working

Cristian synchronization estimates server time at client receipt by adding half the round-trip time to the server reading. Its difference from client receipt time gives the clock adjustment.

1. Read send, server and receive times.
2. Calculate RTT = receive - send.
3. Calculate estimated server time = server + RTT / 2.
4. Calculate clock adjustment = estimated server time - client receive time.

## Files

- `solution.py`: short program for this experiment.
- `cristian_clocks_151.csv`: input data, including the manual's sample row.
- `sample_output.txt`: actual output from a run with this CSV.
- `README.md`: these instructions and a short explanation.

## Notes

- Input rows are clean numeric clock readings in milliseconds; receive time is at least send time.
- The network delay is symmetric and server processing time is negligible.
- t_server_ms is the server reading returned in the response.
- A single exchange estimates clock offset. Clock drift rate requires measurements over time.
- Added rows illustrate positive, zero and negative adjustments.
- Extra CSV rows are illustrative examples. Use the same column names and input conventions when editing them.


Source question: DC SAMPLE LAB MANUAL.pdf, Q151.
