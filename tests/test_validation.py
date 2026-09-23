"""Exercise the shipped validator against isolated, damaged skill packages."""
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="learn-skills-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for folder in ("skills", "docs", "scripts", ".claude-plugin", ".codex-plugin", ".agents"):
            shutil.copytree(ROOT / folder, self.root / folder)

    def run_validator(self):
        return subprocess.run(
            ["ruby", str(self.root / "scripts/validate_skills.rb")],
            capture_output=True, text=True, check=False,
        )

    def edit(self, relative, before, after):
        path = self.root / relative
        text = path.read_text()
        self.assertIn(before, text)
        path.write_text(text.replace(before, after, 1))

    def assert_rejected(self, message):
        result = self.run_validator()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(message, result.stderr)

    def test_current_package(self):
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_invalid_embedded_yaml(self):
        self.edit("skills/start-learn/SKILL.md", "description: ", "description: invalid: ")
        self.assert_rejected("mapping values")

    def test_source_policy_drift(self):
        with (self.root / "skills/quiz-me/SOURCES.md").open("a") as stream:
            stream.write("\nStale content\n")
        self.assert_rejected("source policy missing or stale")

    def test_external_resource(self):
        self.edit("skills/quiz-me/SKILL.md", "(SOURCES.md)", "(../../docs/sources.md)")
        self.assert_rejected("resource escapes skill")

    def test_unknown_router_target(self):
        self.edit("skills/start-learn/FLOWS.md", "`/quiz-me <file-or-topic>`", "`/missing-skill <file-or-topic>`")
        self.assert_rejected("router target missing-skill is not installed")

    def test_router_target_explicit_only_frontmatter(self):
        self.edit("skills/quiz-me/SKILL.md", "name: quiz-me", "name: quiz-me\ndisable-model-invocation: true")
        self.assert_rejected("router target quiz-me disables model invocation")

    def test_router_target_explicit_only_metadata(self):
        with (self.root / "skills/quiz-me/agents/openai.yaml").open("a") as stream:
            stream.write("\npolicy:\n  allow_implicit_invocation: false\n")
        self.assert_rejected("Automatic routing is disabled")

    def test_empty_description(self):
        path = self.root / "skills/quiz-me/SKILL.md"
        lines = path.read_text().splitlines()
        lines[2] = 'description: "   "'
        path.write_text("\n".join(lines) + "\n")
        self.assert_rejected("Invalid description")

    def test_empty_skill_inventory(self):
        shutil.rmtree(self.root / "skills")
        (self.root / "skills").mkdir()
        self.assert_rejected("No skills found")


if __name__ == "__main__":
    unittest.main()
