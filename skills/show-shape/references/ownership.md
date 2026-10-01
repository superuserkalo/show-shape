# Ownership

Box-drawing flowchart: data in, who owns each piece, the gates that turn a path on or off.

```text
┌─ Client ───────────────────────────────────────┐
│ selected file + metadata                       │
│ owns temporary selection, not stored bytes     │
└───────────────────────┬────────────────────────┘
                        ▼
╭─ Upload API gate ──────────────────────────────╮
│ owns validation + authorization                │
│ File allowed and actor authorized?             │
╰───────────────────────┬────────────────────────╯
                        │
          ┌─────────────┴─────────────┐
          │ yes                       │ no
          ▼                           ▼
┌─ Storage ──────────────┐  ┌─ Rejected ─────────────┐
│ bytes + receipt        │  │ no stored bytes        │
│ API owns access policy │  │ Client shows error     │
└────────────────────────┘  └────────────────────────┘
```

Put the owner and retained data inside each box. Label every gate exit. Keep branch stems on fixed columns and join them with junction glyphs. Split independent paths into separate fenced diagrams rather than squeezing a wide graph into the terminal.
