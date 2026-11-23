"""Synthetic filler papers used only by tests (nonsense text; never a real paper)."""
import random, sys
random.seed(1)
W="the forensic artefact survives across encrypted messaging application version device state analysis evidence recovered database backup deletion study shows review evaluated approach reported limited findings sources compared investigators examiner acquisition method result important".split()
def para(n,cites=()):
    ws=[random.choice(W) for _ in range(n)]
    t=" ".join(ws).capitalize()+"."
    for c in cites: t+=" As shown in \\cite{%s}."%c
    return t
def build(topic):
    keys=["k%d"%i for i in range(1,18)]
    bib="\n".join("@article{%s,\n author={A. Author and B. Writer}, title={Study %d on forensic messaging}, journal={Digital Investigation}, year={%d}, pages={1--10}, doi={10.1/%d}}"%(k,i,2021+i%6,i) for i,k in enumerate(keys,1))
    bib+="\n@article{onik, author={A. R. Onik and J. Brown}, title={A systematic literature review of secure instant messaging applications}, journal={ACM CSUR}, year={2025}, pages={1--40}, doi={10.1145/3727641}}\n"
    if topic=="34":
        bib+="@misc{r1, author={R. Rowlingson}, title={A ten step process for forensic readiness}, year={2004}, howpublished={Int. J. Digital Evidence}}\n@techreport{iso, author={ISO/IEC}, title={ISO/IEC 27043:2015 incident investigation}, year={2015}, institution={ISO}}\n"
    cites=keys+["onik"]+(["r1","iso"] if topic=="34" else [])
    it=iter(cites)
    def c(n): return [next(it,"k1") for _ in range(n)]
    ttl={"19":"Version- and State-Robust Forensics of Encrypted Messaging Applications: A Systematic Review","34":"Forensic Readiness and Standardisation in Organisations: A Systematic Review of Maturity Models"}[topic]
    extra19="Signal, Telegram and WhatsApp on Android and iOS are covered. BFU and AFU (before first unlock, after first unlock) states, SQLite database, backup, keystore, cache and media artefacts, WAL checkpoint and deletion, app version update, cloud export, legal warrant MLAT jurisdiction, end-to-end encryption and NIST SP 800-101 are discussed; single-version studies and reproducibility are gaps. "
    extra34="Rowlingson ten-step, ISO/IEC 27043, 27035, 30121 and NIST SP 800-61 are covered, with NCA and PDPL in Saudi Arabia. Governance, logging, retention, time synchronisation, acquisition, cloud, personnel training and tabletop testing are capabilities. Maturity model levels and assessment scoring, inter-rater reliability, validation and predicted incident outcomes appear; admissibility, chain of custody and ISO/IEC 27037, standardisation and accreditation interoperability, and few studies validate instruments. "
    ex=extra19 if topic=="19" else extra34
    db="IEEE Xplore, ACM Digital Library (DL), ScienceDirect, Scopus, SpringerLink and Google Scholar were searched. "
    win={"19":"2014--2026","34":"2001--2026"}[topic]
    ss={"19":"forensic* AND (Signal OR Telegram OR WhatsApp OR instant messag* OR secure messag*) AND (Android OR iOS OR artefact*)","34":"(forensic readiness OR digital forensic readiness) AND (maturity OR framework OR standard OR ISO)"}[topic]
    tex=r"""\documentclass[conference]{IEEEtran}
\usepackage{graphicx}
\begin{document}
\title{%s}
\author{\IEEEauthorblockN{Dawood Test}\IEEEauthorblockA{Hajjah University}}
\maketitle
\begin{abstract}
%s
\end{abstract}
\begin{IEEEkeywords}
digital forensics, encrypted messaging, systematic review, artefacts, mobile forensics
\end{IEEEkeywords}
\section{Introduction}
%s Our contribution and the research questions RQ1, RQ2, RQ3 are stated. The remainder of this paper is organised as follows. 
%s
\section{Background and Related Work}
%s
\section{Review Methodology}
The scope is bounded. %s%s The search string was %s. The window is %s. Inclusion and exclusion criteria apply. A PRISMA flow (Fig.~\ref{fig:prisma}) shows records identified, screened, eligible and included; 42 studies were included. Quality assessment used a rubric.
\begin{figure}[t]\caption{PRISMA selection flow showing identified, screened and included records from all databases.}\label{fig:prisma}\end{figure}
%s
\section{Taxonomy and Analysis}
A taxonomy is proposed (Table~\ref{tab:cmp}). %s
\begin{table}[t]\caption{Comparison of approach, dataset, result and limitation per study}\label{tab:cmp}
\begin{tabular}{llll}
Approach & Dataset & App version state & Artefacts recovered deletion framework standard measurement validation\\ \end{tabular}\end{table}
%s
\section{Results and Discussion}
Anticipated outcomes were met. Compared with prior surveys, the review differs. Limitations and selection bias threaten validity. %s
\section{Conclusion and Future Work}
%s Future work is outlined.
\bibliographystyle{IEEEtran}
\bibliography{refs}
\end{document}
"""%(ttl, para(190),
     para(300,c(3))+" "+ex, para(400,c(3)),
     para(1100,c(4)), db, "", ss, win, para(700,c(2)),
     ex+para(1000,c(2)), "", para(850,c(1)), para(300,c(1)), )
    tex=tex.replace("%s","",1) if False else tex
    return tex,bib
import os
def write_all(base):
    for t in ("19","34"):
        d=os.path.join(base,"t%s"%t); os.makedirs(d,exist_ok=True)
        tex,bib=build(t); open(d+"/main.tex","w").write(tex); open(d+"/refs.bib","w").write(bib)
if __name__=="__main__":
    write_all(sys.argv[1] if len(sys.argv)>1 else ".")
