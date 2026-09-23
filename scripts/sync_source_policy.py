"""Bundle the canonical source policy into each independently installable skill."""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
policy = (root / "docs/sources.md").read_bytes()
for skill in sorted((root / "skills").glob("*/SKILL.md")):
    (skill.parent / "SOURCES.md").write_bytes(policy)
    print(f"Updated {skill.parent.name}/SOURCES.md")
