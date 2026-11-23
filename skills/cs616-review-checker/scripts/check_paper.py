#!/usr/bin/env python3
"""
check_paper.py - deterministic pre-checks for a CS 616 *Type A (review/survey)* paper.
Use --topic 19 (Encrypted Messaging Apps forensics) or --topic 34 (Forensic Readiness). One topic per run.

Input : an Overleaf export (folder or .zip) or a single .tex file (IEEEtran, LaTeX).
Output: a checklist of findings (PASS / WARN / FAIL / MANUAL / INFO) as Markdown or JSON.

This script only *measures and detects*. It never rewrites the paper. Semantic judgement
(is the gap analysis convincing? is the abstract complete?) is left to the reviewer
(Claude / the instructor) - those items are emitted as MANUAL or "verify" hints.

Stdlib only. Python 3.8+.
"""
import argparse, datetime, json, os, re, sys, tempfile, zipfile
from collections import OrderedDict


# --------------------------------------------------------------------- topic profiles
# Everything topic-specific lives here, so each topic is checked against ITS OWN handbook entry only.
PROFILES = {
  "19": dict(
    name="Topic 19 - Version- and State-Robust Forensics of Encrypted Messaging Applications",
    h="Handbook Topic 19",
    title_rx=(r"forensic", r"messag|messenger|signal|telegram|whatsapp"),
    title_hint="Title should name forensics + encrypted/secure messaging apps",
    rq_text="RQ1-RQ3 of Topic 19 (artefacts/storage locations; recoverability across versions, BFU/AFU, deletion, backup/update; legal routes + methodological gaps) are stated and answered",
    dbs={"IEEE Xplore": r"ieee xplore", "ACM Digital Library": r"acm (digital library|dl)", "ScienceDirect": r"sciencedirect", "Scopus": r"scopus", "Google Scholar": r"google scholar"},
    db_need=5, db_text="IEEE Xplore, ACM DL, ScienceDirect, Scopus, Google Scholar",
    string_terms=["forensic", "signal", "telegram", "whatsapp", "instant messag", "secure messag", "android", "ios", "artefact", "artifact"], string_need=6,
    string_text="forensic* AND (Signal OR Telegram OR WhatsApp OR instant/secure messag*) AND (Android OR iOS OR artefact*)",
    window=("2014", "2026"),
    matrix_text="app, version, state (BFU/AFU), artefacts recovered, deletion recovery",
    matrix_groups={"app": r"\bapp\b|messenger|application|signal|telegram|whatsapp", "version": r"version", "state": r"state|bfu|afu|unlock", "artefacts": r"artefact|artifact|recover", "deletion": r"delet"},
    matrix_need=4,
    key_refs=[("Onik et al., ACM Computing Surveys 2025 (prior SLR on this exact topic)", r"onik|systematic literature review of secure instant")],
    key_ref_hint="A review on the same topic already exists - state what this paper adds (versions, BFU/AFU, deletion/WAL, legal routes)",
    standards_std=("C10", "Standards-based method (NIST SP 800-101 Rev. 1; ISO/IEC 27037)", r"800-101|27037|27041|27042"),
    cov=[
      ("C1", "Apps: Signal, Telegram, WhatsApp covered", [r"signal", r"telegram", r"whatsapp"], 3),
      ("C2", "Platforms: Android and iOS covered", [r"android", r"\bios\b"], 2),
      ("C3", "Storage locations / artefacts (device DBs, backups, key stores, caches, media)", [r"sqlite|database", r"backup", r"key ?store|keychain", r"cache", r"media|attachment"], 4),
      ("C4", "Acquisition states: before/after first unlock (BFU/AFU)", [r"before first unlock|\bbfu\b", r"after first unlock|\bafu\b"], 2),
      ("C5", "App versions / app evolution (version-robustness)", [r"\bversions?\b", r"update|upgrade|migration|evolution"], 2),
      ("C6", "Deletion and database maintenance (WAL/SHM, checkpoint, vacuum)", [r"\bwal\b|write-ahead", r"checkpoint", r"delet", r"vacuum|\bshm\b"], 3),
      ("C7", "Backups and cloud exports; update/backup behaviour", [r"backup", r"cloud", r"export"], 2),
      ("C8", "Legal routes to cloud data (warrants, MLAT, lawful access, jurisdiction)", [r"legal|lawful|warrant|court order|subpoena|mlat|mutual legal|jurisdiction|cloud act"], 1),
      ("C9", "Encryption context (E2EE, encrypted DB such as SQLCipher, FBE, keystore)", [r"end-to-end|e2ee", r"sqlcipher|encrypted database|file-based encryption|\bfbe\b|keystore"], 1),
      ("C11", "Methodological gaps (single-version studies, tool disagreement, validation, reproducibility)", [r"single[- ]version|tool (disagreement|differences|validation)|reproducib|validation|ground truth"], 1),
    ]),
  "34": dict(
    name="Topic 34 - Forensic Readiness and Standardisation in Organisations (Handbook: Validated Digital-Forensic Readiness Maturity Model for Organizations)",
    h="Handbook Topic 34",
    title_rx=(r"readiness|standardi[sz]ation|maturity", r"forensic"),
    title_hint="Title should name forensic readiness (and standardisation/maturity) in organisations",
    rq_text="RQ1-RQ3 of Topic 34 (which readiness frameworks/maturity models exist; which capabilities standards support and how readiness is measured; evidence that maturity predicts investigative capability + gaps) are stated and answered",
    dbs={"IEEE Xplore": r"ieee xplore", "ACM Digital Library": r"acm (digital library|dl)", "ScienceDirect": r"sciencedirect", "Scopus": r"scopus", "Google Scholar": r"google scholar", "SpringerLink": r"springerlink|springer link"},
    db_need=4, db_text="databases + standards bodies (ISO, NIST, NCA); standards reviewed directly",
    string_terms=["forensic readiness", "digital forensic readiness", "maturity", "framework", "standard", "iso"], string_need=5,
    string_text='("forensic readiness" OR "digital forensic readiness") AND (maturity OR framework OR standard OR ISO)',
    window=("2001", "2026"),
    matrix_text="framework, standard basis, measurement method, validation",
    matrix_groups={"framework": r"framework|model|approach", "standard": r"standard|iso|nist|nca|basis", "measurement": r"measure|assess|metric|score|maturity", "validation": r"validat|evidence|reliab|empirical"},
    matrix_need=4,
    key_refs=[("Rowlingson 2004 - ten-step forensic readiness process", r"rowlingson|ten step process"),
              ("ISO/IEC 27043 (incident investigation principles and processes)", r"27043"),
              ("ISO/IEC 27037 (digital evidence handling)", r"27037"),
              ("ISO/IEC 27035 (incident management)", r"27035"),
              ("NIST SP 800-61 Rev. 3", r"800-61"),
              ("Horsman 2024 - digital evidence strategies", r"horsman")],
    key_ref_hint="Handbook Topic 34 lists these as the anchor sources; the review must cover frameworks/standards directly",
    standards_std=("C10", "Standards reviewed directly (ISO/IEC 27043, 27037, 27035, 30121; NIST SP 800-61; NCA guidance)", r"27043|27037|27035|30121|800-61|\bnca\b|national cybersecurity authority"),
    cov=[
      ("C1", "Readiness frameworks covered (Rowlingson ten-step, ISO/IEC 27043, 27035, 30121)", [r"rowlingson", r"27043", r"27035", r"30121|governance of digital forensic"], 3),
      ("C2", "Saudi / national guidance covered (NCA - National Cybersecurity Authority controls, PDPL)", [r"\bnca\b|national cybersecurity authority", r"pdpl|personal data protection|saudi"], 1),
      ("C3", "Readiness capabilities: governance, logging, retention, time synchronisation", [r"governance", r"logging|log management", r"retention", r"time synchroni[sz]ation|clock|ntp"], 4),
      ("C4", "Readiness capabilities: acquisition, cloud, personnel/training, testing/exercises", [r"acquisition", r"cloud", r"personnel|training|skills", r"testing|tabletop|exercise"], 3),
      ("C5", "Maturity models / levels / scoring (how readiness is measured)", [r"maturity (model|level)|capability maturity|cmmi", r"scor(e|ing)|assessment|metric"], 2),
      ("C6", "Validation evidence: inter-rater reliability, empirical/scenario validation, predictive link to investigative outcomes", [r"inter-rater|reliab", r"validat", r"predict|outcome|incident|scenario|tabletop"], 2),
      ("C7", "Admissibility link: readiness before an incident -> admissible evidence (chain of custody, ISO/IEC 27037)", [r"admissib", r"chain of custody|evidence handling|27037"], 1),
      ("C8", "Standardisation context (ISO/IEC, NIST, interoperability, accreditation e.g. ISO/IEC 17025)", [r"standardi[sz]", r"17025|accredit|interoperab|iso/iec"], 1),
      ("C11", "Evidence-based gaps stated (rarely validated instruments, no predictive evidence, measurement agenda)", [r"rarely|few studies|lack of|no (empirical|study)|measurement agenda|not validated|unvalidated"], 1),
    ]),
}

