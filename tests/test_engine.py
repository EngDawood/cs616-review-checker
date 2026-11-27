import json, os, subprocess, sys, tempfile, unittest, hashlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tests"))
import make_fixtures
ENGINE = os.path.join(ROOT, "engine", "check_paper.py")

def run(path, topic, extra=()):
    r = subprocess.run([sys.executable, ENGINE, path, "--topic", topic, "--format", "json", *extra], capture_output=True, text=True)
    return json.loads(r.stdout), r.returncode

class T(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp(); make_fixtures.write_all(cls.tmp)
        bad = os.path.join(cls.tmp, "bad"); os.makedirs(bad)
        open(os.path.join(bad, "main.tex"), "w").write(r"""\documentclass{article}
\begin{document}\title{Digital Forensics}\maketitle
\begin{abstract}Short.\end{abstract}\section{Introduction}We think so. TODO. \cite{a,zz} \ref{nope}
\end{document}""")
    def test_good_papers_have_no_fail_for_their_own_topic(self):
        for t in ("19", "34"):
            d, rc = run(os.path.join(self.tmp, "t" + t), t)
            fails = [f["id"] for f in d["findings"] if f["status"] == "FAIL"]
            self.assertEqual(d["meta"]["topic"], t)
            self.assertNotIn("L1", fails); self.assertNotIn("R2", fails)
            self.assertEqual([f for f in fails if f.startswith(("M", "C", "S-", "F", "T"))], [], fails)
    def test_topic_isolation(self):
        d19, _ = run(os.path.join(self.tmp, "t19"), "19"); d34, _ = run(os.path.join(self.tmp, "t19"), "34")
        c19 = {f["id"]: f["status"] for f in d19["findings"]}; c34 = {f["id"]: f["status"] for f in d34["findings"]}
        self.assertEqual(c19["C4"], "PASS")          # BFU/AFU - topic 19 only
        self.assertNotEqual(c34["C1"], "PASS")        # a T19 paper must not satisfy T34 readiness-framework coverage
        self.assertNotIn("Topic 19", json.dumps(d34["findings"]))
        self.assertNotIn("Topic 34", json.dumps(d19["findings"]))
    def test_bad_paper_fails_loudly(self):
        d, rc = run(os.path.join(self.tmp, "bad"), "19")
        self.assertEqual(rc, 1); self.assertGreater(d["summary"]["FAIL"], 15)
        ids = {f["id"] for f in d["findings"] if f["status"] == "FAIL"}
        for need in ("F1", "F3", "T1", "A1", "K1", "R3", "FT3"): self.assertIn(need, ids)
    def test_generic_mode_is_topic_free(self):
        for tp in ("t19", "t34"):
            d, _ = run(os.path.join(self.tmp, tp), "generic")
            ids = {f["id"] for f in d["findings"]}
            self.assertFalse(ids & {"M3", "M4", "M5", "FT6"}); self.assertFalse([i for i in ids if i.startswith("R12.")])
            self.assertNotIn("Topic coverage", {f["category"] for f in d["findings"]})
            self.assertEqual(next(f["status"] for f in d["findings"] if f["id"] == "T1"), "PASS")
        r = subprocess.run([sys.executable, ENGINE, os.path.join(self.tmp, "t19"), "--format", "json"], capture_output=True, text=True)
        self.assertEqual(json.loads(r.stdout)["meta"]["topic"], "generic")  # --topic is optional
    def test_latex_hygiene_checks(self):
        d0 = os.path.join(self.tmp, "hyg"); os.makedirs(d0)
        open(os.path.join(d0, "main.tex"), "w").write(r"""\documentclass[conference]{IEEEtran}
\begin{document}\title{A Clear Title}\maketitle
\section{A}\label{s:a} \section{B}\label{s:a}
\begin{figure}\includegraphics{missing}\caption{x}\label{f:x}\end{figure}
\begin{itemize}\item x
\end{document}""")
        d, _ = run(d0, "generic"); st = {f["id"]: f["status"] for f in d["findings"]}
        for k in ("LX1", "LX2", "LX3"): self.assertEqual(st[k], "FAIL", k)
        d, _ = run(os.path.join(self.tmp, "t19"), "generic"); st = {f["id"]: f["status"] for f in d["findings"]}
        for k in ("LX1", "LX2", "LX3"): self.assertEqual(st[k], "PASS", k)
    def test_zip_input(self):
        import shutil; z = shutil.make_archive(os.path.join(self.tmp, "z"), "zip", os.path.join(self.tmp, "t34"))
        d, _ = run(z, "34"); self.assertEqual(d["meta"]["main_file"], "main.tex")
    def test_plugin_copy_matches_engine(self):
        h = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
        p = os.path.join(ROOT, "skills", "cs616-review-checker", "scripts", "check_paper.py")
        self.assertEqual(h(p), h(ENGINE), "run python3 tools/build.py")
    def test_topic_folders_are_separate(self):
        base = os.path.join(ROOT, "skills", "cs616-review-checker", "references", "topics")
        for a, b in (("19", "34"), ("34", "19")):
            for dp, _, fn in os.walk(os.path.join(base, "t" + a)):
                for f in fn:
                    self.assertNotIn("Topic %s " % b, open(os.path.join(dp, f)).read().replace("Topic %s)" % b, ""), f)
    def test_unmodified_ieee_template_is_flagged(self):
        import zipfile
        d = os.path.join(self.tmp, "tpl"); zipfile.ZipFile(os.path.join(ROOT, "templates", "ieee-conference-template.zip")).extractall(d)
        r, rc = run(d, "19"); st = {f["id"]: f["status"] for f in r["findings"]}
        self.assertEqual(st["F1"], "PASS"); self.assertEqual(st["F3"], "FAIL"); self.assertEqual(rc, 1)
if __name__ == "__main__":
    unittest.main()
