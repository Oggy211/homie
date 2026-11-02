# Simple Distributed Computing Lab Solutions

340 short Python programs, grouped by topic and then project domain.
The folder names and question numbers follow the earlier package.

## Run an experiment

1. Extract this ZIP.
2. Find the question in INDEX.csv.
3. Open its project folder in VS Code.
4. Open a terminal in that folder and run `python solution.py`.

The scripts use direct CSV reading and a few short functions, in the style of your
matrix example. They expect the supplied CSV format. Python's standard library is
enough; there are no extra packages to install.

## Files in each project

- solution.py: the short program.
- Required CSV file: sample input with the exact filename and columns from the manual.
- README.md: aim, run instructions, algorithm, and necessary assumptions.
- sample_output.txt: actual output from that program and input.

## Other files

- INDEX.csv: all questions, topics, project domains, paths, and code line counts.
- FILE_LIST.txt: every file in the ZIP.
- VERIFICATION.txt: run results and algorithm checks.

Only topic/domain combinations that appear in the manual are included: 10 topics,
55 distinct project domains, and 340 project/question folders.

RPC/RMI and MPI are local simulations as specified in the manual. The matrix
program follows your supplied sample and computes A x A. Choices left unspecified
in the manual are explained briefly in the relevant README.

Sample CSV rows beyond those in the manual are illustrative. Worker completion
messages can appear in a different order across runs.
