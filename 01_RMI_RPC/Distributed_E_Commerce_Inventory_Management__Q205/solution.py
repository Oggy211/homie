# Q205 - Distributed E-Commerce Inventory Management
import csv
import json

def processData(value):
    return value * 2

methods = {"processData": processData}
with open('rpc_calls_205.csv', newline="") as file:
    calls = list(csv.DictReader(file))

for call in calls:
    print(f"[DISPATCH] {call['client_name']} calls {call['method_name']}")
    request_json = json.dumps(call)
    print("Request JSON:", request_json)
    request = json.loads(request_json)
    value = float(request["param_value"])
    print(f"[SERVER EXECUTION] Processing parameter {value:g}")
    result = methods[request["method_name"]](value)
    response_json = json.dumps({"result": result})
    response = json.loads(response_json)
    print(f"[RETURN] Result = {response['result']:g}")
