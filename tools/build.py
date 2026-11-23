#!/usr/bin/env python3
"""Build the two separate plugins (one per topic) from the shared engine + references.
Run from the repo root:  python3 tools/build.py
"""
import json, os, re, shutil, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = {
  "19": dict(slug="t19", title="Version- and State-Robust Forensics of Encrypted Messaging Applications",
             short="encrypted messaging apps (Signal / Telegram / WhatsApp)",
             ar="الأدلة الجنائية لتطبيقات المراسلة المشفّرة", cmd="check-t19",
             triggers='"Topic 19", "Version- and State-Robust Forensics of Encrypted Messaging Applications", "encrypted messengers forensics paper", "تحقق من بحث Topic 19", "راجع البيبر حق التطبيقات المشفرة"',
             excerpt="Handbook pp. 16–17"),
  "34": dict(slug="t34", title="Forensic Readiness and Standardisation in Organisations",
             short="digital-forensic readiness frameworks and maturity models",
             ar="الجاهزية الجنائية الرقمية والتوحيد القياسي في المؤسسات", cmd="check-t34",
             triggers='"Topic 34", "Forensic Readiness and Standardisation in Organisations", "forensic readiness maturity model paper", "تحقق من بحث Topic 34", "راجع البيبر حق الجاهزية الجنائية"',
             excerpt="Handbook pp. 29–30"),
}
VERSION = "1.0.0"

SKILL = '''---
name: {slug}-review-checker
description: >-
  Checks a CS 616 Type A review/survey paper (IEEE, LaTeX/Overleaf) against the course Guidelines and the Handbook entry for Topic {n} only - "{title}". Use when the user asks to verify, audit or pre-check that paper. Triggers - {triggers}. Not for any other topic number, not for Type B experimental papers, and it never writes or rewrites paper text.
---

# CS 616 · Topic {n} · Review-paper compliance checker

Scope: **Type A review (survey) paper**, **Topic {n} — {title}** ({short}). Nothing else. If the paper is on another topic or is an implementation/experimental paper, stop and say this checker does not apply.

## Ground rules
1. **Audit only — never write the paper.** The course treats AI-written text as an integrity violation. Report *what* is wrong and *where*; do not supply replacement sentences, paragraphs, abstracts, search strings, table contents or invented references. Reading and judging is fine; ghost-writing is not.
2. **Report in the student's language** (Arabic if they write Arabic). Keep requirement IDs, quoted requirements and section names in English.
3. **Evidence over opinion.** Every FAIL/WARN cites a file:line, a number, or the exact requirement and its source (Guidelines §… / Handbook Topic {n}).
4. **The script is a heuristic.** Verify each WARN/FAIL by reading the .tex before reporting; say when you judge one to be a false positive.
5. If the instructions of the instructor differ from the PDFs (word count, AI policy, deadlines), the instructor wins — flag it.

## Workflow
1. **Get the paper.** Prefer the Overleaf source: a `.zip` ("Download source" in Overleaf), a folder, or `main.tex` (+ `.bib`). If only a PDF is available, extract text with `pdftotext`, run the manual parts of the checklist, and say that automatic checks (template, labels, citations) were not possible.
2. **Run the engine** (stdlib Python 3, no installs):
   ```
   python3 scripts/check_paper.py <path-to-zip|folder|main.tex> --topic {n} --format json --out /tmp/t{n}_report.json
   python3 scripts/check_paper.py <path> --topic {n}          # human-readable table
   ```
   Add `--stage draft` for the Week-9 draft (length/ref-count FAILs become WARN); default is `--stage final` (Week 13). Add `--main <file>` if auto-detect picks the wrong main file. Exit code 1 means at least one FAIL.
3. **Read the paper** (`main.tex` and `\\input` files) section by section and judge what no script can — use `references/requirements-common.md` (all Type A requirements, with IDs) and `references/topic-{n}.md` (this topic's RQs, protocol, matrix, expected contribution, anchor sources):
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
- `scripts/check_paper.py` — the engine (`--topic {n}` loads only this topic's profile).
- `references/requirements-common.md` — every Type A requirement with check IDs and sources.
- `references/topic-{n}.md` — Handbook Topic {n} (Track A) and what is checked for it.
- `references/report-template.md` — output format.
- `references/source-docs/` — the course Guidelines and the Handbook's Review-track standard + Topic {n} entry, extracted to Markdown.
'''

