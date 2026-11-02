# Q070 - HealthCare Management System
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed

def multiply(args):
    i, row, A = args
    return i, [sum(row[k] * A[k][j] for k in range(4)) for j in range(4)]

with open("matrix_70.csv") as f:
    A = [[float(x) for x in r[1:]] for r in list(csv.reader(f))[1:]]

print("MPI MATRIX MULTIPLICATION (SCATTER-GATHER)")
print("Input Matrix:", *A, sep="\n")

C = [None] * 4
print("\n[SCATTER] Distributing rows")

with ThreadPoolExecutor(max_workers=4) as pool:
    tasks = [pool.submit(multiply, (i, A[i], A)) for i in range(4)]

    for task in as_completed(tasks):
        i, C[i] = task.result()
        print(f"[GATHER] Row {i} received")

print("\nFinal Matrix (A x A):")
for row in C:
    print(row)
