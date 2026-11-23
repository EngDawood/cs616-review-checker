#!/usr/bin/env python3
"""Build the single plugin `cs616-review-checker` (one skill, topic sub-folders under references/).
Run from the repo root:  python3 tools/build.py
"""
import json, os, re, shutil, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSION = "1.1.0"
NAME = "cs616-review-checker"
TOPICS = {
  "19": dict(title="Version- and State-Robust Forensics of Encrypted Messaging Applications", cmd="check-t19"),
  "34": dict(title="Forensic Readiness and Standardisation in Organisations", cmd="check-t34"),
}

SKILL = '''---
name: cs616-review-checker
description: >-
  Checks a CS 616 (Digital Crime and Forensics) Type A review/survey paper written in IEEE LaTeX (Overleaf) against the course Guidelines and the Handbook entry of ONE topic - Topic 19 "Version- and State-Robust Forensics of Encrypted Messaging Applications" or Topic 34 "Forensic Readiness and Standardisation in Organisations". Use when the user asks to verify, audit or pre-check such a paper (e.g. "check my Topic 19 paper", "راجع البيبر حق Topic 34", "هل البحث مطابق للمتطلبات"). Also revises the paper on request (fix mode: edits a copy of the .tex to correct what the check found). Not for other topics, not for Type B experimental papers.
---

# CS 616 · Type A review-paper compliance checker

Scope: **Type A review (survey) paper**, **Topic 19** or **Topic 34** — one topic per run. Anything else (another topic number, an implementation/experimental paper): stop and say this checker does not apply.

## Step 0 — fix the topic, then load ONLY that topic's folder
Topic comes from the command used (`/check-t19`, `/check-t34`), the user's words, or the paper's `\\title`. If unclear, ask once.

| Topic | Title | Load only |
|---|---|---|
| 19 | Version- and State-Robust Forensics of Encrypted Messaging Applications | `references/topics/t19/` |
| 34 | Forensic Readiness and Standardisation in Organisations | `references/topics/t34/` |

**Never open the other topic's folder** and never apply its requirements, even if the two sound similar. Shared rules live in `references/common/`.

## Ground rules
1. **Two modes.** *Check* (default): report what is wrong and where, with How-to-fix directions. *Fix* (when the student asks to edit/fix/revise/complete — `/fix-t19`, `/fix-t34`, "عدّل", "أصلح"): edit a **copy** of the paper (never the original) to correct what the report found, then deliver the revised files plus a change log. Fix mode may repair format, structure, labels/citations, acronyms, tone, and may rewrite or complete weak/missing passages from material the student gave or the paper already contains. **Never fabricate**: no invented references/DOIs, search results, PRISMA counts, matrix cells, findings or quotes. Where real research or data is needed, insert a clearly marked `% TODO(student): …` placeholder and tell the student what to supply.
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
3. **Read the paper** (`main.tex` + `\\input` files) section by section and judge what no script can. Apply `references/common/judgement-rubric.md` (items J1–J18) **and** the topic's own `references/topics/tN/judgement-N.md`; give each item a verdict MET / PARTLY / NOT MET / CAN'T TELL with section + file:line evidence and what is missing (never replacement text). Requirements and IDs: `references/common/requirements-common.md`, `references/topics/tN/topic-N.md`. Prompts to keep in mind:
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
6. **Fix mode** (only when asked): copy the source to a working folder; fix blocking FAILs first, then the order in `revision-guidance.md`; keep the IEEE template intact; compile-check labels/refs; re-run the engine on the revised copy and show before/after counts; deliver the revised `.tex`/`.bib` (or zip) and `CHANGES.md` listing every edit (ID, location, what changed) and every `TODO(student)` left. Do not claim the revised paper is ready until the MANUAL items are done.

## Always list as MANUAL
Similarity < 20 % (Turnitin/SafeAssign) · no AI-generated text / the instructor's permitted-use policy · sources really read, nothing fabricated · venue quality (Q1/Q2, CORE A/B, Scopus/WoS, no predatory venues) · table values faithful to sources · topic locked with the instructor, no self-plagiarism.

## Mention once, if relevant
- Topic Catalogue: proposal Week 4; Guidelines: Week 8.
- Catalogue and Handbook titles of the topic differ; the Handbook is the detailed spec; renaming/narrowing needs the instructor's agreement.
- Word count is approximate (prose only); confirm with Overleaf Word Count and the instructor's exact limit.
- An unmodified IEEE sample template is reported as F3 (leftover template text) — expected until the student replaces it.

## Files
- `scripts/check_paper.py` — the engine (`--topic` selects the profile).
- `references/common/` — `requirements-common.md` (every Type A requirement with check IDs + sources), `judgement-rubric.md` (verdict criteria for everything that needs reading), `revision-guidance.md` (how to tell the student what to change, without writing it), `report-template.md`, `guidelines.md` (course Guidelines as Markdown).
- `references/topics/t19/` and `references/topics/t34/` — each: `topic-N.md` (Handbook Track A + what is checked), `judgement-N.md` (topic-specific reading checks) and `handbook-excerpt.md` (Review-track standard + that topic's entry).
'''

