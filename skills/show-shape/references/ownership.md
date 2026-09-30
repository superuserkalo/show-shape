# Ownership

Box-drawing flowchart: data in, who owns each piece, the gates that turn a path on or off.

```text
                      ┌──────────────┐                           ┌─────────────────────┐
                      │ Ctrl-V paste │                           │ /settings Interface │
                      └───────┬──────┘                           └──────────┬──────────┘
                              │                                ┌────────────┴────────────┐
                              ▼                                ▼                         ▼
                ┌──────────────────────────┐      ┌────────────────────────┐   ┌───────────────────┐
                │ Composer chip [Image #N] │      │ Composer image preview │   │ Transcript images │
                │  bytes stay Client-side  │      └────────────┬───────────┘   └─────────┬─────────┘
                └─────────────┬────────────┘                   │                         │
                              ├────────────────────────────────┘                         │
                              ▼                                                          │
                         ┌────────┐                                        ╭─────────────┴────────────╮
                         │ Submit │                                        │ caret on / after chip    │
                         └────┬───┘                                        │ and Composer preview on? │
                              │                                            ╰─────────────┬────────────╯
              ┌───────────────┴────────────────┐                              ┌──────────┴───────────┐
              ▼                                ▼                              ▼yes                   ▼no
┌──────────────────────────┐       ┌───────────────────────┐      ┌───────────────────────┐   ┌────────────┐
│ Kernel / session / model │       │ Fullscreen user block │      │ Live overlay dim +    │   │ No overlay │
│ unchanged: [Image N] +   │       │ text kept for copy    │      │ rounded frame + title │   └────────────┘
│ PNG bytes                │       └───────────┬───────────┘      └───────────┬───────────┘
└──────────────────────────┘                   │                              │
                                               ▼                              ▼
                                 ╭──────────────────────────╮   ╭──────────────────────────╮
                                 │ Transcript images on and │   │ Kitty on Kitty / Ghostty │
                                 │ fullscreen?              │   │ / WezTerm?               │
                                 ╰─────────────┬────────────╯   ╰─────────────┬────────────╯
                    ┌──────────────────────────┼──────────────────────┐       ├──────────────┐
                    ▼yes + Kitty               ▼yes, no Kitty         ▼off    ▼yes           ▼no
      ┌──────────────────────────┐    ┌───────────────┐  ┌──────────────────┐ ┌──────────────┐ ┌───────────────────┐
      │ Reserved rows + Kitty    │    │ Text fallback │  │ [Image #N] text  │ │ Post-flush   │ │ Metadata box only │
      │ place Pi Image component │    └───────────────┘  │ only             │ │ pixel place  │ └───────────────────┘
      └──────────────────────────┘                       └──────────────────┘ └──────────────┘
```
