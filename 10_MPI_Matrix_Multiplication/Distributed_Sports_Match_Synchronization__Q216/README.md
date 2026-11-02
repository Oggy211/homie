# Q216 - MPI MATRIX MULTIPLICATION (PARALLEL SCATTER- GATHER)

Project: Distributed Sports Match Synchronization

## Aim

Implement parallel matrix multiplication using a simulated MPI Scatter-Gather pattern in the terminal using multiprocessing/threads to compute row dot products for the application domain 'Distributed Sports Match Synchronization'.

## Run

Open this folder in VS Code, open a terminal in this same folder, and run:

```text
python solution.py
```

Python 3 and its standard library are enough. On Windows, `py solution.py` also works.
The code reads `matrix_216.csv` directly, like the sample program you supplied.

## Working

Each output row is calculated from one row of A and all columns of A. The thread pool distributes row calculations and gathers the results.

1. Read the 4 x 4 matrix A.
2. Submit one row calculation per thread-pool task.
3. Calculate row-column dot products.
4. Gather each result into its original row position.
5. Print C = A x A.

## Files

- `solution.py`: short program for this experiment.
- `matrix_216.csv`: input data, including the manual's sample row.
- `sample_output.txt`: actual output from a run with this CSV.
- `README.md`: these instructions and a short explanation.

## Notes

- Run solution.py from its own folder.
- The CSV has exactly four data rows and four numeric columns after row_id.
- Only one matrix is supplied, so the script computes A x A.
- The MPI scatter-gather pattern is simulated with local threads, exactly as in the supplied example.
- Gather messages can appear in a different order; the final matrix row order stays correct.
- Extra CSV rows are illustrative examples. Use the same column names and input conventions when editing them.
- Thread or worker messages may appear in a different order on another run. The final result stays the same.

Source question: DC SAMPLE LAB MANUAL.pdf, Q216.