CMD = '''---
description: Check a Topic {n} review paper ({title}) against the CS 616 requirements
argument-hint: <path to Overleaf .zip | folder | main.tex> [--stage draft|final]
---

Use the `cs616-review-checker` skill with **topic {n}** (load only `references/topics/t{n}/`) on: $ARGUMENTS

Run the engine with `--topic {n}`, read the paper section by section, verify every WARN/FAIL, and return the compliance report from the template. Check mode only (no edits); if the student wants fixes applied, point to /fix-t{n}. If no path is given, ask for the Overleaf source (.zip) or `main.tex` + `.bib`.
'''

FIXCMD = '''---
description: Revise a Topic {n} review paper ({title}) - fix what the CS 616 check found
argument-hint: <path to Overleaf .zip | folder | main.tex> [--stage draft|final]
---

Use the `cs616-review-checker` skill in **fix mode** with **topic {n}** (load only `references/topics/t{n}/`) on: $ARGUMENTS
Run the check first, then edit a copy of the paper, never fabricate references/data (use TODO(student) placeholders), re-run the engine, and deliver the revised files with CHANGES.md.
'''

def w(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(text)

def build():
    pdir = ROOT  # the repo root IS the plugin, so installs copy everything
    for old in ("plugins", "skills", "commands"):
        shutil.rmtree(os.path.join(ROOT, old), ignore_errors=True)
    sk = os.path.join(pdir, "skills", NAME)
    w(os.path.join(sk, "SKILL.md"), SKILL.replace("\\\\", "\\"))
    os.makedirs(os.path.join(sk, "scripts"))
    shutil.copy(os.path.join(ROOT, "engine", "check_paper.py"), os.path.join(sk, "scripts", "check_paper.py"))
    common = os.path.join(sk, "references", "common")
    os.makedirs(common)
    for f in ("requirements-common.md", "report-template.md", "judgement-rubric.md", "revision-guidance.md"):
        shutil.copy(os.path.join(ROOT, "shared-references", f), common)
    shutil.copy(os.path.join(ROOT, "source-docs", "01-research-paper-guidelines.md"), os.path.join(common, "guidelines.md"))
    hb = open(os.path.join(ROOT, "source-docs", "03-two-track-handbook-full.md"), encoding="utf-8").read()
    head = hb[:re.search(r"\n#{2,3} Topic 1 ", hb).start()]
    for n, t in TOPICS.items():
        d = os.path.join(sk, "references", "topics", "t" + n); os.makedirs(d)
        shutil.copy(os.path.join(ROOT, "topic-specs", "topic-%s.md" % n), d)
        shutil.copy(os.path.join(ROOT, "topic-specs", "judgement-%s.md" % n), d)
        m = re.search(r"\n#{2,3} Topic %s .*?(?=\n#{2,3} Topic \d+ |\Z)" % n, hb, re.S)
        w(os.path.join(d, "handbook-excerpt.md"), (head + "\n\n" + m.group(0)).replace("all 28 topics", "excerpt: Review-track standard + Topic %s only" % n))
        w(os.path.join(pdir, "commands", t["cmd"] + ".md"), CMD.format(n=n, title=t["title"]))
        w(os.path.join(pdir, "commands", "fix-t%s.md" % n), FIXCMD.format(n=n, title=t["title"]))
    w(os.path.join(pdir, ".claude-plugin", "plugin.json"), json.dumps({
        "name": NAME, "version": VERSION,
        "description": "CS 616 Type A review-paper checker for Topic 19 (encrypted messaging apps forensics) and Topic 34 (forensic readiness); one topic per run",
        "author": {"name": "EngDawood"}, "license": "MIT",
        "keywords": ["cs616", "review-paper", "ieee", "latex", "overleaf", "digital-forensics"]}, indent=2) + "\n")
    w(os.path.join(ROOT, ".claude-plugin", "marketplace.json"), json.dumps({
        "name": "cs616-review-checkers", "owner": {"name": "EngDawood"},
        "metadata": {"description": "CS 616 Digital Crime and Forensics - Type A review-paper checker"},
        "plugins": [{"name": NAME, "source": "./", "version": VERSION,
                     "description": "Topic 19 and Topic 34 review-paper checker (one topic per run)"}]}, indent=2) + "\n")
    shutil.rmtree(os.path.join(ROOT, "dist"), ignore_errors=True); os.makedirs(os.path.join(ROOT, "dist"))
    with zipfile.ZipFile(os.path.join(ROOT, "dist", NAME + ".skill.zip"), "w", zipfile.ZIP_DEFLATED) as z:
        for dp, dn, fn in os.walk(sk):
            for f in fn:
                full = os.path.join(dp, f); z.write(full, os.path.join(NAME, os.path.relpath(full, sk)))
    print("built", NAME, VERSION)

if __name__ == "__main__":
    build()
