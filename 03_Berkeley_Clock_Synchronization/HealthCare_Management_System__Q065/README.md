# Q065 - CLOCK SYNCHRONIZATION - BERKELEY'S ALGORITHM

Project: HealthCare Management System

## Aim

Implement the Berkeley Physical Clock Synchronization algorithm in the terminal to read node times from a CSV, discard faulty outliers, and compute average time offset for the application domain 'HealthCare Management System'.

## Run

Open this folder in VS Code, open a terminal in this same folder, and run:

```text
python solution.py
```

Python 3 and its standard library are enough. On Windows, `py solution.py` also works.
The code reads `node_clocks_65.csv` directly, like the sample program you supplied.

## Working

Berkeley synchronization averages accepted node clocks and sends relative adjustments to synchronize the group.

1. Read the node clocks from CSV.
2. Find the median of nonfaulty readings.
3. Discard flagged faults and readings more than 60 seconds from that median.
4. Average accepted readings and print average - local time for each accepted node.

## Files

- `solution.py`: short program for this experiment.
- `node_clocks_65.csv`: input data, including the manual's sample row.
- `sample_output.txt`: actual output from a run with this CSV.
- `README.md`: these instructions and a short explanation.

## Notes

- Input rows are clean and use TRUE/FALSE exactly as shown.
- At least one nonfaulty reading remains within the 60-second median-distance threshold.
- The 60-second threshold is an explicit demonstration choice. The median filter assumes a majority of reasonable readings.
- The coordinator and polling delays are implicit. Excluded nodes receive no adjustment.
- Additional CSV rows are illustrative demonstration data.
- Extra CSV rows are illustrative examples. Use the same column names and input conventions when editing them.


Source question: DC SAMPLE LAB MANUAL.pdf, Q65.
