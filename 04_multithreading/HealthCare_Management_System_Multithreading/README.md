# Q066 - Multithreading

**Project domain:** HealthCare Management System  
**Topic:** MULTITHREADING (CONCURRENT PROCESSING & LOCKS)  
**Source page: 17** of `DC SAMPLE LAB MANUAL.pdf`

## Aim

Implement a multithreaded worker simulation in the terminal using thread locks (Mutex) to safely process tasks from a CSV file without race conditions for the application domain 'HealthCare Management System'.

## Files and data

- `tasks_66.csv` - exact source filename and ordered schema: `task_id, thread_name, burst_ms, priority, status`
- `main.py` - commented, standard-library-only implementation
- `expected_output.txt` - stdout captured from the included CSV

The first data row is the manual's exact sample row. Remaining rows are synthetic dummy data added only to make the demonstration complete and repeatable.

## How it works

One thread processes each task. A mutex protects the shared completion list, and logs are printed in CSV order for repeatable output.

**Documented demonstration assumption:** Burst delays are scaled down so the offline demonstration finishes quickly while still using real threads and a real lock.

## Run

From this folder:

```bash
python main.py
```

The program also works when launched from another directory because it resolves the CSV beside `main.py`.

## Source-required verification

Terminal prints: Concurrent thread execution logs, lock acquisition/release steps, and final completed task list. Ensure the program executes directly within the VS Code terminal to demonstrate all steps clearly.