# --------------------------------------------------------------------------- sources
G = "Guidelines"                      # CS616_Research_Paper_Guidelines.pdf
H = "Handbook"                        # CS616_TwoTrack_Research_Handbook.pdf (Review track + Topic 19)

# ------------------------------------------------------------------------- findings
FINDINGS = []

def add(fid, cat, status, req, evidence="", source="", hint=""):
    FINDINGS.append(OrderedDict(id=fid, category=cat, status=status, requirement=req,
                                evidence=evidence, source=source, hint=hint))

# ------------------------------------------------------------------------ file input
def safe_extract(zpath, dest):
    with zipfile.ZipFile(zpath) as z:
        for m in z.namelist():
            target = os.path.realpath(os.path.join(dest, m))
            if not target.startswith(os.path.realpath(dest) + os.sep) and target != os.path.realpath(dest):
                raise SystemExit("Unsafe path in zip: %s" % m)
        z.extractall(dest)

def find_main_tex(root, main=None):
    if main:
        p = main if os.path.isabs(main) else os.path.join(root, main)
        if os.path.isfile(p): return p
        raise SystemExit("Main file not found: %s" % main)
    cands = []
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if not d.startswith(".") and d != "__MACOSX"]
        for f in fn:
            if f.endswith(".tex"):
                path = os.path.join(dp, f)
                try: txt = open(path, encoding="utf-8", errors="replace").read()
                except OSError: continue
                if re.search(r"\\documentclass", txt) and re.search(r"\\begin\{document\}", txt):
                    cands.append(path)
    if not cands: raise SystemExit("No main .tex (with \\documentclass + \\begin{document}) found under %s" % root)
    cands.sort(key=lambda p: (os.path.basename(p) != "main.tex", len(p)))
    return cands[0]

def strip_comment(line):
    out, i = [], 0
    while i < len(line):
        c = line[i]
        if c == "\\" and i + 1 < len(line): out.append(line[i:i+2]); i += 2; continue
        if c == "%": break
        out.append(c); i += 1
    return "".join(out)

def expand(path, root, seen=None, depth=0):
    """Return list of (file, lineno, text) with \\input/\\include expanded and comments stripped."""
    seen = seen or set()
    rp = os.path.realpath(path)
    if rp in seen or depth > 12: return []
    seen = seen | {rp}
    out = []
    try: lines = open(path, encoding="utf-8", errors="replace").read().split("\n")
    except OSError: return out
    for n, raw in enumerate(lines, 1):
        line = strip_comment(raw)
        m = re.search(r"\\(?:input|include|subfile)\{([^}]+)\}", line)
        if m:
            name = m.group(1).strip()
            cand = [os.path.join(os.path.dirname(path), name), os.path.join(root, name)]
            cand += [c + ".tex" for c in cand]
            f = next((c for c in cand if os.path.isfile(c)), None)
            if f:
                out.extend(expand(f, root, seen, depth + 1)); continue
        out.append((os.path.relpath(path, root), n, line))
    return out

# ---------------------------------------------------------------------------- bib
def _scan_braced(s, i):
    depth, j = 0, i
    while j < len(s):
        c = s[j]
        if c == "\\": j += 2; continue
        if c == "{": depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0: return s[i+1:j], j + 1
        j += 1
    return s[i+1:], len(s)

def parse_bib(text):
    entries = OrderedDict()
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", text):
        typ = m.group(1).lower()
        if typ in ("comment", "string", "preamble"): continue
        ob = text.index("{", m.start())
        body, _ = _scan_braced(text, ob)
        body = body[body.index(",") + 1:]
        fields, i = {}, 0
        while True:
            fm = re.compile(r"\s*,?\s*([A-Za-z\-]+)\s*=\s*").search(body, i)
            if not fm: break
            i = fm.end()
            if i >= len(body): break
            if body[i] == "{": val, i = _scan_braced(body, i)
            elif body[i] == '"':
                j = i + 1
                while j < len(body) and not (body[j] == '"' and body[j-1] != "\\"): j += 1
                val, i = body[i+1:j], j + 1
            else:
                vm = re.compile(r"[^,]*").match(body, i); val, i = vm.group(0).strip(), vm.end()
            fields[fm.group(1).lower()] = re.sub(r"\s+", " ", val).strip()
        entries[m.group(2)] = dict(type=typ, **fields)
    return entries

WEB_BAD = ["wikipedia.org", "medium.com", "blogspot.", "wordpress.com", "reddit.com", "quora.com",
           "stackoverflow.com", "stackexchange.com", "youtube.com", "youtu.be", "facebook.com", "twitter.com", "x.com/"]
VENDOR = ["cellebrite.com", "magnetforensics.com", "oxygen-forensic", "msab.com", "belkasoft.com",
          "grayshift", "elcomsoft.com", "whatsapp.com", "signal.org", "telegram.org", "blog"]
PEER = {"article", "inproceedings", "conference", "incollection", "inbook", "book"}
OFFICIAL = re.compile(r"\b(NIST|ISO/IEC|ISO|IEC|RFC|IEEE Std|SWGDE|ENISA|Royal Decree|Directive|Regulation|Act)\b", re.I)

