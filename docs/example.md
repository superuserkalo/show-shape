# Task-board example

Actual output from a non-interactive Claude Code run using `show-shape`.

## Request

Use show-shape to draw our agreed task board and its empty, loading, and ready states. The screen has a Workspaces sidebar, To do / In progress / Done columns, and a New task button. Cards show a title and assignee. Keep diagrams compact, use one card per column, keep box edges aligned, and do not truncate labels. Show this existing design, not a new one.

The agent was instructed to read `skills/show-shape/SKILL.md` and its screen and states references, make no file edits, and return only the skill’s headed views.

## Response

### screen
```text
┌────────────────────────────────────────────────────────────────┐
│ Task board                                        [ New task ] │
│                                                                │
│ ┌ Workspaces ┐ ┌ To do ──────┐ ┌ In progress ┐ ┌ Done ───────┐ │
│ │ workspace  │ │ ┌─────────┐ │ │ ┌─────────┐ │ │ ┌─────────┐ │ │
│ │            │ │ │title    │ │ │ │title    │ │ │ │title    │ │ │
│ │            │ │ │assignee │ │ │ │assignee │ │ │ │assignee │ │ │
│ │            │ │ └─────────┘ │ │ └─────────┘ │ │ └─────────┘ │ │
│ └────────────┘ └─────────────┘ └─────────────┘ └─────────────┘ │
└────────────────────────────────────────────────────────────────┘
```
The sidebar, the three columns and the New task button stay in the same place in every state.

### states
```text
┌─ empty ───────┐  ┌─ loading ─────┐  ┌─ ready ───────┐
│3 empty columns│  │skeleton cards │  │title+assignee │
│New task CTA   │  │per column     │  │cards/column   │
└───────────────┘  └───────────────┘  └───────────────┘
```
Only the inside of each column changes. The sidebar and the New task button stay the same.
