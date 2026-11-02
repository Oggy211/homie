# Q091 - Cristian's Algorithm

**Project domain:** Adaptive Fault-Tolerant Distributed Task Execution System  
**Topic:** CLOCK SYNCHRONIZATION - CRISTIAN'S ALGORITHM  
**Source page: 23** of `DC SAMPLE LAB MANUAL.pdf`

## Aim

Implement Cristian's Clock Synchronization in the terminal to calculate round-trip time (RTT), time server drift, and adjusted client time from CSV records for the application domain 'Adaptive Fault-Tolerant Distributed Task Execution System'.

## Files and data

- `cristian_clocks_91.csv` - exact source filename and ordered schema: `client_id, t0_send_ms, t_server_ms, t1_recv_ms`
- `main.py` - commented, standard-library-only implementation
- `expected_output.txt` - stdout captured from the included CSV

The first data row is the manual's exact sample row. Remaining rows are synthetic dummy data added only to make the demonstration complete and repeatable.

## How it works

For each request, the program calculates RTT, estimates server time at receipt, and prints the signed local-clock adjustment.

**Documented demonstration assumption:** The calculation follows the chit formula and assumes symmetric one-way network delay.

## Run

From this folder:

```bash
python main.py
```

The program also works when launched from another directory because it resolves the CSV beside `main.py`.

## Source-required verification

Terminal prints: Calculated RTT = (T1 - T0), estimated server time = T_server + (RTT / 2), and local clock offset adjustment. Ensure the program executes directly within the VS Code terminal to demonstrate all steps clearly.
