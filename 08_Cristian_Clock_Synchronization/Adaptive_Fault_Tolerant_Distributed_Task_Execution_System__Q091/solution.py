# Q091 - Adaptive Fault-Tolerant Distributed Task Execution System
import csv

print('Cristian clock synchronization')
with open('cristian_clocks_91.csv', newline="") as file:
    rows = list(csv.DictReader(file))

for row in rows:
    t0 = float(row["t0_send_ms"])
    server = float(row["t_server_ms"])
    t1 = float(row["t1_recv_ms"])
    rtt = t1 - t0
    estimated = server + rtt / 2
    offset = estimated - t1
    print("Client:", row["client_id"])
    print("RTT:", rtt, "ms")
    print("Estimated server time:", estimated, "ms")
    print("Clock adjustment:", offset, "ms")
    print("Adjusted client time:", estimated, "ms")
