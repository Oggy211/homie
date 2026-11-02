# Q114 - Distributed Data Syncing in Disaster Drone Networks
import csv

with open("workload_114.csv") as f:
    jobs = list(csv.DictReader(f))

workers = ["Worker_1", "Worker_2", "Worker_3"]
loads = dict.fromkeys(workers, 0)
counts = dict.fromkeys(workers, 0)

for i, job in enumerate(jobs):
    worker = workers[i % len(workers)]
    job["assigned_worker"] = worker
    job["status"] = "ASSIGNED"
    loads[worker] += int(job["compute_units"])
    counts[worker] += 1
    print(f"{job['job_id']} -> {worker}")
    print("Current load:", loads)

print("\nFinal summary:")
for worker in workers:
    print(f"{worker}: {counts[worker]} jobs, {loads[worker]} compute units")
