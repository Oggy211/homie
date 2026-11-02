"""Deterministic multithreading and mutex demonstration."""

import csv
import threading
import time
from pathlib import Path


CSV_FILE = Path(__file__).resolve().parent / "tasks_321.csv"
EXPECTED_COLUMNS = ["task_id", "thread_name", "burst_ms", "priority", "status"]


def read_tasks():
    with CSV_FILE.open("r", encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != EXPECTED_COLUMNS:
            raise ValueError(f"Expected columns {EXPECTED_COLUMNS}, got {reader.fieldnames}")
        tasks = list(reader)
    if not tasks:
        raise ValueError("The task dataset is empty")
    return tasks


def main():
    tasks = read_tasks()
    mutex = threading.Lock()
    completed = []
    ordered_logs = [None] * len(tasks)

    def worker(index, task):
        # A scaled delay models work without making the lab demo slow.
        time.sleep(int(task["burst_ms"]) / 100000.0)
        logs = [
            f"[THREAD] {task['thread_name']} starts {task['task_id']} "
            f"priority={task['priority']} burst={task['burst_ms']}ms",
            f"[LOCK] {task['thread_name']} waiting",
        ]
        # Only one thread may update the shared completion list at a time.
        with mutex:
            logs.append(f"[LOCK] {task['thread_name']} acquired")
            completed.append(task["task_id"])
            logs.append(f"[PROCESS] {task['task_id']} status=COMPLETED")
        logs.append(f"[LOCK] {task['thread_name']} released")
        ordered_logs[index] = logs

    threads = []
    for index, task in enumerate(tasks):
        thread = threading.Thread(target=worker, args=(index, task), name=task["thread_name"])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

    # Logs are printed in CSV order so repeated runs have identical output.
    for logs in ordered_logs:
        for line in logs:
            print(line)
    input_order = {task["task_id"]: index for index, task in enumerate(tasks)}
    completed.sort(key=input_order.get)
    print("[FINAL COMPLETED TASK LIST] " + ", ".join(completed))


if __name__ == "__main__":
    main()
