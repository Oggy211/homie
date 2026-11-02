# Q328 - Online Banking System
import csv
import threading
import time

with open("tasks_328.csv") as f:
    tasks = list(csv.DictReader(f))

lock = threading.Lock()
completed = []

def worker(name):
    for task in tasks:
        if task["thread_name"] != name or task["status"] != "PENDING":
            continue
        task_id = task["task_id"]
        with lock:
            print(f"{name} locked task {task_id}")
            task["status"] = "RUNNING"
        print(f"{name} released lock; working on {task_id}")
        time.sleep(int(task["burst_ms"]) / 1000)
        with lock:
            task["status"] = "COMPLETED"
            completed.append(task_id)
            print(f"{name} completed {task_id}; count = {len(completed)}")

names = list(dict.fromkeys(task["thread_name"] for task in tasks))
threads = [threading.Thread(target=worker, args=(name,)) for name in names]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("Completed tasks:", ", ".join(sorted(completed)))
print("Total completed:", len(completed))
