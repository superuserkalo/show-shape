# States

Side-by-side boxes of one surface, one per state that looks different. Same outer frame, different inner contents. Label each box with the state and what appears or disappears.

```text
┌─ empty ───────┐  ┌─ loading ─────┐  ┌─ done ────────┐
│ hint text     │  │ skeleton rows │  │ rows + count  │
│ + CTA         │  │ + spinner     │  │ CTA gone      │
└───────────────┘  └───────────────┘  └───────────────┘
```

Only states that look different get a box. Identical-looking states merge into one. Stack the same-width frames if they would exceed the column budget.
