---
description: Check any paper's LaTeX / IEEE format with no topic (template, references, figures, labels, acronyms, tone)
argument-hint: <path to Overleaf .zip | folder | main.tex> [--stage draft|final]
---

Use the `cs616-review-checker` skill in **generic LaTeX mode** (no topic; do not open `references/topics/`) on: $ARGUMENTS

Run the engine with `--topic generic`, verify every WARN/FAIL by reading the .tex, and report using the template without the judgement table. Make no edits unless the user asks for a change — then switch to fix mode and do exactly what they ask.
