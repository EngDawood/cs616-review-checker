# Judgement rubric — the checks that need reading, not code

For each item give a verdict **MET / PARTLY / NOT MET / CAN'T TELL**, one line of evidence (section + file:line; quote at most ~12 words), and — if not MET — *what is missing*, never replacement text. Judge against what the paper actually says, not what it intends. When two readings are possible, take the stricter one and say so. CAN'T TELL is allowed (e.g. cited sources not accessible); never guess.

| # | Item | MET when | PARTLY / NOT MET signs |
|---|---|---|---|
| J1 | **Abstract** (G §4) | States the problem, the review approach (databases, window, corpus size) and the single most important finding, in ~150–250 words | Only describes the topic; no finding; findings vague ("results are discussed"); method missing; numbers contradict the body |
| J2 | **Introduction** (G §4 I) | Context + why it matters; a precise problem; explicit RQs/objectives; stated contribution; one sentence mapping the sections | Topic essay with no problem; RQs absent or different from those answered later; contribution = "we review the literature"; map sentence missing or wrong |
| J3 | **Synthesis, not summaries** (G §1, §2.1) | Related work/analysis is organised by themes; studies are compared against each other and critiqued (what holds, what doesn't, why) | "Author X did A. Author Y did B." chains; one paragraph per paper; no cross-paper comparison; no critique |
| J4 | **Gap** (G §4 II) | Ends with a specific, evidence-based gap that follows from the reviewed studies and that the paper then addresses | Gap is generic ("more research is needed"); gap not supported by the matrix; gap never revisited in Results/Conclusion |
| J5 | **Reproducible protocol** (G §2.1, H Review track) | Another student could repeat it: named databases, exact strings per database, time window, inclusion + exclusion criteria, screening steps, PRISMA counts that add up, corpus size and why it is justified | Strings paraphrased not printed; counts missing or inconsistent (e.g. included > screened); criteria not applied in the flow; corpus size arbitrary |
| J6 | **Quality appraisal** (H) | A stated rubric/criteria applied to the included studies, with results shown (table or summary) and used in the synthesis | Mentioned but never applied; no per-study result; appraisal ignored when drawing conclusions |
| J7 | **Taxonomy & matrix** (H, G §2.1) | Taxonomy has defensible dimensions; matrix columns are the topic's required ones; cells filled consistently; matrix actually used in the discussion | Columns missing; many empty or "N/A" cells with no explanation; taxonomy not used afterwards; rows contradict the text |
| J8 | **Matrix fidelity** (X5) | Spot-check 3–5 rows against the cited primary studies (if accessible): values match | Any value contradicted by its source; claims attributed to a study that does not make them; → report as potential fabrication risk, don't accuse |
| J9 | **RQs answered** (H) | Each RQ is answered explicitly in Results/Discussion, with evidence from the corpus (names the RQ or clearly maps to it) | RQ silently dropped; answered with opinion not evidence; answer contradicts the matrix |
| J10 | **Anticipated vs actual** (G §2.1, §4 V) | States what the review was expected to establish, then says whether and how the findings met, exceeded or missed it | Anticipated outcomes absent; or stated but never compared |
| J11 | **Positioning vs prior reviews** (G §4 V) | Names existing surveys/SLRs on the topic and states precisely what this paper adds | Claims novelty without naming prior reviews; contribution identical to an existing review |
| J12 | **Interpretation** (G §4 V) | Findings are interpreted (why, so what, implications), not just reported | Results restate the matrix in prose |
| J13 | **Limitations & bias** (H) | Limitations of the *review itself* (search, language, database, selection, publication, appraisal bias; threats to validity) + of the evidence | Only generic limitations; none about the review process |
| J14 | **Conclusion** (G §4 VI) | Summarises findings and why they matter; concrete next steps; no new facts, citations or claims | New results/citations appear; future work vague; repeats abstract verbatim |
| J15 | **Claims supported** (G §7) | Non-obvious claims carry citations; numbers have sources; opinion marked as the author's analysis | Strong claims with no support; citations that do not plausibly support the sentence |
| J16 | **Writing** (G §7) | Formal third person, one idea per paragraph with topic sentence, logical flow between sections, defined acronyms | Informal/first person; paragraphs that jump; heavy repetition; inconsistent terminology |
| J17 | **Integrity signals** (G §6) — *signals only, never an accusation* | Voice and detail are consistent; quotes short and marked | Very long near-verbatim passages; sudden style/level changes; generic filler with no specifics; citations that look invented (unknown venue, odd DOI) → recommend similarity check and discussion with the instructor |
| J18 | **Figures/tables in context** (G §3) | Each float is introduced and explained in the text; PRISMA figure matches the numbers in the protocol | Float never discussed; numbers differ between figure and text |

## How to report
- Put J-items in a table: `| J# | verdict | evidence | missing |`.
- A paper is **READY** only if: no script FAIL, no J-item NOT MET, and at most two J-items PARTLY (none of J1, J5, J9, J13). Say which items drive the verdict.
- Keep the MANUAL items (similarity, no AI text, sources read, venue quality) separate; they are never "met" by Claude's judgement.
