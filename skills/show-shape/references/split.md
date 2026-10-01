# Split

A box-drawing table for the remaining axis. One table.

- Corner cell: a noun that names the row labels, chosen to fit those rows. Never blank.
- Other header cells: the options being compared.
- First column: `Label - short gloss` when the label needs it.
- One constraint line under the table when something sits outside the comparison.

```text
┌────────────────────────────┬─────────────────────────┬──────────────────────────┐
│ Axis                       │ CodeMode                │ RLM + Python REPL        │
├────────────────────────────┼─────────────────────────┼──────────────────────────┤
│ Job - loop purpose         │ compose host tools      │ keep data out of prompt  │
├────────────────────────────┼─────────────────────────┼──────────────────────────┤
│ Heap - values live         │ ends with execute       │ lives across turns       │
├────────────────────────────┼─────────────────────────┼──────────────────────────┤
│ Runtime - executor         │ allowlist JS walker     │ CPython kernel           │
├────────────────────────────┼─────────────────────────┼──────────────────────────┤
│ Effects - code access      │ tools.* and search      │ ambient unless wrapped   │
├────────────────────────────┼─────────────────────────┼──────────────────────────┤
│ LLM from inside            │ no                      │ llm_query on heap slices │
├────────────────────────────┼─────────────────────────┼──────────────────────────┤
│ Resume - survives          │ transcript + files      │ process is the resume    │
├────────────────────────────┼─────────────────────────┼──────────────────────────┤
│ Loop - turn owner          │ ReAct, execute = Action │ REPL often is the loop   │
└────────────────────────────┴─────────────────────────┴──────────────────────────┘
```
