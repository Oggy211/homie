# Q072 - BULLY ALGORITHM (LEADER ELECTION)

Project: Cloud-Edge Distributed Computing Framework

## Aim

Implement the Bully Leader Election Algorithm in the terminal where a node detects coordinator failure from CSV data and bullies lower-ID nodes to become leader for the application domain 'Cloud-Edge Distributed Computing Framework'.

## Run

Open this folder in VS Code, open a terminal in this same folder, and run:

```text
python solution.py
```

Python 3 and its standard library are enough. On Windows, `py solution.py` also works.
The code reads `bully_cluster_72.csv` directly, like the sample program you supplied.

## Working

In the Bully algorithm, a detecting live node sends ELECTION messages to higher-ID nodes. Higher live nodes reply OK and take over; the highest live node then announces itself as coordinator.

1. Read the cluster and identify live nodes and the old coordinator.
2. If the coordinator failed, let the lowest live node start an election.
3. Send ELECTION to every higher ID and print OK only for live respondents.
4. Let a higher respondent continue the election until no live higher node responds.
5. Broadcast COORDINATOR from the final candidate.

## Files

- `solution.py`: short program for this experiment.
- `bully_cluster_72.csv`: input data, including the manual's sample row.
- `sample_output.txt`: actual output from a run with this CSV.
- `README.md`: these instructions and a short explanation.

## Notes

- IDs determine priority. The sample marks node 5, the former coordinator, as failed.
- The cascade runs sequentially through higher respondents to keep the printed simulation easy to follow.
- The CSV contains unique numeric IDs, TRUE/FALSE fields, and at most one recorded coordinator.
- Sample data is illustrative. Run this program from its experiment folder with python solution.py.
- Extra CSV rows are illustrative examples. Use the same column names and input conventions when editing them.


Source question: DC SAMPLE LAB MANUAL.pdf, Q72.