def classify_ref(e):
    """-> peer | standard | thesis | preprint | web | other"""
    t, blob = e.get("type", ""), " ".join(str(v) for v in e.values()).lower()
    if "arxiv" in blob or e.get("archiveprefix", "").lower() == "arxiv": return "preprint"
    if t in ("phdthesis", "mastersthesis", "thesis"): return "thesis"
    if t in ("techreport", "standard", "manual") or OFFICIAL.search(blob) and t in ("misc", "techreport", "manual", "online", "standard"): return "standard"
    if t in PEER: return "peer"
    if t in ("misc", "online", "electronic", "webpage", "unpublished") or "url" in e or "howpublished" in e: return "web"
    return "other"

# -------------------------------------------------------------------------- text
ENV_DROP = ["figure", "figure*", "table", "table*", "tabular", "tabular*", "tabularx", "longtable", "thebibliography",
            "equation", "equation*", "align", "align*", "eqnarray", "eqnarray*", "lstlisting", "verbatim", "tikzpicture",
            "algorithm", "algorithmic", "IEEEbiography", "IEEEbiographynophoto", "wrapfigure", "abstract", "IEEEkeywords",
            "displaymath", "multline", "gather", "minted"]

def drop_envs(t, names):
    for n in names:
        pat = re.compile(r"\\begin\{%s\}.*?\\end\{%s\}" % (re.escape(n), re.escape(n)), re.S)
        prev = None
        while prev != t:
            prev, t = t, pat.sub(" ", t)
    return t

def to_plain(t):
    t = re.sub(r"\\IEEEPARstart\{(\w)\}\{(\w*)\}", r"\1\2", t)
    t = re.sub(r"\$\$.*?\$\$|\\\[.*?\\\]|\\\(.*?\\\)|\$[^$]*\$", " ", t, flags=re.S)
    t = re.sub(r"\\(?:cite[a-z]*|nocite|ref|eqref|cref|Cref|autoref|pageref|label|url|footnotemark|vspace\*?|hspace\*?)\*?(?:\[[^\]]*\])*\{[^}]*\}", " ", t)
    t = re.sub(r"\\href\{[^}]*\}\{([^}]*)\}", r"\1", t)
    t = re.sub(r"\\(?:begin|end)\{[^}]*\}(?:\[[^\]]*\])?", " ", t)
    t = re.sub(r"\\(?:sub)*section\*?(?:\[[^\]]*\])?\{[^}]*\}", " ", t)
    t = re.sub(r"\\(?:IEEEauthorblock[NA]|author|title|thanks|maketitle|centering|noindent|appendix|appendices|IEEEpeerreviewmaketitle|bibliographystyle|bibliography)\b(\{[^}]*\})?", " ", t)
    t = re.sub(r"\\[a-zA-Z@]+\*?(?:\[[^\]]*\])*", " ", t)
    t = t.replace("~", " ").replace("\\\\", " ").replace("\\&", "&").replace("\\%", "%")
    t = re.sub(r"[{}$^_\\]", " ", t)
    return re.sub(r"\s+", " ", t).strip()

def wcount(plain):
    return sum(1 for tok in plain.split() if re.search(r"\w", tok))

# ---------------------------------------------------------------------- main logic
SEC_CLASSES = [  # (key, regex, label, rough word guide)
    ("intro",      r"introduct",                                                  "Introduction",                 (600, 800)),
    ("conclusion", r"conclu|future (work|research|direction)|concluding",         "Conclusion & Future Work",     (250, 350)),
    ("results",    r"result|discussion|findings|limitation|implication",          "Results & Discussion",         (700, 1000)),
    ("method",     r"method|approach|protocol|search strateg|review design|research design", "Methodology / Approach", (800, 1200)),
    ("related",    r"background|related|literature|state[- ]of[- ]the[- ]art|preliminar|prior", "Background / Related Work", (1000, 1400)),
    ("analysis",   r"analy|synthes|taxonom|compar|implement|evidence|artefact|artifact|landscape|survey of|review of|legal", "Implementation / Analysis", (1000, 1400)),
]
REQ_ORDER = ["intro", "related", "method", "analysis", "results", "conclusion"]

def classify_section(title):
    t = title.lower()
    if re.search(r"acknowledg|funding", t): return "ack"
    if re.search(r"^\s*references?\s*$|bibliograph", t): return "refs"
    if re.search(r"appendi", t): return "appendix"
    for key, rx, _, _ in SEC_CLASSES:
        if re.search(rx, t): return key
    return "other"

