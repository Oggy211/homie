"""Offline Cristian clock-synchronization calculation."""

import csv
from pathlib import Path


CSV_FILE = Path(__file__).resolve().parent / "cristian_clocks_271.csv"
EXPECTED_COLUMNS = ["client_id", "t0_send_ms", "t_server_ms", "t1_recv_ms"]


def read_records():
    with CSV_FILE.open("r", encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != EXPECTED_COLUMNS:
            raise ValueError(f"Expected columns {EXPECTED_COLUMNS}, got {reader.fieldnames}")
        return list(reader)


def main():
    for record in read_records():
        # RTT estimates the complete request-response network delay.
        t0 = int(record["t0_send_ms"])
        server = int(record["t_server_ms"])
        t1 = int(record["t1_recv_ms"])
        rtt = t1 - t0
        if rtt < 0:
            raise ValueError(f"Negative RTT for {record['client_id']}")
        # Symmetric delay means the response takes approximately RTT / 2.
        estimated = server + rtt / 2
        adjustment = estimated - t1
        print(
            f"[CLIENT {record['client_id']}] RTT={rtt} ms | "
            f"estimated_server_time={estimated:.1f} ms | "
            f"adjustment={adjustment:+.1f} ms"
        )


if __name__ == "__main__":
    main()
