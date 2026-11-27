---
name: cs616-review-checker
description: >-
  Checks a CS 616 (Digital Crime and Forensics) Type A review/survey paper written in IEEE LaTeX (Overleaf) against the course Guidelines and the Handbook entry of ONE topic - Topic 19 "Version- and State-Robust Forensics of Encrypted Messaging Applications" or Topic 34 "Forensic Readiness and Standardisation in Organisations". Use when the user asks to verify, audit or pre-check such a paper (e.g. "check my Topic 19 paper", "راجع البيبر حق Topic 34", "هل البحث مطابق للمتطلبات"). Also runs a topic-free IEEE/LaTeX check (/check-latex) and revises the paper on request (fix mode: edits a copy of the .tex to correct what the check found or whatever the user asks). Not for other topics, not for Type B experimental papers.
---

# CS 616 · Type A review-paper compliance checker

Scope: **Type A review (survey) paper**, **Topic 19** or **Topic 34** — one topic per run. For topic checks: anything else (another topic number, an implementation/experimental paper) — say the topic check does not apply and offer `/check-latex`.

## Step 0 — choose the run
**Generic LaTeX check (`/check-latex`, or the user asks to check the LaTeX / IEEE format / compile problems without naming a topic):** do not pick a topic and do not open any `references/topics/` folder. Run `python3 scripts/check_paper.py <path> --topic generic` (the default when `--topic` is omitted), read the .tex only to confirm or dismiss each WARN/FAIL, and report: template and layout, title/abstract/keywords, length, references (style, citation↔list match, numbering, completeness), figures/tables (captions, labels, refs), acronyms, tone, and the LaTeX-hygiene items (duplicate labels, missing images, unbalanced environments). Skip the J-rubric and every topic requirement; say the paper was not checked against any topic. If the user later names Topic 19 or 34, rerun with that topic. The fix-mode rules below apply here too.

**Topic check (everything else):** fix the topic, then load ONLY that topic's folder.
Topic comes from the command used (`/check-t19`, `/check-t34`), the user's words, or the paper's `\title`. If unclear, ask once.

| Topic | Title | Load only |
|---|---|---|
| 19 | Version- and State-Robust Forensics of Encrypted Messaging Applications | `references/topics/t19/` |
| 34 | Forensic Readiness and Standardisation in Organisations | `references/topics/t34/` |

**Never open the other topic's folder** and never apply its requirements, even if the two sound similar. Shared rules live in `references/common/`.

## Ground rules
1. **Do what the user asks with their paper.** Two modes, switchable at any time in the same conversation, with or without a slash command: *Check* (default when asked to verify): report what is wrong and where, with How-to-fix directions. *Fix*: as soon as the user asks for any change (edit, fix, rewrite, expand, shorten, translate, restructure, reformat, add or remove a section, rebuild a table, adjust the bibliography, "عدّل", "أصلح", "أضف", "احذف", "أعد كتابة"), Claude makes it. **The user's instruction decides what changes** — anything in the paper (text, structure, tables, figures, formatting, references, abstract, title), not only what the check flagged; do not refuse, narrow or second-guess a requested edit. Work on a **copy** (never the original), apply the edits the user asked for, then deliver the revised files plus a change log. When the user gives no specific request (plain `/fix-tN`), fix what the report found. If a request is ambiguous, ask one short question first. After edits, re-run the engine and tell the user if a change moves a requirement from pass to fail, but keep the change unless asked to revert. **One limit: never fabricate** — no invented references/DOIs, search results, PRISMA counts, matrix cells, findings or quotes. Where real research or data is needed, insert a clearly marked `% TODO(student): …` placeholder and tell the user what to supply.
2. **Report in the student's language** (Arabic if they write Arabic). Keep requirement IDs, quoted requirements and section names in English.
3. **Evidence over opinion.** Every FAIL/WARN cites a file:line, a number, or the exact requirement and its source (Guidelines §… / Handbook Topic N).
4. **The script is a heuristic.** Verify each WARN/FAIL by reading the .tex before reporting; say when you judge one a false positive.
5. If the instructor's instructions differ from the PDFs (word count, AI policy, deadlines), the instructor wins — flag it.

