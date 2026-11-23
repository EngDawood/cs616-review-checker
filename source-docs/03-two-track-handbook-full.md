CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

## CS 616 — Digital Crime and Forensics

Research Paper Topics — Two-Track Proposals

Consolidated handbook — all 28 topics, two tracks each, with verified references.

The two tracks (choose one).

- ▶ **Review track — Systematic Review.** A protocol-driven critical review, not a narrative summary. *Minimum standard:* a bounded review question; a documented, reproducible search protocol (databases, search strings, inclusion/exclusion, time window); a PRISMA-style selection flow; a justified corpus size; a structured taxonomy and comparison matrix; quality appraisal of the included studies; an explicit evidence-based gap analysis; and discussion of scope, bias and limitations.
- ▶ **Practical track — Experimental Contribution.** *Minimum standard:* a precise research question/hypothesis and an identified gap; a leakage-resistant train/validation/test design; ≥2 baselines including a simple interpretable one; task-appropriate metrics beyond accuracy, with confidence intervals and effect sizes; ablation, robustness or distribution-shift testing plus structured error analysis; repeated runs with documented seeds and statistical tests at the correct unit; a reproducible package; and an ethics/authorization/dual-use statement.

**Reference policy.** Peer-reviewed work, official standards, official datasets and primary legal sources are prioritised. Preprints, theses, software and proposed rules are labelled as such. Students re-verify (recording access dates) before submission.

### Topic 1 — Distribution-Robust Ranking for Automated Digital-Evidence Triage

**Research problem.** Seizures now reach terabyte scale, yet examiners can inspect only a small review budget. Automated triage must *rank* artefacts so the most relevant surface first and stay reliable under class imbalance and case/source shift. A file classifier on a random split is a course exercise; the research problem is a *constrained ranking problem under distribution shift* with an examiner-workload objective.

#### ▶ Track A — Systematic Review: ML for Evidence Triage and Prioritisation

**Review questions.**

- RQ1. Which ML approaches have been proposed for evidence triage/prioritisation, and how do they group (content- vs metadata-based; classification vs ranking)?
- RQ2. How are they evaluated — datasets, splitting strategies, metrics — and how prevalent is leakage-prone (random-split) evaluation?
- RQ3. What evidence exists on robustness to class imbalance, case/source shift and review-budget constraints, and where are the gaps?

**Scope & search protocol.** Databases: IEEE Xplore, ACM DL, ScienceDirect, Scopus, Google Scholar. String: ("digital forensic*" OR evidence) AND (triage OR prioriti* OR ranking) AND ("machine learning" OR classif* OR "deep learning"). Window 2010–2026 with snowballing. Inclusion: peer-reviewed ML triage studies for digital forensics; exclusion: non-forensic triage, non-ML, non-peer-reviewed (except datasets/standards). Report a PRISMA-style flow.

**Synthesis & appraisal.** Taxonomy; comparison matrix (approach, features, dataset, split strategy, metrics, robustness tested, limitations); appraise leakage control, baselines and statistical rigour; map gaps.

- ▶ **Expected contribution.** A reproducible, critical synthesis that maps the field, exposes evaluation weaknesses (notably random-split leakage), and defines an evidence-based research agenda.

#### ▶ Track B — Practical / Experimental Contribution

**Research gap.** Evaluate triage as a constrained ranking problem under class imbalance and source shift with a fixed review budget — beyond a file classifier.

**Research questions.** (i) How much does random splitting overestimate performance versus case-/source-held-out evaluation? (ii) Which model gives the greatest relevant-evidence yield at fixed review budgets? (iii) How do calibration and abstention affect missed critical evidence and examiner workload?

1 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

**Proposed design.** Labelled public/synthetic corpus with case, source and duplicate groups; baselines = keyword/BM25, logistic regression or gradient boosting, one neural embedding; grouped and leave-one-source-out tests with simulated top-k budgets; ablate metadata/content/context; robustness to corrupted filenames, missing metadata, novel file types; blinded error review.

**Evaluation & minimum evidence.** PR-AUC, macro-F1, precision@k, recall@k, nDCG, calibration error, workload saved, critical-item miss rate; bootstrap by *case*; $\geq 2$ baselines; robustness + $\geq 1$ ablation; confidence intervals; reproducibility package.

► **Expected contribution & level.** A reproducible protocol quantifying the relevant-evidence-recall vs examiner-workload trade-off. Master's-appropriate; may support a workshop/applied-conference submission. *Publication possible, not guaranteed.*

**References** (verified; source type labelled)

[1] D. Dunsin, M. C. Ghanem, K. Ouazzane, and V. Vassilev, "A comprehensive analysis of the role of artificial intelligence and machine learning in modern digital forensics and incident response," *Forensic Science International: Digital Investigation*, vol. 48, art. 301675, 2024. (journal)
[2] D. Quick and K.-K. R. Choo, "Impacts of increasing volume of digital forensic data: A survey and future research challenges," *Digital Investigation*, vol. 11, no. 4, pp. 273–294, 2014. (journal)
[3] F. Marturana and S. Tacconi, "A machine learning-based triage methodology for automated categorization of digital media," *Digital Investigation*, vol. 10, no. 2, pp. 193–204, 2013. (journal — foundational)
[4] A. Jarrett and K.-K. R. Choo, "The impact of automation and artificial intelligence on digital forensics," *WIREs Forensic Science*, vol. 3, no. 6, e1418, 2021. (journal)
[5] I. Homem, *Advancing Automation in Digital Forensic Investigations*, Ph.D. dissertation, Stockholm University, Sweden, 2018. (PhD thesis)
[6] ISO/IEC 27043:2015, *Incident investigation principles and processes*. (international standard)

## Topic 2 — Temporal and Cross-Family Generalization in Static Malware Detection and Attribution

**Research problem.** Training a CNN on malware images or gradient boosting on a random EMBER subset is a standard ML assignment. A publishable study must examine *temporal drift, family leakage*, and the distinction between malware *detection* and family *attribution*.

► **Track A — Systematic Review: Deep Learning for Static Malware Detection and Family Attribution**

**Review questions.**

RQ1. Which input representations (bytes, opcodes, images, behaviour) and model families are used for static detection and attribution?
RQ2. What evaluation practices dominate — datasets, splitting (random vs temporal vs family-disjoint), metrics — and how often is temporal/family leakage controlled?
RQ3. What evidence exists on temporal drift, unseen-family generalisation, open-set attribution and adversarial robustness, and where are the gaps?

**Scope & search protocol.** Databases as above. String: malware AND ("deep learning" OR "machine learning") AND (detection OR classification OR attribution). Window 2015–2026 plus foundational works. Inclusion: peer-reviewed static-analysis ML studies; exclusion: dynamic-only or non-ML unless a baseline. PRISMA-style flow.

**Synthesis & appraisal.** Taxonomy of representations and models; matrix (dataset, split strategy, metrics, drift/family handling, robustness); appraise temporal/leakage control; map gaps.

► **Expected contribution.** A synthesis exposing how random, non-temporal, non-family-disjoint evaluation inflates reported generalisation, with a research agenda for drift-aware, open-set-aware evaluation.

2 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

# ▶ Track B — Practical / Experimental Contribution

Research gap. Evaluate detection and attribution under temporal and family-disjoint splits, and define when a model should abstain from attribution.

Research questions. (i) How much do random splits inflate performance versus temporal and family-disjoint splits? (ii) Which representation is most robust to packing, feature removal and unseen families? (iii) When should the model abstain from family attribution?

Proposed design. EMBER or SOREL-20M metadata with chronological splits; a manageable MalImg-style family subset as a secondary benchmark; baselines = PE-feature gradient boosting, byte-based neural embedding, a simple linear model; deduplicate by hash and family; hold out complete families and later periods; test packing indicators, stripped metadata, feature corruption (no operational-malware distribution); add open-set family rejection and calibration; error analysis by family size and period.

Evaluation & minimum evidence. Detection PR-AUC and TPR at low FPR; attribution macro-F1, open-set AUROC/OSCR, calibration, worst-family recall, temporal degradation; ≥2 baselines; robustness + ≥1 ablation; confidence intervals; reproducibility package.

▶ Expected contribution & level. Evidence on which representations generalise across time and unknown families, with a defensible abstaining-attribution protocol. Master's-appropriate; workshop/applied-conference potential. Publication possible, not guaranteed.

# References (verified; source type labelled)

[1] P. Maniriho, A. N. Mahmood, and M. J. M. Chowdhury, “A survey of recent advances in deep learning models for detecting malware in desktop and mobile platforms,” ACM Computing Surveys, vol. 56, no. 6, 2024. (journal — survey)

[2] H. S. Anderson and P. Roth, “EMBER: An open dataset for training static PE malware machine learning models,” arXiv:1804.04637, 2018. (dataset / preprint)

[3] E. Raff, J. Barker, J. Sylvester, R. Brandon, B. Catanzaro, and C. Nicholas, “Malware detection by eating a whole EXE,” in AAAI Workshops, 2018. (workshop — “MalConv”)

[4] R. Harang and E. M. Rudd, “SOREL-20M: A large scale benchmark dataset for malicious PE detection,” arXiv:2012.07634, 2020. (dataset / preprint)

[5] L. Nataraj, S. Karthikeyan, G. Jacob, and B. S. Manjunath, “Malware images: visualization and automatic classification,” in Proc. VizSec, 2011. (conference — MalImg dataset)

[6] D. Gibert Llauradó, Convolutional Neural Networks for Malware Classification, M.Sc. thesis, Universitat Politècnica de Catalunya, 2016. (MSc thesis)

# Topic 3 — Faithfulness and Stability of Explanations for Digital-Forensic Classifiers

Research problem. Displaying SHAP and LIME plots does not validate an explanation. The research must test whether explanations are faithful, stable and useful for forensic review under equivalent inputs and model uncertainty.

# ▶ Track A — Systematic Review: Explainable AI for Forensic and Security Classifiers

# Review questions

RQ1. Which XAI methods have been applied to forensic/security ML, and for which tasks?

RQ2. How are faithfulness, stability and human usefulness evaluated — if at all — across these studies?

RQ3. How is explanation quality linked to reliability/admissibility standards (Daubert, ISO/IEC 27037), and where are the gaps?

Scope & search protocol. Databases as above. String: ("explainable" OR XAI OR interpretab*) AND ("digital forensic*" OR cyber OR intrusion OR malware). Window 2016–2026 plus SHAP/LIME foundations. Inclusion: peer-reviewed studies applying/evaluating XAI in forensic/security contexts. PRISMA-style flow.

Synthesis & appraisal. Taxonomy of XAI methods; matrix (method, task, faithfulness/stability tests used, admissibility discussion); appraise evaluation rigour; map gaps.

▶ Expected contribution. A synthesis distinguishing validated from merely plausible explanations

3 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

in forensic ML, and an evaluation-standard agenda for court-facing use.

# ▶ Track B — Practical / Experimental Contribution

Research gap. Test whether forensic-classifier explanations are faithful, stable and decision-useful, rather than visually plausible.

Research questions. (i) Do SHAP, LIME and a model-specific method identify features that causally influence predictions? (ii) How stable are explanations across seeds, equivalent samples and model versions? (iii) Do explanations improve examiner error detection without inducing automation bias?

Proposed design. Train an interpretable baseline and one nonlinear classifier on a bounded forensic task; generate SHAP, LIME and counterfactual/model-specific explanations; run deletion/insertion, feature-randomisation and sanity tests; measure rank stability across seeds and harmless transformations; small blinded evaluator study comparing prediction-only vs prediction-plus-explanation.

Evaluation & minimum evidence. Predictive performance, faithfulness curves, rank correlation, explanation stability, counterfactual validity, evaluator accuracy/time/confidence, inter-rater agreement; ≥2 baselines; robustness + ≥1 ablation; confidence intervals; reproducibility package.

▶ Expected contribution & level. A forensic-XAI validation protocol separating faithful, reproducible explanations from plausible ones. Master's-appropriate; strong workshop/applied-conference potential. Publication possible, not guaranteed.

# References (verified; source type labelled)

[1] S. W. Hall, A. Sakzad, and K.-K. R. Choo, "Explainable artificial intelligence for digital forensics," WIREs Forensic Science, vol. 4, no. 2, 2022. (journal)

[2] A. A. Solanke, "Explainable digital forensics AI: Towards mitigating distrust in AI-based digital forensics analysis using interpretable models," Forensic Science International: Digital Investigation, vol. 42, 2022. (journal)

[3] S. M. Lundberg and S.-I. Lee, "A unified approach to interpreting model predictions," in NeurIPS, 2017. (conference — SHAP)

[4] M. T. Ribeiro, S. Singh, and C. Guestrin, "'Why should I trust you?': Explaining the predictions of any classifier," in Proc. ACM SIGKDD, 2016. (conference — LIME)

