"""Offline RPC/RMI procedure-dispatch simulation."""

import csv
from pathlib import Path


CSV_FILE = Path(__file__).resolve().parent / "rpc_calls_251.csv"
EXPECTED_COLUMNS = ["call_id", "client_name", "method_name", "param_value", "timestamp"]


def read_calls():
    """Read calls and reject a CSV whose ordered schema differs from the chit."""
    # DictReader lets the program validate and use the exact named columns.
    with CSV_FILE.open("r", encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != EXPECTED_COLUMNS:
            raise ValueError(f"Expected columns {EXPECTED_COLUMNS}, got {reader.fieldnames}")
        calls = list(reader)
    if not calls:
        raise ValueError("The RPC call dataset is empty")
    return calls


def remote_procedure(method_name, value):
    """Small deterministic server-side procedure table for this demonstration."""
    if method_name == "processData":
        return value * 2
    if method_name == "squareValue":
        return value * value
    if method_name == "incrementValue":
        return value + 1
    if method_name == "validateData":
        return "VALID" if value >= 0 else "INVALID"
    raise ValueError(f"Unknown remote method: {method_name}")


def main():
    # Each CSV row is treated as one client-to-server remote call.
    for call in read_calls():
        parameter = int(call["param_value"])
        print(
            f"[DISPATCH] call={call['call_id']} client={call['client_name']} "
            f"method={call['method_name']} timestamp={call['timestamp']}"
        )
        print(f"[MARSHAL] args=[{parameter}]")
        print(f"[SERVER EXECUTION] {call['method_name']}({parameter})")
        result = remote_procedure(call["method_name"], parameter)
        print(f"[RETURN] call={call['call_id']} result={result}")


if __name__ == "__main__":
    main()
