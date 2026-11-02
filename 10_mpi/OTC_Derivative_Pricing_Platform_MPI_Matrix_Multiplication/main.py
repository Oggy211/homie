"""Thread-based MPI Scatter-Gather matrix-multiplication simulation."""

import csv
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


CSV_FILE = Path(__file__).resolve().parent / "matrix_237.csv"
EXPECTED_COLUMNS = ["row_id", "col_0", "col_1", "col_2", "col_3"]


def read_matrix():
    with CSV_FILE.open("r", encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != EXPECTED_COLUMNS:
            raise ValueError(f"Expected columns {EXPECTED_COLUMNS}, got {reader.fieldnames}")
        rows = list(reader)
    labels = [row["row_id"] for row in rows]
    matrix = [[int(row[f"col_{column}"]) for column in range(4)] for row in rows]
    if len(matrix) != 4 or len(set(labels)) != 4:
        raise ValueError("The Scatter-Gather demo requires four unique 4-column rows")
    return labels, matrix


def main():
    labels, matrix_a = read_matrix()
    matrix_b = matrix_a  # The source supplies one matrix, so demonstrate A x A.

    def multiply_row(item):
        row_index, row = item
        output = []
        for column in range(4):
            dot_product = sum(
                row[position] * matrix_b[position][column]
                for position in range(4)
            )
            output.append(dot_product)
        return row_index, output

    for row_index, label in enumerate(labels):
        print(f"[MASTER SCATTER] {label} -> Worker {row_index}")
    # executor.map preserves input order, making captured output deterministic.
    with ThreadPoolExecutor(max_workers=4) as executor:
        partial_rows = list(executor.map(multiply_row, enumerate(matrix_a)))
    for row_index, output in partial_rows:
        print(f"[WORKER {row_index}] partial_row={output}")
        print(f"[MASTER GATHER] received {labels[row_index]}")
    print("[FINAL MATRIX PRODUCT A x A]")
    for _row_index, output in partial_rows:
        print(output)


if __name__ == "__main__":
    main()
