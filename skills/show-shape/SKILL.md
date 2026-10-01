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

### Keep the geometry intact

Every diagram goes in a fenced `text` block. Use Unicode box-drawing glyphs and spaces, never tabs. The references teach box logic, not fixed widths. Recalculate the geometry for the current labels instead of pasting longer text into the example's frame.

- Use the user's column limit or a known narrower display width. Otherwise keep every diagram line within 88 display columns. Never rely on terminal wrapping. Stack boxes or split independent paths into separate blocks when needed. Keep the view's meaning, not its example's orientation.
- Choose each box's width from its longest title or body line, including padding. Wrap long labels inside the box before drawing its borders. Pad every body line so both sides and all four corners stay on the same columns, including blank lines. Nested boxes and table dividers must align too.
- Fix connector columns first. Use `┬`, `┴`, `├`, `┤`, and `┼` for joins. Connect each line to its source and arrow tail without gaps. Put each arrow directly at its destination border. Label gate exits beside the connector, without moving it. Keep wide characters, emoji, and combining marks out of diagrams unless their display widths are measured.

### Check before replying

Inspect every diagram after substituting the real labels. Check all rows, not just the top and bottom. If tools and Python 3 are available, pipe the drafted Markdown into `python3 <skill-directory>/scripts/check_diagrams.py` through stdin, then fix every reported error and rerun. Use `--max-width N` only for an explicit different column budget. The checker is optional authoring tooling, not a runtime dependency. Without tools, count columns and perform the same border and connector checks manually. Do not emit a known-broken diagram or include checking logs in the reply.

This step is complete when each picked view is present, no unpicked view is present, every diagram fits its column budget with aligned borders and connected paths, and a later implementer could build from them without rereading the prior prose.
