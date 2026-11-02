# Q074 - MULTITHREADING (CONCURRENT PROCESSING & LOCKS)

Project: Cloud-Edge Distributed Computing Framework

## Aim

Implement a multithreaded worker simulation in the terminal using thread locks (Mutex) to safely process tasks from a CSV file without race conditions for the application domain 'Cloud- Edge Distributed Computing Framework'.

## Run

Open this folder in VS Code, open a terminal in this same folder, and run:

```text
python solution.py
```

Python 3 and its standard library are enough. On Windows, `py solution.py` also works.
The code reads `tasks_74.csv` directly, like the sample program you supplied.

## Working

Threads work at the same time. A lock protects task status changes and the shared completed-task list.

1. Read tasks from the CSV.
2. Start one thread for each worker name.
3. Lock briefly to claim a task, then release the lock while doing the work.
4. Lock again to record completion.
5. Wait for all threads and print the completed tasks.

## Files

- `solution.py`: short program for this experiment.
- `tasks_74.csv`: input data, including the manual's sample row.
- `sample_output.txt`: actual output from a run with this CSV.
- `README.md`: these instructions and a short explanation.

## Notes

- Run solution.py from its own folder so the CSV filename can be found.
- The sample contains unique task IDs, integer nonnegative burst times and PENDING tasks.
- thread_name assigns each task to that named worker. Each worker processes its tasks in CSV order; priority is not used.
- The work is simulated with a short sleep. Output lines from different threads can appear in a different order.
- Updated statuses stay in memory; the CSV is not changed.
- Extra CSV rows are illustrative examples. Use the same column names and input conventions when editing them.
- Thread or worker messages may appear in a different order on another run. The final result stays the same.

Source question: DC SAMPLE LAB MANUAL.pdf, Q74.