[5] J. Adebayo, J. Gilmer, M. Muelly, I. Goodfellow, M. Hardt, and B. Kim, "Sanity checks for saliency maps," in NeurIPS, 2018. (conference — faithfulness tests)

[6] "A systematic review on the integration of explainable AI in intrusion detection systems," Frontiers in Artificial Intelligence, 2025. (journal — systematic review)

# Topic 4 — Cross-Domain Reliability and Demographic Bias in Face-Sketch Retrieval

Research problem. Generating a few faces from sketches is demonstration work. The research value is evaluating retrieval reliability across sketch types, domains and demographic groups, treating outputs as investigative leads rather than identification evidence.

# ▶ Track A — Systematic Review: Face-Sketch Synthesis and Recognition for Forensic Identification

# Review questions

RQ1. Which face-sketch synthesis and recognition/retrieval approaches have been proposed for identification, and how do they group (synthesis-then-recognise vs direct cross-modal embedding)?

RQ2. How are they evaluated — datasets, retrieval metrics, cross-domain protocols, demographic-bias analysis?

RQ3. What is known about reliability as an investigative lead versus identification evidence, and where are the gaps?

Scope & search protocol. Databases as above. String: ("face sketch" OR "composite sketch") AND (synthesis OR recognition OR retrieval OR identification). Window 2009–2026 plus foundational works. Inclusion: peer-reviewed studies on face-sketch identification. PRISMA-style flow.

4 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

Synthesis & appraisal. Taxonomy of approaches; matrix (dataset, protocol, metrics, cross-domain, bias analysis); appraise identity-leakage control and bias handling; map gaps.

▶ Expected contribution. A synthesis clarifying when face-sketch systems generalise across domains and demographics, and when uncertainty precludes even an investigative lead — with a benchmarking agenda.

▶ Track B — Practical / Experimental Contribution

Research gap. Evaluate cross-domain retrieval reliability and demographic disparity under leakage-resistant, identity-disjoint protocols.

Research questions. (i) How large is the matched-dataset versus cross-dataset retrieval gap? (ii) Do synthesis-based and direct-embedding approaches fail differently? (iii) Are rank/error disparities present across usable demographic or sketch-style groups?

Proposed design. Licensed CUFS/CUFSF-style pairs and, where possible, a second sketch domain; baselines = a direct cross-modal embedding and a synthesis-plus-face-recognition pipeline; separate identities across partitions; test viewed, forensic and artist-style shifts; evaluate gallery-size sensitivity, image degradation and top-k retrieval; audit subgroups only where labels are reliable and sizes reported.

Evaluation & minimum evidence. Rank-1/rank-5 retrieval, mean average precision, false-match rate, cross-domain loss, subgroup confidence intervals, calibration; bootstrap by identity; ≥2 baselines; robustness + ≥1 ablation; reproducibility package.

▶ Expected contribution & level. A leakage-resistant assessment of when face-sketch retrieval generalises and when domain/demographic uncertainty makes a result unsuitable even as a lead. Master's-appropriate; workshop/applied-conference potential. Publication possible, not guaranteed.

# References (verified; source type labelled)

[1] X. Wang and X. Tang, "Face photo-sketch synthesis and recognition," IEEE Trans. Pattern Analysis and Machine Intelligence, vol. 31, no. 11, pp. 1955–1967, 2009. (journal — CUHK dataset)

[2] W. Zhang, X. Wang, and X. Tang, "Coupled information-theoretic encoding for face photo-sketch recognition," in Proc. IEEE CVPR, 2011. (conference — CUFSF dataset)

[3] S.-Y. Chen, W. Su, L. Gao, S. Xia, and H. Fu, "DeepFaceDrawing: Deep generation of face images from sketches," ACM Trans. Graphics (SIGGRAPH), vol. 39, no. 4, 2020. (journal / conference)

[4] S.-Y. Wang, D. Bau, and J.-Y. Zhu, "Sketch Your Own GAN," in Proc. IEEE/CVF ICCV, 2021, pp. 14050–14060. (conference)

[5] National Institute of Standards and Technology, Face Recognition Vendor Test (FRVT) Part 3: Demographic Effects, NISTIR 8280, 2019. (standards-body report)

### Topic 5 — Cross-Generator and Post-Processing Robustness of Video Deepfake Detectors

Research problem. In-domain accuracy on FaceForensics++ is no longer a sufficient contribution. The study must quantify unseen-manipulation and real-world laundering failures at the video level.

▶ Track A — Systematic Review: Video Deepfake Detection: Methods, Datasets and Generalisation

Review questions.

RQ1. Which detector families exist (spatial artefacts, physiological signals, multimodal audio-video inconsistency, generator fingerprinting)?

RQ2. How are they evaluated — datasets, in-domain vs cross-dataset/cross-generator, frame- vs video-level, robustness to compression?

RQ3. What evidence exists on generalisation to unseen manipulations and laundering, and where are the gaps?

Scope & search protocol. Databases as above. String: (deepfake OR "face forgery") AND (detection) AND (video OR generalis* OR robustness). Window 2018–2026 plus foundational

5 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

datasets. PRISMA-style flow.

Synthesis & appraisal. Taxonomy of detectors; matrix (dataset, protocol, video/frame, post-processing tested, generalisation gap); appraise cross-generator/laundering rigour; map gaps.

▶ Expected contribution. A synthesis quantifying the in-domain-to-cross-domain reliability gap and mapping which detector designs survive generator and processing shift.

▶ Track B — Practical / Experimental Contribution

Research gap. Quantify cross-generator and post-processing robustness of video detectors, at the video level, with calibration and abstention.

Research questions. (i) How large is the in-domain vs leave-one-manipulation / cross-dataset gap? (ii) Which compound post-processing operations cause the greatest degradation? (iii) Can temporal aggregation, calibration and abstention reduce high-confidence errors?

Proposed design. Controlled subsets of FaceForensics++, Celeb-DF v2 and DF40 or DFDC; ≥3 detector families via a standardised framework (e.g. DeepfakeBench); identities and source videos disjoint; evaluate videos, not correlated frames; apply paired recompression, resizing, cropping, blur, denoising and frame-rate changes; compare mean/top-k/temporal aggregation plus calibrated selective prediction.

Evaluation & minimum evidence. Video AUROC, PR-AUC, balanced accuracy, TPR at fixed FPR, EER, Brier/ECE, worst-domain AUROC, relative degradation, risk-coverage curves; ≥2 baselines; robustness + ≥1 ablation; confidence intervals; reproducibility package.

▶ Expected contribution & level. A reproducible stress-test protocol showing when modern video detectors remain reliable after generator and processing shifts. Master's-appropriate; strong workshop/applied-conference potential. Publication possible, not guaranteed.

# References (verified; source type labelled)

[1] Z. Yan, Y. Zhang, X. Yuan, S. Lyu, and B. Wu, “DeepfakeBench: A comprehensive benchmark of deepfake detection,” in NeurIPS Datasets and Benchmarks Track, 2023. (conference — benchmark)

[2] Z. Yan, T. Yao, S. Chen, et al., “DF40: Toward next-generation deepfake detection,” in NeurIPS Datasets and Benchmarks Track, 2024. (conference — benchmark/dataset)

[3] Z. Yan, Y. Luo, S. Lyu, Q. Liu, and B. Wu, “Transcending forgery specificity with latent space augmentation for generalizable deepfake detection,” in Proc. IEEE/CVF CVPR, 2024. (conference)

[4] D. Nguyen, N. Mejri, I. P. Singh, et al., “LAA-Net: Localized artifact attention network for quality-agnostic and generalizable deepfake detection,” in Proc. IEEE/CVF CVPR, 2024. (conference)

[5] A. Rössler, D. Cozzolino, L. Verdoliva, C. Riess, J. Thies, and M. Nießner, “FaceForensics++: Learning to detect manipulated facial images,” in Proc. IEEE/CVF ICCV, 2019. (conference — benchmark)

[6] Y. Li, X. Yang, P. Sun, H. Qi, and S. Lyu, “Celeb-DF: A large-scale challenging dataset for DeepFake forensics,” in Proc. IEEE/CVF CVPR, 2020. (conference — dataset)

# Topic 6 — Open-Set Source-Model Attribution of Synthetic Face Images under Post-Processing

Research problem. Frequency separation of outputs from two generators is a closed-set demonstration. The paper must reject unknown generators, control semantic leakage, and distinguish family-level from exact-model attribution.

▶ Track A — Systematic Review: Attribution of Synthetic Media to its Source Model Review questions.

RQ1. Which attribution approaches exist (spectral/residual fingerprints, learned features, foundation-model features)?

RQ2. How is attribution evaluated — closed-set vs open-set, robustness to compression/resizing/denoising, calibration?

RQ3. What is the state of family- vs exact-model attribution and unknown-generator rejection, and where are the gaps?

6 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

Scope & search protocol. Databases as above. String: (deepfake OR "generated image" OR synthetic) AND (attribution OR fingerprint OR "source model"). Window 2019–2026. PRISMA-style flow.

Synthesis & appraisal. Taxonomy of features/methods; matrix (generators covered, open-set handling, post-processing robustness, calibration); appraise open-set/laundering rigour; map gaps.

▶ Expected contribution. A synthesis of when attribution is reliable, when it should stop at a model family, and when it should return inconclusive.

# ▶ Track B — Practical / Experimental Contribution

Research gap. Attribute known generators while rejecting unseen ones under post-processing, distinguishing family- from exact-model attribution.

Research questions. (i) Can known generators be attributed while unseen ones are correctly rejected? (ii) Which fingerprint features survive compression, resizing and denoising? (iii) Is hierarchical family-then-model attribution safer than flat classification?

Proposed design. A controlled corpus from 4–6 GAN/diffusion/face-manipulation sources with matched prompts/identities; split prompts, identities and content; normalise metadata/encoders; compare spectral, residual, CNN and foundation-model features; evaluate closed-set, leave-one-model-out, leave-one-family-out and version-shift; compare maximum-softmax, energy and prototype-distance rejection under post-processing.

Evaluation & minimum evidence. Known-source macro-F1, family/model accuracy, unknown AUROC/AUPR, FPR95, OSCR, calibration, risk-coverage and performance-decay curves; ≥2 baselines; robustness + ≥1 ablation; confidence intervals; reproducibility package.

▶ Expected contribution & level. A content-controlled open-set benchmark identifying when attribution should stop at a family or return inconclusive. Master's-appropriate; strong workshop/applied-conference potential. Publication possible, not guaranteed.

# References (verified; source type labelled)

[1] Z. Sun, S. Chen, T. Yao, R. Yi, S. Ding, and L. Ma, “Contrastive pseudo learning for open-world deepfake attribution,” in Proc. IEEE/CVF ICCV, 2023. (conference)

[2] Z. Sun, et al., “Rethinking open-world deepfake attribution with multi-perspective sensory learning,” Int. J. Computer Vision, vol. 133, pp. 628–651, 2025, doi:10.1007/s11263-024-02184-7. (journal)

[3] Z. Sha, Z. Li, N. Yu, and Y. Zhang, “DE-FAKE: Detection and attribution of fake images generated by text-to-image generation models,” in Proc. ACM CCS, 2023, pp. 3418–3432. (conference)

[4] K. Xu, L. Zhang, and J. Shi, “Detecting origin attribution for text-to-image diffusion models,” in Proc. IEEE/CVF WACV, 2025, pp. 8764–8774. (conference)

[5] N. Yu, L. Davis, and M. Fritz, “Attributing fake images to GANs: Learning and analyzing GAN fingerprints,” in Proc. IEEE/CVF ICCV, 2019. (conference — foundational)

# Topic 7 — Cross-Dataset Localization of Image Manipulation under Recompression

Research problem. Running a copy-move detector and checking EXIF is a laboratory exercise. The contribution is to compare localization generalisation across manipulation families, datasets and processing histories.

# ▶ Track A — Systematic Review: Deep Learning for Image Manipulation Detection and Localization

# Review questions

RQ1. Which detector/localiser architectures exist (noise-inconsistency, frequency, segmentation), and for which manipulation types?

RQ2. How are they evaluated — datasets, pixel- vs image-level metrics, cross-dataset, robustness to recompression?

RQ3. What is known about dataset shortcuts and laundering limits, and where are the gaps?

7 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

Scope & search protocol. Databases as above. String: (image AND (forgery OR manipulation OR tamper*)) AND (detection OR localization) AND ("deep learning"). Window 2013–2026 plus foundational. PRISMA-style flow.

Synthesis & appraisal. Taxonomy; matrix (dataset, split, pixel/image metrics, recompression robustness, cross-dataset); appraise leakage/laundering rigour; map gaps.

▶ Expected contribution. A synthesis exposing within-dataset over-estimation and identifying which methods generalise across datasets and processing histories.

▶ Track B — Practical / Experimental Contribution

Research gap. Compare localisation generalisation across manipulation families, datasets and recompression pipelines.