## Workflow
1. **Get the paper.** Prefer the Overleaf source: a `.zip` ("Download source"), a folder, or `main.tex` (+ `.bib`). If only a PDF exists, extract with `pdftotext`, do the manual/judgement parts, and say automatic checks (template, labels, citations) were not possible.
2. **Run the engine** (stdlib Python 3, no installs):
   ```
   python3 scripts/check_paper.py <zip|folder|main.tex> --topic <19|34> --format json --out /tmp/report.json
   python3 scripts/check_paper.py <path> --topic <19|34>        # readable table
   ```
   `--stage draft` for the Week-9 draft (length/ref-count FAILs become WARN); default `final` (Week 13). `--main <file>` if auto-detect picks the wrong main file. Exit code 1 = at least one FAIL.
3. **Read the paper** (`main.tex` + `\input` files) section by section and judge what no script can. Apply `references/common/judgement-rubric.md` (items J1–J18) **and** the topic's own `references/topics/tN/judgement-N.md`; give each item a verdict MET / PARTLY / NOT MET / CAN'T TELL with section + file:line evidence and what is missing (never replacement text). Requirements and IDs: `references/common/requirements-common.md`, `references/topics/tN/topic-N.md`. Prompts to keep in mind:
   - Abstract: problem, approach, single key finding?
   - Introduction: context/why it matters, problem, RQs, contribution, one-sentence organisation?
   - Related work: grouped by theme and critiqued — or a list of summaries? Ends with the gap?
   - Methodology: reproducible (databases, exact strings, window, inclusion/exclusion, PRISMA numbers, appraisal rubric, corpus size justified)?
   - Analysis: taxonomy + comparison matrix with the topic's columns, consistent with the cited studies (spot-check 3–5 rows if sources are accessible)?
   - Results/Discussion: RQ1–RQ3 each answered explicitly? Anticipated vs actual outcomes? Compared with prior reviews? Limitations incl. review bias?
   - Conclusion: nothing new; future work?
   - Tone: formal third person; topic sentences; acronyms defined.
4. **Compose the report** with `references/common/report-template.md`; give every FAIL/WARN/NOT MET/PARTLY a **How to fix** direction from `references/common/revision-guidance.md` (directions only, never replacement text). Include: verdict (READY / NOT READY — rule in the rubric), blocking FAILs, WARNs, the judgement table (J-items + topic items), MANUAL items, what passes, revision plan, section word-count table.
5. **Offer** a revision (fix mode) and a re-check. If the student asks "how do I fix X?" or for a revision plan, answer from `references/common/revision-guidance.md`.
6. **Fix mode** (whenever the user asks for a change): copy the source to a working folder; do the user's requested edits first, then (if they asked for a general fix) blocking FAILs and the order in `revision-guidance.md`; keep the IEEE template intact; compile-check labels/refs; re-run the engine on the revised copy and show before/after counts; deliver the revised `.tex`/`.bib` (or zip) and `CHANGES.md` listing every edit (ID, location, what changed) and every `TODO(student)` left. Do not claim the revised paper is ready until the MANUAL items are done.

## Always list as MANUAL
Similarity < 20 % (Turnitin/SafeAssign) · sources really read, nothing fabricated · venue quality (Q1/Q2, CORE A/B, Scopus/WoS, no predatory venues) · table values faithful to sources · topic locked with the instructor, no self-plagiarism.

## Mention once, if relevant
- Topic Catalogue: proposal Week 4; Guidelines: Week 8.
- Catalogue and Handbook titles of the topic differ; the Handbook is the detailed spec; renaming/narrowing needs the instructor's agreement.
- Word count is approximate (prose only); confirm with Overleaf Word Count and the instructor's exact limit.
- An unmodified IEEE sample template is reported as F3 (leftover template text) — expected until the student replaces it.

## Files
- `scripts/check_paper.py` — the engine (`--topic` selects the profile).
- `references/common/` — `requirements-common.md` (every Type A requirement with check IDs + sources), `judgement-rubric.md` (verdict criteria for everything that needs reading), `revision-guidance.md` (how to tell the student what to change, without writing it), `report-template.md`, `guidelines.md` (course Guidelines as Markdown).
- `references/topics/t19/` and `references/topics/t34/` — each: `topic-N.md` (Handbook Track A + what is checked), `judgement-N.md` (topic-specific reading checks) and `handbook-excerpt.md` (Review-track standard + that topic's entry).
