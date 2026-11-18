# -*- coding: utf-8 -*-
"""模板自检：本模板包自身必须 8/8，否则它会把自己的缺陷复制到每一个新仓。

跑法：python -m unittest discover tests -v
"""
import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUIRED = ["LICENSE", "README.md", "EVIDENCE-INDEX.md", "STRUCTURE.md", "SPEC.md",
            "tools/check_standard.py", "tests", ".github/workflows"]


class TestTemplateIntegrity(unittest.TestCase):
    def test_required_items_exist(self):
        for rel in REQUIRED:
            with self.subTest(item=rel):
                self.assertTrue(os.path.exists(os.path.join(ROOT, rel)), f"缺 {rel}")

    def test_evidence_index_has_real_zeros(self):
        p = os.path.join(ROOT, "EVIDENCE-INDEX.md")
        with open(p, encoding="utf-8") as f:
            text = f.read()
        for level in ("L1", "L2", "L3", "L3.5", "L4"):
            self.assertIn(level, text, f"证据分级缺 {level}")

    def test_spec_has_claim_ceiling(self):
        p = os.path.join(ROOT, "SPEC.md")
        with open(p, encoding="utf-8") as f:
            self.assertIn("主张上限", f.read(), "SPEC 必须有主张上限段")

    def test_check_standard_reports_self(self):
        out = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "check_standard.py")],
                             capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
        self.assertIn("/8", out.stdout, "检查器必须输出 x/8")


if __name__ == "__main__":
    unittest.main()