Research questions. (i) How much does within-dataset evaluation overestimate localisation? (ii) Which manipulation/laundering combinations cause the greatest failures? (iii) Can uncertainty or provenance cues reduce false localisation?

Proposed design. ≥2 licensed datasets with splicing/copy-move/removal masks; baselines = a classical keypoint/noise method and two modern localisers; split by source image and manipulation pipeline (prevent derivative leakage); test JPEG/WebP recompression, scaling, screenshot recapture and compound transforms; evaluate masks, image-level decisions, calibration and failure localisation.

Evaluation & minimum evidence. Image AUROC/PR-AUC; pixel F1, IoU, MCC; boundary F1; TPR at fixed FPR; worst-dataset performance; calibration; ≥2 baselines; robustness + ≥1 ablation; confidence intervals; reproducibility package.

▶ Expected contribution & level. A cross-dataset, mask-level robustness evaluation identifying dataset shortcuts and realistic laundering limits. Master's-appropriate; workshop/applied-conference potential. Publication possible, not guaranteed.

# References (verified; source type labelled)

[1] J. Wang, Z. Wu, J. Chen, X. Han, A. Shrivastava, S.-N. Lim, and Y.-G. Jiang, “ObjectFormer for image manipulation detection and localization,” in Proc. IEEE/CVF CVPR, 2022, pp. 2364–2373. (conference)

[2] X. Liu, Y. Liu, J. Chen, and X. Liu, “PSCC-Net: Progressive spatio-channel correlation network for image manipulation detection and localization,” IEEE Trans. Circuits and Systems for Video Technology, vol. 32, no. 11, 2022. (journal)

[3] J. Dong, W. Wang, and T. Tan, “CASIA image tampering detection evaluation database,” in Proc. IEEE ChinaSIP, 2013. (conference — dataset)

[4] D. Cozzolino and L. Verdoliva, “Noiseprint: A CNN-based camera model fingerprint,” IEEE Trans. Information Forensics and Security, vol. 15, 2020. (journal)

[5] M.-J. Kwon, S.-H. Nam, I.-J. Yu, H.-K. Lee, and C. Kim, “Learning JPEG compression artifacts for image manipulation detection and localization (CAT-Net v2),” Int. J. Computer Vision, vol. 130, 2022. (journal)

# Topic 8 — Security Evaluation of Fragile Chaotic Watermarking for Image Tamper Localization

Research problem. Implementing an LSB watermark and plotting compression errors is insufficient. The scheme must be evaluated against realistic benign processing, targeted attacks, key reuse and localisation-security trade-offs.

▶ Track A — Systematic Review: Fragile Watermarking for Image Tamper Detection and Localization

# Review questions

RQ1. Which fragile/semi-fragile schemes exist, and what role do chaotic maps play (key generation, scrambling, self-recovery)?

RQ2. How are they evaluated — localisation, capacity, imperceptibility, robustness to benign processing, security against attacks?

8 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

RQ3. What security guarantees are actually demonstrated, and where are the gaps?

**Scope & search protocol.** Databases as above. String: (fragile OR semi-fragile) AND watermark*AND (tamper* OR authenticat*) AND (image). Window 2010–2026 plus foundational. PRISMA-style flow.

**Synthesis & appraisal.** Taxonomy; matrix (scheme, chaotic component, localisation, capacity, PSNR/SSIM, robustness, attacks tested); appraise threat-model rigour; map gaps.

► **Expected contribution.** A synthesis distinguishing schemes with demonstrated security from those whose chaotic components are decorative.

► **Track B — Practical / Experimental Contribution**

**Research gap.** Evaluate a fragile chaotic scheme against a defined threat model: benign processing, targeted tampering, key reuse and localisation–security trade-offs.

**Research questions.** (i) Does chaotic scrambling add security beyond key-controlled permutation? (ii) How do benign transforms and targeted tampering affect false alarms and localisation? (iii) Can an attacker estimate or exploit structure when keys or images are reused?

**Proposed design.** Implement the scheme and ≥2 non-chaotic baselines with identical payload; define attacker knowledge, key management and tamper goals; test copy-paste, collage, vector-quantization, block substitution, recompression and resizing; measure key sensitivity, reuse leakage, payload and visual distortion; ablate chaos map, authentication code, block size and recovery component.

**Evaluation & minimum evidence.** Tamper precision/recall, pixel IoU, false-alarm rate under benign processing, PSNR/SSIM, payload, runtime, attack success, key-sensitivity distributions; ≥2 baselines; robustness + ≥1 ablation; confidence intervals; reproducibility package.

► **Expected contribution & level.** A security-focused evaluation revealing whether chaotic components provide measurable protection rather than decorative complexity. Master’s-appropriate; workshop/applied-conference potential. *Publication possible, not guaranteed.*

**References** (verified; source type labelled)

[1] P. Korus, “Digital image integrity — a survey of protection and verification techniques,” *Digital Signal Processing*, vol. 71, pp. 1–26, 2017. (journal — survey)
[2] J. Molina-Garcia, B. P. Garcia-Salgado, V. Ponomaryov, R. Reyes-Reyes, S. Sadovnychiy, and C. Cruz-Ramos, “An effective fragile watermarking scheme for color image tampering detection and self-recovery,” *Signal Processing: Image Communication*, vol. 81, 2020. (journal)
[3] A. Shehab, M. Elhoseny, K. Muhammad, *et al.*, “Secure and robust fragile watermarking scheme for medical images,” *IEEE Access*, vol. 6, pp. 10269–10278, 2018, doi:10.1109/ACCESS.2018.2799240. (journal)
[4] S. Rawat and B. Raman, “A chaotic system based fragile watermarking scheme for image tamper detection,” *AEU — Int. J. Electronics and Communications*, vol. 65, no. 10, 2011. (journal — foundational chaotic scheme)
[5] NIST SP 800-57 Part 1 Rev. 5, *Recommendation for Key Management*, 2020. (standards-body publication)

## Topic 10 — Reproducibility and Evidence-Groundedness of Large Language Models as Forensic Assistants

**Research problem.** A few log summaries are demonstrations. The research must use *hidden ground truth*, *repeated runs* and *evidence-linked scoring* to measure hallucination, omission and non-determinism.

► **Track A — Systematic Review: Large Language Models in Digital Forensic Investigation**

**Review questions.**

RQ1. Which LLM use-cases are proposed across the investigation process (IOC/keyword generation, log/narrative summarisation, report drafting, parser-code generation)?

RQ2. How are outputs evaluated — ground truth, hallucination/omission measurement, reproducibil-

9 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

ity, privacy of evidence handling?

RQ3. What is the evidence on trustworthy, reproducible LLM assistance, and where are the gaps?

Scope & search protocol. Databases as above. String: ("large language model" OR LLM OR ChatGPT) AND ("digital forensic*" OR "incident response"). Window 2022–2026. PRISMA-style flow.

Synthesis & appraisal. Taxonomy of use-cases mapped to the DFRWS process; matrix (task, ground truth, hallucination measure, reproducibility, privacy); appraise evaluation rigour; map gaps.

▶ Expected contribution. A synthesis clarifying where LLMs genuinely help versus where the probabilistic, non-reproducible nature of their output conflicts with admissibility, with an evaluation agenda.

# ▶ Track B — Practical / Experimental Contribution

Research gap. Measure LLM factuality, omission and run-to-run stability on bounded forensic tasks with evidence-linked scoring.

Research questions. (i) How accurate and complete are LLM outputs on bounded forensic tasks? (ii) How do model, prompt, temperature and evidence length affect reproducibility? (iii) Can retrieval, schemas and citation requirements reduce unsupported claims?

Proposed design. Synthetic/public cases with known events, IOCs and timelines; baselines = keyword/rule methods, a local model and one controlled API model where privacy permits; evaluate extraction, summarisation, hypothesis generation and timeline narration separately; repeat each condition; require artifact-line citations and verify each claim; test prompt injection in evidence, irrelevant context, conflicting logs and missing artifacts.

Evaluation & minimum evidence. Fact precision/recall, unsupported-claim rate, critical-omission rate, citation correctness, cross-run consistency, time and reviewer workload;  \( \geq2 \)  baselines; robustness +  \( \geq1 \)  ablation; confidence intervals; reproducibility package.

▶ Expected contribution & level. A versioned benchmark for forensic-assistant reliability with evidence-linked scoring and reproducibility reporting. Master's-appropriate; very strong workshop/applied-conference potential. Publication possible, not guaranteed.

# References (verified; source type labelled)

[1] M. Scanlon, F. Breitinger, C. Hargreaves, J.-N. Hilgert, and J. Sheppard, “ChatGPT for digital forensic investigation: The good, the bad, and the unknown,” *Forensic Science International: Digital Investigation*, vol. 46, art. 301609, 2023. (journal — seminal)

[2] A. Wickramasekara, F. Breitinger, and M. Scanlon, “Exploring the potential of large language models for improving digital forensic investigation efficiency,” arXiv:2402.19366, 2024. (preprint)

[3] B. Sharma, et al., "ForensicLLM: A local large language model for digital forensics," Forensic Science International: Digital Investigation (DFRWS EU), 2025. (conference / journal special issue)

[4] NIST AI 600-1, Artificial Intelligence Risk Management Framework: Generative AI Profile, 2024. (standards-body publication)

[5] OWASP, Top 10 for Large Language Model Applications, current edition. (industry technical report)

[6] B. Sharma, ForensicLLM: A Local Large Language Model for Digital Forensics, M.Sc. thesis, Louisiana State University, 2024. (MSc thesis)

# Topic 12 — Uncertainty-Aware Timeline Reconstruction from Heterogeneous Digital Artifacts

Research problem. Building a super-timeline is a tool exercise. The research problem is to fuse conflicting clocks, duplicate events and uncertain timestamps while measuring event-level correctness.

▶ Track A — Systematic Review: Digital-Forensic Timeline Reconstruction

Review questions.

RQ1. Which timeline-reconstruction approaches exist (super-timeline/Plaso, rule-based correlation, formal/knowledge-representation, ML/LLM-assisted)?

10 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

RQ2. How are they evaluated — ground truth, event-level correctness, timestamp/timezone normalisation, uncertainty?

RQ3. How is temporal uncertainty and conflicting evidence handled, and where are the gaps?

**Scope & search protocol.** Databases as above. String: (timeline OR "event reconstruction") AND ("digital forensic*" OR "digital investigation"). Window 2004–2026. PRISMA-style flow.

**Synthesis & appraisal.** Taxonomy; matrix (method, sources fused, ground truth, uncertainty handling, evaluation); appraise correctness measurement; map gaps.

► **Expected contribution.** A synthesis of how (rarely) event-level correctness and temporal uncertainty are measured, with a methodology agenda for defensible timelines.

► **Track B — Practical / Experimental Contribution**

**Research gap.** Fuse conflicting clocks, duplicate events and uncertain timestamps, and measure event-level correctness with explicit uncertainty.

**Research questions.** (i) How should events with conflicting timestamp semantics be normalised? (ii) Does provenance-aware fusion improve reconstruction over simple sorting? (iii) How should uncertainty and missing evidence be communicated?

**Proposed design.** Multiple synthetic cases plus one public image with ground-truth event sequences; extract ≥2 artifact families via Plaso or reproducible parsers; compare simple sorting, rule-based fusion and a probabilistic/scored fusion method; inject clock skew, timezone errors, missing logs, duplicates and timestamp manipulation; evaluate event recovery and ordering; trace every inferred event to source artifacts.

**Evaluation & minimum evidence.** Event precision/recall, ordering accuracy, temporal error, duplicate-reduction, provenance coverage, uncertainty calibration, case-level conclusion accuracy; ≥2 baselines; robustness + ≥1 ablation; confidence intervals; reproducibility package.

► **Expected contribution & level.** A benchmark and provenance-aware fusion method for defensible timelines with explicit temporal uncertainty. Master's-appropriate; strong workshop/applied-conference potential. *Publication possible, not guaranteed.*

**References** (verified; source type labelled)

[1] P. Gladyshev and A. Patel, "Finite state machine approach to digital event reconstruction," *Digital Investigation*, vol. 1, no. 2, pp. 130–149, 2004. (journal — foundational)
[2] Y. Chabot, A. Bertaux, C. Nicolle, and T. Kechadi, "A complete formalized knowledge representation model for advanced digital forensics timeline analysis," *Digital Investigation*, vol. 11, Suppl. 2, pp. S95–S105, 2014. (journal (DFRWS EU))
[3] C. Hargreaves and J. Patterson, "An automated timeline reconstruction approach for digital forensic investigations," *Digital Investigation*, vol. 9, pp. S69–S79, 2012. (journal (DFRWS))
[4] F. Breitinger, H. Studiawan, and C. Hargreaves, "SoK: Timeline based event reconstruction for digital forensics: Terminology, methodology, and current challenges," arXiv:2504.18131, 2025 (DFRWS USA). (preprint)
[5] Plaso Project (log2timeline/plaso), documentation and format specifications, current release. (software)
[6] NIST IR 8387, *Digital Evidence Preservation: Considerations for Evidence Handlers*, 2022. (standards-body publication)

