# Split

A box-drawing table for the remaining axis. One table.

- Corner cell: a noun that names the row labels, chosen to fit those rows. Never blank.
- Other header cells: the options being compared.
- First column: `Label - short gloss` when the label needs it.
- One constraint line under the table when something sits outside the comparison.

```text
┌───────────────────────────────┬──────────────────────────────┬─────────────────────────────┐
│ Axis                          │ CodeMode                     │ RLM + Python REPL           │
├───────────────────────────────┼──────────────────────────────┼─────────────────────────────┤
│ Job - what the loop is for    │ compose host tools           │ keep data out of the prompt │
├───────────────────────────────┼──────────────────────────────┼─────────────────────────────┤
│ Heap - where values live      │ dies when execute returns    │ lives across turns          │
├───────────────────────────────┼──────────────────────────────┼─────────────────────────────┤
│ Runtime - who executes        │ allowlist JS walker          │ CPython kernel              │
├───────────────────────────────┼──────────────────────────────┼─────────────────────────────┤
│ Effects - what code may touch │ tools.* and search only      │ ambient unless wrapped      │
├───────────────────────────────┼──────────────────────────────┼─────────────────────────────┤
│ LLM from inside               │ no                           │ llm_query on heap slices    │
├───────────────────────────────┼──────────────────────────────┼─────────────────────────────┤
│ Resume - what survives        │ transcript + files           │ the process is the resume   │
├───────────────────────────────┼──────────────────────────────┼─────────────────────────────┤
│ Loop - who owns the turn      │ ReAct, execute is one Action │ REPL often is the loop      │
└───────────────────────────────┴──────────────────────────────┴─────────────────────────────┘
```
