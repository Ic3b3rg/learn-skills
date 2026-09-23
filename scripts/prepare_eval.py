"""Prepare a reproducible evaluation workspace; never invokes an LLM."""
import argparse
import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case_id")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--skills-root", type=Path, default=ROOT / "skills")
    parser.add_argument("--without-skills", action="store_true")
    parser.add_argument("--skill-dir", default=".agents/skills", choices=[
        ".agents/skills", ".claude/skills", ".github/skills", ".gemini/skills", ".cursor/skills",
    ])
    args = parser.parse_args()
    cases = json.loads((ROOT / "evals/cases.json").read_text())
    case = next((item for item in cases if item["id"] == args.case_id), None)
    if case is None:
        parser.error(f"Unknown case: {args.case_id}")
    if args.output.exists():
        parser.error("Output already exists; choose a fresh directory")
    folders = [] if args.without_skills else sorted(args.skills_root.glob("*/SKILL.md"))
    if not args.without_skills and not folders:
        parser.error("No skills found in --skills-root")
    if case.get("install_only"):
        folders = [p for p in folders if p.parent.name in case["install_only"]]
        if not args.without_skills and {p.parent.name for p in folders} != set(case["install_only"]):
            parser.error("Required isolated skill is missing from --skills-root")
    workspace = args.output / "workspace"
    workspace.mkdir(parents=True)
    shutil.copytree(ROOT / "evals/fixtures/code", workspace, dirs_exist_ok=True)
    if case["workspace"]:
        shutil.copytree(ROOT / "evals/fixtures/workspace", workspace, dirs_exist_ok=True)
    for entry in folders:
        shutil.copytree(entry.parent, workspace / args.skill_dir / entry.parent.name)
    (args.output / "prompt.txt").write_text(case["prompt"] + "\n")
    files = [p for p in workspace.rglob("*") if p.is_file()]
    manifest = {
        "case_id": case["id"], "status": "prepared-not-executed",
        "mode": case["mode"], "skill_dir": args.skill_dir,
        "skills": [p.parent.name for p in folders],
        "prompt_sha256": hashlib.sha256((case["prompt"] + "\n").encode()).hexdigest(),
        "files_sha256": {str(p.relative_to(workspace)): hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in sorted(files)},
    }
    (args.output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Prepared {case['id']} at {args.output}; no model run performed.")


if __name__ == "__main__":
    main()
