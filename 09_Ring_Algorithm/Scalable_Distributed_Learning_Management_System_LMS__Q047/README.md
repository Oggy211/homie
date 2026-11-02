# Q047 - RING ALGORITHM (LEADER ELECTION)

Project: Scalable Distributed Learning Management System (LMS)

## Aim

Implement the Ring Leader Election Algorithm in the terminal to simulate coordinator failure and circulate election tokens among active ring nodes from a CSV for the application domain 'Scalable Distributed Learning Management System (LMS)'.

## Run

Open this folder in VS Code, open a terminal in this same folder, and run:

```text
python solution.py
```

Python 3 and its standard library are enough. On Windows, `py solution.py` also works.
The code reads `ring_nodes_47.csv` directly, like the sample program you supplied.

## Working

A ring election passes a token along the configured ring. Active nodes add their IDs; the highest collected ID wins. A coordinator message then circulates around the active ring.

1. Read the nodes and identify active IDs.
2. Treat the highest configured ID as the previous coordinator and detect its failure.
3. Follow next_node_id links, bypass inactive nodes, and circulate an election token.
4. Choose the highest ID in the returned token.
5. Circulate the coordinator announcement around the active ring.

## Files

- `solution.py`: short program for this experiment.
- `ring_nodes_47.csv`: input data, including the manual's sample row.
- `sample_output.txt`: actual output from a run with this CSV.
- `README.md`: these instructions and a short explanation.

## Notes

- Because the CSV has no coordinator field, the highest configured ID is assumed to be the former coordinator; sample node 5 is inactive.
- Election uses the highest active node ID, as the manual requires. priority_rank does not determine the winner.
- The CSV contains valid numeric IDs and next_node_id links forming one complete ring. Inactive nodes are bypassed along those links.
- Sample data is illustrative. Run this program from its experiment folder with python solution.py.
- Extra CSV rows are illustrative examples. Use the same column names and input conventions when editing them.


Source question: DC SAMPLE LAB MANUAL.pdf, Q47.
