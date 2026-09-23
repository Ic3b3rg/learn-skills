# Reproducible skill evaluation cases

`cases.json` contains an ordinary request, a non-trigger request, and an edge case for each of the nine skills. These are evaluation inputs and human grading criteria, **not recorded successful runs**. The fixture code is deliberately small so its ground truth can be inspected directly.

Prepare one isolated run without invoking a model or using credentials:

```bash
python3 scripts/prepare_eval.py quiz-me-positive --output /tmp/learn-skills-quiz-run
```

The destination must not exist. The command writes:

- `workspace/`: source fixtures and installed skills, with no grading criteria.
- `prompt.txt`: the exact user request to submit.
- `manifest.json`: preparation metadata and file hashes, outside the agent workspace.

Use `--skill-dir .claude/skills` for a Claude Code standalone installation; the default is `.agents/skills`. Other supported directory choices are `.github/skills`, `.gemini/skills`, and `.cursor/skills`. This exercises standalone directory discovery, not plugin marketplace installation.

Use `--skills-root /path/to/another-checkout/skills` to prepare a baseline, or `--without-skills` for a no-skill comparison. The missing-dependency case installs only `start-learn`. Use a clean host profile with unrelated user/global skills disabled; otherwise record those additional skills and treat the run as a coexistence test. Application settings and install paths can change; verify them against the [provider matrix](../docs/research/skill-portability.md#application-compatibility).

## Running and grading

1. Start a fresh agent session in the generated `workspace/` using the chosen host/model. Submit only `prompt.txt`; keep this README, the case checks and the manifest out of the model's input.
2. For implicit cases, observe which skill is actually loaded. For explicit cases the prompt names the skill; these cannot establish automatic discovery quality. Negative cases mean the **target** skill should not activate; a different relevant skill may be appropriate.
3. Save the actual transcript, tool trace and produced files outside `workspace/`. Record host/model version, install configuration, source availability, token use and elapsed time. Do not invent a reply from the learner to satisfy a waiting boundary.
4. Grade each case check as pass, fail, or not observed, citing a turn or artifact. Use a human to judge answer leakage, learner authorship and reasoning questions. A stopped session is not a completed multi-turn evaluation.
5. Compare baseline and revised runs under the same settings, with repeated trials. Start with three repetitions as an exploratory project choice, not a statistical guarantee. Report individual failures and unobserved checks instead of only an aggregate percentage.

The supplied cases target initial turns and selected artifact decisions. They do not cover every learning session, assessment edge case, human retention outcome, or provider. Extend with actual failures rather than treating 27 cases as exhaustive. The [performance evidence review](../docs/research/skill-performance-evidence.md) explains why structural validity, instruction adherence, efficiency and educational benefit are separate measurements.
