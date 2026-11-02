# Q168 - Vector Clocks

**Project domain:** Banking Home Loan Management  
**Topic:** CLOCK SYNCHRONIZATION - VECTOR CLOCKS  
**Source page: 42** of `DC SAMPLE LAB MANUAL.pdf`

## Aim

Implement Vector Clocks [V1, V2, V3] in the terminal to track event vectors from a CSV and determine whether event pairs are causally related or concurrent for the application domain 'Banking Home Loan Management'.

## Files and data

- `vector_events_168.csv` - exact source filename and ordered schema: `event_id, process_id, event_action, target_process`
- `main.py` - commented, standard-library-only implementation
- `expected_output.txt` - stdout captured from the included CSV

The first data row is the manual's exact sample row. Remaining rows are synthetic dummy data added only to make the demonstration complete and repeatable.

## How it works

Each process maintains a three-element vector. SEND snapshots are queued, RECEIVE merges a snapshot, and event pairs are classified as causal or concurrent.

**Documented demonstration assumption:** Because the schema has no message ID, SEND/RECEIVE records are matched FIFO; on RECEIVE, `target_process` is interpreted as the source process.

## Run

From this folder:

```bash
python main.py
```

The program also works when launched from another directory because it resolves the CSV beside `main.py`.

## Source-required verification

Terminal prints: Updated vector clock [v1, v2, v3] after each event and explicitly identifies pairs as Causally Preceding (V1 < V2) or Concurrent (E1 || E2). Ensure the program executes directly within the VS Code terminal to demonstrate all steps clearly.
