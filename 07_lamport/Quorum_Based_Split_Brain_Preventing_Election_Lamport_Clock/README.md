# Q095 - Lamport Clock

**Project domain:** Quorum-Based Split-Brain-Preventing Election  
**Topic:** CLOCK SYNCHRONIZATION - LAMPORT'S LOGICAL CLOCK  
**Source page: 24** of `DC SAMPLE LAB MANUAL.pdf`

## Aim

Implement Lamport's Logical Clock in the terminal to assign timestamps to a sequence of events from a CSV and print their total causal order for the application domain 'Quorum-Based Split-Brain-Preventing Election'.

## Files and data

- `events_95.csv` - exact source filename and ordered schema: `event_id, process_id, event_type, message_to, initial_clock`
- `main.py` - commented, standard-library-only implementation
- `expected_output.txt` - stdout captured from the included CSV

The first data row is the manual's exact sample row. Remaining rows are synthetic dummy data added only to make the demonstration complete and repeatable.

## How it works

Each event updates a process clock. RECEIVE events apply L = max(L, T_msg) + 1, followed by a deterministic total order.

**Documented demonstration assumption:** Because the schema has no message ID/source column, messages are matched FIFO; on RECEIVE, `message_to` is interpreted as the source process.

## Run

From this folder:

```bash
python main.py
```

The program also works when launched from another directory because it resolves the CSV beside `main.py`.

## Source-required verification

Terminal prints: Step-by-step clock updates using L = max(L, T_msg) + 1 and the final sorted causal order of all events. Ensure the program executes directly within the VS Code terminal to demonstrate all steps clearly.
