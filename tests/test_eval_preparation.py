import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class EvalPreparationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="learn-skills-eval-test-")
        self.addCleanup(self.temp.cleanup)
        self.parent = Path(self.temp.name)

    def prepare(self, case, output, *options):
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts/prepare_eval.py"), case,
             "--output", str(output), *options],
            capture_output=True, text=True, check=False,
        )

    def test_all_cases_prepare_with_reproducible_files(self):
        cases = json.loads((ROOT / "evals/cases.json").read_text())
        names = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
        self.assertEqual(len({c["id"] for c in cases}), len(cases))
        self.assertEqual({c["skill"] for c in cases}, names)
        for name in names:
            self.assertEqual({c["kind"] for c in cases if c["skill"] == name},
                             {"positive", "negative", "edge"})
        for case in cases:
            with self.subTest(case=case["id"]):
                self.assertTrue(case["checks"])
                dest = self.parent / case["id"]
                result = self.prepare(case["id"], dest)
                self.assertEqual(result.returncode, 0, result.stderr)
                manifest = json.loads((dest / "manifest.json").read_text())
                self.assertEqual(manifest["status"], "prepared-not-executed")
                self.assertEqual((dest / "prompt.txt").read_text(), case["prompt"] + "\n")
                self.assertEqual((dest / "workspace/CURRICULUM.md").exists(), case["workspace"])
                self.assertEqual(set(manifest["skills"]), set(case.get("install_only", names)))
                self.assertFalse((dest / "workspace/evals").exists())
                self.assertFalse((dest / "workspace/manifest.json").exists())
                for path, expected in manifest["files_sha256"].items():
                    self.assertEqual(hashlib.sha256((dest / "workspace" / path).read_bytes()).hexdigest(), expected)

    def test_refuses_existing_output_without_overwriting(self):
        dest = self.parent / "existing"
        dest.mkdir()
        marker = dest / "keep.txt"
        marker.write_text("user content")
        result = self.prepare("quiz-me-positive", dest)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(marker.read_text(), "user content")
        self.assertEqual(list(dest.iterdir()), [marker])

    def test_no_skill_control(self):
        dest = self.parent / "control"
        result = self.prepare("quiz-me-positive", dest, "--without-skills")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse((dest / "workspace/.agents").exists())
        self.assertEqual(json.loads((dest / "manifest.json").read_text())["skills"], [])

    def test_alternate_source_and_host(self):
        source = self.parent / "baseline/quiz-me"
        source.mkdir(parents=True)
        (source / "SKILL.md").write_text("Baseline bytes preserved\n")
        dest = self.parent / "alternate"
        result = self.prepare("quiz-me-positive", dest, "--skills-root", str(source.parent),
                              "--skill-dir", ".claude/skills")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((dest / "workspace/.claude/skills/quiz-me/SKILL.md").read_bytes(),
                         (source / "SKILL.md").read_bytes())

    def test_unknown_case_has_no_side_effect(self):
        dest = self.parent / "unknown"
        result = self.prepare("missing", dest)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(dest.exists())


if __name__ == "__main__":
    unittest.main()