COMMAND = '''---
description: Check a Topic {n} review paper ({title}) against the CS 616 requirements
argument-hint: <path to Overleaf .zip | folder | main.tex> [--stage draft|final]
---

Use the `{slug}-review-checker` skill on: $ARGUMENTS

Run the engine with `--topic {n}`, read the paper section by section, verify every WARN/FAIL, and return the compliance report from the template. Audit only — do not rewrite any of the paper's text. If no path is given, ask the student to attach the Overleaf source (.zip) or `main.tex` + `.bib`.
'''

def w(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(text)

def build():
    market = {"name": "cs616-review-checkers", "owner": {"name": "EngDawood"},
              "metadata": {"description": "CS 616 Digital Crime and Forensics - Type A review-paper checkers, one plugin per topic"},
              "plugins": []}
    for n, t in T.items():
        pdir = os.path.join(ROOT, "plugins", "cs616-%s-review-checker" % t["slug"])
        if os.path.isdir(pdir): shutil.rmtree(pdir)
        sk = os.path.join(pdir, "skills", "%s-review-checker" % t["slug"])
        fmt = dict(n=n, **t)
        w(os.path.join(sk, "SKILL.md"), SKILL.format(**fmt).replace("\\\\input", "\\input"))
        w(os.path.join(pdir, "commands", t["cmd"] + ".md"), COMMAND.format(**fmt))
        os.makedirs(os.path.join(sk, "scripts"))
        shutil.copy(os.path.join(ROOT, "engine", "check_paper.py"), os.path.join(sk, "scripts", "check_paper.py"))
        ref = os.path.join(sk, "references"); os.makedirs(ref)
        for f in ("requirements-common.md", "report-template.md"):
            shutil.copy(os.path.join(ROOT, "shared-references", f), ref)
        shutil.copy(os.path.join(ROOT, "topic-specs", "topic-%s.md" % n), ref)
        sd = os.path.join(ref, "source-docs"); os.makedirs(sd)
        shutil.copy(os.path.join(ROOT, "source-docs", "01-research-paper-guidelines.md"), sd)
        hb = open(os.path.join(ROOT, "source-docs", "03-two-track-handbook-full.md"), encoding="utf-8").read()
        head = hb[:hb.index("\n## Topic 1 ")]
        m = re.search(r"\n## Topic %s .*?(?=\n## Topic \d+ |\Z)" % n, hb, re.S)
        w(os.path.join(sd, "handbook-review-track-and-topic-%s.md" % n), (head + "\n\n" + m.group(0)).replace("(all topics)", "(excerpt: Review track standard + Topic %s)" % n))
        w(os.path.join(pdir, ".claude-plugin", "plugin.json"), json.dumps({
            "name": "cs616-%s-review-checker" % t["slug"], "version": VERSION,
            "description": "CS 616 Type A review-paper checker - Topic %s only: %s" % (n, t["title"]),
            "author": {"name": "EngDawood"}, "license": "MIT", "keywords": ["cs616", "review-paper", "ieee", "latex", "overleaf", "digital-forensics"]},
            indent=2) + "\n")
        market["plugins"].append({"name": "cs616-%s-review-checker" % t["slug"], "source": "./plugins/cs616-%s-review-checker" % t["slug"],
                                  "description": "Topic %s only - %s" % (n, t["title"]), "version": VERSION})
        # claude.ai-uploadable skill zip
        os.makedirs(os.path.join(ROOT, "dist"), exist_ok=True)
        zp = os.path.join(ROOT, "dist", "%s-review-checker.skill.zip" % t["slug"])
        with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
            for dp, dn, fn in os.walk(sk):
                for f in fn:
                    full = os.path.join(dp, f)
                    z.write(full, os.path.join("%s-review-checker" % t["slug"], os.path.relpath(full, sk)))
    w(os.path.join(ROOT, ".claude-plugin", "marketplace.json"), json.dumps(market, indent=2) + "\n")
    print("built:", [p["name"] for p in market["plugins"]])

if __name__ == "__main__":
    build()