## Topic 13 — Topic-Robust Authorship Attribution for Short Communications Evidence

**Research problem.** Randomly splitting Enron messages allows topic, signature and thread leakage. A research paper must test author attribution under topic, time and platform shift and include an *open-set rejection* option.

11 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

# ▶ Track A — Systematic Review: Authorship Attribution for Forensic and Short-Text Communications

# Review questions

RQ1. Which authorship-attribution approaches exist (stylometry, neural, transformers), and for which forensic/short-text settings?
RQ2. How are they evaluated — splitting (random vs thread/topic/temporal-disjoint), leakage control, open-set rejection?
RQ3. What is known about robustness to topic and temporal shift, and where are the gaps?

Scope & search protocol. Databases as above. String: ("authorship attribution" OR stylometr*) AND (forensic* OR email OR "social media" OR "short text"). Window 2009–2026. PRISMA-style flow.

Synthesis & appraisal. Taxonomy; matrix (features/models, dataset, split strategy, open-set, calibration); appraise leakage control; map gaps.

▶ Expected contribution. A synthesis exposing how topic/thread leakage inflates attribution results and mapping which signals survive shift, with an open-set evaluation agenda.

# ▶ Track B — Practical / Experimental Contribution

Research gap. Test attribution under topic, time and platform shift, with an open-set rejection option, on short messages.

Research questions. (i) How much performance comes from topic and thread leakage? (ii) Which stylometric and transformer features generalise across topics and time? (iii) Can the system reject messages from unseen authors?

Proposed design. Enron or another authorized public corpus with thread/author/time metadata; remove signatures, quoted replies, addresses and trivial identifiers; compare character n-grams, stylometric features and a transformer embedding; evaluate random, thread-disjoint, topic-held-out, temporal and open-set splits; test short-message length, paraphrase, spelling normalisation and quoted-content contamination.

Evaluation & minimum evidence. Macro-F1, balanced accuracy, per-author recall, open-set AU-ROC/OSCR, calibration, worst-topic performance; bootstrap by thread or author; ≥2 baselines; robustness + ≥1 ablation; confidence intervals; reproducibility package.

▶ Expected contribution & level. A leakage-resistant assessment of whether authorship signals survive topic and temporal change and when an attribution should be rejected. Master's-appropriate; workshop/applied-conference potential. Publication possible, not guaranteed.

# References (verified; source type labelled)

[1] E. Stamatatos, “A survey of modern authorship attribution methods,” J. American Society for Information Science and Technology, vol. 60, no. 3, pp. 538–556, 2009. (journal — survey)

[2] A. Rocha, W. J. Scheirer, C. W. Forstall, et al., “Authorship attribution for social media forensics,” IEEE Trans. Information Forensics and Security, vol. 12, no. 1, pp. 5–33, 2017. (journal)

[3] S. H. H. Ding, B. C. M. Fung, F. Iqbal, and W. K. Cheung, “Learning stylometric representations for authorship analysis,” IEEE Trans. Cybernetics, vol. 49, no. 1, 2019. (journal)

[4] P. Shrestha, S. Sierra, F. A. González, P. Rosso, M. Montes-y-Gómez, and T. Solorio, “Convolutional neural networks for authorship attribution of short texts,” in Proc. EACL, 2017. (conference)

[5] M. Fabien, E. Villatoro-Tello, P. Motlicek, and S. Parida, “BertAA: BERT fine-tuning for authorship attribution,” in Proc. 17th Int. Conf. on Natural Language Processing (ICON), 2020, pp. 127–137. (conference)

[6] M. W. Corney, Analysing E-mail Text Authorship for Forensic Purposes, Ph.D. thesis, Queensland University of Technology, 2003. (PhD thesis)

# Topic 15 — Cross-Source Event Reconstruction in Smart-Home Forensics

Research problem. Parsing one companion-app database is a course exercise. The stronger question is whether device, app, cloud and network traces can be fused reliably when sources are incomplete or

12 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

disagree.

# ► Track A — Systematic Review: IoT and Smart-Home Forensics

# Review questions

RQ1. What are the evidence sources (device, companion app, vendor cloud, network) and acquisition strategies for each?
RQ2. How is occupancy/device-action reconstruction evaluated, and how is timestamp/presence validated?
RQ3. How do source incompleteness, disagreement and app/firmware versions affect conclusions, and where are the gaps?

Scope & search protocol. Databases as above. String: (IoT OR "smart home" OR "smart device") AND forensic*AND (acquisition OR artefact* OR evidence). Window 2016–2026. PRISMA-style flow.

Synthesis & appraisal. Taxonomy of sources/methods; matrix (device class, sources used, timestamp validation, cross-source fusion); appraise reliability under incompleteness; map gaps.

► Expected contribution. A synthesis of which smart-home conclusions remain defensible under fragmented evidence, with a cross-source methodology agenda.

# ► Track B — Practical / Experimental Contribution

Research gap. Fuse device/app/cloud/network traces and quantify which reconstructions survive source loss and disagreement.

Research questions. (i) Which sources contribute unique versus redundant event evidence? (ii) How accurately can occupancy/device-action timelines be reconstructed after source loss? (iii) How do clock drift, app versions and cloud dependence affect conclusions?

Proposed design. A controlled smart-home testbed or a documented public dataset with several event types; collect device, companion-app, cloud-export and network traces where authorized; a common event schema with provenance and uncertainty; ablate one source at a time; inject clock skew and missing events; repeat across firmware/app versions where feasible; distinguish household presence from individual attribution.

Evaluation & minimum evidence. Event precision/recall, temporal error, source coverage, reconstruction accuracy, provenance completeness, degradation after source removal; ≥2 baselines; robustness + ≥1 ablation; confidence intervals; reproducibility package.

► Expected contribution & level. A source-ablation benchmark showing which smart-home conclusions remain defensible when evidence is fragmented. Master's-appropriate; workshop/applied-conference potential. Publication possible, not guaranteed.

# References (verified; source type labelled)

[1] M. Stoyanova, Y. Nikoloudakis, S. Panagiotakis, E. Pallis, and E. K. Markakis, “A survey on the Internet of Things (IoT) forensics: Challenges, approaches, and open issues,” IEEE Communications Surveys & Tutorials, vol. 22, no. 2, 2020. (journal — survey)
[2] F. Servida and E. Casey, “IoT forensic challenges and opportunities for digital traces,” Forensic Science International: Digital Investigation, vol. 28, pp. S22–S29, 2019. (journal)
[3] A. Nieto, R. Rios, and J. Lopez, “IoT-forensics meets privacy: Towards cooperative digital investigations,” Sensors, vol. 18, no. 2, art. 492, 2018. (journal)
[4] “Do you ‘relay’ want to give me away? — Forensic cues of smart relays and their IoT companion apps,” Forensic Science International: Digital Investigation, 2024. (journal — recent)
[5] NIST, NISTIR 8259, Foundational Cybersecurity Activities for IoT Device Manufacturers, 2020. (standards-body publication)
[6] Challenges in Forensic Investigations of IoT Devices, M.Sc. thesis (via DiVA, diva2:1983130), 2024. (MSc thesis)

13 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

## Topic 17 — Multi-Source Consistency and Uncertainty in UAV Flight Reconstruction

**Research problem.** Plotting one DJI log or extracting GPS metadata demonstrates a tool. Research value comes from comparing aircraft, controller, app and media traces and quantifying *disagreement* and *missing-source* effects.

### ► Track A — Systematic Review: Drone / UAV Forensics

#### Review questions

RQ1. What are the UAV evidence sources (aircraft/flight logs, controller/app records, media) and how are they acquired and parsed?

RQ2. How is flight/operator reconstruction validated — ground truth, position/time error, parser agreement?

RQ3. How do source deletion, corruption and app-version changes affect conclusions, and where are the gaps?

**Scope & search protocol.** Databases as above. String: (drone OR UAV OR "unmanned aerial") AND forensic* AND ("flight log" OR telemetry OR acquisition). Window 2016–2026. PRISMA-style flow.

**Synthesis & appraisal.** Taxonomy of sources/parsers; matrix (device, sources, validation, attribution); appraise multi-source/uncertainty handling; map gaps.

► **Expected contribution.** A synthesis of how consistently UAV evidence is cross-validated and where single-source reconstructions are unreliable.

### ► Track B — Practical / Experimental Contribution

**Research gap.** Compare aircraft/controller/app/media traces and quantify disagreement and missing-source effects on flight and operator reconstruction.

**Research questions.** (i) How consistent are time, position and altitude across available UAV evidence sources? (ii) Which sources best survive deletion, corruption or app-version changes? (iii) How should uncertainty affect operator or flight attribution?

**Proposed design.** Controlled flights or public logs with ground-truth waypoints/timestamps; parse aircraft/flight logs, controller/app records and media EXIF where available; normalise coordinate systems, time zones and altitude references; ablate sources; introduce truncation, missing records and clock offsets; compare $\geq 2$ parsers and validate fields against independent ground truth.

**Evaluation & minimum evidence.** Position/altitude/temporal error, route similarity, event recall, parser agreement, source-ablation loss, uncertainty coverage; $\geq 2$ baselines; robustness + $\geq 1$ ablation; confidence intervals; reproducibility package.

► **Expected contribution & level.** A validated multi-source UAV reconstruction method with quantified parser and source uncertainty. Master's-appropriate; workshop/applied-conference potential. *Publication possible, not guaranteed.*

#### References (verified; source type labelled)

[1] D. R. Clark, C. Meffert, I. Baggili, and F. Breitinger, "DROP (DRone Open source Parser) your drone: Forensic analysis of the DJI Phantom III," *Digital Investigation* (DFRWS USA), 2017. (conference / journal — foundational)
[2] F. E. Salamh, U. Karabiyik, M. K. Rogers, and E. T. Matson, "UAV forensic analysis and software tools assessment: DJI Phantom 4 and Matrice 210 as case studies," *Electronics*, vol. 10, no. 6, art. 733, 2021. (journal)
[3] S. Lee, H. Seo, and D. Kim, "Digital forensic research for analyzing drone pilot: Focusing on DJI remote controller," *Sensors*, vol. 23, no. 21, art. 8934, 2023. (journal)
[4] Z. Zhao, Y. Wang, and G. Liao, "Digital forensic research for analyzing drone and mobile data: A case study on DJI Mavic 2 Pro," *Drones*, vol. 8, no. 7, art. 281, 2024. (journal)
[5] "A digital forensics case study of the DJI Mini 3 Pro and DJI RC," arXiv:2309.10487, 2023. (preprint — case study)

14 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

## Topic 18 — Cross-View Detection of Process and Memory Hiding in Contemporary Memory Forensics

**Research problem.** Finding one injected process in a public image is a lab. The research contribution is a controlled evaluation of *acquisition quality* and *cross-view detection* under several hiding or injection techniques.

### ► Track A — Systematic Review: Memory Forensics and Anti-Forensic Evasion

#### Review questions

RQ1. Which memory views and artefacts are used, and how reliable are they under process hiding and injection?

RQ2. How is detection evaluated — ground truth, cross-view agreement, false positives, acquisition/OS-build effects?

RQ3. What evasion techniques (injection, DKOM) are documented, and where are the detection gaps?

**Scope & search protocol.** Databases as above. String: ("memory forensic*" OR "volatile memory") AND (Volatility OR "process hiding" OR injection OR DKOM OR anti-forensic*). Window 2014–2026. PRISMA-style flow.

**Synthesis & appraisal.** Taxonomy of hiding/injection and detection views; matrix (technique, view, detection, false positives, OS build); appraise ground-truth rigour; map gaps.

► **Expected contribution.** A synthesis separating genuine anti-forensic success from acquisition and parser limitations, with a cross-view evaluation agenda.

### ► Track B — Practical / Experimental Contribution

**Research gap.** Controlled evaluation of acquisition quality and cross-view detection under several hiding/injection techniques with ground truth.

**Research questions.** (i) Which memory views remain reliable under process hiding and injection? (ii) How do acquisition method and OS build affect artifact recovery? (iii) Can cross-view inconsistency provide robust detection with acceptable false positives?

**Proposed design.** Isolated Windows test VMs with benign research implants or approved samples; acquire memory using $\geq 2$ methods and document observer effects; compare Volatility 3 plugins and independent views (lists, scans, handles, threads, VADs, network objects); test process hollowing/injection and safe hiding simulations across supported builds; create ground truth from controlled execution; analyse parser failures separately from detection failures.

**Evaluation & minimum evidence.** Artifact recall, hidden-object detection rate, false positives, acquisition time, image consistency, cross-view agreement, results by OS build; $\geq 2$ baselines; robustness + $\geq 1$ ablation; confidence intervals; reproducibility package. **Ethics:** isolated environment; no operational malware distribution.

