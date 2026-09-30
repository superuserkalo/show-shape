# Flow

Box-drawing of order over time, left to right. One box per handoff, arrow between. Label each box with the step and what it hands to the next.

```text
┌──────────┐     ┌──────────┐     ┌──────────┐
│ trigger  │────▶│ derive   │────▶│ render   │
│ event in │     │ rule +   │     │ what the │
│ + payload│     │ inputs   │     │ person   │
│          │     │ used     │     │ sees     │
└──────────┘     └──────────┘     └──────────┘
```

Only steps that change hands. Branches and gates live in ownership, not here.
