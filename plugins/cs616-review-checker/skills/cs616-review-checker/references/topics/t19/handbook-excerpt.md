# CS 616 — Research Topics: Two-Track Handbook (excerpt: Review track standard + Topic 19)

> Auto-extracted from the course PDF (text layer; glyph-level fixes applied for ligatures/dashes). Tables/layout may differ from the PDF — the PDF is the authority.

<!-- page 1 -->
CS 616 — Digital Crime and Forensics
Research Topics — Two-Track Handbook
CS 616 — Digital Crime and Forensics
Research Paper Topics — Two-Track Proposals
Consolidated handbook — all 28 topics, two tracks each, with verified references.
The two tracks (choose one).

▶
Review track — Systematic Review. A protocol-driven critical review, not a narrative summary.
Minimum standard: a bounded review question; a documented, reproducible search protocol (databases,
search strings, inclusion/exclusion, time window); a PRISMA-style selection flow; a justified corpus size; a
structured taxonomy and comparison matrix; quality appraisal of the included studies; an explicit evidencebased gap analysis; and discussion of scope, bias and limitations.

▶
Practical track — Experimental Contribution.
Minimum standard:
a precise research question/hypothesis and an identified gap; a leakage-resistant train/validation/test design; ≥2 baselines including a simple interpretable one; task-appropriate metrics beyond accuracy, with confidence intervals
and effect sizes; ablation, robustness or distribution-shift testing plus structured error analysis; repeated
runs with documented seeds and statistical tests at the correct unit; a reproducible package; and an
ethics/authorization/dual-use statement.
Reference policy. Peer-reviewed work, official standards, official datasets and primary legal sources are
prioritised. Preprints, theses, software and proposed rules are labelled as such. Students re-verify (recording
access dates) before submission.



## Topic 19 — Version- and State-Robust Forensics of Encrypted Messaging Applications
Research problem.
Extracting messages from one SQLite database is routine.
A research paper should measure which artifacts survive application versions, device security states, deletion and
WAL/checkpoint behaviour.

▶Track A — Systematic Review: Forensics of Secure/Encrypted Messaging Applications
Review questions.
RQ1. Which artifacts and storage locations are documented across secure messengers (device DBs,
backups, key stores)?
RQ2. How is recoverability evaluated across app versions, BFU/AFU states, deletion and backup/update
behaviour?
RQ3. What legal routes exist to cloud data, and where are the methodological gaps?
Scope & search protocol. Databases as above. String: (forensic*) AND (Signal OR Telegram
OR WhatsApp OR "instant messag*" OR "secure messag*") AND (Android OR iOS OR artefact*).
Window 2014–2026. PRISMA-style flow.
Synthesis & appraisal. Taxonomy of artefacts/apps; matrix (app, version, state, artefacts recovered, deletion recovery); appraise version/state coverage; map gaps.

▶Expected contribution. A synthesis of what is recoverable under encryption, acquisition state
and app evolution, exposing where prior single-version studies no longer hold.

▶Track B — Practical / Experimental Contribution
Research gap. Measure artifact survival across app versions, device states, deletion and WAL/checkpoint
behaviour for one messenger.
Research questions. (i) Which artifacts persist across app versions and backup states? (ii) How do
before/after-first-unlock states change accessible evidence? (iii) What can be recovered after deletion,
logout or database maintenance?
Proposed design. Researcher-owned devices/accounts and synthetic conversations; one messenger,
≥2 versions; capture logical backups, app sandboxes and permitted device images at controlled states;
document databases, WAL/SHM, caches, media, notifications, keystores and cloud exports; repeat
send/edit/delete/reaction/attachment events with known times; compare ≥2 tools or a tool against
manual parsing; validate every claimed artifact.
Evaluation & minimum evidence. Event/artifact recall, timestamp error, deleted-item recovery,
parser agreement, version survival, false-attribution rate, reproducibility; ≥2 baselines; robustness +
≥1 ablation; confidence intervals; reproducibility package. Ethics: researcher-owned accounts/devices
only.

▶Expected contribution & level. A versioned artifact-survival matrix and validation dataset for
one encrypted messenger, with explicit acquisition-state limits. Master's-appropriate; strong workshop/appliedconference potential. Publication possible, not guaranteed.
References (verified; source type labelled)
[1] A. R. Onik, J. Brown, C. Walker, and I. Baggili, “A systematic literature review of secure instant
messaging applications from a digital forensics perspective,” ACM Computing Surveys, vol. 57,
no. 9, 2025, doi:10.1145/3727641. (journal — systematic review)
[2] C. Anglano, “Forensic analysis of WhatsApp Messenger on Android smartphones,” Digital Investigation, vol. 11, no. 3, pp. 201–213, 2014. (journal — seminal)
[3] C. Anglano, M. Canonico, and M. Guazzone, “Forensic analysis of Telegram Messenger on Android
smartphones,” Digital Investigation, vol. 23, 2017. (journal — seminal)
[4] N. Rathi, U. Karabiyik, T. Aderibigbe, and H. Chi, “Forensic analysis of encrypted instant messaging applications on Android,” in Proc. Int. Symp. Digital Forensics and Security (ISDFS), 2018.
(conference)
[5] NIST SP 800-101 Rev. 1, Guidelines on Mobile Device Forensics, 2014. (standards-body publication)
16 of 30


<!-- page 17 -->
CS 616 — Digital Crime and Forensics
Research Topics — Two-Track Handbook