► **Expected contribution & level.** A ground-truthed cross-view benchmark distinguishing anti-forensic success from acquisition/parser limitations. Master's-appropriate; workshop/applied-conference potential. *Publication possible, not guaranteed.*

#### References (verified; source type labelled)

[1] A. Case and G. G. Richard III, "Memory forensics: The path forward," *Digital Investigation*, vol. 20, pp. 23–33, 2017. (journal — survey)
[2] R. Palutke, F. Block, P. Reichenberger, and D. Stripeika, "Hiding process memory via anti-forensic techniques," *Forensic Science International: Digital Investigation*, vol. 33, 2020 (DFRWS USA). (conference / journal)
[3] "Memory analysis for malware detection: A comprehensive survey using the OSCAR methodology," *ACM Computing Surveys*, 2025. (journal — survey)
[4] Volatility Foundation, *Volatility 3 documentation and symbol specifications*, current release. (software)
[5] M. H. Ligh, A. Case, J. Levy, and A. Walters, *The Art of Memory Forensics*, Wiley, 2014. (book — foundational practitioner reference)

15 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

## Topic 19 — Version- and State-Robust Forensics of Encrypted Messaging Applications

**Research problem.** Extracting messages from one SQLite database is routine. A research paper should measure which artifacts survive *application versions*, *device security states*, *deletion* and WAL/checkpoint behaviour.

### ► Track A — Systematic Review: Forensics of Secure/Encrypted Messaging Applications Review questions

RQ1. Which artifacts and storage locations are documented across secure messengers (device DBs, backups, key stores)?

RQ2. How is recoverability evaluated across app versions, BFU/AFU states, deletion and backup/update behaviour?

RQ3. What legal routes exist to cloud data, and where are the methodological gaps?

**Scope & search protocol.** Databases as above. String: (forensic*) AND (Signal OR Telegram OR WhatsApp OR "instant messag*" OR "secure messag*") AND (Android OR iOS OR artefact*). Window 2014–2026. PRISMA-style flow.

**Synthesis & appraisal.** Taxonomy of artefacts/apps; matrix (app, version, state, artefacts recovered, deletion recovery); appraise version/state coverage; map gaps.

► **Expected contribution.** A synthesis of what is recoverable under encryption, acquisition state and app evolution, exposing where prior single-version studies no longer hold.

### ► Track B — Practical / Experimental Contribution

**Research gap.** Measure artifact survival across app versions, device states, deletion and WAL/checkpoint behaviour for one messenger.

**Research questions.** (i) Which artifacts persist across app versions and backup states? (ii) How do before/after-first-unlock states change accessible evidence? (iii) What can be recovered after deletion, logout or database maintenance?

**Proposed design.** Researcher-owned devices/accounts and synthetic conversations; one messenger, $\geq 2$ versions; capture logical backups, app sandboxes and permitted device images at controlled states; document databases, WAL/SHM, caches, media, notifications, keystores and cloud exports; repeat send/edit/delete/reaction/attachment events with known times; compare $\geq 2$ tools or a tool against manual parsing; validate every claimed artifact.

**Evaluation & minimum evidence.** Event/artifact recall, timestamp error, deleted-item recovery, parser agreement, version survival, false-attribution rate, reproducibility; $\geq 2$ baselines; robustness + $\geq 1$ ablation; confidence intervals; reproducibility package. **Ethics:** researcher-owned accounts/devices only.

► **Expected contribution & level.** A versioned artifact-survival matrix and validation dataset for one encrypted messenger, with explicit acquisition-state limits. Master's-appropriate; strong workshop/applied-conference potential. *Publication possible, not guaranteed.*

### References (verified; source type labelled)

- [1] A. R. Onik, J. Brown, C. Walker, and I. Baggili, "A systematic literature review of secure instant messaging applications from a digital forensics perspective," *ACM Computing Surveys*, vol. 57, no. 9, 2025, doi:10.1145/3727641. (journal — systematic review)
- [2] C. Anglano, "Forensic analysis of WhatsApp Messenger on Android smartphones," *Digital Investigation*, vol. 11, no. 3, pp. 201–213, 2014. (journal — seminal)
- [3] C. Anglano, M. Canonico, and M. Guazzone, "Forensic analysis of Telegram Messenger on Android smartphones," *Digital Investigation*, vol. 23, 2017. (journal — seminal)
- [4] N. Rathi, U. Karabiyik, T. Aderibigbe, and H. Chi, "Forensic analysis of encrypted instant messaging applications on Android," in *Proc. Int. Symp. Digital Forensics and Security (ISDFS)*, 2018. (conference)
- [5] NIST SP 800-101 Rev. 1, *Guidelines on Mobile Device Forensics*, 2014. (standards-body publication)

16 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

## Topic 20 — Acquisition-State Effects on Recovery of Encrypted Data and Keys

**Research problem.** Attempting one public key recovery is a demonstration and may rely on obsolete systems. The study should *compare acquisition states* and quantify *repeatability* on contemporary, researcher-controlled encrypted systems.

### ► Track A — Systematic Review: Full-Disk / File-Based Encryption and its Impact on Investigations

#### Review questions

RQ1. Which encryption schemes (BitLocker, FileVault, LUKS, Android FBE) are studied, and how does each change acquisition?

RQ2. How is key/data recovery evaluated across acquisition states (before/after unlock, mounted, after lock), and how repeatable is it?

RQ3. What are the lawful-access boundaries and the memory-key role, and where are the gaps?

**Scope & search protocol.** Databases as above. String: ("full disk encryption" OR "file-based encryption" OR BitLocker OR FileVault OR LUKS) AND (forensic* OR "key recovery" OR acquisition). Window 2008–2026. PRISMA-style flow.

**Synthesis & appraisal.** Taxonomy of schemes/attacks; matrix (scheme, acquisition state, recovery method, reliability); appraise repeatability and currency; map gaps.

► **Expected contribution.** A synthesis of when encrypted evidence and key material are actually recoverable on *contemporary* systems, correcting claims based on obsolete platforms.

### ► Track B — Practical / Experimental Contribution

**Research gap.** Compare acquisition states and quantify repeatability of key/data recovery on contemporary, researcher-controlled encrypted systems.

**Research questions.** (i) Which evidence remains available before unlock, after first unlock, while mounted and after lock? (ii) How reliably can authorized memory acquisition recover useful key material? (iii) How do sleep, reboot, timeout and memory pressure affect recovery?

**Proposed design.** Self-created BitLocker, LUKS or Android test systems (1–2 platforms); define acquisition states and repeat each multiple times; collect memory and storage using documented, authorized procedures; compare known-key validation, mounted-volume access and memory scanning; measure acquisition disturbance and report failures. **Do not distribute secrets or bypass third-party devices.**

**Evaluation & minimum evidence.** Key-recovery success, data-access coverage, time, repeatability, false candidates, state-dependent loss, acquisition overhead; $\geq 2$ baselines; robustness + $\geq 1$ ablation; confidence intervals; reproducibility package.

► **Expected contribution & level.** A reproducible acquisition-state study showing when encrypted evidence and key material are actually recoverable and when claims no longer hold. Master's-appropriate; workshop/applied-conference potential. *Publication possible, not guaranteed.*

#### References (verified; source type labelled)

[1] T. Müller and F. C. Freiling, "A systematic assessment of the security of full disk encryption," *IEEE Trans. Dependable and Secure Computing*, vol. 12, no. 5, 2015. (journal)
[2] T. Groß, M. Busch, and T. Müller, "One key to rule them all: Recovering the master key from RAM to break Android's file-based encryption," *Forensic Science International: Digital Investigation*, vol. 36 (Suppl.), art. 301113, 2021 (DFRWS EU). (conference / journal)
[3] J. A. Halderman, S. D. Schoen, N. Heninger, *et al.*, "Lest we remember: Cold-boot attacks on encryption keys," in *Proc. USENIX Security*, 2008. (conference — foundational)
[4] Microsoft, *BitLocker security and recovery documentation*, current edition. (vendor documentation)
[5] NIST SP 800-111, *Guide to Storage Encryption Technologies for End User Devices*, 2007. (standards-body publication)

17 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

## Topic 21 — Query-Constrained Functionality-Preserving Evasion of Static Windows Malware Detectors

**Research problem.** FGSM/PGD on arbitrary features ignore executable validity. A publishable study evaluates *realizable* problem-space transformations against a genuine detector under *query*, *size* and *functionality* constraints.

► **Track A — Systematic Review: Adversarial Machine Learning against Malware Detectors**

**Review questions.**

RQ1. Which attack types exist (feature-space vs problem-space/realizable; evasion vs poisoning) against static malware detectors?

RQ2. How is realizability (validity, functionality preservation, query cost) evaluated, and how often is it verified?

RQ3. Which defences exist (adversarial training, certified/smoothed detectors), and where are the gaps?

**Scope & search protocol.** Databases as above. String: (adversarial OR evasion) AND malware AND ("machine learning" OR "deep learning") AND (Windows OR PE OR executable). Window 2015–2026. PRISMA-style flow.

**Synthesis & appraisal.** Taxonomy of attacks/defences; matrix (attack, realizability check, query budget, detector, defence); appraise functionality-preservation rigour; map gaps.

► **Expected contribution.** A synthesis separating feature-space demonstrations from realizable, functionality-preserving attacks, with an evaluation agenda for defensible robustness claims.

► **Track B — Practical / Experimental Contribution**

**Research gap.** Evaluate realizable, functionality-preserving PE transformations against a genuine detector under a bounded query budget.

**Research questions.** (i) How effective are semantics-preserving PE manipulations under limited queries? (ii) How does a query budget change evasion success? (iii) Does adversarial training or a smoothed/certified defence reduce evasion while preserving accuracy?

**Proposed design.** An open-source static detector and a public dataset; baselines = a random-transformation attack and a naive feature-space attack; apply padding/section-injection/slack transformations verified to preserve validity and behaviour in an isolated sandbox; sweep query budgets; evaluate adversarial training and a (de)randomized-smoothing defence; error analysis on failed evasions. **Ethics:** isolated lab; no operational-malware distribution.

**Evaluation & minimum evidence.** Clean detection, evasion rate vs query budget, functionality-verified success, transferability, defended accuracy/robustness trade-off; $\geq 2$ baselines; robustness + $\geq 1$ ablation; confidence intervals; reproducibility package.

► **Expected contribution & level.** A query-aware, functionality-verified evasion and defence evaluation against a real detector. Master's-appropriate; strong workshop/applied-conference potential. *Publication possible, not guaranteed.*

**References** (verified; source type labelled)

[1] L. Demetrio, S. E. Coull, B. Biggio, G. Lagorio, A. Armando, and F. Roli, "Adversarial EXEmples: A survey and experimental evaluation of practical attacks on machine learning for Windows malware detection," *ACM Trans. Privacy and Security*, vol. 24, no. 4, 2021. (journal)
[2] L. Demetrio, B. Biggio, G. Lagorio, F. Roli, and A. Armando, "Functionality-preserving black-box optimization of adversarial Windows malware," *IEEE Trans. Information Forensics and Security*, vol. 16, pp. 3469–3478, 2021. (journal)
[3] K. Lucas, M. Sharif, L. Bauer, M. K. Reiter, and S. Shintre, "Malware makeover: Breaking ML-based static analysis by modifying executable bytes," in *Proc. ACM AsiaCCS*, 2021. (conference)
[4] D. Gibert, G. Zizzo, and Q. Le, "Certified robustness of static deep learning-based malware detectors against patch and append attacks," in *Proc. 16th ACM Workshop on Artificial Intelligence and*

18 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

Security (AISec), 2023, pp. 173–184. (workshop)

[5] A. Ponte, D. Trizna, L. Demetrio, B. Biggio, I. T. Ogbu, and F. Roli, “SLIFER: Investigating performance and robustness of malware detection pipelines,” Computers & Security, vol. 150, art. 104264, 2025. (journal)

## Topic 22 — Robustness of Image-Forensic Detectors to Learned Anti-Forensic Transformations

**Research problem.** Metadata scrubbing is not deep-learning anti-forensics. The study must define an *adaptive attacker* using learned restoration/fingerprint-suppression and test whether it transfers across detectors and processing chains.

# ► Track A — Systematic Review: Anti-Forensics and Counter-Forensics for Image Integrity

**Review questions.**

RQ1. Which anti-forensic techniques exist (traditional vs learned/GAN), and which forensic traces do they target (PRNU, compression, manipulation)?

RQ2. How is anti-forensic success evaluated, and how often is transfer across detectors/processing tested?

RQ3. What counter-forensic defences exist, and where are the gaps?

**Scope & search protocol.** Databases as above. String: ("anti-forensic*" OR "counter-forensic*") AND image AND ("deep learning" OR GAN OR adversarial). Window 2011–2026. PRISMA-style flow.

**Synthesis & appraisal.** Taxonomy of anti-forensic methods; matrix (technique, target trace, transfer tested, counter-method); appraise adaptive-attacker rigour; map gaps.

