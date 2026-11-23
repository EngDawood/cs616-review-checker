# Revision guidance (how to tell the student what to change)

Use this for the **"How to fix"** line of every FAIL/WARN and every NOT MET / PARTLY judgement item, and when the student asks "how do I fix X?".

## Boundary
Check mode gives **directions** (what, where, how to verify). Fix mode (see SKILL) may also **apply** them to a copy of the paper. In both modes never fabricate: no invented references or DOIs, search results, PRISMA counts, matrix cells, findings or quotes. If a fix needs real research or data the student has not supplied, leave a `% TODO(student): …` marker and say what is needed. Never overwrite the student's original files.

## How to phrase one suggestion
`[ID] where (file:line / section) → action → how to verify`. One action per suggestion, imperative, concrete. Say what is *missing or wrong*, not how it should read. Mark effort: quick (<10 min) / medium / heavy (needs more reading or searching).

## Script checks → fix directions

| ID | Fix direction | Effort |
|---|---|---|
| F1 | Start from the official IEEE conference template (`\documentclass[conference]{IEEEtran}`); move the content into it rather than restyling another class. | medium |
| F2 | Remove margin/spacing/font overrides (`geometry`, `\vspace` tricks, `\setlength`, font packages); fit length by editing content. | quick |
| F3 | Replace every template placeholder (sample author block, sample abstract/keywords, "Lorem", TODO/FIXME) with the paper's own; search the source for each marker the report lists. | quick |
| T1 / T2 | Title must name the topic's subject precisely and may signal a review; compare with the Handbook title of the chosen topic. Renaming/narrowing the topic needs the instructor's agreement. | quick |
| A1 | Count words of the abstract only; add or cut content until it is within 150–250. Write it last so it reflects the finished paper. | quick |
| A2 | Check the abstract carries three things: problem, review approach (databases, window, corpus size), the single most important finding; add the missing one. | medium |
| A3 | Remove `\cite` from the abstract; the claim stays, the citation moves to the body. | quick |
| K1 | Use 4–6 index terms in `IEEEkeywords`, specific to the paper (not generic words already in the title). | quick |
| L1 | Compare the prose word count with 5,000–6,000 (±10 %). Too long: cut repetition, merge overlapping subsections, move detail to tables. Too short: add the missing analysis the judgement table flags, not filler. Confirm the count with Overleaf Word Count. | medium |
| R1 | Use `\bibliographystyle{IEEEtran}` with a `.bib` (or numbered `thebibliography`); no author-year styles. | quick |
| R2 | Reach ≥ 15 references by adding sources actually read and used; do not pad. | heavy |
| R3 | For each missing key, add the entry to the `.bib` or fix the key typo in `\cite{}`. | quick |
| R4 | Cite each listed reference where it supports a claim, or remove it if unused. | quick |
| R5 | Numbering follows first appearance; with BibTeX this is automatic — check the style is `IEEEtran` and no `\nocite{*}` or manual numbers interfere. | quick |
| R6 / R7 | Raise the share of recent and/or peer-reviewed sources above 50 %: replace weak/old sources by searching the same databases used in the protocol (Scopus, IEEE Xplore, ACM DL, Web of Science …) within the window. | heavy |
| R8 | Replace each flagged blog/Wikipedia/forum source with the primary or peer-reviewed source it points to; if none exists, drop the claim. | medium |
| R9 | Keep vendor/app-maker pages only as clearly labelled primary technical sources, dated and accessed-on. | quick |
| R10 | Complete each flagged entry: authors, title, venue, year, volume/pages, DOI/URL, accessed date for web pages. | medium |
| R11 | Merge duplicate entries into one key and update citations. | quick |
| FT1 | Add a caption (IEEE: figure caption below, table caption above) to each flagged float. | quick |
| FT2 | Add `\label` right after `\caption`, and refer to every float in the text with `\ref`/Fig./Table, introducing what the reader should see. | quick |
| FT3 | Fix the `\ref` target name or add the missing `\label`; recompile twice. | quick |
| FT4 | Expand flagged captions so the float is understandable alone and the text explains its significance. | quick |
| FT5 / FT6 | Build/extend the comparison table with the topic's required columns (see `topic-N.md`); fill each cell from the cited study; explain any empty cell; use the table in the discussion. | heavy |
| AC1 | Define each acronym at first use (full form + acronym in parentheses), then use it consistently. | quick |
| W1 | Rewrite first-person passages in formal third person yourself (e.g. passive or "this review"). | quick |
| W2 | Remove contractions yourself. | quick |
| W3 | Re-read each long quoted passage against its source; keep only short, necessary quotes and paraphrase the rest in your own words with a citation. Run the similarity check (limit 20 %). | medium |
| W4 | For each long uncited paragraph, identify the source of each non-original idea and cite it; mark your own analysis as yours. | medium |
| M1 | State 3 clear research questions in the Introduction (Handbook RQ1–RQ3 of the topic) and answer each later. | medium |
| M3 | Name at least the required number of databases actually searched, per the topic profile. | medium |
| M4 | Print the exact Boolean string used per database (as run, not paraphrased) and keep it consistent with the Handbook's required terms. | medium |
| M5 | State the time window and keep it inside the Handbook window; apply it in the screening. | quick |
| M6 | List inclusion and exclusion criteria as separate, testable rules and show they were applied in the flow. | medium |
| M7 | Add a PRISMA-style flow figure and make every count add up (identified → screened → eligible → included); text and figure must agree. | medium |
| M8 | State the final number of included studies and why that number is justified. | quick |
| M11 | Add open problems / research agenda grounded in the gaps the matrix shows (≥ 3). | medium |
| M13 | State anticipated outcomes up front (methodology), then compare them with actual findings in Results. | medium |
| M14 | Name the existing surveys/SLRs on the topic and state precisely what this paper adds beyond them. | heavy |
| I4 | Move any first-time citation or new claim out of the Conclusion into the body; the Conclusion only summarises. | quick |

