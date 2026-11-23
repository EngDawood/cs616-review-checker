---
description: Check a Topic 34 review paper (Forensic Readiness and Standardisation in Organisations) against the CS 616 requirements
argument-hint: <path to Overleaf .zip | folder | main.tex> [--stage draft|final]
---

Use the `cs616-review-checker` skill with **topic 34** (load only `references/topics/t34/`) on: $ARGUMENTS

Run the engine with `--topic 34`, read the paper section by section, verify every WARN/FAIL, and return the compliance report from the template. Report only; make no edits unless the user asks for a change — then switch to fix mode (same as /fix-t34) and do exactly what they ask. If no path is given, ask for the Overleaf source (.zip) or `main.tex` + `.bib`.
