# Impact

Box-drawing of the existing surface with the feature's touch marked. Same frame, changed regions tagged, unchanged regions left as same with no detail.

```text
┌─ surface ──────────────────────────────┐
│ ┌─ list ─────────┐  ┌─ detail ───────┐ │
│ │ same           │  │ CHANGED:       │ │
│ │                │  │ new badge +    │ │
│ │                │  │ action         │ │
│ └────────────────┘  └────────────────┘ │
│ ┌─ toolbar ──────────────────────────┐ │
│ │ same                               │ │
│ └────────────────────────────────────┘ │
└────────────────────────────────────────┘
```

Every changed region names the change. Unchanged regions stay labeled same.