## Judgement items → improvement directions
Use the rubric's "NOT MET / PARTLY" signs to say *what is absent*, then pick the direction:

- **J1 Abstract** — list the three missing elements (problem / approach / key finding); redo the abstract last.
- **J2 Introduction** — check the sequence: context → problem → RQs → contribution → section map; add the missing link.
- **J3 Synthesis** — regroup the related-work paragraphs by theme; each paragraph compares ≥ 2 studies and says which finding is stronger and why.
- **J4 Gap** — derive the gap from a visible pattern in the matrix; revisit it in Results and Conclusion.
- **J5 Protocol** — walk the protocol with a checklist (databases, strings, window, criteria, screening steps, counts, size) and fill each missing item.
- **J6 Appraisal** — define the rubric criteria, score each included study, show the table, and use it when weighting evidence.
- **J7/J8 Matrix** — check columns against `topic-N.md`; re-verify 3–5 rows against the primary sources; fix every contradicted cell.
- **J9 RQs** — add a "RQ → answer → evidence" mapping in Results/Discussion; answer from the corpus, not opinion.
- **J10 Anticipated vs actual** — add the explicit comparison; say what matched and what did not.
- **J11 Positioning** — list prior reviews and the delta in coverage, method, or time window.
- **J12 Interpretation** — for each major result add the "why" and the "so what" for practitioners/investigators.
- **J13 Limitations** — separate limits of the review (search, language, database, selection, appraisal bias) from limits of the evidence.
- **J14 Conclusion** — remove new material; keep summary, importance, concrete next steps.
- **J15 Claims** — add a citation or mark as own analysis for each flagged claim; drop claims no source supports.
- **J16 Writing** — fix flow section by section: topic sentence, one idea per paragraph, consistent terms.
- **J17 Integrity signals** — never an accusation: recommend a similarity check and, if concerns remain, a conversation with the instructor; the student should be able to explain every sentence and source.
- **J18 Floats in context** — introduce and interpret each float; make the PRISMA figure match the protocol numbers.
- **Topic items (`judgement-N.md`)** — follow the "what is missing" column; point to the Handbook entry text in `handbook-excerpt.md`.

## Order of work (when proposing a revision plan)
1. Blocking FAILs that take minutes (F3, FT1–FT3, R1, R3–R5, K1, A1/A3).
2. Structural content (M1, M3–M8, FT5/FT6, J5–J9) — these decide whether the paper is a valid review.
3. Evidence quality (R2, R6–R10, J15) — reading and searching time.
4. Analysis depth (J3, J4, J10–J14, M11, M13, M14).
5. Language and polish (W1–W4, AC1, J16, J18), then compile twice, re-run the checker, and do the MANUAL items (similarity, venue quality, sources really read).
