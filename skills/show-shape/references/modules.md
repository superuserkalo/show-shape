# Modules

Box-drawing of the modules as they sit. Label each box with what it owns and the constraint that would otherwise vanish.

```text
┌─ Kernel ────────┐  ┌─ Client ──────────┐
│ session / model │  │ tokens, overlay   │
│ unchanged       │  │ owns presentation │
└─────────────────┘  └───────────────────┘
```
