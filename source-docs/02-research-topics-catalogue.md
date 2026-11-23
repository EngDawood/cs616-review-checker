# CS 616 — Research Paper Topic Catalogue

> Auto-extracted from the course PDF (text layer; glyph-level fixes applied for ligatures/dashes). Tables/layout may differ from the PDF — the PDF is the authority.

<!-- page 1 -->
Digital Crime and Forensics (CS 616)
Research Paper — Topic Catalogue
CS 616 · Digital Crime and Forensics · examples for students to select from
How to use this list. Each entry below is a starting point, not a fixed title — you may
narrow, combine, or adapt a topic in agreement with the instructor. Choose something that
genuinely interests you and that you can support with the course sources and recent literature. Your paper is assessed by the instructor (it need not be published) and runs on four
milestones: a proposal in Week 4, a draft in Week 9, the final paper in Week 13, and
a presentation in Week 14. A strong choice states a clear question, engages real forensic
evidence or a concrete method, and connects to the legal and ethical frame studied in this
course.
Where the topics come from. The catalogue draws on the course's primary text (Easttom), Moustafa's Digital Forensics in the Era of Artificial Intelligence, the 2025 collection
Digital Forensics and Cyber Crime Investigation: Recent Advances and Future Directions
(Abd El-Latif et al.), and the most recent “hot” directions in the field (2025–2026).
1 · Artificial Intelligence and Machine Learning in Forensics
1. Machine-Learning Pipelines for Automated Evidence Triage
Modern cases involve terabytes of seized data, and investigators must decide what to examine
first. This topic studies how supervised machine-learning models can rank and classify documents,
images, and logs so that the most relevant artefacts surface early. Building on Moustafa's treatment
of machine learning across the investigation workflow, the paper would cover feature extraction,
model choice (support-vector machines, random forests, neural networks), evaluation with precision
and recall, and the serious consequences of misclassification when the output may become evidence.
2. Deep Learning for Malware Detection and Family Attribution
Deep models can classify malware directly from binaries, opcode sequences, or behavioural traces
and can attribute a sample to a known family or campaign. The paper would compare convolutional
and recurrent architectures, survey the standard datasets, and weigh detection accuracy against
evasion by obfuscation and packing. A forensic angle asks how such attribution could be presented
in court and how a defence might challenge it.
3. Explainable AI for Forensic Evidence
Because AI findings must satisfy reliability standards such as Daubert and ISO/IEC 27037, a
model's decision cannot be an unexaminable “black box.” This topic examines explainability methods (for example SHAP, LIME, and attention visualisation) that make a classifier's reasoning
transparent, and analyses the real tension between the accuracy of complex models and the court's
need for interpretable, reproducible justification.