► **Expected contribution.** A synthesis of how well learned anti-forensics generalises and which detectors resist it, with an adaptive-evaluation agenda.

# ► Track B — Practical / Experimental Contribution

**Research gap.** Test whether learned anti-forensic transformations transfer across detectors and processing chains, under an adaptive attacker.

**Research questions.** (i) How much do learned anti-forensic transforms reduce detector performance? (ii) Do they transfer across detectors and datasets? (iii) Do they survive benign recompression/resizing, and can detectors be hardened?

**Proposed design.** A forensic task (manipulation or camera-model detection) with ≥2 detectors; a learned anti-forensic transform (restoration/fingerprint suppression) with a non-learned baseline (e.g. metadata/noise removal); split by source; evaluate white-box (attacker-known) and black-box (transfer) settings; test post-anti-forensic recompression and adversarial-aware retraining.

**Evaluation & minimum evidence.** Detector AUROC/accuracy before/after; transfer success; visual-quality (PSNR/SSIM); survival after recompression; hardened-detector recovery; ≥2 baselines; robustness + ≥1 ablation; confidence intervals; reproducibility package.

► **Expected contribution & level.** An adaptive-attacker evaluation showing when learned anti-forensics defeats detectors and when it fails to transfer or survive processing. Master’s-appropriate; workshop/applied-conference potential. *Publication possible, not guaranteed.*

**References** (verified; source type labelled)

[1] D. Kim, H.-U. Jang, S.-M. Mun, S. Choi, and H.-K. Lee, “Median filtered image restoration and anti-forensics using adversarial networks,” IEEE Signal Processing Letters, vol. 25, no. 2, 2018. (journal)
[2] C. Chen, X. Zhao, and M. C. Stamm, “MISLGAN: An anti-forensic camera model falsification framework using a generative adversarial network,” in Proc. IEEE ICIP, 2018. (conference)
[3] J. C. Neves, R. Tolosana, R. Vera-Rodriguez, V. Lopes, H. Proença, and J. Fierrez, “GANprintR: Improved fakes and evaluation of the state of the art in face manipulation detection,” IEEE J. Selected Topics in Signal Processing, vol. 14, no. 5, 2020. (journal)

19 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

[4] M. C. Stamm and K. J. R. Liu, “Anti-forensics of digital image compression,” *IEEE Trans. Information Forensics and Security*, vol. 6, no. 3, 2011. (journal — foundational)
[5] P. Korus, “Digital image integrity — a survey of protection and verification techniques,” *Digital Signal Processing*, vol. 71, pp. 1–26, 2017. (journal — survey)

## Topic 23 — Robust Image Steganalysis under Cover-Source Mismatch

**Research problem.** An in-domain BOSSBase classifier plus a tool run is course work. The central research problem is *cover-source mismatch* across cameras, development pipelines and embedding conditions.

# ► Track A — Systematic Review: Machine-Learning Image Steganalysis

Review questions.

RQ1. Which steganalysis approaches exist (rich models vs CNN steganalysers), and for which embedding schemes?

RQ2. How is cover-source mismatch measured and mitigated across the literature?

RQ3. How does performance degrade under adaptive/unknown embedding, and where are the gaps?

**Scope & search protocol.** Databases as above. String: steganalysis AND ("deep learning" OR CNN OR "machine learning") AND (image) AND ("cover-source mismatch" OR generalis* OR robustness) Window 2012–2026. PRISMA-style flow.

**Synthesis & appraisal.** Taxonomy; matrix (method, dataset/source, embedding, mismatch handling, metrics); appraise CSM control; map gaps.

► **Expected contribution.** A synthesis of how cover-source mismatch is (rarely) controlled, and which methods generalise across sources and embeddings.

# ► Track B — Practical / Experimental Contribution

**Research gap.** Quantify and mitigate cover-source mismatch across cameras/pipelines and embedding conditions.

**Research questions.** (i) How large is the accuracy drop under camera/pipeline mismatch? (ii) Which features/architectures are most mismatch-robust? (iii) Do mismatch-mitigation strategies transfer to unseen sources and payloads?

**Proposed design.** ≥2 image sources (e.g. BOSSBase/BOWS and an ALASKA2-style realistic set); embed with ≥2 algorithms at multiple payloads; baselines = a rich-model classifier (SRM+ensemble) and a CNN steganalyser (e.g. SRNet); train/test with matched and mismatched sources; leave-one-source-out; evaluate mitigation (augmentation, domain adaptation); prevent cover-source leakage between train and test.

**Evaluation & minimum evidence.** Detection error $P_E$, AUROC, TPR at fixed FPR, matched vs mismatched gap, per-source worst-case, payload sensitivity; ≥2 baselines; robustness + ≥1 ablation; confidence intervals; reproducibility package.

► **Expected contribution & level.** A leakage-controlled evaluation of steganalysis under cover-source mismatch, quantifying which methods generalise across sources and payloads. Master’s-appropriate; strong workshop/applied-conference potential. *Publication possible, not guaranteed.*

**References** (verified; source type labelled)

[1] M. Boroumand, M. Chen, and J. Fridrich, “Deep residual network for steganalysis of digital images (SRNet),” *IEEE Trans. Information Forensics and Security*, vol. 14, no. 5, 2019. (journal)
[2] R. Cogranne, Q. Giboulot, and P. Bas, “ALASKA#2: Challenging academic research on steganalysis with realistic images,” in *Proc. IEEE WIFS*, 2020. (conference — dataset/challenge)
[3] Q. Giboulot, P. Bas, R. Cogranne, and D. Borghys, “The cover source mismatch problem in deep-learning steganalysis,” in *Proc. EUSIPCO*, 2022, pp. 1032–1036. (conference)
[4] A. Mallet, M. Beneš, and R. Cogranne, “Cover-source mismatch in steganalysis: Systematic review,” *EURASIP J. Information Security*, 2024, doi:10.1186/s13635-024-00171-6. (journal — systematic review)

20 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

[5] J. Fridrich and J. Kodovský, “Rich models for steganalysis of digital images (SRM),” IEEE Trans. Information Forensics and Security, vol. 7, no. 3, pp. 868–882, 2012. (journal — foundational)

## Topic 24 — Temporally Robust and Cost-Sensitive Detection of Illicit Bitcoin Transactions

**Research problem.** A simple Elliptic classifier or explorer tracing is not research. The paper must evaluate *future-period* performance and *limited-queue* investigative yield under severe class imbalance and drift.

# ► Track A — Systematic Review: Machine Learning for Cryptocurrency De-Anonymisation and Illicit-Transaction Detection

**Review questions.**

RQ1. Which approaches exist (clustering heuristics, graph/GNN, temporal models) for illicit-transaction detection and de-anonymisation?
RQ2. How are they evaluated — splits (random vs temporal), imbalance-aware metrics, drift, robustness to mixers?
RQ3. What is known about temporal generalisation and cost-sensitive deployment, and where are the gaps?

**Scope & search protocol.** Databases as above. String: (Bitcoin OR cryptocurrency OR blockchain) AND (illicit OR "anti-money laundering" OR de-anonymi*) AND ("machine learning" OR "graph neural network"). Window 2013–2026. PRISMA-style flow.

**Synthesis & appraisal.** Taxonomy; matrix (method, split strategy, imbalance metric, drift/robustness); appraise temporal evaluation; map gaps.

► **Expected contribution.** A synthesis exposing how random splits and threshold-free metrics overstate performance, with a temporal, cost-sensitive evaluation agenda.

# ► Track B — Practical / Experimental Contribution

**Research gap.** Evaluate illicit-transaction detection under temporal splits with imbalance-aware, cost-sensitive metrics and drift robustness.

**Research questions.** (i) How much does random splitting overstate performance versus training on the past and testing on the future? (ii) Which model gives the best yield at a fixed investigative review budget? (iii) How robust is detection to concept drift and unlabelled nodes?

**Proposed design.** The public Elliptic dataset (and, if feasible, Elliptic++); baselines = logistic regression, gradient boosting and a graph neural network; strictly temporal train/validation/test by time step; handle unknown-class nodes explicitly; evaluate precision@budget and recall at fixed alert budgets; test drift by training on early periods and testing later; ablate graph vs node features.

**Evaluation & minimum evidence.** PR-AUC, F1 on the illicit class, precision@k/recall@budget, temporal degradation, calibration, cost-weighted error; bootstrap by time block; ≥2 baselines; robustness + ≥1 ablation; confidence intervals; reproducibility package.

► **Expected contribution & level.** A temporally honest, cost-sensitive evaluation of illicit-transaction detection, quantifying real investigative yield under drift. Master’s-appropriate; strong workshop/applied-conference potential. *Publication possible, not guaranteed.*

**References** (verified; source type labelled)

[1] M. Weber, G. Domeniconi, J. Chen, D. K. I. Weidele, C. Bellei, T. Robinson, and C. E. Leiserson, “Anti-money laundering in Bitcoin: Experimenting with graph convolutional networks for financial forensics,” arXiv:1908.02591 (KDD Workshop on Anomaly Detection in Finance), 2019. (preprint — Elliptic dataset)
[2] S. Meiklejohn, M. Pomarole, G. Jordan, K. Levchenko, D. McCoy, G. M. Voelker, and S. Savage, “A fistful of Bitcoins: Characterizing payments among men with no names,” in *Proc. ACM Internet Measurement Conf. (IMC)*, 2013. (conference — foundational)
[3] F. Reid and M. Harrigan, “An analysis of anonymity in the Bitcoin system,” in *Security and Privacy in Social Networks*, Springer, 2013. (book chapter — foundational)

21 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

[4] “Machine learning on blockchain data: A systematic mapping study,” arXiv:2403.17081, 2024.
(preprint — systematic mapping)
[5] J. D. Nick, Data-Driven De-Anonymization in Bitcoin, M.Sc. thesis, ETH Zürich, 2015. (MSc thesis)

### Topic 25 — Threat-Modelled Chain of Custody using Merkle Transparency Logs and Permissioned Ledgers

**Research problem.** Building a blockchain that stores hashes and timing it is a systems exercise. The research should compare simpler *append-only transparency logs* with *permissioned blockchain* under explicit tampering, availability and governance threats.

# ▶ Track A — Systematic Review: Blockchain / Transparency Logs for Digital-Evidence Chain of Custody

**Review questions.**

RQ1. Which architectures have been proposed (public vs permissioned blockchain, signed Merkle/transparency logs) for evidence custody?
RQ2. What do they actually guarantee (integrity, timestamping, non-repudiation) versus claim, and at what performance/governance cost?
RQ3. How is legal acceptance addressed, and where are the gaps versus non-blockchain alternatives?

**Scope & search protocol.** Databases as above. String: (blockchain OR "distributed ledger" OR "transparency log") AND ("chain of custody" OR "digital evidence") AND forensic*. Window 2016–2026. PRISMA-style flow.

**Synthesis & appraisal.** Taxonomy; matrix (architecture, guarantee, threat model, performance, legal discussion); appraise threat-model rigour; map gaps.

▶ **Expected contribution.** A synthesis clarifying which custody guarantees require consensus and which a signed transparency log already provides, exposing over-claiming in the literature.

# ▶ Track B — Practical / Experimental Contribution

**Research gap.** Compare a signed Merkle transparency log with a permissioned ledger for evidence custody under a defined threat model.

**Research questions.** (i) Which guarantees require consensus and which are provided by signed Merkle logs? (ii) How do systems detect deletion, reordering, equivocation and unauthorised updates? (iii) What latency, storage and governance costs accompany each design?

**Proposed design.** Implement a signed hash-chain/Merkle log and a small permissioned-ledger baseline; define roles, trust assumptions, key-compromise and failure cases; simulate registration, transfer, verification, correction and authorised disposal; inject alteration, deletion, reordering, replay, equivocation and node unavailability; measure verification scalability; produce human-auditable chain-of-custody reports.

**Evaluation & minimum evidence.** Tamper-detection coverage, false alarms, write/verify latency, throughput, storage, proof size, recovery time, governance complexity; ≥2 baselines; robustness + ≥1 ablation; confidence intervals; reproducibility package.

▶ **Expected contribution & level.** A comparative security and performance evaluation showing when blockchain adds value beyond a signed transparency log. Master’s-appropriate; workshop/applied-conference potential. *Publication possible, not guaranteed.*

**References** (verified; source type labelled)

[1] A. H. Lone and R. N. Mir, “Forensic-chain: Blockchain based digital forensics chain of custody with PoC in Hyperledger Composer,” *Digital Investigation*, vol. 28, pp. 44–55, 2019. (journal)
[2] Z. Tian, M. Li, M. Qiu, Y. Sun, and S. Su, “Block-DEF: A secure digital evidence framework using blockchain,” *Information Sciences*, vol. 491, 2019. (journal)
[3] D. Billard, “Weighted forensics evidence using blockchain,” in *Proc. Int. Conf. Computing and Big Data (ICCBB)*, 2018. (conference)
[4] IETF RFC 9162, *Certificate Transparency Version 2.0*, 2021. (Internet standard — Merkle transparency

22 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

logs)

