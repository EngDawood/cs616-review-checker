# cs616-t19-review-checker

Claude plugins that check a **CS 616 (Digital Crime and Forensics) Type A — Review / Survey paper** against *every* requirement in the course documents, for **one topic each**. Feed Claude the paper's **Overleaf LaTeX source**; get back a compliance report (PASS / WARN / FAIL / MANUAL) with evidence and a fix order.

| Plugin | Topic | Invoke |
|---|---|---|
| `cs616-t19-review-checker` | **Topic 19** — Version- and State-Robust Forensics of Encrypted Messaging Applications | `/check-t19` or ask about Topic 19 |
| `cs616-t34-review-checker` | **Topic 34** — Forensic Readiness and Standardisation in Organisations | `/check-t34` or ask about Topic 34 |

The two plugins are fully separate: install one, the other, or both. Each loads only its own topic's requirements.

## What is checked
Everything is derived from the three course PDFs (extracted to Markdown in [`source-docs/`](source-docs/)):
*Research Paper Guidelines*, *Research Paper Topic Catalogue*, *Two-Track Research Handbook* (Review track + the topic's Track A entry).

- **Format** — IEEEtran `[conference]` two-column, no layout hacks, no template leftovers, ~5,000–6,000 words (±10 %), abstract 150–250, 4–6 keywords, required sections in order, figures/tables captioned + referenced, acronyms defined.
- **Review method (Guidelines §2.1 + Handbook "Review track")** — bounded RQs, databases, reproducible search string, time window, inclusion/exclusion, **PRISMA flow**, corpus size, taxonomy, **comparison matrix**, **quality appraisal**, gap analysis, scope/bias/limitations, anticipated vs actual outcomes.
- **Topic coverage** — the topic's RQ1–RQ3, search protocol, matrix columns and anchor sources ([topic 19](topic-specs/topic-19.md), [topic 34](topic-specs/topic-34.md)).
- **References** — ≥ 15, majority peer-reviewed and recent, IEEE numbered, all cited ↔ all listed, no blogs/Wikipedia, entry completeness, access dates.
- **Writing/integrity** — third person, quotes, uncited long paragraphs; and a **MANUAL** list of what no tool can verify (Turnitin < 20 %, no AI-written text, sources actually read, venue quality).

Full ID-by-ID list: [`shared-references/requirements-common.md`](shared-references/requirements-common.md).

> **Audit only.** The course forbids AI-generated text, so the checker points to *what* and *where* to fix — it never rewrites or drafts paper text.

## Install
**Claude Code**
```
/plugin marketplace add EngDawood/cs616-t19-review-checker
/plugin install cs616-t19-review-checker@cs616-review-checkers      # Topic 19
/plugin install cs616-t34-review-checker@cs616-review-checkers      # Topic 34
```
**Claude app / claude.ai** — upload the skill zip from [`dist/`](dist/) as a custom skill (`t19-review-checker.skill.zip` or `t34-review-checker.skill.zip`).

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
plugins/                     built, self-contained plugins (one per topic)
dist/                        skill zips for claude.ai
tools/build.py               rebuild plugins + zips after editing engine/ or references
tests/                       python3 -m unittest discover -s tests
```
After editing anything under `engine/`, `shared-references/` or `topic-specs/`, run `python3 tools/build.py` (a test fails if the plugin copies drift).

## Limits (read this)
- Word count is approximate (prose only); confirm with Overleaf's word count and your instructor's exact limit.
- Keyword/heuristic checks (acronyms, coverage, "peer-reviewed" by BibTeX entry type) can be wrong — Claude re-checks each WARN/FAIL by reading the paper.
- Cannot measure similarity, detect AI text, or confirm that cited sources were read and the table is true to them.
- The Handbook is the detailed spec; the Topic Catalogue and the Guidelines differ slightly (e.g. proposal Week 4 vs 8) — confirm with the instructor.

MIT licence.
