# cs616-review-checker

A Claude plugin that checks a **CS 616 (Digital Crime and Forensics) Type A — Review / Survey paper** against *every* requirement in the course documents, for **Topic 19 or Topic 34**. Feed Claude the paper's **Overleaf LaTeX source**; get back a compliance report (PASS / WARN / FAIL / MANUAL) with evidence and a fix order.

One plugin, one skill, **one topic per run**. Each topic has its own reference sub-folder; the skill loads only the folder of the chosen topic and never opens the other.

| Topic | Command | Reference folder |
|---|---|---|
| **19** — Version- and State-Robust Forensics of Encrypted Messaging Applications | `/check-t19` | `references/topics/t19/` |
| **34** — Forensic Readiness and Standardisation in Organisations | `/check-t34` | `references/topics/t34/` |

Shared rules (all Type A requirements, report template, Guidelines) are in `references/common/`.

## What is checked
Everything is derived from the three course PDFs (extracted to Markdown in [`source-docs/`](source-docs/)):
*Research Paper Guidelines*, *Research Paper Topic Catalogue*, *Two-Track Research Handbook* (Review track + the topic's Track A entry).

- **Format** — IEEEtran `[conference]` two-column, no layout hacks, no template leftovers, ~5,000–6,000 words (±10 %), abstract 150–250, 4–6 keywords, required sections in order, figures/tables captioned + referenced, acronyms defined.
- **Review method (Guidelines §2.1 + Handbook "Review track")** — bounded RQs, databases, reproducible search string, time window, inclusion/exclusion, **PRISMA flow**, corpus size, taxonomy, **comparison matrix**, **quality appraisal**, gap analysis, scope/bias/limitations, anticipated vs actual outcomes.
- **Topic coverage** — the topic's RQ1–RQ3, search protocol, matrix columns and anchor sources ([topic 19](topic-specs/topic-19.md), [topic 34](topic-specs/topic-34.md)).
- **References** — ≥ 15, majority peer-reviewed and recent, IEEE numbered, all cited ↔ all listed, no blogs/Wikipedia, entry completeness, access dates.
- **Writing/integrity** — third person, quotes, uncited long paragraphs; and a **MANUAL** list of what no tool can verify (Turnitin < 20 %, sources actually read, venue quality).

Full ID-by-ID list: [`shared-references/requirements-common.md`](shared-references/requirements-common.md).

> **Two modes.** `/check-t19` · `/check-t34` audit the paper and say what and where to fix. `/fix-t19` · `/fix-t34` revise a copy of the paper and return the edited files plus a change log. Fix mode never invents references, numbers or findings; it leaves `TODO(student)` markers instead.

## Install
**Claude Code**
```
/plugin marketplace add EngDawood/cs616-review-checker
/plugin install cs616-review-checker@cs616-review-checkers
/check-t19 paper.zip        # or /check-t34 paper.zip
```
**Claude app / claude.ai** — upload [`dist/cs616-review-checker.skill.zip`](dist/cs616-review-checker.skill.zip) as a custom skill, then say which topic (19 or 34) when you attach the paper.

## Use
1. In Overleaf: *Menu → Download → Source* (a `.zip`), or attach `main.tex` + `.bib`.
2. Attach it to Claude and say e.g. `/check-t19 paper.zip` (add `--stage draft` for the Week-9 draft).
3. Read the report, fix, re-run.

Direct CLI (Python 3.8+, stdlib only):
```
python3 engine/check_paper.py paper.zip --topic 19            # or --topic 34
python3 engine/check_paper.py main.tex  --topic 34 --format json --out report.json
```

## Layout
```
engine/check_paper.py        single source of the checker (both topic profiles)
shared-references/           common requirements + report template
topic-specs/                 Handbook entry + checks for topic 19 and 34
source-docs/                 course PDFs extracted to Markdown
skills/ + commands/          generated plugin parts (the repo root is the plugin; installs copy everything)
dist/                        skill zip for claude.ai
templates/                   official IEEE conference template (Overleaf) for students
tools/build.py               rebuild skills/, commands/ + zip after editing engine/ or references
tests/                       python3 -m unittest discover -s tests
```
After editing anything under `engine/`, `shared-references/` or `topic-specs/`, run `python3 tools/build.py` (a test fails if the plugin copies drift).

## Limits (read this)
- Word count is approximate (prose only); confirm with Overleaf's word count and your instructor's exact limit.
- Keyword/heuristic checks (acronyms, coverage, "peer-reviewed" by BibTeX entry type) can be wrong — Claude re-checks each WARN/FAIL by reading the paper.
- Cannot measure similarity, detect AI text, or confirm that cited sources were read and the table is true to them.
- The Handbook is the detailed spec; the Topic Catalogue and the Guidelines differ slightly (e.g. proposal Week 4 vs 8) — confirm with the instructor.

MIT licence.