[5] NIST IR 8387, Digital Evidence Preservation: Considerations for Evidence Handlers, 2022. (standards-body publication)

## Topic 27 — Cost-Sensitive and Temporally Robust Insider-Threat Detection

**Research problem.** Running anomaly detection on a random CERT subset is common and can leak scenario patterns. The contribution is a *temporal*, *user-held-out* and *review-budget* evaluation with explicit false-alert costs.

# ► Track A — Systematic Review: Machine Learning for Insider-Threat Detection

Review questions.

RQ1. Which detection approaches exist (statistical/UEBA, sequence, graph), and on which datasets (notably CERT)?
RQ2. How are they evaluated — splitting (random vs temporal/user-disjoint), class imbalance, alert-budget metrics?
RQ3. What is known about generalisation to unseen users/scenarios and false-alert cost, and where are the gaps?

**Scope & search protocol.** Databases as above. String: "insider threat" AND (detection) AND ("machine learning" OR "anomaly detection" OR "user behavior"). Window 2013–2026. PRISMA-style flow.

**Synthesis & appraisal.** Taxonomy; matrix (method, dataset, split strategy, imbalance, budget metric); appraise temporal/leakage control; map gaps.

► **Expected contribution.** A synthesis exposing how random splits and threshold-free metrics overstate insider-threat detection, with a temporal, cost-sensitive evaluation agenda.

# ► Track B — Practical / Experimental Contribution

**Research gap.** Evaluate detection under temporal and user/scenario-disjoint splits with alert-budget and false-alert cost metrics.

**Research questions.** (i) How much do random splits inflate detection? (ii) Which behavioural features generalise to unseen users and scenarios? (iii) Which detector maximises detection under a fixed daily review capacity?

**Proposed design.** A documented CERT Insider-Threat release preserving scenario chronology; baselines = rules/statistics, isolation forest and one sequence/representation model; temporal, user-held-out and scenario-held-out tests; simulate daily alert queues and delayed labels; user-level aggregation; ablate email/web/logon/file/removable-media sources; privacy-impact discussion.

**Evaluation & minimum evidence.** Scenario/user recall, time-to-detection, PR-AUC, alerts per user-day, precision@k, investigation burden, calibration, worst-scenario performance; ≥2 baselines; robustness + ≥1 ablation; confidence intervals; reproducibility package.

► **Expected contribution & level.** An operational insider-threat benchmark connecting temporal generalisation to analyst workload and privacy cost. Master's-appropriate; strong workshop/applied-conference potential. *Publication possible, not guaranteed.*

**References** (verified; source type labelled)

[1] J. Glasser and B. Lindauer, "Bridging the gap: A pragmatic approach to generating insider threat data," in *Proc. IEEE Security and Privacy Workshops (SPW)*, 2013. (conference — CERT dataset)
[2] G. Gavai, K. Sricharan, D. Gunning, J. Hanley, M. Singhal, and R. Rolleston, "Supervised and unsupervised methods to detect insider threat from enterprise social and online activity data," *J. Wireless Mobile Networks, Ubiquitous Computing, and Dependable Applications (JoWUA)*, vol. 6, no. 4, pp. 47–63, 2015. (journal)
[3] A. Tuor, S. Kaplan, B. Hutchinson, N. Nichols, and S. Robinson, "Deep learning for unsupervised insider threat detection in structured cybersecurity data streams," arXiv:1710.00811 (AAAI Workshops), 2017. (preprint / workshop)

23 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

[4] D. C. Le and A. N. Zincir-Heywood, “Evaluating insider threat detection workflow using supervised and unsupervised learning,” in Proc. IEEE Security and Privacy Workshops (SPW), 2018, pp. 270–275. (conference)
[5] A. L. Buczak and E. Guven, “A survey of data mining and machine learning methods for cyber security intrusion detection,” IEEE Communications Surveys & Tutorials, vol. 18, no. 2, 2016. (journal — survey)

## Topic 29 — Uncertainty-Aware Ransomware Incident Reconstruction from Heterogeneous Telemetry

**Research problem.** Mapping a public case to ATT&CK is analytical coursework. The research should reconstruct a controlled attack from endpoint, identity and network telemetry and quantify which conclusions survive missing evidence.

### ► Track A — Systematic Review: Ransomware Incident Reconstruction and Attribution Review questions

RQ1. Which reconstruction/attribution approaches exist, and which telemetry sources and indicators (IOCs, TTPs) do they use?

RQ2. How is reconstruction accuracy/completeness evaluated, and how is uncertainty handled?

RQ3. What are the attribution limits, and where are the gaps?

**Scope & search protocol.** Databases as above. String: ransomware AND (forensic* OR reconstruction OR attribution OR "incident response") AND (telemetry OR "kill chain" OR ATT&CK). Window 2017–2026. PRISMA-style flow.

**Synthesis & appraisal.** Taxonomy of methods/indicators; matrix (telemetry sources, method, evaluation, uncertainty); appraise ground-truth rigour; map gaps.

► **Expected contribution.** A synthesis of how ransomware reconstruction is (rarely) evaluated against ground truth and how uncertainty is (rarely) reported, with a methodology agenda.

### ► Track B — Practical / Experimental Contribution

**Research gap.** Reconstruct a controlled attack from heterogeneous telemetry and quantify which conclusions survive missing evidence and clock disagreement.

**Research questions.** (i) Which telemetry sources are necessary for accurate stage reconstruction? (ii) How do missing logs and clock disagreement affect ordering and root cause? (iii) Can competing hypotheses be ranked with traceable evidence?

**Proposed design.** An isolated ransomware-emulation dataset or safely generated ATT&CK-aligned benign simulations; collect endpoint, Windows event, authentication, DNS/proxy and network telemetry; a ground-truth action sequence and provenance graph; compare manual/rule reconstruction with one automated correlation method; ablate each source; inject log loss, clock skew and decoy indicators.

**No live malware propagation.**

**Evaluation & minimum evidence.** Stage/event precision/recall, ordering accuracy, root-cause accuracy, time-to-reconstruct, provenance coverage, degradation after source loss; ≥2 baselines; robustness + ≥1 ablation; confidence intervals; reproducibility package.

► **Expected contribution & level.** A ground-truthed reconstruction benchmark with explicit source-ablation and uncertainty reporting. Master’s-appropriate; workshop/applied-conference potential. *Publication possible, not guaranteed.*

### References (verified; source type labelled)

[1] H. Oz, A. Aris, A. Levi, and A. S. Uluagac, “A survey on ransomware: Evolution, taxonomy, and defense solutions,” ACM Computing Surveys, vol. 54, no. 11s, 2022. (journal — survey)
[2] B. E. Strom, A. Applebaum, D. P. Miller, K. C. Nickels, A. G. Pennington, and C. B. Thomas, MITRE ATT&CK: Design and Philosophy, MITRE Technical Report, 2020. (technical report)
[3] MITRE, ATT&CK Enterprise knowledge base, current version. (knowledge base)
[4] Cybersecurity and Infrastructure Security Agency (CISA), #StopRansomware Guide, current edi-

24 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

tion. (government guidance)

[5] M. Akbanov, V. G. Vassilakis, and M. D. Logothetis, “WannaCry ransomware: Analysis of infection, persistence, recovery prevention and propagation mechanisms,” J. Telecommunications and Information Technology, 2019. (journal)

[6] P. Pols, The Unified Kill Chain: Designing a Unified Kill Chain for Analyzing, Comparing and Defending against Cyber Attacks, M.Sc. thesis, Cyber Security Academy (Leiden/Delft), 2017. (MSc thesis)

### Topic 30 — Temporal and Cross-Dataset Generalization of Network Intrusion Reconstruction Models

Research problem. A classifier on UNSW-NB15 or CIC-IDS with a random split is heavily studied. The revised topic evaluates generalisation, label realism and attack-stage reconstruction rather than another accuracy comparison.

▶ Track A — Systematic Review: Machine-Learning Network Intrusion Detection and Reconstruction

Review questions.

RQ1. Which ML/DL intrusion-detection approaches exist, and on which benchmark datasets?

RQ2. How are they evaluated — splits (random vs temporal/cross-dataset), duplication/label issues, encrypted traffic?

RQ3. What is known about cross-dataset generalisation and attack-stage reconstruction, and where are the gaps?

Scope & search protocol. Databases as above. String: ("intrusion detection" OR "network forensic*") AND ("deep learning" OR "machine learning") AND (UNSW-NB15 OR CIC-IDS OR generalis* OR cross-dataset). Window 2015–2026. PRISMA-style flow.

Synthesis & appraisal. Taxonomy; matrix (dataset, split, features, generalisation tested, reconstruction); appraise dataset weaknesses and evaluation rigour; map gaps.

▶ Expected contribution. A synthesis exposing how random splits and dataset artefacts inflate NIDS results, with a cross-dataset, temporally honest evaluation agenda.

▶ Track B — Practical / Experimental Contribution

Research gap. Evaluate detection and attack-stage reconstruction under temporal and cross-dataset shift, not another same-split accuracy comparison.

Research questions. (i) How much do random flows and duplicated records inflate results? (ii) Which feature sets generalise across days, networks and datasets? (iii) Can predicted flows support correct incident-stage reconstruction?

Proposed design. UNSW-NB15 or CIC-IDS2017 plus a second compatible corpus or held-out capture period; remove duplicates and identifiers; split chronologically and by capture scenario; baselines = rules/logistic regression, gradient boosting and one sequence/graph model; test encrypted-feature subsets, missing packets, sampling and unseen attack classes; aggregate flow predictions into incident timelines and assess reconstruction separately.

Evaluation & minimum evidence. Per-class PR-AUC/F1, TPR at low FPR, calibration, worst-day/cross-dataset performance, event-stage recall, timeline ordering accuracy; ≥2 baselines; robustness + ≥1 ablation; confidence intervals; reproducibility package.

▶ Expected contribution & level. A reproducible demonstration of how dataset and temporal shift affect both detection and downstream incident reconstruction. Master’s-appropriate; workshop/applied-conference potential. Publication possible, not guaranteed.

References (verified; source type labelled)

[1] N. Moustafa and J. Slay, “UNSW-NB15: A comprehensive data set for network intrusion detection systems,” in Proc. Military Communications and Information Systems Conf. (MilCIS), 2015. (conference — dataset)

[2] I. Sharafaldin, A. H. Lashkari, and A. A. Ghorbani, “Toward generating a new intrusion detection

25 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

dataset and intrusion traffic characterization,” in Proc. ICISSP, 2018. (conference — CIC-IDS2017 dataset)

[3] M. Ring, S. Wunderlich, D. Scheuring, D. Landes, and A. Hotho, “A survey of network-based intrusion detection data sets,” Computers & Security, vol. 86, pp. 147–167, 2019. (journal — survey)

[4] A. Khraisat, I. Gondal, P. Vamplew, and J. Kamruzzaman, “Survey of intrusion detection systems: Techniques, datasets and challenges,” Cybersecurity, vol. 2, 2019. (journal — survey)

[5] A. L. Buczak and E. Guven, “A survey of data mining and machine learning methods for cyber security intrusion detection,” IEEE Communications Surveys & Tutorials, vol. 18, no. 2, 2016. (journal — survey)

### Topic 31 — Operationalizing Reliability and Authentication Requirements for AI-Derived Digital Forensic Evidence

Research problem. A single-author checklist is not validated research. The revised study maps legal requirements to observable tests, evaluates real tool outputs, and measures agreement between independent assessors. Note: this is a legal/doctrinal + evaluation topic; Track B is analytical, not an ML experiment.

▶ Track A — Systematic Review: Admissibility and Reliability of AI-Derived / AI-Generated Evidence

Review questions.

RQ1. Which legal requirements (Daubert factors, FRE 702/901, ISO/IEC 27037) govern AI-derived and AI-generated evidence?

RQ2. Which requirements are technically testable, and how have tools/methods been assessed against them?

RQ3. How are courts and rule-makers responding (case law; proposed rules), and where are the gaps?

Scope & search protocol. Legal databases and IEEE Xplore/ScienceDirect. Scope to United States federal evidence law and one AI-forensics use case. String: ("AI" OR "machine learning" OR deepfake) AND (evidence OR admissibility OR authentication) AND (Daubert OR "Rule 702" OR "Rule 901" OR "ISO 27037"). Window 2018–2026 plus controlling authority. PRISMA-style flow for the technical literature; structured legal analysis for authorities.

Synthesis & appraisal. Map legal requirements to testable criteria; matrix (requirement, testable?, tool evidence, case/rule support); appraise how technical scores are (mis)equated with legal admissibility; map gaps.

▶ Expected contribution. A traceable synthesis separating what is technically testable from what remains a legal judgment, exposing the conflation of accuracy with admissibility.

