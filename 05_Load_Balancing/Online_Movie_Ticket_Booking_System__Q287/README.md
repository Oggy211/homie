# Q287 - LOAD BALANCING (DYNAMIC WORKLOAD SCHEDULING)

Project: Online Movie Ticket Booking System

## Aim

Implement a Dynamic Load Balancing simulator (Round-Robin or Least- Connections) in the terminal to distribute a batch of incoming jobs from a CSV among worker nodes for the application domain 'Online Movie Ticket Booking System'.

## Run

Open this folder in VS Code, open a terminal in this same folder, and run:

```text
python solution.py
```

Python 3 and its standard library are enough. On Windows, `py solution.py` also works.
The code reads `workload_287.csv` directly, like the sample program you supplied.

## Working

Round-robin gives the next incoming job to the next worker, then starts again from the first worker.

1. Read the jobs and create three workers.
2. Assign each job using its row number modulo three.
3. Update the worker load and print the allocation.
4. Print the final job counts and loads.

## Files

- `solution.py`: short program for this experiment.
- `workload_287.csv`: input data, including the manual's sample row.
- `sample_output.txt`: actual output from a run with this CSV.
- `README.md`: these instructions and a short explanation.

## Notes

- Run solution.py from its own folder.
- All input jobs are PENDING and UNASSIGNED, with unique IDs and nonnegative integer compute units.
- The workers are Worker_1, Worker_2 and Worker_3.
- Round-robin balances job counts; unequal job sizes can produce unequal compute-unit loads.
- This script assigns jobs without executing them. Changes stay in memory.
- Extra CSV rows are illustrative examples. Use the same column names and input conventions when editing them.


Source question: DC SAMPLE LAB MANUAL.pdf, Q287.
