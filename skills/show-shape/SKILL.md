---
name: show-shape
description: Draw the shape of a design, architecture, or feature already under discussion. Use when the user asks for the shape, layout, or diagram of what is on the table. Do not use to plan or pick the design itself.
---

# Show shape

Shape is the spatial and ownership layout of a design already on the table. Each run draws a different set: start from none and add only the views that answer the open question.

## Route

Match the open question to the views. The When column is the whole decision.

| View | When | File |
|---|---|---|
| screen | the answer needs what a person sees | `references/screen.md` |
| states | the answer needs how one surface looks across states | `references/states.md` |
| flow | the answer needs order over time | `references/flow.md` |
| modules | the answer needs what each code piece owns | `references/modules.md` |
| ownership | the answer needs who owns data or what gates a path | `references/ownership.md` |
| impact | the answer needs what an existing surface keeps vs changes | `references/impact.md` |
| split | a comparison axis stays open after the other picked views | `references/split.md` |

A feature that touches UI often takes screen plus ownership. A backend-only question often takes modules plus ownership. Take states only when one surface visibly differs by state. Take impact only when existing surfaces keep parts unchanged. Take split only while its axis is still undecided.

This step is complete when every picked view answers the open question and every dropped view fails its When.

## Draw

Read the File for each picked view. Keep its box logic and redraw it with the current design's names. The example's nouns never leave its file. Emit the picked views in the order that answers the question, most explanatory first. Each view becomes a `### <view>` heading. Prose under the view is at most one line. The reply is only those headed views.

This step is complete when each picked view is present, no unpicked view is present, and a later implementer could build from them without rereading the prior prose.
