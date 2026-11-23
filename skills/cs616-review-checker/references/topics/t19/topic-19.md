# Topic 19 — Version- and State-Robust Forensics of Encrypted Messaging Applications
*(Course catalogue name: "Mobile Forensics of Encrypted Messengers", catalogue topic 19 — the Handbook title above is the narrowed version; narrowing a topic is allowed by agreement with the instructor.)*
Source: CS616 Two-Track Handbook, pp. 16–17 · Track A (Review) only.

**Research problem.** Extracting messages from one SQLite database is routine. A research paper should measure which artifacts survive **application versions, device security states, deletion and WAL/checkpoint behaviour**.

## Track A — Systematic Review: Forensics of Secure/Encrypted Messaging Applications
**Review questions**
- **RQ1.** Which artifacts and storage locations are documented across secure messengers (device DBs, backups, key stores)?
- **RQ2.** How is recoverability evaluated across app versions, BFU/AFU states, deletion and backup/update behaviour?
- **RQ3.** What legal routes exist to cloud data, and where are the methodological gaps?

**Scope & search protocol.** Databases: IEEE Xplore, ACM DL, ScienceDirect, Scopus, Google Scholar ("Databases as above"). String:
`(forensic*) AND (Signal OR Telegram OR WhatsApp OR "instant messag*" OR "secure messag*") AND (Android OR iOS OR artefact*)`. Window **2014–2026**. **PRISMA-style flow.**

**Synthesis & appraisal.** Taxonomy of artefacts/apps; matrix (**app, version, state, artefacts recovered, deletion recovery**); appraise version/state coverage; map gaps.

**Expected contribution.** A synthesis of what is recoverable under encryption, acquisition state and app evolution, exposing where prior **single-version studies no longer hold**.

**Handbook references (verified):**
1. A. R. Onik, J. Brown, C. Walker, I. Baggili, "A systematic literature review of secure instant messaging applications from a digital forensics perspective," *ACM Computing Surveys*, vol. 57, no. 9, 2025, doi:10.1145/3727641 (journal — systematic review).
2. C. Anglano, "Forensic analysis of WhatsApp Messenger on Android smartphones," *Digital Investigation*, vol. 11, no. 3, pp. 201–213, 2014 (seminal).
3. C. Anglano, M. Canonico, M. Guazzone, "Forensic analysis of Telegram Messenger on Android smartphones," *Digital Investigation*, vol. 23, 2017 (seminal).
4. N. Rathi, U. Karabiyik, T. Aderibigbe, H. Chi, "Forensic analysis of encrypted instant messaging applications on Android," *Proc. ISDFS*, 2018.
5. NIST SP 800-101 Rev. 1, *Guidelines on Mobile Device Forensics*, 2014.

## What the checker looks for (Topic 19)
- Title names forensics + encrypted/secure messaging apps.
- RQ1–RQ3 stated **and answered** in the analysis/discussion.
- Search string reproducing the Handbook string (or a justified variant), five databases, window 2014–2026.
- Comparison matrix with columns for **app · version · state (BFU/AFU) · artefacts recovered · deletion recovery**.
- Coverage: Signal/Telegram/WhatsApp · Android/iOS · device DBs, backups, key stores, caches, media · BFU/AFU · app versions & updates · deletion, WAL/SHM, checkpoint, vacuum · cloud exports · legal routes (warrants, MLAT, jurisdiction) · E2EE/SQLCipher/keystore · NIST SP 800-101.
- Positions itself against **Onik et al. 2025** (an SLR on the same subject already exists) and states what it adds.
- Shows where **single-version studies no longer hold** (the expected contribution).
