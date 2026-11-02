# Q253 - Book My Show Ticket Reservation
import csv
from statistics import mean, median

print('Berkeley clock synchronization')
with open('node_clocks_253.csv', newline="") as file:
    nodes = list(csv.DictReader(file))

threshold = 60
times = [float(n["clock_time_sec"]) for n in nodes if n["is_faulty"] == "FALSE"]
center = median(times)
accepted = []
print("Median:", center, "Outlier threshold:", threshold, "seconds")

for node in nodes:
    name = node["node_id"]
    time = float(node["clock_time_sec"])
    print("Polled", name, "time:", time)
    if node["is_faulty"] == "TRUE":
        print("Discarded", name, "because it is faulty")
    elif abs(time - center) > threshold:
        print("Discarded", name, "because it is an outlier")
    else:
        accepted.append((name, time))

average = mean(time for name, time in accepted)
print("Average time:", round(average, 3))
for name, time in accepted:
    print(name, "adjustment:", round(average - time, 3), "seconds")
