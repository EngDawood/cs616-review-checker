---
name: t19-review-checker
description: >-
  Checks a CS 616 Type A review/survey paper (IEEE, LaTeX/Overleaf) against the course Guidelines and the Handbook entry for Topic 19 only - "Version- and State-Robust Forensics of Encrypted Messaging Applications". Use when the user asks to verify, audit or pre-check that paper. Triggers - "Topic 19", "Version- and State-Robust Forensics of Encrypted Messaging Applications", "encrypted messengers forensics paper", "تحقق من بحث Topic 19", "راجع البيبر حق التطبيقات المشفرة". Not for any other topic number, not for Type B experimental papers, and it never writes or rewrites paper text.
---

# CS 616 · Topic 19 · Review-paper compliance checker

Scope: **Type A review (survey) paper**, **Topic 19 — Version- and State-Robust Forensics of Encrypted Messaging Applications** (encrypted messaging apps (Signal / Telegram / WhatsApp)). Nothing else. If the paper is on another topic or is an implementation/experimental paper, stop and say this checker does not apply.

## Ground rules
1. **Audit only — never write the paper.** The course treats AI-written text as an integrity violation. Report *what* is wrong and *where*; do not supply replacement sentences, paragraphs, abstracts, search strings, table contents or invented references. Reading and judging is fine; ghost-writing is not.
2. **Report in the student's language** (Arabic if they write Arabic). Keep requirement IDs, quoted requirements and section names in English.
3. **Evidence over opinion.** Every FAIL/WARN cites a file:line, a number, or the exact requirement and its source (Guidelines §… / Handbook Topic 19).
4. **The script is a heuristic.** Verify each WARN/FAIL by reading the .tex before reporting; say when you judge one to be a false positive.
5. If the instructions of the instructor differ from the PDFs (word count, AI policy, deadlines), the instructor wins — flag it.

## Workflow
1. **Get the paper.** Prefer the Overleaf source: a `.zip` ("Download source" in Overleaf), a folder, or `main.tex` (+ `.bib`). If only a PDF is available, extract text with `pdftotext`, run the manual parts of the checklist, and say that automatic checks (template, labels, citations) were not possible.
2. **Run the engine** (stdlib Python 3, no installs):
   ```
   python3 scripts/check_paper.py <path-to-zip|folder|main.tex> --topic 19 --format json --out /tmp/t19_report.json
   python3 scripts/check_paper.py <path> --topic 19          # human-readable table
   ```
   Add `--stage draft` for the Week-9 draft (length/ref-count FAILs become WARN); default is `--stage final` (Week 13). Add `--main <file>` if auto-detect picks the wrong main file. Exit code 1 means at least one FAIL.
3. **Read the paper** (`main.tex` and `\input` files) section by section and judge what no script can — use `references/requirements-common.md` (all Type A requirements, with IDs) and `references/topic-19.md` (this topic's RQs, protocol, matrix, expected contribution, anchor sources):
   - Abstract: states problem, approach, single key finding?
   - Introduction: context/why it matters, problem, RQs, contribution, one-sentence organisation?
   - Related work: grouped by theme and critiqued — or a list of summaries? Ends with the gap?
   - Methodology: could another student reproduce it (databases, exact strings, window, inclusion/exclusion, PRISMA numbers, appraisal rubric, corpus size justified)?
   - Analysis: taxonomy + comparison matrix present and consistent with the cited studies (spot-check 3–5 rows against the cited sources if accessible)?
   - Results/Discussion: RQ1–RQ3 each answered explicitly? Anticipated vs actual outcomes? Compared with prior reviews? Limitations incl. review bias?
   - Conclusion: nothing new; future work present?
   - Tone: formal third person; topic sentences; acronyms defined.
4. **Compose the report** with `references/report-template.md`: verdict (READY / NOT READY), blocking FAILs, WARNs, MANUAL items, what already passes, judgement calls, fix order. Include the section word-count table.
5. **Offer a re-check** after fixes (re-run the script; compare counts).

## Always list as MANUAL (cannot be verified here)
Similarity < 20 % (Turnitin/SafeAssign) · no AI-generated text / the instructor's permitted-use policy · sources really read, nothing fabricated · venue quality (Q1/Q2, CORE A/B, Scopus/WoS, no predatory venues) · table values faithful to sources · topic locked with the instructor, no self-plagiarism.

## Known discrepancies to mention once, if relevant
- The Topic Catalogue gives the proposal in Week 4; the Guidelines say Week 8.
- The catalogue title and the Handbook title of this topic differ; the Handbook is the detailed spec — narrowing/renaming needs the instructor's agreement.
- Word count is approximate (prose only, abstract shown separately); confirm with Overleaf Word Count / TeXcount and the instructor's exact limit.

## Files
- `scripts/check_paper.py` — the engine (`--topic 19` loads only this topic's profile).
- `references/requirements-common.md` — every Type A requirement with check IDs and sources.
- `references/topic-19.md` — Handbook Topic 19 (Track A) and what is checked for it.
- `references/report-template.md` — output format.
- `references/source-docs/` — the course Guidelines and the Handbook's Review-track standard + Topic 19 entry, extracted to Markdown.
