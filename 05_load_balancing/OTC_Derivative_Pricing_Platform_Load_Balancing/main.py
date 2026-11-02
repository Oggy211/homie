"""Offline Round-Robin dynamic load-balancing simulation."""

import csv
from pathlib import Path


CSV_FILE = Path(__file__).resolve().parent / "workload_234.csv"
EXPECTED_COLUMNS = ["job_id", "compute_units", "assigned_worker", "status"]


def read_jobs():
    with CSV_FILE.open("r", encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != EXPECTED_COLUMNS:
            raise ValueError(f"Expected columns {EXPECTED_COLUMNS}, got {reader.fieldnames}")
        jobs = list(reader)
    if not jobs:
        raise ValueError("The workload dataset is empty")
    return jobs


def main():
    jobs = read_jobs()
    # Three local workers keep the terminal demonstration easy to follow.
    worker_names = ["W1", "W2", "W3"]
    loads = {worker: 0 for worker in worker_names}
    counts = {worker: 0 for worker in worker_names}
    for index, job in enumerate(jobs):
        # Modulo cycles deterministically through W1, W2, and W3.
        worker = worker_names[index % len(worker_names)]
        units = int(job["compute_units"])
        loads[worker] += units
        counts[worker] += 1
        print(
            f"[ALLOCATE] {job['job_id']} -> {worker} | units={units} | "
            f"current_load={loads[worker]} | status=ASSIGNED"
        )
    print("[FINAL LOAD DISTRIBUTION]")
    for worker in worker_names:
        print(f"{worker}: jobs={counts[worker]} total_load={loads[worker]}")


if __name__ == "__main__":
    main()
