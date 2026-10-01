# Task-board example

Actual output from a `show-shape` run in Radian. The README screenshot shows this response rendered by Radian’s native terminal harness.

## Request

Use show-shape to draw our agreed task board: Workspaces sidebar, To do / In progress / Done columns, New task button, cards with title and assignee. Show screen and empty, loading, and ready states. Keep the diagrams compact and aligned. Do not redesign or edit files.

## Response

### screen

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│Workspaces    │Task board                                        [ New task ]│
├──────────────┼──────────────────────────────────────────────────────────────┤
│[Workspace]   │       To do        │    In progress     │        Done        │
│              │ ┌────────────────┐ │ ┌────────────────┐ │ ┌────────────────┐ │
│              │ │[Title]         │ │ │[Title]         │ │ │[Title]         │ │
│              │ │Assignee: [Name]│ │ │Assignee: [Name]│ │ │Assignee: [Name]│ │
│              │ └────────────────┘ │ └────────────────┘ │ └────────────────┘ │
└──────────────┴────────────────────┴────────────────────┴────────────────────┘
```

### states

Board contents change. Workspaces, To do / In progress / Done columns, and New task remain visible.

```text
┌─ empty ─────────────────┐  ┌─ loading ───────────────┐  ┌─ ready ─────────────────┐
│No cards in any column   │  │Loading cards…           │  │Cards in their columns   │
│                         │  │                         │  │┌──────────────────┐     │
│                         │  │                         │  ││ [Title]          │     │
│                         │  │                         │  ││ Assignee: [Name] │     │
│                         │  │                         │  │└──────────────────┘     │
└─────────────────────────┘  └─────────────────────────┘  └─────────────────────────┘
```
