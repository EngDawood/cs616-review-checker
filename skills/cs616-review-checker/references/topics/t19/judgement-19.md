# Topic 19 — extra judgement checks (read the paper; verdict per item as in the common rubric)

| # | Check | MET when |
|---|---|---|
| T19-J1 | **Version-robustness is the lens** | The synthesis explicitly asks which artefacts survive across **app versions/updates**, and shows where results from one version no longer hold ("single-version" limits), rather than listing artefacts of one release |
| T19-J2 | **Acquisition state is explicit** | Findings are separated by **BFU vs AFU** (and logical/backup/full-file-system access where relevant); each claim says under which state it was observed |
| T19-J3 | **Deletion, WAL and maintenance** | Deleted-item recovery is discussed with the mechanism (WAL/SHM, checkpointing, vacuum, secure-delete, disappearing messages), not just "deleted messages can be recovered" |
| T19-J4 | **Encryption is handled correctly** | Distinguishes transport end-to-end encryption, encrypted-at-rest databases, key storage (keystore/keychain) and platform file-based encryption; no conflation |
| T19-J5 | **RQ1 answered** | A taxonomy of artefacts and storage locations (device DBs, backups, key stores, caches, media, notifications) tied to specific apps |
| T19-J6 | **RQ2 answered** | Shows *how recoverability was evaluated* in the reviewed studies (ground truth, synthetic conversations, tool vs manual parsing, timestamps) and comments on the weakness of those evaluations |
| T19-J7 | **RQ3 answered** | Legal routes to cloud data are described concretely (e.g. provider requests, warrants, mutual legal assistance, jurisdiction limits) and tied to what they yield vs device acquisition; methodological gaps listed separately |
| T19-J8 | **Matrix** | Rows = studies/apps; columns include app, version, state, artefacts recovered, deletion recovery; versions are real release identifiers where the source gives them |
| T19-J9 | **Contribution vs Onik et al. (2025)** | States what is added beyond that SLR (version/state/deletion lens, later window, legal routes) instead of repeating it |
| T19-J10 | **Platform balance** | Android and iOS both treated, or the restriction to one platform is declared and justified in the scope |
| T19-J11 | **Ethics/safety tone** | Describes acquisition methods at the level the literature does; no step-by-step guidance for bypassing device security or accessing someone else's account |