▶ Track B — Practical / Experimental Contribution

Research gap. A traceable, empirically evaluated framework mapping legal requirements to tests, applied to real tools with independent assessors.

Research questions. (i) Which legal requirements are technically testable and which remain legal judgments? (ii) Do accuracy rankings differ from forensic-readiness rankings? (iii) How consistently can independent evaluators apply the framework?

Proposed design. Map Rules 702/901, Daubert and ISO/IEC 27037 to evidence requirements and tests; evaluate 2–3 AI forensic tools on in-domain, external and degraded samples; test repeatability, versioning, logging, calibration and explanation stability; run a documentation-ablation and an independent-evaluator study permitting an “insufficient information” verdict.

Evaluation & minimum evidence. Tool accuracy/calibration/robustness; framework coverage; inter-rater agreement (Cohen’s κ); completion time; indeterminate-criteria rate; sensitivity to weights; ≥2 tools; ablation; confidence intervals where applicable; reproducible protocol.

▶ Expected contribution & level. A traceable, empirically evaluated framework for assessing AI-derived forensic output without confusing technical scores with legal admissibility. Master’s-appropriate; strong potential for a legal-technology or forensics venue. Publication possible, not guar-

26 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

anteed.

**References** (verified; source type labelled)

[1] *Federal Rules of Evidence* 702 and 901, current text. (primary legal source)
[2] *Daubert v. Merrell Dow Pharmaceuticals, Inc.*, 509 U.S. 579 (1993). (controlling case law)
[3] P. W. Grimm, M. R. Grossman, and G. V. Cormack, “Artificial intelligence as evidence,” *Northwestern J. Technology and Intellectual Property*, vol. 19, no. 1, pp. 9–106, 2021. (law-review article)
[4] M. R. Grossman and P. W. Grimm, “Judicial approaches to acknowledged and unacknowledged AI-generated evidence,” *Columbia Science & Technology Law Review*, 2025. (law-review article)
[5] “The admissibility of digital evidence from open-source forensic tools: Development of a framework for legal acceptance,” *PLOS ONE*, 2025. (journal)
[6] U.S. Judicial Conference, Advisory Committee on Evidence Rules, proposed *Federal Rule of Evidence 707* (“Machine-Generated Evidence”) and Rule 901(c), 2024–2026. (proposed/developing rules — not settled law)

# **Topic 32 — Privacy-Aware Digital Incident Investigation under Saudi Arabia’s PDPL and NCA Controls**

**Research problem.** A legal mapping applied to one fictional case is coursework. The revised paper implements and evaluates a *progressive acquisition workflow* that maps Saudi requirements to technical decisions and audit evidence. *Legal/analytical topic; Track B is a workflow evaluation, not an ML experiment.*

# **► Track A — Systematic Review: The Saudi Legal–Regulatory Frame for Digital Investigations**

**Review questions.**

RQ1. How do the PDPL, its implementing and transfer regulations, NCA controls and the Anti-Cyber Crime Law govern lawful collection, breach notification, consent and cross-border transfer?
RQ2. Which requirements apply at each investigation stage, and how are the roles of SDAIA and the NCA delineated?
RQ3. How does the Saudi frame compare with international frameworks (Budapest Convention, GDPR), and where are the gaps?

**Scope & search protocol.** Official Saudi instruments (SDAIA, NCA), plus comparative legal sources. Structured doctrinal analysis of primary instruments; comparative mapping against the Budapest Convention (*Saudi Arabia is not a party*) and GDPR.

**Synthesis & appraisal.** A traceability matrix (instrument → requirement → investigation stage); comparison table vs international frameworks; appraise coverage and procedural/e-evidence provisions; map gaps.

**► Expected contribution.** A structured, sourced analysis of the Kingdom-first legal frame for digital investigations and its gaps relative to international standards.

# **► Track B — Practical / Experimental Contribution**

**Research gap.** Implement and evaluate a progressive-acquisition workflow that maps Saudi requirements to technical decisions and audit evidence.

**Research questions.** (i) Which PDPL and NCA requirements apply at each investigation stage? (ii) Can progressive acquisition reduce irrelevant personal-data exposure without losing critical evidence? (iii) How consistently can analysts apply authorisation, notification and transfer decisions?

**Proposed design.** Build a traceability matrix for the PDPL, implementing/transfer regulations, ECC-2:2024 and evidence handling; create synthetic insider/account-compromise/ransomware scenarios with relevant and irrelevant personal data; compare full, selective and progressive acquisition; implement role-based approval, sensitivity classification, logging, retention and cross-border/cloud variants; two assessors record ambiguous items needing qualified legal review.

**Evaluation & minimum evidence.** Relevant-artifact recall, investigation accuracy/time, irrelevant/sensitive-

27 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

data exposure, access count, audit completeness, inter-rater agreement; ≥2 acquisition baselines; ablation; reproducible protocol.

► **Expected contribution & level.** An evaluated Saudi privacy-aware forensic workflow quantifying evidence completeness, privacy exposure, delay and decision consistency. Master's-appropriate; strong local/regional relevance. *Publication possible, not guaranteed.*

**References** (verified; source type labelled)

[1] Kingdom of Saudi Arabia, *Personal Data Protection Law*, Royal Decree No. M/19 (1443H/2021), amended by Royal Decree No. M/148 (1444H/2023). (primary law)
[2] Saudi Data & AI Authority (SDAIA), *Implementing Regulation of the Personal Data Protection Law*, 2023. (primary regulation)
[3] SDAIA, *Regulation on Personal Data Transfer outside the Kingdom*, 2023 (and updates). (primary regulation)
[4] National Cybersecurity Authority (NCA), *Essential Cybersecurity Controls* ECC-2:2024. (regulatory controls)
[5] Kingdom of Saudi Arabia, *Anti-Cyber Crime Law*, Royal Decree No. M/17 (1428H/2007). (primary law — governing)
[6] Council of Europe, *Convention on Cybercrime* (Budapest Convention, ETS No. 185), 2001 — for comparison; **Saudi Arabia is not a party (status: NA)**. (international instrument — comparison only)

### Topic 33 — Selective Acquisition with Verifiable Redaction for Privacy-Preserving Digital Forensic Triage

**Research problem.** A toy encrypted query or differentially private statistic does not establish forensic validity. The revised work evaluates *selective acquisition*, *progressive disclosure* and *cryptographically verifiable redaction*.

► **Track A — Systematic Review: Privacy-Preserving Digital Forensics**

**Review questions.**

RQ1. Which privacy-preserving techniques exist (selective disclosure/redaction, differential privacy, encryption-aware search, verifiable manifests)?

RQ2. How is the privacy-evidence trade-off measured, and how is redaction integrity guaranteed?

RQ3. How do techniques reconcile investigation with data-protection duties, and where are the gaps?

**Scope & search protocol.** Databases as above. String: ("privacy-preserving" OR "selective acquisition" OR redaction OR "differential privacy") AND ("digital forensic*" OR "evidence"). Window 2012–2026. PRISMA-style flow.

**Synthesis & appraisal.** Taxonomy; matrix (technique, privacy metric, evidence recall, integrity guarantee); appraise forensic-validity rigour; map gaps.

► **Expected contribution.** A synthesis of the privacy-evidence trade-off and of which techniques provide verifiable, admissible privacy preservation.

► **Track B — Practical / Experimental Contribution**

**Research gap.** Evaluate selective acquisition and progressive disclosure with cryptographically verifiable redaction, quantifying the privacy-evidence frontier.

**Research questions.** (i) How much irrelevant personal data can selective acquisition avoid? (ii) What evidence and exculpatory context are lost at different minimisation levels? (iii) Can cryptographic manifests detect alteration and support reproducible disclosure?

**Proposed design.** A synthetic filesystem/email corpus with relevant, sensitive, irrelevant and exculpatory ground truth; compare full, keyword, metadata-scoped, combined and progressive acquisition; create signed manifests and Merkle commitments with inclusion proofs; record redactions and policy versions; test modification, substitution, omission and unauthorised expansion; repeat with a second examiner; report the evidence-recall/privacy-exposure Pareto frontier.

28 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

**Evaluation & minimum evidence.** Relevant/exculpatory recall, irrelevant/sensitive exposure, exposure per relevant artifact, tamper detection, proof size/time, examiner reproducibility; ≥2 baselines; robustness + ≥1 ablation; confidence intervals; reproducibility package.

► **Expected contribution & level.** An open, verifiable workflow and benchmark for the privacy-evidence trade-off in progressive forensic disclosure. Master's-appropriate; strong workshop/applied-conference potential. *Publication possible, not guaranteed.*

**References** (verified; source type labelled)

[1] G. Horsman, "Defining principles for preserving privacy in digital forensic examinations," *Forensic Science International: Digital Investigation*, vol. 40, art. 301350, 2022. (journal)
[2] T. B. Ogunseyi and O. M. Adedayo, "Cryptographic techniques for data privacy in digital forensics," *IEEE Access*, vol. 11, pp. 142392–142410, 2023, doi:10.1109/ACCESS.2023.3343360. (journal)
[3] F. Armknecht and A. Dewald, "Privacy-preserving email forensics," *Digital Investigation*, vol. 14, pp. S127–S136, 2015. (journal)
[4] A. Nieto, R. Rios, and J. Lopez, "IoT-forensics meets privacy: Towards cooperative digital investigations," *Sensors*, vol. 18, no. 2, art. 492, 2018. (journal)
[5] NIST IR 8387, *Digital Evidence Preservation: Considerations for Evidence Handlers*, 2022. (standards-body publication)

## Topic 34 — Validated Digital-Forensic Readiness Maturity Model for Organizations

**Research problem.** Applying a checklist to one scenario is an assessment exercise. A research contribution requires transparent model construction, *independent scoring, scenario validation*, and evidence that maturity levels *predict* investigative capability.

► **Track A — Systematic Review: Digital-Forensic Readiness Frameworks and Maturity Models**

**Review questions.**

RQ1. Which forensic-readiness frameworks and maturity models exist (Rowlingson; ISO/IEC 27043/27035; NIST/NCA guidance)?

RQ2. Which readiness capabilities are supported by standards and practice, and how is readiness measured?

RQ3. Is there evidence that maturity predicts investigative capability, and where are the gaps?

**Scope & search protocol.** Databases and standards bodies. String: ("forensic readiness" OR "digital forensic readiness") AND (maturity OR framework OR standard OR ISO). Window 2001–2026. PRISMA-style flow; standards reviewed directly.

**Synthesis & appraisal.** Taxonomy of capabilities; matrix (framework, standard basis, measurement method, validation); appraise reliability/validation evidence; map gaps.

► **Expected contribution.** A synthesis of readiness capabilities grounded in standards and of how (rarely) maturity instruments are validated, with a measurement agenda.

► **Track B — Practical / Experimental Contribution**

**Research gap.** Develop a standards-traceable maturity instrument whose scores are reproducible and linked to measured incident-investigation outcomes.

**Research questions.** (i) Which readiness capabilities are supported by current standards and practice? (ii) Can independent assessors score the model consistently? (iii) Do maturity scores predict performance in simulated incidents?

**Proposed design.** Derive capabilities from ISO/IEC 27043, 27037, 27035 and current NIST/NCA guidance; define observable evidence and maturity anchors (governance, logging, time, retention, acquisition, cloud, personnel, testing); independent assessors score several synthetic organisations or willing participants; run tabletop incidents; measure evidence availability, time and reconstruction accuracy; revise ambiguous criteria; test inter-rater reliability and weighting sensitivity.

**Evaluation & minimum evidence.** Inter-rater agreement, assessment time, missing-evidence rate,

29 of 30

CS 616 — Digital Crime and Forensics

Research Topics — Two-Track Handbook

reconstruction accuracy, time-to-evidence, criterion discrimination, weight sensitivity; ≥2 assessors; ablation; reproducible instrument and protocol.

► **Expected contribution & level.** A standards-traceable maturity model whose scores are reproducible and linked to measured investigation outcomes. Master's-appropriate; workshop/applied-conference potential. *Publication possible, not guaranteed.*

**References** (verified; source type labelled)

[1] R. Rowlingson, "A ten step process for forensic readiness," *Int. J. Digital Evidence*, vol. 2, no. 3, 2004. (journal — foundational)
[2] ISO/IEC 27043:2015, *Incident investigation principles and processes*; ISO/IEC 27037:2012, *Digital evidence handling*; ISO/IEC 27035 series, *Information security incident management*. (international standards)
[3] ISO/IEC 30121:2015, *Governance of digital forensic risk framework*. (international standard)
[4] NIST SP 800-61 Rev. 3, *Incident Response Recommendations and Considerations for Cybersecurity Risk Management*, 2025. (standards-body publication)
[5] G. Horsman, "The importance of digital evidence strategies," *WIREs Forensic Science*, vol. 6, no. 1, e1507, 2024. (journal)

30 of 30
