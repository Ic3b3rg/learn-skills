# Skill quality pass: preservation and validation

Baseline: `bbfd0916ce6a8b3318dc6de7728821e832d53d51`. Date: 2026-09-23.

Scope: implement the [portability audit](research/skill-portability.md) and conservative improvements from the [per-skill research](research/per-skill-quality.md). Research findings describe the baseline; the corrections below describe the updated files. No new teaching method, scheduler, skill name, or assessment scale was introduced.

## Preserved contracts

| Skill | Contract retained | Quality correction |
| --- | --- | --- |
| `ask-me-questions` | One question at a time; citation/safety exceptions; user controls stopping | Example now waits between questions; overview acknowledges its existing exceptions |
| `explain-and-check` | Learner explanation, prerequisite carve-out, source verification, transfer, learner-drawn trace | Silent orientation read and final trace sequencing are explicit |
| `quiz-me` | Source-closed confirmation, retrieval before verification, retry, new-scenario exit | Example now separates confirmation from the recall prompt |
| `connect-to-what-you-know` | Learner creates analogy; agent checks structure, breakpoint, consequence; one structural bridge | Versioned evidence must cover both sides of the comparison |
| `assess` | Bloom default/SOLO option; baseline; evidence; two consecutive failures; discrete verdict; dominant-gap routing | Checklist and verdict label work for either scale |
| `flashcards` | User fronts, verified cited backs, folded answers, 15-card cap, user stop, workspace paths | Follow-up uses the saved path; cap described as a product choice |
| `learn-by-doing` | 3–7 exercises, required code-mode E4, folded solutions, source verification, learner-paced retries | Checklist and reference use workspace paths; unsupported ranking/cutoff claims removed |
| `linked-notes` | User prose, atomic notes, citations, accepted links only, existing bodies protected | Link lookup and reference use workspace paths; YAML wikilinks quoted as strings |
| `start-learn` | Single opening question, declared automatic Scenario A routing, user-paced Scenario B, curriculum approval | Valid YAML, explicit instruction loading/missing-target response, direct lesson reference, obsolete confirmation-exit removed |

Shared changes preserve the full source hierarchy, version anchoring, and uncertainty fallback. `docs/sources.md` remains canonical; `SOURCES.md` copies are byte-checked installation resources. Provider tool names became capabilities. The two Italian references were translated while retaining lesson formats, equal-character answer options, offline inline JavaScript, paths, and generated-lesson checkbox semantics.

### Conflict resolution

The old assessment checklist gated Q5/Q6 on a single previous pass, while both its session protocol and `LEVELS.md` said to stop after two consecutive failures. The checklist now follows the existing full protocol. The old card reference rejected files below five cards while the session protocol allowed the user to stop earlier; the default remains 5–15 and the explicit stop rule governs. These are reconciliations of conflicting instructions, not claims of byte-for-byte behavioral equivalence.

## Verification performed

- Before edits: real YAML parsing rejected `start-learn`; the new validator rejected external skill resources and absent bundled policies.
- After edits: `ruby scripts/validate_skills.rb` passes all nine skills, including YAML/name/description constraints, the local 100-line cap, Markdown resource closure, exact policy copies, optional metadata, and JSON syntax.
- Skill Creator's `quick_validate.py` passes all nine skills, run with PyYAML supplied through an isolated `uv run --with pyyaml` environment.
- Temporary-copy mutation checks confirm that the repository validator rejects malformed YAML, stale policy copies, escaping resource paths, and mismatched skill names.
- All nine skill directories were copied independently into a temporary location and retained the complete source policy. `start-learn` still requires target workflows for Scenario A; a complete folder is not a complete router installation.
- `git diff --check` passes. No plugin installation, marketplace update, publication, or provider runtime test was performed.

## Evaluation limits

Independent baseline instruction traces reproduced the missing router dependency, contradictory workspace paths, and source-closure example. Updated instruction traces cover all nine skills; they are simulated next turns and decisions, not live longitudinal learner sessions or a cross-provider benchmark.

The independent pass found no lost source-verification, withholding, workspace, folded-answer, learner-authorship, or required debug-task contract. Eight scenario traces were consistent; `assess` exposed a Bloom-only verdict placeholder and remaining taxonomy edge cases. The placeholder and assessment opening's confirmation turn were corrected; an unsupported debug-task superlative in the exercise reference was also removed. The remaining assessment interpretation ambiguity prevents claiming complete behavioral equivalence.

Assessment edge cases such as how to handle failure below Bloom L1 or interpret SOLO Prestructural remain a separate design question. The taxonomy algorithm, lesson option-length rule, and exact count limits were not scientifically recalibrated. The research identifies these boundaries without silently changing the teaching contract.

## Expanded evidence audit

The subsequent [ecosystem crosscheck](research/ecosystem-crosscheck.md), [OpenAI and empirical performance review](research/skill-performance-evidence.md), and [Matt PR coverage audit](research/matt-pr-coverage.md) expand source coverage beyond the original four PRs. They do not establish exhaustive coverage of all publications or all upstream diffs.

Five further wording corrections align claims with actual behavior: questions-only metadata acknowledges existing exceptions; insight, paraphrase, and saved cards are not described as demonstrated transfer; optional E5–E7 exercise selection is no longer described as guaranteed. These edits preserve the learner-facing sequence and introduce no new exam or completion gate. Runtime, comparative efficiency, and educational-outcome claims remain unverified.

## Follow-through: discovery and automation

All nine descriptions now state a concise purpose and activation context. Detailed protocols and exceptions stay in the unchanged bodies for this metadata pass. Serialized description length fell by roughly half; this reduces metadata size but does not demonstrate better routing by a model. Positive and negative discovery prompts are included for subsequent evaluation.

Four new failing regression cases exposed validator gaps: whitespace-only descriptions, empty skill inventory, nonexistent router targets, and router targets marked explicit-only in frontmatter. These now fail validation. The complete local suite has 14 passing tests, including preparation of all 27 evaluation cases and rejection of malformed packages.

The [workflow](../.github/workflows/validate-skills.yml) invokes the same validator and tests on pushes and pull requests, using read-only repository access and a checkout commit pinned from the upstream v7 tag. This follows [GitHub's action-pinning guidance](https://docs.github.com/en/actions/reference/security/secure-use) and [checkout's credential option](https://github.com/actions/checkout). The workflow has been inspected locally, not executed on GitHub; it takes effect after publication. No branch-protection settings were changed.

The [evaluation kit](../evals/README.md) has three cases per skill: ordinary request, non-trigger request and edge case. Its offline preparer copies fixtures and selected skill resources into a fresh workspace, keeps grading data outside, and records file hashes. It supports an alternate baseline checkout, no-skill controls, host-specific skill directories and the isolated router case. Tests verify preparation, not model behavior. No latency, token-efficiency or discovery gain is claimed from this pass.
