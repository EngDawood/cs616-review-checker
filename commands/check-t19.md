---
description: Check a Topic 19 review paper (Version- and State-Robust Forensics of Encrypted Messaging Applications) against the CS 616 requirements
argument-hint: <path to Overleaf .zip | folder | main.tex> [--stage draft|final]
---

Use the `cs616-review-checker` skill with **topic 19** (load only `references/topics/t19/`) on: $ARGUMENTS

Run the engine with `--topic 19`, read the paper section by section, verify every WARN/FAIL, and return the compliance report from the template. Report only; make no edits unless the user asks for a change — then switch to fix mode (same as /fix-t19) and do exactly what they ask. If no path is given, ask for the Overleaf source (.zip) or `main.tex` + `.bib`.