def main():
    ap = argparse.ArgumentParser(description="CS616 review-paper pre-checker (topic 19 or 34)")
    ap.add_argument("path", help="Overleaf folder, .zip export, or a .tex file")
    ap.add_argument("--topic", choices=sorted(PROFILES), required=True, help="19 or 34 - checks ONLY that topic's requirements")
    ap.add_argument("--main", help="main .tex file (relative to root) if auto-detect picks the wrong one")
    ap.add_argument("--stage", choices=["draft", "final"], default="final",
                    help="draft (Week 9) downgrades length/reference-count FAILs to WARN")
    ap.add_argument("--year", type=int, default=datetime.date.today().year, help="current year for recency (default: today)")
    ap.add_argument("--format", choices=["md", "json"], default="md")
    ap.add_argument("--out", help="write report to this file instead of stdout")
    a = ap.parse_args()

    tmp = None
    p = os.path.abspath(a.path)
    if p.lower().endswith(".zip"):
        tmp = tempfile.mkdtemp(prefix="t19_"); safe_extract(p, tmp); root = tmp
    elif os.path.isfile(p): root = os.path.dirname(p); a.main = a.main or os.path.basename(p)
    else: root = p
    mainf = find_main_tex(root, a.main)
    lines = expand(mainf, root)
    full = "\n".join(l[2] for l in lines)
    T = PROFILES[a.topic]; HT = T["h"]
    soft = (lambda s: "WARN" if (a.stage == "draft" and s == "FAIL") else s)

    def line_of(pos):
        n = full.count("\n", 0, pos); f, ln, _ = lines[min(n, len(lines) - 1)]
        return "%s:%d" % (f, ln)

    bd = re.search(r"\\begin\{document\}", full)
    pre, body = (full[:bd.start()], full[bd.end():]) if bd else ("", full)
    body = re.split(r"\\end\{document\}", body)[0]
    boff = len(pre) + (bd.end() - bd.start() if bd else 0)

    # ---- 1. template / format ------------------------------------------------
    dc = re.search(r"\\documentclass(?:\[([^\]]*)\])?\{([^}]+)\}", pre)
    cls, opts = (dc.group(2), dc.group(1) or "") if dc else ("?", "")
    if cls == "IEEEtran" and "conference" in opts and not re.search(r"onecolumn|journal|transmag|peerreview", opts):
        add("F1", "Format", "PASS", "Official IEEE conference two-column template (IEEEtran, [conference])",
            "\\documentclass[%s]{IEEEtran}" % opts, G + " §3 Format")
    elif cls == "IEEEtran":
        add("F1", "Format", "WARN", "Official IEEE *conference* template",
            "\\documentclass[%s]{IEEEtran} - no [conference] option or a non-conference option" % opts, G + " §3 Format",
            "Use \\documentclass[conference]{IEEEtran} (two-column)")
    else:
        add("F1", "Format", "FAIL", "Official IEEE conference two-column template (IEEEtran)",
            "documentclass = %s" % cls, G + " §3 Format", "Start from the Overleaf IEEE conference template; do not invent a layout")
    hacks = [x for x in [r"\\usepackage(\[[^\]]*\])?\{geometry\}", r"\\geometry\{", r"\\usepackage\{fullpage\}",
                         r"\\usepackage\{setspace\}", r"\\linespread", r"\\baselinestretch", r"\\setlength\{\\(?:textwidth|textheight|columnsep|parindent)\}",
                         r"\\fontsize\{", r"\\usepackage(\[[^\]]*\])?\{(?:times|mathptmx|fontspec)\}"] if re.search(x, pre + body)]
    vs = len(re.findall(r"\\vspace\*?\{-", body))
    if hacks or vs > 6:
        add("F2", "Format", "WARN", "No layout hacks that alter the IEEE template (margins, spacing, fonts)",
            "found: %s; negative \\vspace count: %d" % (", ".join(hacks) or "-", vs), G + " §3 Format", "Remove layout overrides; fit length by editing text")
    else:
        add("F2", "Format", "PASS", "No layout hacks that alter the IEEE template", "none detected", G + " §3 Format")

    res_residue = [s for s in ["component, formatting, style, styling, insert", "Given Name Surname", "line 1 (of Affiliation)",
                               "model and instructions for", "Identify applicable funding agency", "email address or ORCID",
                               "Lorem", "lorem", "ipsum", "TODO", "FIXME", "TBD", "XXX", "\\todo", "Your text here",
                               "Enter text", "Heading 1", "Template Heading"] if s in full]
    if res_residue:
        add("F3", "Format", "FAIL", "No leftover template text or draft markers (author block, sample abstract/keywords, TODO)",
            "found: " + "; ".join(res_residue), G + " §10 Checklist (Proofread)", "Replace/remove all template sample text and TODO markers")
    else:
        add("F3", "Format", "PASS", "No leftover template text or draft markers", "none detected", G + " §10 Checklist (Proofread)")

    # ---- 2. title / abstract / keywords --------------------------------------
    tm = re.search(r"\\title\{(.*?)\}\s*(?:\\|$)", pre + body, re.S)
    title = to_plain(tm.group(1)) if tm else ""
    if not title:
        add("T1", "Title", "FAIL", "Specific, informative title", "no \\title found", G + " §4 Title")
    else:
        generic = title.lower().strip(" .:") in ("digital forensics", "forensics", "a survey", "a review", "mobile forensics")
        on_topic = bool(re.search(T["title_rx"][0], title, re.I) and re.search(T["title_rx"][1], title, re.I))
        st = "FAIL" if generic else ("PASS" if on_topic else "WARN")
        add("T1", "Title", st, "Specific, informative title that matches " + T["name"].split(" (")[0],
            "title = “%s”" % title, G + " §4 Title; " + HT,
            "" if st == "PASS" else T["title_hint"] + "; the instructor allows narrowing the topic by agreement")
        if not re.search(r"review|survey|systematic|literature", title, re.I):
            add("T2", "Title", "INFO", "Title signals a review paper (optional but helpful)", "no review/survey/systematic word in title", H + " Review track")
    am = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", full, re.S)
    if am:
        aw = wcount(to_plain(am.group(1)))
        st = "PASS" if 150 <= aw <= 250 else ("WARN" if 120 <= aw <= 280 else "FAIL")
        add("A1", "Abstract", st, "Abstract 150-250 words", "%d words" % aw, G + " §4 Abstract")
        add("A2", "Abstract", "MANUAL", "Abstract states the problem, the approach (review method) and the single most important finding; written last",
            "read the abstract", G + " §4 Abstract")
        if re.search(r"\\cite", am.group(1)):
            add("A3", "Abstract", "WARN", "No citations inside the abstract (IEEE convention)", "\\cite found in abstract", G + " §3 / IEEE")
    else:
        add("A1", "Abstract", "FAIL", "Abstract present (150-250 words)", "no abstract environment found", G + " §4 Abstract")
    km = re.search(r"\\begin\{IEEEkeywords\}(.*?)\\end\{IEEEkeywords\}", full, re.S) or re.search(r"\\keywords\{(.*?)\}", full, re.S)
    if km:
        terms = [x.strip() for x in re.split(r"[,;]", to_plain(km.group(1))) if x.strip()]
        st = "PASS" if 4 <= len(terms) <= 6 else "FAIL"
        add("K1", "Keywords", st, "Index Terms / Keywords: 4-6 terms", "%d terms: %s" % (len(terms), "; ".join(terms)), G + " §4 Index Terms")
    else:
        add("K1", "Keywords", "FAIL", "Index Terms / Keywords (4-6 terms)", "no IEEEkeywords environment", G + " §4 Index Terms")

    # ---- 3. sections ------------------------------------------------------------
    sec_re = re.compile(r"\\section(\*?)(?:\[[^\]]*\])?\{([^}]*)\}")
    ms = list(sec_re.finditer(body))
    secs = []
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(body)
        title_s = to_plain(m.group(2)); key = classify_section(title_s)
        raw = body[m.end():end]
        if key in ("appendix",) or re.search(r"\\appendix", raw):
            raw = re.split(r"\\appendix", raw)[0]
        subs = [to_plain(x) for x in re.findall(r"\\subsection\*?(?:\[[^\]]*\])?\{([^}]*)\}", raw)]
        plain = to_plain(drop_envs(raw, ENV_DROP))
        secs.append(dict(title=title_s, key=key, words=wcount(plain), subs=subs, raw=raw, plain=plain,
                         line=line_of(boff + m.start())))
    # appendices that start with \appendix inside the last section stay excluded by the split above
    counted = [s for s in secs if s["key"] not in ("refs", "ack", "appendix")]
    abs_plain = to_plain(am.group(1)) if am else ""
    total = sum(s["words"] for s in counted)
    total_with_abs = total + wcount(abs_plain)
    if 5000 <= total <= 6000 or 5000 <= total_with_abs <= 6000: st = "PASS"
    elif 4500 <= total <= 6600 or 4500 <= total_with_abs <= 6600: st = "WARN"
    else: st = soft("FAIL")
    add("L1", "Length", st, "~5,000-6,000 words excluding references, tables, figures, appendices (±10% => 4,500-6,600)",
        "body = %d words (+abstract = %d). Approximate: counts prose only." % (total, total_with_abs), G + " §3 Length",
        "Confirm with Overleaf's Word Count / TeXcount, and confirm the exact limit with the instructor")

    present = OrderedDict()
    for s in secs:
        present.setdefault(s["key"], []).append(s)
    for key in REQ_ORDER:
        label = next(c[2] for c in SEC_CLASSES if c[0] == key); rng = next(c[3] for c in SEC_CLASSES if c[0] == key)
        if key not in present:
            add("S-" + key, "Structure", "FAIL", "Section present: %s" % label, "no section title matches", G + " §4 Structure",
                "If it exists under another name, rename it to match the required structure")
        else:
            w = sum(s["words"] for s in present[key]); lo, hi = int(rng[0] * .75), int(rng[1] * 1.25)
            st = "PASS" if lo <= w <= hi else "WARN"
            add("S-" + key, "Structure", st, "Section present: %s (rough guide %d-%d words)" % (label, *rng),
                "“%s” - %d words (line %s)" % (" + ".join(s["title"] for s in present[key]), w, present[key][0]["line"]),
                G + " §4 Structure", "" if st == "PASS" else "Outside the rough guide (guide only; ±25%% tolerated)")
    order = [next((i for i, s in enumerate(secs) if s["key"] == k), None) for k in REQ_ORDER]
    ordv = [o for o in order if o is not None]
    add("S-order", "Structure", "PASS" if ordv == sorted(ordv) else "WARN", "Sections follow the required order (Intro > Related Work > Methodology > Analysis > Results > Conclusion)",
        " > ".join("%s" % s["title"] for s in secs), G + " §4 Structure")
    add("S-refs", "Structure", "PASS" if re.search(r"\\bibliography\{|\\begin\{thebibliography|\\printbibliography", full) else "FAIL",
        "References section present", "bibliography command found" if re.search(r"\\bibliography\{|thebibliography|printbibliography", full) else "none", G + " §4 References")

    # ---- 4. citations & references ---------------------------------------------
    nobib = re.sub(r"\\begin\{thebibliography\}.*?\\end\{thebibliography\}", " ", body, flags=re.S)
    cite_re = re.compile(r"\\(?:cite[a-z]*|parencite|textcite|autocite|footcite)\*?(?:\[[^\]]*\])*\{([^}]+)\}")
    order_keys, cite_pos = [], {}
    nocite_all = bool(re.search(r"\\nocite\{\*\}", full))
    for m in cite_re.finditer(nobib):
        for k in [x.strip() for x in m.group(1).split(",") if x.strip()]:
            if k not in cite_pos: cite_pos[k] = m.start(); order_keys.append(k)
    bibs = OrderedDict()
    for bf in re.findall(r"\\(?:bibliography|addbibresource)\{([^}]+)\}", full):
        for b in bf.split(","):
            b = b.strip(); b = b if b.endswith(".bib") else b + ".bib"
            for c in (os.path.join(root, b), os.path.join(os.path.dirname(mainf), b)):
                if os.path.isfile(c): bibs.update(parse_bib(open(c, encoding="utf-8", errors="replace").read())); break
    items = OrderedDict()
    tb = re.search(r"\\begin\{thebibliography\}.*?\\end\{thebibliography\}", full, re.S)
    if tb:
        for m in re.finditer(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}(.*?)(?=\\bibitem|\\end\{thebibliography\})", tb.group(0), re.S):
            txt = to_plain(m.group(2)); ym = re.findall(r"\b(19\d\d|20\d\d)\b", txt)
            items[m.group(1)] = dict(type="bibitem", year=ym[-1] if ym else "", title=txt, note=txt,
                                     **({"url": "x"} if re.search(r"http|Online|Available", txt) else {}))
    ref_db = bibs if bibs else items
    style = re.search(r"\\bibliographystyle\{([^}]+)\}", full); bl = re.search(r"\\usepackage(?:\[([^\]]*)\])?\{biblatex\}", full)
    if bibs:
        ok = (style and style.group(1) == "IEEEtran") or (bl and "ieee" in (bl.group(1) or ""))
        add("R1", "References", "PASS" if ok else "FAIL", "IEEE numbered reference style (\\bibliographystyle{IEEEtran} or biblatex style=ieee)",
            "style = %s" % (style.group(1) if style else ("biblatex[%s]" % (bl.group(1) if bl else "") if bl else "none")), G + " §5.3 How to cite")
    elif items:
        add("R1", "References", "PASS", "IEEE numbered style via thebibliography (numbered by order of \\bibitem)", "%d \\bibitem entries" % len(items), G + " §5.3")
    else:
        add("R1", "References", "FAIL", "A bibliography (.bib or thebibliography)", "none found", G + " §5")
    cited_keys = set(order_keys) if not nocite_all else set(ref_db)
    in_list = [k for k in ref_db if (k in cited_keys)] if bibs else list(items)
    n_refs = len(in_list)
    add("R2", "References", "PASS" if n_refs >= 15 else soft("FAIL"), "At least 15 references",
        "%d references in the list" % n_refs, G + " §5.1 Minimum")
    missing = [k for k in order_keys if k not in ref_db]
    add("R3", "References", "FAIL" if missing else "PASS", "Every citation in the text appears in the reference list",
        ("undefined keys: " + ", ".join(missing)) if missing else "all %d cited keys resolve" % len(order_keys), G + " §5.3")
    unused = [k for k in ref_db if k not in cited_keys]
    if tb: st = "FAIL" if unused else "PASS"
    else: st = ("FAIL" if nocite_all and unused else ("WARN" if unused else "PASS"))
    add("R4", "References", st, "Every reference in the list is cited in the text",
        ("uncited: " + ", ".join(unused[:20])) if unused else "none uncited", G + " §5.3",
        "Remove uncited entries (BibTeX hides them unless \\nocite{*} is used)" if unused else "")
    if tb:
        want = [k for k in order_keys if k in items]; have = [k for k in items if k in cited_keys]
        add("R5", "References", "PASS" if want == have else "FAIL", "Reference numbering follows order of first appearance (IEEE)",
            "bibitem order %s citation order" % ("matches" if want == have else "differs from"), G + " §5.3")
    cl = OrderedDict()
    for k in in_list:
        cl.setdefault(classify_ref(ref_db[k]), []).append(k)
    if n_refs:
        peer_like = len(cl.get("peer", [])) + len(cl.get("standard", [])) + len(cl.get("thesis", []))
        pct = 100.0 * len(cl.get("peer", [])) / n_refs
        add("R6", "References", "PASS" if pct > 50 else ("WARN" if pct >= 40 else "FAIL"),
            "Majority of references are peer-reviewed (journal/conference); preprints, theses, web pages are labelled and minority",
            "peer-reviewed-type %d/%d (%.0f%%); standards %d; theses %d; preprints %d; web/other %d" % (
                len(cl.get("peer", [])), n_refs, pct, len(cl.get("standard", [])), len(cl.get("thesis", [])), len(cl.get("preprint", [])),
                len(cl.get("web", [])) + len(cl.get("other", []))), G + " §5.1; " + H + " Reference policy",
            "Entry *type* is only a proxy - verify venues (Q1/Q2, CORE A/B) manually")
        yrs = [int(ref_db[k].get("year", 0) or 0) for k in in_list if str(ref_db[k].get("year", "")).isdigit()]
        recent = [y for y in yrs if y >= a.year - 5]
        rp = 100.0 * len(recent) / max(len(yrs), 1)
        add("R7", "References", "PASS" if rp > 50 else ("WARN" if rp >= 40 else "FAIL"),
            "Majority of references are recent (last ~5 years; older only for foundational work)",
            "%d/%d dated >= %d (%.0f%%); oldest %s; entries without year: %d" % (len(recent), len(yrs), a.year - 5, rp, min(yrs) if yrs else "-", n_refs - len(yrs)),
            G + " §5.1 Recency")
        bad, ven = [], []
        for k in in_list:
            blob = " ".join(str(v) for v in ref_db[k].values()).lower()
            if any(d in blob for d in WEB_BAD): bad.append(k)
            elif any(d in blob for d in VENDOR) and ref_db[k].get("type") in ("misc", "online", "bibitem", "electronic"): ven.append(k)
        if bad: add("R8", "References", "FAIL", "No blogs/Wikipedia/forums as sources", "flagged: " + ", ".join(bad), G + " §5.1 Avoid")
        else: add("R8", "References", "PASS", "No blogs/Wikipedia/forum sources detected", "none flagged", G + " §5.1 Avoid")
        if ven: add("R9", "References", "WARN", "Vendor / app-maker web pages only as labelled primary technical sources, dated",
                    "check: " + ", ".join(ven), G + " §5.1 Avoid; " + H + " Reference policy", "Keep only if they are primary technical documentation; add access date")
        incomplete = [k for k in in_list if ref_db[k].get("type") != "bibitem" and not (ref_db[k].get("author") and ref_db[k].get("title") and ref_db[k].get("year"))]
        nodoi = [k for k in in_list if ref_db[k].get("type") in ("article", "inproceedings", "conference") and not (ref_db[k].get("doi") or ref_db[k].get("pages"))]
        undated_web = [k for k in cl.get("web", []) if not (ref_db[k].get("urldate") or ref_db[k].get("note") or ref_db[k].get("urlaccessdate"))]
        add("R10", "References", "WARN" if (incomplete or nodoi or undated_web) else "PASS",
            "IEEE entries complete: authors, title, venue, year, pages/DOI; web sources carry access date",
            "missing author/title/year: %s | no pages/DOI: %s | web without access date: %s" % (
                ", ".join(incomplete) or "-", ", ".join(nodoi[:15]) or "-", ", ".join(undated_web) or "-"), G + " §5.3; " + H + " Reference policy")
        seen_t, dups = {}, []
        for k in in_list:
            tt = re.sub(r"\W+", "", str(ref_db[k].get("title", "")).lower())
            if tt and tt in seen_t: dups.append("%s=%s" % (seen_t[tt], k))
            elif tt: seen_t[tt] = k
        if dups: add("R11", "References", "WARN", "No duplicate entries", ", ".join(dups), G + " §5.3")
        for ki, (lab, rx) in enumerate(T["key_refs"], 1):
            hit = [k for k in ref_db if re.search(rx, " ".join(str(v) for v in ref_db[k].values()), re.I)]
            add("R12.%d" % ki, "References", "PASS" if hit else "WARN", "Anchor source cited: " + lab,
                "found: %s" % (", ".join(hit) if hit else "not found in bibliography"), HT + " references", "" if hit else T["key_ref_hint"])

    # ---- 5. figures / tables ----------------------------------------------------
    envs = []
    for m in re.finditer(r"\\begin\{(figure\*?|table\*?)\}(.*?)\\end\{\1\}", body, re.S):
        cap = re.search(r"\\caption(?:\[[^\]]*\])?\{((?:[^{}]|\{[^{}]*\})*)\}", m.group(2))
        lab = re.search(r"\\label\{([^}]+)\}", m.group(2))
        envs.append(dict(kind=m.group(1).rstrip("*"), caption=to_plain(cap.group(1)) if cap else "", label=lab.group(1) if lab else "",
                         has_img="includegraphics" in m.group(2), raw=m.group(2), line=line_of(boff + m.start())))
    refs_used = set()
    for m in re.finditer(r"\\(?:ref|cref|Cref|autoref|eqref|vref)\*?\{([^}]+)\}", full):
        refs_used.update(x.strip() for x in m.group(1).split(","))
    nocap = [e["line"] for e in envs if not e["caption"]]; nolab = [e["line"] for e in envs if not e["label"]]
    unref = [e["label"] for e in envs if e["label"] and e["label"] not in refs_used]
    add("FT1", "Figures/Tables", "FAIL" if nocap else "PASS", "Every figure/table is numbered and captioned",
        "%d floats; without caption at %s" % (len(envs), ", ".join(nocap) or "-"), G + " §3 Figures & tables")
    add("FT2", "Figures/Tables", "FAIL" if (nolab or unref) else "PASS", "Every figure/table has a \\label and is referred to in the text (e.g. “Fig. 2 shows…”)",
        "no label: %s | never referenced: %s" % (", ".join(nolab) or "-", ", ".join(unref) or "-"), G + " §3 Figures & tables")
    defined = set(re.findall(r"\\label\{([^}]+)\}", full))
    dangling = sorted(r for r in refs_used if r not in defined)
    add("FT3", "Figures/Tables", "FAIL" if dangling else "PASS", "No dangling \\ref (would print “??”)", ", ".join(dangling) or "none", G + " §10 Proofread")
    short = [e["line"] for e in envs if e["has_img"] and wcount(e["caption"]) < 6]
    if short: add("FT4", "Figures/Tables", "WARN", "Figures/screenshots explained (caption not a bare label)", "short captions at " + ", ".join(short), G + " §3: do not paste screenshots without explanation")
    kw_groups = {
        "approach": r"approach|method|technique|study|tool|app\b|application|messenger|reference|work",
        "dataset": r"dataset|corpus|data\b|device|platform|os\b|android|ios|sample|evidence|version",
        "results": r"result|finding|outcome|recover|artefact|artifact|performance|survive|retriev",
        "limitations": r"limitation|gap|weakness|constraint|threat|caveat",
    }
    t19_groups = T["matrix_groups"]
    best, best_t19, tinfo = (0, None), (0, None), []
    for e in [x for x in envs if x["kind"] == "table"]:
        head = " ".join(e["raw"].split("\\\\")[:3]).lower() + " " + e["caption"].lower()
        g = [n for n, rx in kw_groups.items() if re.search(rx, head)]
        g19 = [n for n, rx in t19_groups.items() if re.search(rx, head)]
        tinfo.append("%s (%d/4 generic, %d/%d topic)" % (e["line"], len(g), len(g19), len(t19_groups)))
        if len(g) > best[0]: best = (len(g), e)
        if len(g19) > best_t19[0]: best_t19 = (len(g19), e)
    ntab = len([e for e in envs if e["kind"] == "table"])
    st = "FAIL" if ntab == 0 else ("PASS" if best[0] >= 3 else "WARN")
    add("FT5", "Review content", st, "At least one comparison table (approach vs dataset vs results vs limitations)",
        "%d tables; %s" % (ntab, "; ".join(tinfo) or "no tables"), G + " §2.1 Methodology", "Header/caption should make the four dimensions visible")
    st = "FAIL" if ntab == 0 else ("PASS" if best_t19[0] >= T["matrix_need"] else "WARN")
    add("FT6", "Review content", st, "Comparison matrix covers the topic's dimensions: " + T["matrix_text"],
        "best table matches %d/%d dimensions" % (best_t19[0], len(t19_groups)), HT + " Synthesis & appraisal")

    # ---- 6. acronyms ------------------------------------------------------------
    prose = to_plain(drop_envs(body, [e for e in ENV_DROP if e not in ("abstract",)])) if body else ""
    prose = (abs_plain + " " + prose) if abs_plain else prose
    allow = {"IEEE", "ACM", "USA", "UK", "EU", "II", "III", "IV", "VI", "VII", "VIII", "IX", "XI", "AND", "OR", "NOT", "RQ", "RQ1", "RQ2", "RQ3", "RQ4", "SP"}
    seen, undefined = set(), []
    for m in re.finditer(r"\b([A-Z][A-Z0-9]{1,7}|i[A-Z]{2,}|[A-Z]{1,3}[a-z]?[A-Z]{1,4})s?\b", prose):
        ac = m.group(1)
        if ac in seen or ac in allow or not re.search(r"[A-Z]{2}", ac): continue
        seen.add(ac)
        before, after = prose[max(0, m.start() - 90):m.start()], prose[m.end():m.end() + 80]
        forward = before.rstrip().endswith("(") and len(before.split()) >= 2
        reverse = bool(re.match(r"\s*\(([A-Za-z][^()]{5,70})\)", after)) and len(re.match(r"\s*\(([^()]+)\)", after).group(1).split()) >= 2
        if not (forward or reverse): undefined.append(ac)
    add("AC1", "Acronyms", "PASS" if not undefined else ("WARN" if len(undefined) < 3 else "FAIL"),
        "Every acronym defined on first use (e.g. digital forensics (DF))",
        ("first use not a definition: " + ", ".join(undefined)) if undefined else "all acronyms appear defined", G + " §3 Acronyms",
        "Heuristic - verify each flagged acronym; proper-name bodies (IEEE, ACM) are tolerated" if undefined else "")

    # ---- 7. writing style -------------------------------------------------------
    fp = re.findall(r"\b(I|my|me|we|our|us)\b", prose)
    add("W1", "Writing", "PASS" if not fp else "WARN", "Formal third-person English (avoid I/we/our)",
        "%d first-person tokens%s" % (len(fp), (": " + ", ".join(sorted(set(fp)))) if fp else ""), G + " §7 Writing guidance")
    cont = re.findall(r"\b\w+n't\b|\b\w+'(?:re|ve|ll)\b", prose)
    if cont: add("W2", "Writing", "WARN", "No informal contractions", "%d found: %s" % (len(cont), ", ".join(sorted(set(cont))[:8])), G + " §7")
    quotes = re.findall(r"``(.*?)''|\\enquote\{(.*?)\}|(?<![\w\\])\"([^\"]{3,}?)\"", body, re.S)
    qlens = [wcount(to_plain(next(x for x in q if x))) for q in quotes]
    st = "PASS" if (len(qlens) <= 5 and all(l <= 25 for l in qlens)) else "WARN"
    add("W3", "Plagiarism", st, "Direct quotes are rare and short; everything else paraphrased and cited",
        "%d quoted passages, longest %d words" % (len(qlens), max(qlens) if qlens else 0), G + " §6 Plagiarism")
    # long uncited paragraphs
    paras = [p for p in re.split(r"\n\s*\n", drop_envs(nobib, ENV_DROP)) if wcount(to_plain(p)) > 90]
    uncited = [p for p in paras if not cite_re.search(p)]
    if uncited:
        lines_u = [line_of(boff + body.find(p[:40])) for p in uncited[:6]]
        add("W4", "Plagiarism", "WARN", "Every idea that is not yours has a citation (long paragraphs without any citation)",
            "%d paragraphs >90 words with no \\cite, e.g. at %s" % (len(uncited), ", ".join(lines_u)), G + " §6 Plagiarism",
            "A review paper is normally citation-dense; check these paragraphs (own analysis is fine, but say so)")

    # ---- 8. review-paper methodology / content ----------------------------------
    low = prose.lower()
    sec = lambda k: " ".join(s["plain"] for s in present.get(k, [])).lower()
    def has(rx, text=low): return bool(re.search(rx, text, re.I))
    def det(fid, cat, req, ok, ev, src, hint="", missing_status="WARN", where=""):
        add(fid, cat, "PASS" if ok else missing_status, req, ev if ok else "not detected" + (" (" + where + ")" if where else ""), src, hint if not ok else "")

    rq = sorted(set(re.findall(r"\bRQ\s?([1-9])\b", prose)))
    add("M1", "Review method", "PASS" if len(rq) >= 3 else ("WARN" if has(r"research question|review question|RQ") else "FAIL"),
        "A focused, bounded review question; " + T["rq_text"],
        "RQ labels found: %s" % (", ".join("RQ" + x for x in rq) or "none"), G + " §2.1; " + HT + " RQ1-3")
    det("M2", "Review method", "Scope stated (what is in / out of the review)", has(r"\bscope\b|in[- ]scope|out[- ]of[- ]scope|scoping"), "scope wording found", G + " §2.1 Methodology")
    dbs = T["dbs"]
    got = [n for n, rx in dbs.items() if has(rx)]
    add("M3", "Review method", "PASS" if len(got) >= T["db_need"] else ("WARN" if len(got) >= 3 else "FAIL"),
        "Search strategy names the databases (Handbook: " + T["db_text"] + ")",
        "named: %s; missing: %s" % (", ".join(got) or "-", ", ".join(n for n in dbs if n not in got) or "-"), G + " §2.1; " + HT + " protocol")
    terms = [t for t in T["string_terms"] if t in low]
    boolean = bool(re.search(r"\bAND\b", body)) and bool(re.search(r"\bOR\b", body))
    add("M4", "Review method", "PASS" if boolean and len(terms) >= T["string_need"] else "WARN", "Reproducible search string with Boolean operators (Handbook string: " + T["string_text"] + ")",
        "boolean AND/OR %s; string terms seen: %d/%d" % ("present" if boolean else "absent", len(terms), len(T["string_terms"])), G + " §2.1; " + HT + " protocol",
        "Print the exact string(s) per database (verbatim/lstlisting) so another student can reproduce")
    win = re.search(T["window"][0] + r"\s*(?:--|–|-|to|and|through)\s*" + T["window"][1], prose + body)
    add("M5", "Review method", "PASS" if win else "WARN", "Time window stated (Handbook: %s-%s)" % T["window"], "window %s" % (win.group(0) if win else "not found"), HT + " protocol")
    inc, exc = has(r"\binclusion\b"), has(r"\bexclusion\b")
    add("M6", "Review method", "PASS" if inc and exc else ("WARN" if inc or exc else "FAIL"),
        "Explicit inclusion AND exclusion criteria (recency, venue quality, peer review)", "inclusion=%s exclusion=%s" % (inc, exc), G + " §2.1; " + H + " Review track")
    pr = has(r"prisma"); nums = len(re.findall(r"\b(?:identified|screened|eligible|included|excluded|retrieved|duplicates?)\b", low))
    flowfig = any(re.search(r"prisma|flow|selection|screening", (e["caption"] + e["raw"]), re.I) for e in envs)
    add("M7", "Review method", "PASS" if pr and flowfig and nums >= 4 else ("WARN" if pr or flowfig else "FAIL"),
        "PRISMA-style selection flow (identified > screened > eligible > included) with counts", "PRISMA word=%s; flow float=%s; stage words=%d" % (pr, flowfig, nums), HT + " Review track")
    cs = re.search(r"(\d{1,3})\s+(?:primary\s+)?(?:studies|papers|articles|publications)\s+(?:were\s+)?(?:included|selected|retained|analy[sz]ed)|corpus of (\d+)|final (?:set|corpus|sample) of (\d+)", prose, re.I)
    add("M8", "Review method", "PASS" if cs else "WARN", "Justified corpus size (number of included studies stated and justified)", "found: %s" % (cs.group(0) if cs else "none"), H + " Review track")
    det("M9", "Review method", "Structured taxonomy of artefacts/apps", has(r"taxonom"), "taxonomy wording found", HT + " Synthesis")
    det("M10", "Review method", "Quality appraisal of included studies (criteria/rubric/risk of bias)", has(r"quality (assessment|appraisal|criteria)|critical appraisal|risk of bias|appraisal|rubric|quality score"), "appraisal wording found", H + " Review track", "", "FAIL")
    gaps = len(re.findall(r"\bgaps?\b", low))
    add("M11", "Review content", "PASS" if gaps >= 3 and has(r"open (problems|challenges|questions)|research agenda|future (work|research|directions)") else "WARN",
        "Explicit, evidence-based gap analysis and open problems", "'gap' x%d; open-problems/agenda wording: %s" % (gaps, has(r"open (problems|challenges|questions)|research agenda")), G + " §2.1; " + H + " Review track")
    det("M12", "Review content", "Discussion of scope, bias and limitations of the review itself", has(r"limitation") and has(r"bias|threats? to validity|selection bias|publication bias"), "limitations + bias wording found", H + " Review track; " + G + " §4 V", "", "FAIL")
    ant_all = has(r"anticipated outcome|expected outcome|anticipated|expected contribution|was expected|expected to")
    ant_res = bool(re.search(r"anticipat|expected", sec("results") + " " + sec("conclusion"), re.I))
    add("M13", "Review content", "PASS" if ant_all and ant_res else "WARN", "Anticipated outcomes stated and, in the final paper, compared with actual findings (Results)",
        "anticipated/expected wording anywhere=%s; in Results/Conclusion=%s" % (ant_all, ant_res), G + " §2.1 & §4 V")
    prior = has(r"(previous|prior|existing|earlier|recent) (surveys?|reviews?|slr|systematic)") 
    add("M14", "Review content", "PASS" if prior else "WARN", "Results compared with prior work / existing surveys; contribution beyond them stated", "prior-review wording %s" % ("found" if prior else "absent"), G + " §4 V")
    intro = sec("intro")
    for fid, req, rx, hint in [("I1", "Introduction states the objective(s)/research questions", r"objective|research question|\bRQ|aim of|this (paper|review|survey) (aims|examines|investigates|reviews)", ""),
                               ("I2", "Introduction states the contribution(s)", r"contribution", ""),
                               ("I3", "Introduction ends with one sentence on how the paper is organised", r"organi[sz]ed|remainder of|rest of (this|the) paper|section\s+(ii|2)|is structured", "")]:
        det(fid, "Introduction", req, has(rx, intro), "found in Introduction", G + " §4 I", hint, where="Introduction")
    newc = [k for k in order_keys if cite_pos.get(k, 0) and any(cite_pos[k] >= body.find(s["raw"][:50]) >= 0 and s["key"] == "conclusion" and cite_pos[k] < body.find(s["raw"][:50]) + len(s["raw"]) for s in secs)]
    if newc: add("I4", "Conclusion", "WARN", "Conclusion contains no new information (no first-time citations)", "first cited in Conclusion: " + ", ".join(newc), G + " §4 VI")
    det("I5", "Conclusion", "Conclusion has future work / next steps", has(r"future (work|research|direction)|next steps|should be done", sec("conclusion")), "future-work wording found", G + " §4 VI", where="Conclusion")
    det("I6", "Results", "Limitations discussed (Results & Discussion)", has(r"limitation", sec("results") + " " + " ".join(" ".join(s["subs"]) for s in present.get("results", [])).lower()), "limitation wording found", G + " §4 V", where="Results & Discussion")

    # ---- 9. Topic coverage -----------------------------------------------------
    cov = [(fid, req, rxs, need, HT) for fid, req, rxs, need in T["cov"]]
    sid, sreq, srx = T["standards_std"]
    cov.append((sid, sreq, [srx], 1, HT + " references"))
    for fid, req, rxs, need, src in cov:
        hit = [r for r in rxs if has(r)]
        add(fid, "Topic coverage", "PASS" if len(hit) >= need else ("WARN" if hit else "FAIL"), req, "%d/%d indicators found" % (len(hit), len(rxs)), src)

    # ---- 10. manual items -----------------------------------------------------------
    for fid, req, src in [
        ("X1", "Similarity index < 20% (Turnitin / SafeAssign) - cannot be measured here", G + " §6 Plagiarism"),
        ("X3", "Sources were actually read (no citing unread papers); no fabricated findings in the comparison table", G + " §6 Also prohibited"),
        ("X4", "Venue quality of cited sources (Q1/Q2 by JCR/SJR, CORE A/B), indexing in Scopus/WoS, no predatory journals", G + " §5.1"),
        ("X5", "Comparison-table cell values are true to the cited primary studies (spot-check 3-5 rows)", H + " Review track"),
        ("X6", "Paper is original synthesis, not a list of summaries: grouped by theme, compared, critiqued", G + " §1, §2.1"),
        ("X7", "Not a re-submission of earlier work (self-plagiarism); topic locked with the instructor (one student per topic)", G + " §6, §1"),
    ]:
        add(fid, "Manual", "MANUAL", req, "verify by hand", src)

    # ---------------------------------------------------------------------------- output
    summary = OrderedDict((s, sum(1 for f in FINDINGS if f["status"] == s)) for s in ["PASS", "WARN", "FAIL", "MANUAL", "INFO"])
    meta = OrderedDict(main_file=os.path.relpath(mainf, root), stage=a.stage, year=a.year, track="Review (Type A / Track A)", topic=a.topic, topic_name=T["name"],
                       body_words=total, body_words_with_abstract=total_with_abs, references=n_refs,
                       sections=[OrderedDict(title=s["title"], class_=s["key"], words=s["words"], line=s["line"]) for s in secs])
    if a.format == "json":
        out = json.dumps(OrderedDict(meta=meta, summary=summary, findings=FINDINGS), indent=2, ensure_ascii=False)
    else:
        L = ["# CS616 review-paper pre-check - " + T["name"], "", "- main file: `%s` | stage: %s | body words: %d (+abstract %d) | references: %d" % (
            meta["main_file"], a.stage, total, total_with_abs, n_refs),
             "- **%s**" % " | ".join("%s %d" % (k, v) for k, v in summary.items()), "",
             "| Sec. | Words | Line |", "|---|---:|---|"]
        L += ["| %s (%s) | %d | %s |" % (s["title"], s["key"], s["words"], s["line"]) for s in secs]
        cat = None
        for f in FINDINGS:
            if f["category"] != cat: cat = f["category"]; L += ["", "## " + cat, "", "| ID | Status | Requirement | Evidence | Source |", "|---|---|---|---|---|"]
            L.append("| %s | **%s** | %s | %s%s | %s |" % (f["id"], f["status"], f["requirement"], f["evidence"].replace("|", "/"),
                                                         (" - _%s_" % f["hint"]) if f["hint"] else "", f["source"]))
        out = "\n".join(L) + "\n"
    if a.out: open(a.out, "w", encoding="utf-8").write(out)
    else: sys.stdout.write(out)
    sys.exit(1 if summary["FAIL"] else 0)

if __name__ == "__main__":
    main()
