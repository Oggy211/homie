# Q100 - Bully Algorithm

**Project domain:** Quorum-Based Split-Brain-Preventing Election  
**Topic:** BULLY ALGORITHM (LEADER ELECTION)  
**Source page: 25** of `DC SAMPLE LAB MANUAL.pdf`

## Aim

Implement the Bully Leader Election Algorithm in the terminal where a node detects coordinator failure from CSV data and bullies lower-ID nodes to become leader for the application domain 'Quorum-Based Split-Brain-Preventing Election'.

## Files and data

- `bully_cluster_100.csv` - exact source filename and ordered schema: `node_id, is_alive, is_current_coordinator`
- `main.py` - commented, standard-library-only implementation
- `expected_output.txt` - stdout captured from the included CSV

The first data row is the manual's exact sample row. Remaining rows are synthetic dummy data added only to make the demonstration complete and repeatable.

## How it works

A live initiator contacts higher-ID live nodes. The highest live node wins and announces itself as coordinator.

**Documented demonstration assumption:** The extra rows create a deterministic failed-coordinator scenario while preserving the source sample row exactly.

## Run

From this folder:

```bash
python main.py
```

The program also works when launched from another directory because it resolves the CSV beside `main.py`.

## Source-required verification

Terminal prints: Initiator sending ELECTION to higher nodes, higher nodes responding with OK, and the highest alive node broadcasting COORDINATOR. Ensure the program executes directly within the VS Code terminal to demonstrate all steps clearly.
