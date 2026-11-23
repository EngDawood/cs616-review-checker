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
    def test_zip_input(self):
        import shutil; z = shutil.make_archive(os.path.join(self.tmp, "z"), "zip", os.path.join(self.tmp, "t34"))
        d, _ = run(z, "34"); self.assertEqual(d["meta"]["main_file"], "main.tex")
    def test_plugin_copies_match_engine(self):
        h = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest() if True else None
        for s in ("t19", "t34"):
            p = os.path.join(ROOT, "plugins", "cs616-%s-review-checker" % s, "skills", "%s-review-checker" % s, "scripts", "check_paper.py")
            self.assertEqual(h(p), h(ENGINE), "run python3 tools/build.py")
if __name__ == "__main__":
    unittest.main()
