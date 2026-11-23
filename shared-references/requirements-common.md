# Requirements common to every Type A (review / survey) paper — CS 616

Sources: **G** = *CS616 Research Paper Guidelines* · **H** = *CS616 Two-Track Handbook* (Review track = "Track A — Systematic Review").
`ID` = the row id in the checker's report (`check_paper.py`). **Auto** = measured by the script; **Read** = Claude must read the paper and judge; **Manual** = only the student/instructor can verify.

## 1. Format & length  (G §3)
| ID | Requirement | How |
|---|---|---|
| F1 | Official IEEE **conference, two-column** template (IEEEtran `[conference]`) — do not invent a layout | Auto |
| F2 | No layout hacks (geometry, fullpage, linespread, negative `\vspace`, font changes) | Auto |
| F3 | No leftover template text / TODO / placeholder author block | Auto |
| L1 | ~**5,000–6,000 words** excluding references, tables, figures, appendices (±10 % ⇒ 4,500–6,600). Instructor confirms exact count | Auto (approx.) |
| FT1–FT3 | Figures/tables **numbered, captioned, referred to in text** ("as Fig. 2 shows…"); no unexplained screenshots; no `??` refs | Auto |
| AC1 | **Every acronym defined on first use** — e.g. digital forensics (DF) | Auto + Read |

## 2. Structure, in this order  (G §4)
| ID | Section | Rough size | How |
|---|---|---|---|
| T1 | **Title** — specific & informative (not "Digital Forensics") | — | Auto |
| A1/A2 | **Abstract** 150–250 words: problem, approach, single most important finding; written last | 150–250 | Auto + Read |
| K1 | **Index Terms** 4–6 | 4–6 | Auto |
| S-intro, I1–I3 | **I. Introduction**: context & why it matters; the problem; objective(s)/research question(s); contribution; one sentence on paper organisation | 600–800 | Auto + Read |
| S-related | **II. Background / Related Work**: grouped **by theme**, critiqued, ending with the **gap** (heart of a Type A paper) | 1,000–1,400 | Auto + Read |
| S-method | **III. Methodology**: exactly how the review was done; reproducible | 800–1,200 | Auto + Read |
| S-analysis | **IV. Analysis**: the synthesis; design decisions; the comparison table | 1,000–1,400 | Auto + Read |
| S-results, I6 | **V. Results & Discussion**: findings interpreted (not just reported); compared with **anticipated outcomes** and **prior work**; then **limitations** | 700–1,000 | Auto + Read |
| S-conclusion, I4, I5 | **VI. Conclusion & Future Work**: what was found, why it matters, next steps; **no new information** | 250–350 | Auto + Read |
| S-refs | **References**, IEEE numbered style | — | Auto |
| S-order | Sections follow the order above | — | Auto |

## 3. Type A methodology  (G §2.1)
| ID | Requirement | How |
|---|---|---|
| M2 | State the **scope** | Auto + Read |
| M3, M4 | Describe the **search strategy**: which databases, which search terms/strings | Auto + Read |
| M6 | State **inclusion criteria** (recency, venue quality) — and exclusion criteria | Auto + Read |
| — | Then **synthesise thematically** (not a list of summaries) | Read / X6 |
| FT5 | At least **one comparison table** (approach vs dataset vs results vs limitations) | Auto + Read |
| M13 | **Anticipated outcomes** stated (proposal) and, in the final paper, **compared to actual** | Auto + Read |
| — | Original analysis, clear methodology, discussion of findings, **limitations and future work** | Read |

## 4. Systematic-review minimum standard  (H, "Review track")
A protocol-driven critical review, **not a narrative summary**:
| ID | Requirement | How |
|---|---|---|
| M1 | A **bounded review question** (RQ1–RQ3 of the topic) | Auto + Read |
| M3–M5 | **Documented, reproducible search protocol**: databases, search strings, inclusion/exclusion, time window | Auto + Read |
| M7 | **PRISMA-style selection flow** (identified → screened → eligible → included, with counts) | Auto + Read |
| M8 | **Justified corpus size** | Auto + Read |
| M9, FT6 | **Structured taxonomy and comparison matrix** (matrix columns are topic-specific) | Auto + Read |
| M10 | **Quality appraisal** of the included studies (criteria / rubric / risk of bias) | Auto + Read |
| M11 | **Explicit evidence-based gap analysis** | Auto + Read |
| M12 | **Scope, bias and limitations** of the review itself | Auto + Read |

## 5. References  (G §5)
| ID | Requirement | How |
|---|---|---|
| R2 | **≥ 15** references | Auto |
| R6 | **Majority peer-reviewed** (journals/conferences; theses, standards (NIST, ISO/IEC), well-regarded books also acceptable). Preprints/theses/software labelled as such (H reference policy) | Auto (proxy) + X4 |
| R7 | **Majority recent** (last ~5 years); older only for foundational ideas | Auto |
| R8, R9 | Avoid as primary sources: blogs, Wikipedia, vendor marketing, undated web pages, predatory/non-reviewed venues. Standards & government/primary sites are fine | Auto |
| R1, R5 | **IEEE numbered style**, numbers in order of first appearance | Auto |
| R3, R4 | **Every reference cited in text; every citation in the list** | Auto |
| R10 | IEEE entry format: author initials, title, venue, year, pages/DOI; **record access dates** for web sources (H) | Auto |
| X4 | Venue quality: JCR/SJR Q1/Q2, CORE A/B (IEEE S&P, USENIX Security, ACM CCS, NDSS, DFRWS); indexed in Scopus/WoS | Manual |

## 6. Integrity & writing  (G §6–§7)
| ID | Requirement | How |
|---|---|---|
| X1 | **Similarity index < 20 %** (Turnitin / SafeAssign) | Manual |
| X3 | No fabricated data/results, **no citing unread sources**, no self-plagiarism | Manual |
| W3, W4 | Paraphrase and cite every non-own idea; quotes short and few | Auto + Read |
| W1, W2 | Formal, precise, **third-person** English; one idea per paragraph with a topic sentence | Auto + Read |
| — | Proofread | Read |

## 7. Course milestones (context only)
Topic locked Week 6 · proposal/outline Week 8 (topic, objective/RQs, type, anticipated outcomes, 3–5 key references, outline) · substantial draft Week 9 · **final paper Week 13** (IEEE format, similarity < 20 %) · presentation Week 14.
> The Topic Catalogue PDF says the proposal is due in **Week 4**, the Guidelines say **Week 8** — confirm with the instructor.

## Status meanings in the report
**PASS** requirement met · **WARN** probable gap or heuristic doubt, verify · **FAIL** requirement not met · **MANUAL** cannot be machine-checked · **INFO** advisory.
