# Q078 - RMI / RPC

**Project domain:** Cost-Efficient Fault Monitoring for Distributed Clusters  
**Topic:** RMI / RPC (REMOTE INVOCATION SIMULATION)  
**Source page: 20** of `DC SAMPLE LAB MANUAL.pdf`

## Aim

Simulate an RPC/RMI client-server procedure dispatcher in the terminal that reads method calls from a CSV file, marshals arguments, executes the remote function, and prints the returned result for the application domain 'Cost-Efficient Fault Monitoring for Distributed Clusters'.

## Files and data

- `rpc_calls_78.csv` - exact source filename and ordered schema: `call_id, client_name, method_name, param_value, timestamp`
- `main.py` - commented, standard-library-only implementation
- `expected_output.txt` - stdout captured from the included CSV

The first data row is the manual's exact sample row. Remaining rows are synthetic dummy data added only to make the demonstration complete and repeatable.

## How it works

The client reads each call, marshals its argument, dispatches it to a local server procedure, and prints the returned value.

**Documented demonstration assumption:** The manual does not define remote method semantics. The included method rules are deterministic demonstration behavior and are not presented as source facts.

## Run

From this folder:

```bash
python main.py
```

The program also works when launched from another directory because it resolves the CSV beside `main.py`.

## Source-required verification

Terminal prints: [DISPATCH] Client invoking method -> [SERVER EXECUTION] Processing parameter -> [RETURN] Result printed to terminal. Ensure the program executes directly within the VS Code terminal to demonstrate all steps clearly.
