# Q258 - RMI / RPC (REMOTE INVOCATION SIMULATION)

Project: Airline E-Ticketing Booking System

## Aim

Simulate an RPC/RMI client-server procedure dispatcher in the terminal that reads method calls from a CSV file, marshals arguments, executes the remote function, and prints the returned result for the application domain 'Airline E-Ticketing Booking System'.

## Run

Open this folder in VS Code, open a terminal in this same folder, and run:

```text
python solution.py
```

Python 3 and its standard library are enough. On Windows, `py solution.py` also works.
The code reads `rpc_calls_258.csv` directly, like the sample program you supplied.

## Working

RPC uses client and server stubs to serialize a call, dispatch a remote procedure, and return its result. Here JSON carries the request and response in a local terminal simulation.

1. Read calls from the CSV.
2. Serialize each call as JSON, then deserialize it at the simulated server.
3. Use the method table to execute processData, which doubles the numeric input.
4. Serialize and deserialize the response and print the result.

## Files

- `solution.py`: short program for this experiment.
- `rpc_calls_258.csv`: input data, including the manual's sample row.
- `sample_output.txt`: actual output from a run with this CSV.
- `README.md`: these instructions and a short explanation.

## Notes

- processData is defined as doubling a numeric domain reading because the manual does not specify its calculation.
- The supplied dataset contains valid processData calls. This short demonstration assumes the same headers and valid numeric input.
- RPC is simulated locally; the JSON request and response are actually serialized and deserialized.
- Sample data is illustrative. Run this program from its experiment folder with python solution.py.
- Extra CSV rows are illustrative examples. Use the same column names and input conventions when editing them.


Source question: DC SAMPLE LAB MANUAL.pdf, Q258.
