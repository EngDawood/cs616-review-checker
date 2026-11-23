CS 616 — Digital Crime and Forensics

Research Paper — Guidelines

# CS 616 — Digital Crime and Forensics

Research Paper — Guidelines & Structure

How to plan, write, reference, and submit your paper. Your instructor will discuss each part in class.

At a glance. The research paper is an individual piece of work (worth 15% of the course). You will write it in IEEE two-column format, roughly 5,000–6,000 words excluding references (±10%; your instructor will confirm the exact count). You may write either a review paper or an implementation / experimental paper (see §2). The similarity score must be below 20%, and the work must be your own — not AI-generated (§7). Read this whole guide before you start.

# 1. Purpose of the paper

The paper trains you to do what forensic professionals and researchers do: take a current problem, investigate what is known, add your own careful analysis (or your own experiment), and communicate it clearly and honestly. It is not a summary of what you read — it must show your thinking. Choose a topic from the list posted in the Blackboard Content folder; each topic may be taken by only one student across both sections.

# 2. Two types of paper — choose one

# 2.1 Type A — Review (survey) paper

A critical review that synthesises recent research on a topic — not a list of summaries. You define a focused question, gather and read the key recent work, group it by theme, compare and critique it, and identify the gaps and open problems.

- Methodology (how you do it): state your scope; describe your search strategy (which databases and search terms); state inclusion criteria (recency, venue quality); then synthesise thematically. Include at least one comparison table (approach vs. dataset vs. results vs. limitations).
- Anticipated outcomes: at the proposal stage, state what your review is expected to establish — e.g. “a structured comparison of X approaches and an identified gap in Y.”

# 2.2 Type B — Implementation / experimental paper

You build, reproduce, or experiment with a technique or tool (e.g. reproduce a detection method, test a forensic tool on a dataset, or implement a small artefact), then evaluate it and report the results.

- Methodology (how you do it): state your objective or hypothesis; describe the dataset, tools, and experimental setup in enough detail that another student could reproduce it; define your evaluation metrics (e.g. accuracy, precision/recall, time, false-positive rate); and compare against a baseline where possible.
- Anticipated outcomes: at the proposal stage, state the results you expect and how you will measure success (the metrics and the target). In the final paper, report the actual results against those expectations.

Either way: the paper must contain original analysis, a clear methodology, and a discussion of results/findings, limitations, and future work.

# 3. Format

- Template: the standard IEEE conference (two-column) format. Use the official template — do not invent your own layout.
  - IEEE templates (Word & LaTeX): ieee.org/conferences/publishing/templates.html
  - IEEE template selector: template-selector.ieee.org
  - Ready-to-use on Overleaf (LaTeX, IEEEtran): overleaf.com/gallery/tagged/ieee-official
- Length: ~5,000–6,000 words excluding the reference list, tables, figures, and appendices (±10%).
- Figures & tables: numbered, captioned, and referred to in the text (“as Fig. 2 shows…”). Do

1 of 3

CS 616 — Digital Crime and Forensics

Research Paper — Guidelines

not paste screenshots without explanation.

- **Acronyms:** define every acronym on first use, e.g. “digital forensics (DF).”

#### 4. Structure of the paper (section by section)

Follow this order. The word figures are a rough guide for a ~5,500-word paper.

- **Title** — specific and informative (not “Digital Forensics”).
- **Abstract** (~150–250 words) — the problem, your approach, and the single most important result/finding. Written last.
- **Index Terms / Keywords** — 4–6 terms.
- **I. Introduction** (~600–800) — the context and why it matters; the problem; your *objective(s)* or research question(s); your *contribution*; and one sentence on how the paper is organised.
- **II. Background / Related Work** (~1,000–1,400) — the literature review: what others have done, *grouped by theme and critiqued*, ending with the **gap** your paper addresses. (This is the heart of a Type A paper.)
- **III. Methodology / Approach** (~800–1,200) — exactly how you did the review or the experiment (see §2). Must be reproducible.
- **IV. Implementation / Analysis** (~1,000–1,400) — what you built or analysed; design decisions; the comparison table.
- **V. Results & Discussion** (~700–1,000) — the findings, *interpreted* (not just reported); comparison with the anticipated outcomes and with prior work; then **limitations**.
- **VI. Conclusion & Future Work** (~250–350) — what you found, why it matters, and what should be done next. No new information here.
- **References** — IEEE numbered style (see §6).
- **Appendices** (optional) — extra data, code listings, or full tables.

#### 5. References — choosing and citing sources

##### 5.1 What to cite (quality first)

Use recent, peer-reviewed, high-quality sources:

