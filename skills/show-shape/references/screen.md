# Screen

Box-drawing of the thing as a person would see it. Label each region with what it is and the constraint that would otherwise vanish.

```text
┌─ Client ─────────────────────────────────────────────┐
│ ┌─ transcript (fullscreen, redrawable) ────────────┐ │
│ │ > look at this                                   │ │
│ │ > [Image #1]                                     │ │
│ │                                                  │ │
│ │ ┌─ user attachment ────────────────────────────┐ │ │
│ │ │ Kitty placement (Pi)                         │ │ │
│ │ │ reserved blank rows                          │ │ │
│ │ └──────────────────────────────────────────────┘ │ │
│ │                                                  │ │
│ │ assistant reply...                               │ │
│ │ dimmed live area, while caret is at chip         │ │
│ │   ┌─ Image #1 ───────────────────────────────┐   │ │
│ │   │ PNG / Client-side live pixels            │   │ │
│ │   │ Kitty overlay (Grok Build)               │   │ │
│ │   │ never committed to scrollback            │   │ │
│ │   └──────────────────────────────────────────┘   │ │
│ └──────────────────────────────────────────────────┘ │
│                                                      │
│ ┌─ composer ───────────────────────────────────────┐ │
│ │ > look at this [Image #1]                        │ │
│ │ status line                                      │ │
│ └──────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────┘
```

Overlay only exists while the caret is on or right after the chip. Transcript pixels stay in the user block after submit.