<!-- page 2 -->
Digital Crime and Forensics (CS 616)
Research Paper — Topic Catalogue
4. Neural Networks for Face-Sketch Synthesis and Suspect Identification
Drawing on the Abd El-Latif collection, this topic explores deep-learning models that turn descriptions or low-quality captures into photorealistic facial images to support identification. The paper
would assess accuracy, demographic bias, and the evidentiary risks of presenting a synthesised
likeness, treating the technique as an investigative lead rather than proof.
2 · Deepfakes, Image Integrity, and Multimedia Forensics
5. Deepfake Video Detection: Techniques and Limits
Synthetic video now fuels fraud and disinformation, and detection is an active arms race. The
paper would survey current approaches — physiological-signal analysis, multimodal audio-video
inconsistency detection, and generator “fingerprinting” — and evaluate how robust they remain as
generative models improve, using recent 2025 cases to ground the discussion.
6. Deepfake Attribution: Tracing Synthetic Media to Its Source Model
Beyond deciding whether media is fake, attribution asks which model produced it.
This topic
studies model-attribution techniques (such as spatio-temporal networks for face-swap attribution)
and argues their forensic value for linking fabricated media to a tool, actor, or campaign, along
with their current limitations.
7. Image-Forgery Detection with Deep Learning
Copy-move, splicing, and inpainting manipulations can be exposed by deep networks trained on
forgery datasets. The paper would review these methods and, importantly for this course, show how
their output is corroborated with the EXIF and metadata analysis studied in the image-forensics
week.
8. Chaotic Watermarking for Tamper Detection
Fragile and semi-fragile watermarks embedded with chaotic maps can reveal whether an image or
video has been altered and even localise the change. Following the Abd El-Latif collection, the
paper would compare schemes on robustness, security, and practical forensic use for proving media
integrity.
9. Source-Camera Identification from Sensor Noise
Every camera sensor leaves a subtle, near-unique noise pattern (PRNU) that can tie an image to
a specific device. The paper would explain the technique and critically test its reliability after
compression, editing, and social-media re-encoding — the conditions real evidence usually arrives
in.
3 · Large Language Models and Automation in Investigations
10. Large Language Models as Forensic Assistants
This topic maps where LLMs genuinely help across the investigation process — generating keyword
lists, summarising logs and narratives, and drafting reports — using the DFRWS process model as
a frame. Its critical core is the tension between the probabilistic, sometimes hallucinating nature
of LLM output and the deterministic, reproducible, court-admissible standard forensics demands.
11. Benchmarking and Validating AI Forensic Tools
If investigators are to trust AI-generated analysis or code, it must be measured. The paper would
examine emerging benchmarks (such as AutoDFBench evaluated against NIST's Computer Forensics Tool Testing datasets) and propose the validation controls needed to preserve forensic integrity
when AI is in the loop.
2


<!-- page 3 -->
Digital Crime and Forensics (CS 616)
Research Paper — Topic Catalogue
12. Automated Timeline Reconstruction from Heterogeneous Artefacts
Investigations succeed by fusing many sources into one coherent sequence of events. This topic
studies rule-based and machine-learning (or LLM-assisted) methods that merge logs, file metadata,
and device records into a single timeline — exactly the multi-source fusion demonstrated in the
running case — and evaluates accuracy and error handling.
13. Natural-Language Processing for Communications Evidence
Chats, emails, and social-media posts are central to many cases. The paper would examine NLP
techniques for authorship attribution, threat and sentiment detection, and entity extraction, and
would confront the privacy limits and bias risks of analysing personal communications at scale.
4 · Cloud, IoT, and Emerging Environments
14. Cloud Forensics: Evidence Acquisition Across Jurisdictions
Cloud evidence is volatile, multi-tenant, provider-controlled, and frequently cross-border.
The
paper would analyse these acquisition and chain-of-custody challenges and evaluate recent AIdriven automation frameworks and the “Digital Forensics as a Service” model, with attention to
the legal process required for cross-border data.
15. IoT and Smart-Home Forensics
Evidence in the Internet of Things is scattered across the device, its companion app, the vendor
cloud, and the network. Building on the course's mobile and IoT week, the paper would evaluate
practical acquisition strategies for smart cameras, wearables, speakers, and access-control logs, and
how their timestamps establish presence.
16. Connected-Vehicle (Automotive) Forensics
Modern vehicles record a surprising amount of data across infotainment, telematics, and eventdata recorders. This topic investigates what can be recovered, how it reconstructs movements and
incidents, and the tooling and legal constraints involved.
17. Drone and UAV Forensics
Drones and their controllers store flight logs, telemetry, and media that can place a device — and,
with care, an operator — at a location and time. The paper would survey acquisition methods and
the attribution challenge of linking operation to a suspect.
5 · Memory, Mobile, and Device Forensics
18. Advances in Memory Forensics and Anti-Forensic Evasion
Volatile memory holds keys, injected code, and hidden processes that never touch disk. Extending
the course's memory week, the paper would study modern acquisition and analysis and the techniques attackers use to evade it, such as process injection and direct-kernel-object manipulation.
19. Mobile Forensics of Encrypted Messengers
Apps such as Signal, Telegram, and WhatsApp protect data aggressively, yet artefacts often survive
on the device or in cloud backups. The paper would examine what is recoverable given encryption
and the before/after-first-unlock state, and the legal routes to obtain the rest.
20. Full-Disk and File-Based Encryption: Impact on Investigations
Default encryption (BitLocker, FileVault, Android file-based encryption) has reshaped acquisition
strategy. This topic analyses how encryption changes the investigator's options, the decisive role
of memory-resident keys, and the boundaries of lawful access.
3


<!-- page 4 -->
Digital Crime and Forensics (CS 616)
Research Paper — Topic Catalogue
6 · Anti-Forensics, Adversarial Machine Learning, and Robustness
21. Adversarial Attacks on AI Forensic Tools
The same models that aid investigators can be fooled. The paper would study adversarial examples and data poisoning against malware, deepfake, and forgery detectors, and defences such as
adversarial training — a pressing robustness question as AI enters the courtroom.
22. Deep-Learning-Based Anti-Forensics
Generative models can erase traces or fabricate plausible ones, from hiding manipulation to synthesising convincing metadata. Following the Abd El-Latif collection, the paper would survey these
anti-forensic techniques and the counter-methods forensics can deploy.
23. Machine-Learning Steganalysis and Data-Hiding Detection
Building on the course's steganography week, this topic studies machine-learning steganalysis across
images, audio, and network channels, and tests its limits against adaptive, content-aware embedding.
7 · Blockchain, Cryptocurrency, and Emerging Technology
24. Cryptocurrency Transaction Tracing and De-Anonymisation
Financial-crime cases increasingly turn on following funds on-chain. The paper would study clustering and heuristic techniques to trace transactions through mixers and tumblers and to link
addresses to real-world actors, along with the limits imposed by privacy coins.
25. Blockchain for Evidence Integrity and Chain of Custody
Several proposals use blockchain or Hyperledger to make custody records tamper-evident. Echoing
the Abd El-Latif smart-city and healthcare chapters, the paper would weigh the integrity benefits
against practicality, performance, and legal acceptance.
26. Forensics of Smart Contracts and DeFi Exploits
Decentralised finance has produced a new class of attacks. This topic examines methods to analyse
malicious smart contracts and to reconstruct an exploit from on-chain evidence.
8 · Incident Response, Insider Threat, and Enterprise Forensics
27. Machine-Learning Analytics for Insider-Threat Detection
Insiders hold legitimate access, so detection is behavioural. Mirroring the running insider-exfiltration
case, the paper would study user-and-entity behaviour analytics that flag after-hours access, bulk
copies, and anomalous data movement, and would weigh the real cost of false positives.
28. AI-Assisted SIEM Triage and Alert Correlation
Security operations drown in alerts. This topic investigates how machine-learning and LLM techniques cluster, correlate, and prioritise alerts to shorten detection and response times, and analyses
the risk of automation error in a security-critical setting.
29. Ransomware Incident Reconstruction and Attribution
Ransomware leaves a rich trail across initial access, lateral movement, and encryption. The paper
would reconstruct such an attack forensically and examine the indicators used to scope and attribute
it.
4


<!-- page 5 -->
Digital Crime and Forensics (CS 616)
Research Paper — Topic Catalogue
30. Deep-Learning Network Forensics and Intrusion Reconstruction
Combining Moustafa's network-forensics material with recent CNN-based intrusion detection, this
topic studies how network evidence reconstructs an attack, including the growing challenge of
analysing encrypted traffic.
9 · Legal, Standards, Privacy, and the Saudi Context
31. Admissibility of AI-Generated Evidence
As AI produces more findings, courts must judge their reliability. The paper would analyse how
AI-derived evidence meets — or fails — the Daubert factors and ISO/IEC 27037, and what documentation, validation, and explainability are required for admissibility.
32. Digital Forensics under Saudi Arabia's PDPL and Anti-Cyber Crime Law
This topic grounds the course's Kingdom-first legal framing by examining how the Personal Data
Protection Law, the Anti-Cyber Crime Law (Royal Decree No. M/17), and National Cybersecurity
Authority controls shape lawful collection, breach notification, and cross-border data handling in
a Saudi investigation.
33. Privacy-Preserving Forensics
Investigators must find evidence without needlessly exposing unrelated personal data. The paper
would study techniques such as selective disclosure, differential privacy, and encryption-aware search
that reconcile effective investigation with data-protection obligations.
34. Forensic Readiness and Standardisation in Organisations
Whether an organisation can later produce admissible evidence is decided before an incident. This
topic examines forensic-readiness frameworks — logging, retention, time synchronisation, and relevant ISO standards — and how an organisation's maturity can be assessed.
10 · Data, Reproducibility, and Investigative Tooling
35. The Dataset Problem in AI Forensics
Progress in AI forensics is throttled by a shortage of realistic, shareable datasets, held back by
privacy and legal barriers. The paper would examine recent dataset-building efforts (including
LLM-oriented forensic datasets), the promise and pitfalls of synthetic data, and the effect on tool
validation and reproducibility.
36. Augmented Reality for Crime-Scene Investigation
Following the Abd El-Latif collection, this topic studies augmented-reality tools that capture,
annotate, and reconstruct a crime scene, evaluating their evidentiary value and their usefulness for
training investigators.
Choosing well. Prefer a focused question you can actually investigate over a broad survey.
Most of these topics pair naturally with a small practical component — a dataset experiment,
a tool evaluation, or a worked case analysis — which strengthens the paper. Confirm your
choice with the instructor by the Week 4 proposal milestone, and cite the course's primary
sources alongside recent (2024–2026) literature.
5


<!-- page 6 -->
Digital Crime and Forensics (CS 616)
Research Paper — Topic Catalogue
Key reference sources
[1] Easttom, W. Digital Forensics, Investigation, and Response, 5th Edition. Jones & Bartlett Learning,
2024. (Course primary text.)
[2] Moustafa, N. Digital Forensics in the Era of Artificial Intelligence. CRC Press. (AI/ML for forensics;
network forensics; ML trends.)
[3] Abd El-Latif, A. A., Tawalbeh, L., Mohanty, M., Gupta, B. B., & Psannis, K. E. (Eds.).
Digital
Forensics and Cyber Crime Investigation: Recent Advances and Future Directions. 2025.
[4] Holt, T. J., Bossler, A. M., & Seigfried-Spellar, K. C. Cybercrime and Digital Forensics: An Introduction.
Routledge.
[5] Britz, M. T. Computer Forensics and Cyber Crime: An Introduction, 3rd Edition, 2023.
[6] Recent literature (2024–2026) on LLMs in digital forensics, deepfake detection and attribution, adversarial and anti-forensics, and cloud/IoT forensic automation, located via the library databases (IEEE
Xplore, ScienceDirect, ACM Digital Library).
6
