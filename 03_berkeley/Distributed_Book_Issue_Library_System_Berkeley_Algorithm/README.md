# Q200 - Berkeley Algorithm

**Project domain:** Distributed Book Issue / Library System  
**Topic:** CLOCK SYNCHRONIZATION - BERKELEY'S ALGORITHM  
**Source page: 50** of `DC SAMPLE LAB MANUAL.pdf`

## Aim

Implement the Berkeley Physical Clock Synchronization algorithm in the terminal to read node times from a CSV, discard faulty outliers, and compute average time offset for the application domain 'Distributed Book Issue / Library System'.

## Files and data

- `node_clocks_200.csv` - exact source filename and ordered schema: `node_id, clock_time_sec, is_faulty`
- `main.py` - commented, standard-library-only implementation
- `expected_output.txt` - stdout captured from the included CSV

The first data row is the manual's exact sample row. Remaining rows are synthetic dummy data added only to make the demonstration complete and repeatable.

## How it works

The coordinator polls clocks, discards rows explicitly marked faulty, averages valid times, and calculates each node's adjustment.

**Documented demonstration assumption:** The `is_faulty` field supplied by the chit controls outlier removal; no additional statistical threshold is invented.

## Run

From this folder:

```bash
python main.py
```

The program also works when launched from another directory because it resolves the CSV beside `main.py`.

## Source-required verification

Terminal prints: Polled node times, identified and discarded outlier times, calculated average time, and relative adjustment per node. Ensure the program executes directly within the VS Code terminal to demonstrate all steps clearly.
