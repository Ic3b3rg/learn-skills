# Changelog

All notable changes to learn-skills are documented here. Versions follow semantic versioning (pre-1.0: minor bumps cover new behaviour and behaviour-changing reversals).

## Unreleased

### Fixed — skill portability and instruction consistency
- Corrected `start-learn` YAML without changing its description.
- Bundled the complete source policy with every skill and added synchronization and validation commands.
- Replaced provider-specific tool requirements with equivalent retrieval capabilities.
- Clarified missing router dependencies, workspace output paths, source-closed turn ordering, and the assessment checklist for both taxonomies.
- Translated the workspace and lesson references into English, preserving their formats and requirements.

### Improved — discovery and regression checks
- Shortened all nine descriptions to their purpose and activation context; teaching protocols remain in the bodies.
- Added router-target checks and regression tests for invalid or incomplete packages.
- Added a GitHub validation workflow with read-only permissions and a pinned checkout action.
- Added 27 behavioral evaluation cases and an offline preparer for baseline/current, no-skill, and missing-dependency comparisons. Actual model runs are separate.

### Added — Codex distribution
- Added `.codex-plugin/plugin.json` so the existing skills package as a Codex plugin.
- Added `.agents/plugins/marketplace.json` so the repository can be added as a Codex marketplace.
- Added `agents/openai.yaml` UI metadata for every skill.
- Documented the Codex marketplace installation flow in `README.md`.

## 0.3.0 — 2026-06-19

### Changed — architecture
- **The agent now auto-selects the methodology** ([ADR 0004](docs/adr/0004-agent-selects-methodology.md)). `start-learn` detects the goal, declares the chosen skill + a one-line reason, and runs it; the user can redirect. This **reverses** the previous "propose, the user decides" rule. The reversal is narrow: principle 1 still binds *content* (sessions withhold explanations, students speak first) — only the *meta-choice* of method is automated.

### Improved — `explain-and-check`
- **Prerequisite carve-out (gap interception).** When the user stalls on a fact they cannot derive (a symbol's referent, a local convention, vocabulary), the agent supplies it in one sentence instead of withholding — withholding an underivable prerequisite produces confusion, not retrieval. Added repo-wide to principle 1 in `CONTEXT.md`.
- **"Follow the thread" code-mode rule.** Both the user's explanation and the agent's questions now trace one datum's journey — where it enters, how each function transforms it, where it exits — so the user doesn't lose the thread mid-trace.
- **Structural-map Frame.** The opening states the cast (files + one-line roles) and the event to trace, while withholding mechanism — orientation without spoon-feeding.
- **Draw-the-thread takeaway.** After the transfer test, the user sketches the full flow themselves; the agent verifies *their* drawing against the code, then offers `/linked-notes` to save it.

### Fixed
- `skills/start-learn/FLOWS.md` translated from Italian to English (English-everywhere convention).

## 0.2.0

- Stateful teaching workspace for Scenario B (CURRICULUM.md, HTML lessons, glossary, resources). See [ADR 0003](docs/adr/0003-stateful-teaching-workspace-for-scenario-b.md).

## 0.1.0

- Initial release: 9 pedagogical skills, ADRs, source-fidelity policy.
