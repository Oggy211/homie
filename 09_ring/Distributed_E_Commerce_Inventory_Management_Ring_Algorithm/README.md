# Q203 - Ring Algorithm

**Project domain:** Distributed E-Commerce Inventory Management  
**Topic:** RING ALGORITHM (LEADER ELECTION)  
**Source page: 51** of `DC SAMPLE LAB MANUAL.pdf`

## Aim

Implement the Ring Leader Election Algorithm in the terminal to simulate coordinator failure and circulate election tokens among active ring nodes from a CSV for the application domain 'Distributed E-Commerce Inventory Management'.

## Files and data

- `ring_nodes_203.csv` - exact source filename and ordered schema: `node_id, next_node_id, is_active, priority_rank`
- `main.py` - commented, standard-library-only implementation
- `expected_output.txt` - stdout captured from the included CSV

The first data row is the manual's exact sample row. Remaining rows are synthetic dummy data added only to make the demonstration complete and repeatable.

## How it works

An election token follows the ring, skips inactive nodes, and elects the highest active node ID as required by the chit.

**Documented demonstration assumption:** The schema has no coordinator flag, so the highest-ID node is treated as the previous coordinator. `priority_rank` is retained but the source-required highest node ID determines the winner.

## Run

From this folder:

```bash
python main.py
```

The program also works when launched from another directory because it resolves the CSV beside `main.py`.

## Source-required verification

Terminal prints: Detected failure of coordinator, token message circulation across active ring nodes, and final election of node with the highest ID. Ensure the program executes directly within the VS Code terminal to demonstrate all steps clearly.