- **Recency:** favour work from the **last ~5 years**; older papers only for foundational ideas.
- **Venue quality:** **top journals** (e.g. IEEE Transactions, ACM, Elsevier/Springer forensic & security journals — ideally **Q1/Q2** by JCR/SJR) and **top conferences** (e.g. IEEE S&P, USENIX Security, ACM CCS, NDSS, and forensics venues such as DFRWS — ideally **CORE A/B**).
- **Also acceptable:** reputable **PhD/MSc theses, standards** (NIST, ISO/IEC), and well-regarded **books**.
- **How to judge a source:** is it peer-reviewed? indexed in **Scopus / Web of Science**? reasonably cited? from a known publisher (not a *predatory* journal)?
- **Minimum:** at least **15 references**, the majority peer-reviewed and recent.
- **Avoid** as primary sources: blogs, Wikipedia, vendor marketing, undated web pages, and predatory or non-reviewed venues. (Standards and government/primary sites are fine.)

##### 5.2 Where to search

IEEE Xplore, ACM Digital Library, ScienceDirect, SpringerLink, Google Scholar, and Scopus. Use a **reference manager** to collect and format citations: Zotero (free) or Mendeley.

##### 5.3 How to cite (IEEE style)

IEEE uses **numbered** citations in order of appearance: “...as shown in [3].” Each number maps to one entry in the reference list; every reference must be cited in the text, and every citation must appear in the list. Follow the IEEE reference format (author initials, title, venue, year, pages/DOI). See the IEEE Author Center for the reference guide.

2 of 3

CS 616 — Digital Crime and Forensics

Research Paper — Guidelines

## 6. Academic integrity — read carefully

- **Plagiarism:** presenting others' words or ideas as your own. **Paraphrase** in your own words *and cite the source*; use **quotation marks** for the rare direct quote (keep quotes short and few). Every idea that is not yours needs a citation.
- **Similarity limit:** your submission will be checked (e.g. Turnitin/SafeAssign). The similarity index must be **below 20%**. High similarity — even if cited — signals over-quoting or poor paraphrasing; rewrite in your own words.
- **No AI-generated work:** text produced by an AI tool and submitted as your own is an **integrity violation**, treated the same as plagiarism. The analysis and the writing must be yours. (Your instructor will state the exact policy on any permitted use, e.g. for grammar checking only.)
- **Also prohibited:** fabricating data or results; citing sources you did not read; and re-submitting your own past work (self-plagiarism).

## 7. Writing guidance (for first-time authors)

- Write in **formal, precise, third-person** English; short, clear sentences beat long ones.
- **One idea per paragraph**, opened by a topic sentence; make the logic flow from section to section.
- Support claims with evidence and **citations**, not opinion.
- Draft the body first, then the **Introduction**, then the **Abstract** last.
- Leave time to **proofread**, run the similarity check, and fix the IEEE formatting before the deadline.
- If you have never written a paper: start from the section structure in §5, put your points as bullets under each heading, then turn each bullet into sentences. Bring your outline to your instructor early.

## 8. Milestones

|  **Week 5** | Browse the topic list (Blackboard *Content* folder) and **select your topic**; coordinate in the section WhatsApp group so there are no duplicates across both sections.  |
| --- | --- |
|  **Week 6** | **Finalise** your topic (locked, no duplicates).  |
|  **Week 7** | **Methods & evaluation:** develop and refine your **methodology** and your **evaluation plan** (discussed in class), ready to feed into your proposal.  |
|  **Week 8** | **Proposal / outline due:** topic, objective/questions, chosen type (A or B), **anticipated outcomes**, 3–5 key references, and a section outline.  |
|  **Week 9** | **Draft due** — a substantial working draft, for feedback.  |
|  **Week 13** | **Final paper due** (IEEE format, similarity <20%).  |
|  **Week 14** | **Presentation** of your paper.  |

## 9. What makes a strong paper

A clear, focused question; genuine synthesis or a reproducible experiment (not a summary); recent, high-quality references; honest discussion of limitations and anticipated vs. actual outcomes; correct IEEE format; original writing with a low similarity score. Aim for these, not just the word count.

## 10. Checklist before you submit

☐ IEEE two-column template used; length within range.
☐ All sections present (Abstract → Conclusion → References).
☐ Type A or B methodology clearly described and reproducible.
☐ Anticipated outcomes stated (and, in the final, compared to actual).
☐ ≥15 references, recent and peer-reviewed; all cited in text; IEEE numbering.
☐ Every acronym defined; every figure/table captioned and referenced.
☐ Paraphrased and cited; similarity <20%; your own work (no AI-generated text).
☐ Proofread.

3 of 3
