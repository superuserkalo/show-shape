# Flow

Box-drawing of order over time, left to right when it fits. One box per handoff, arrow between. Label each box with the step and what it hands to the next.

```text
┌─ trigger ──┐     ┌─ derive ────┐     ┌─ render ────┐
│ event in   ├────▶┤ rule +      ├────▶┤ what the    │
│ + payload  │     │ inputs used │     │ person sees │
└────────────┘     └─────────────┘     └─────────────┘
```

Only steps that change hands. Branches and gates live in ownership, not here. If the handoffs exceed the column budget, stack them top to bottom with downward arrows. Never let the terminal wrap a border.
