# Q227 - Load Balancing

**Project domain:** Distributed Payment Gateway System  
**Topic:** LOAD BALANCING (DYNAMIC WORKLOAD SCHEDULING)  
**Source page: 57** of `DC SAMPLE LAB MANUAL.pdf`

## Aim

Implement a Dynamic Load Balancing simulator (Round-Robin or Least-Connections) in the terminal to distribute a batch of incoming jobs from a CSV among worker nodes for the application domain 'Distributed Payment Gateway System'.

## Files and data

- `workload_227.csv` - exact source filename and ordered schema: `job_id, compute_units, assigned_worker, status`
- `main.py` - commented, standard-library-only implementation
- `expected_output.txt` - stdout captured from the included CSV

The first data row is the manual's exact sample row. Remaining rows are synthetic dummy data added only to make the demonstration complete and repeatable.

## How it works

The simulator uses the Round-Robin option allowed by the chit and reports each assignment plus final worker loads.

**Documented demonstration assumption:** Three synthetic worker nodes (W1-W3) are used for the local demonstration.

## Run

From this folder:

```bash
python main.py
```

The program also works when launched from another directory because it resolves the CSV beside `main.py`.

## Source-required verification

Terminal prints: Incoming job allocations, current load per worker, and balanced summary of tasks across all worker nodes. Ensure the program executes directly within the VS Code terminal to demonstrate all steps clearly.
