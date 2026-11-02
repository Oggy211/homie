# Q156 - MPI Matrix Multiplication

**Project domain:** Garment Shopping System  
**Topic:** MPI MATRIX MULTIPLICATION (PARALLEL SCATTER-GATHER)  
**Source page: 39** of `DC SAMPLE LAB MANUAL.pdf`

## Aim

Implement parallel matrix multiplication using a simulated MPI Scatter-Gather pattern in the terminal using multiprocessing/threads to compute row dot products for the application domain 'Garment Shopping System'.

## Files and data

- `matrix_156.csv` - exact source filename and ordered schema: `row_id, col_0, col_1, col_2, col_3`
- `main.py` - commented, standard-library-only implementation
- `expected_output.txt` - stdout captured from the included CSV

The first data row is the manual's exact sample row. Remaining rows are synthetic dummy data added only to make the demonstration complete and repeatable.

## How it works

The master scatters rows to thread workers, workers compute row dot-products, and the master gathers the ordered result matrix.

**Documented demonstration assumption:** The chit supplies one matrix only, so the deterministic demonstration computes A x A using a thread-based MPI Scatter-Gather simulation.

## Run

From this folder:

```bash
python main.py
```

The program also works when launched from another directory because it resolves the CSV beside `main.py`.

## Source-required verification

Terminal prints: Master scattering matrix rows to worker tasks, workers computing partial dot products, and master gathering the final matrix product. Ensure the program executes directly within the VS Code terminal to demonstrate all steps clearly.
