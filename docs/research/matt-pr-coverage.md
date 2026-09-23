# Matt Pocock PR coverage and transferable findings

Audit snapshot: 2026-09-23 08:55:42 UTC. Repository: [mattpocock/skills](https://github.com/mattpocock/skills), main SHA `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`.

## What was actually covered

The earlier portability report examined four selected PRs. That was useful evidence, **not a review of every upstream improvement**. This follow-up enumerated every public PR returned by GitHub's first-party REST API at the snapshot: **149 PRs, 98 merged, 46 closed without merge, 5 open**. This includes contributions from all authors, rather than filtering to Matt's account. PR and issue numbers share a sequence, so number 1092 does not mean 1,092 PRs exist.

Command: `gh api --paginate 'repos/mattpocock/skills/pulls?state=all&per_page=100&sort=created&direction=asc' --slurp`. The API supplied two pages, containing 100 and 49 records; pagination followed GitHub's Link headers. No date or author filter was applied. The [machine-readable inventory](matt-pr-inventory.json) preserves all returned titles, bodies, URLs, timestamps, states, authors, and screening decisions. [GitHub pulls endpoint](https://api.github.com/repos/mattpocock/skills/pulls?state=all&per_page=100&sort=created&direction=asc)

**Coverage boundary:** every title is inventoried; bodies were retained and used for relevance screening with selected reading. Relevant file patches were inspected for the PRs marked “targeted diff review” below. This does **not** mean every body, every changed file, every comment, every review thread, or every linked issue was exhaustively read. It also excludes direct-to-main changes that never had a PR and private/deleted material. Inventory completeness and review depth are separate claims. This is a point-in-time API snapshot, not an atomic transaction over future changes.

## Findings relevant to learn-skills

| Upstream evidence | Transfer to this repository | Current assessment |
| --- | --- | --- |
| [#905](https://github.com/mattpocock/skills/pull/905) changed punctuation; [#911](https://github.com/mattpocock/skills/pull/911) repaired resulting invalid frontmatter; [issue #907](https://github.com/mattpocock/skills/issues/907) records installer failure. | Parse **embedded SKILL.md YAML**, including after seemingly editorial changes. | Addressed structurally by quoting `start-learn` and the local validation script. Installer/runtime evidence remains separate. |
| [#551](https://github.com/mattpocock/skills/pull/551), [#766](https://github.com/mattpocock/skills/pull/766), [issue #748](https://github.com/mattpocock/skills/issues/748). | Keep optional provider metadata aligned with actual invocation policy and names. | Sidecars exist. Preserve implicit invocation for router targets; do not copy Matt's user-only policy indiscriminately. |
| [#781](https://github.com/mattpocock/skills/pull/781). | Express capabilities rather than a provider's particular agent/tool names. | Previously addressed in source retrieval wording. Runtime tool availability still needs testing. |
| [#878](https://github.com/mattpocock/skills/pull/878), [#880](https://github.com/mattpocock/skills/pull/880), [issue #453](https://github.com/mattpocock/skills/issues/453). | Test cross-skill dispatch and target invocation policy together. | `start-learn` has portable loading wording and missing-target behavior. Actual dispatch tests are still required. Importing “call the Skill tool” verbatim would reintroduce provider coupling. |
| [#650](https://github.com/mattpocock/skills/pull/650). | Give references explicit loading conditions, co-locate rules and exceptions, use observable completion criteria, distinguish a procedure from a format reference. | Direct lesson-format pointer was added. Nine skill bodies still repeat rules across protocol, anti-patterns, and governing principles; review with a requirement map and behavioral comparison before deleting. Shortening alone is not evidence of improvement. |
| [#463](https://github.com/mattpocock/skills/pull/463). | Prefer an actionable positive target alongside a necessary prohibition. | Worth testing against the many local “Don't…” anti-patterns. Preserve answer-withholding and source-closed guardrails. Upstream's explanation about negation is a practitioner hypothesis, not a universal measured result. |
| [#682](https://github.com/mattpocock/skills/pull/682). | Read environment facts instead of maintaining stale copies of them. | Local skills already read project versions. Keep those steps; audit fixed examples as examples, and avoid treating example versions as detected facts. |
| [#472](https://github.com/mattpocock/skills/pull/472), [issue #471](https://github.com/mattpocock/skills/issues/471). | Respect the configured artifact location instead of silently falling back to a hardcoded path. | Workspace/legacy path branches deserve explicit integration cases. This does not justify removing intentional paths from the workspace contract. |
| [#504](https://github.com/mattpocock/skills/pull/504), [issue #495](https://github.com/mattpocock/skills/issues/495). | Generated prose can contain serialization leftovers even when Markdown looks plausible. | Add such cases to a structural review when generation/import occurs; no equivalent local stray-tag defect established by this report. |
| [#406](https://github.com/mattpocock/skills/pull/406). | Keep router choices and installed skill inventory synchronized when names or capabilities change. | Check `start-learn/FLOWS.md` against the nine installed names and routing intent. Do not make every skill a router target if the pedagogical flow intentionally excludes it. |
| [#779](https://github.com/mattpocock/skills/pull/779). | Code/log excerpts retained in notes or exercises should not retain secrets. | Candidate targeted artifact-safety test for code-mode learning. No actual credential exposure identified here. |
| [#1083](https://github.com/mattpocock/skills/pull/1083). | Put mechanical invariants in deterministic checks, and verify the checks are actually run. | A local validator is useful, but CI/pre-commit wiring must be inspected separately. Prose promises and a one-off green run do not enforce future changes. |
| [#488](https://github.com/mattpocock/skills/pull/488), [#1092](https://github.com/mattpocock/skills/pull/1092). | Preserve original evidence and distinguish the intended outcome from measured before/after behavior. | Retain test transcripts, environment/model versions, and rubric outcomes for skill changes. A statement that validation passed is weaker than reproducible evidence. |

The five issues explicitly followed above (#907, #748, #453, #471, #495) were all `closed` with `state_reason: completed` when retrieved. Their reports establish observed upstream failures in their stated environments; they do not establish that the identical failure occurred locally.

## What not to copy

- [#7](https://github.com/mattpocock/skills/pull/7) proposes improved third-party “skill scores”, including 100% scores, but is **closed without merge** in this snapshot. Its own body notes judge variance. These scores are not proof of 100% runtime performance or learning efficacy.
- [#393](https://github.com/mattpocock/skills/pull/393) moves TDD refactoring responsibility into a different stage. That is an upstream workflow decision, not a portable requirement for learning skills.
- [#593](https://github.com/mattpocock/skills/pull/593) switches interviewing to multi-question rounds. Copying that would violate local one-question-at-a-time pedagogy in several skills.
- [#807](https://github.com/mattpocock/skills/pull/807) and [#565](https://github.com/mattpocock/skills/pull/565) propose packaging changes but remain **open**. Treat as proposals, not shipped standards.
- Punctuation preferences, ticket tracker mechanics, personal-wiki paths, and Matt's release process do not transfer automatically. More copied conventions can reduce portability.

## Next verification work

Prioritize real dispatch/discovery cases; then isolated installation and resource loading; then multi-turn behavior with hidden-answer constraints, source failures, termination/transfer rules, and workspace path variants. Run a baseline/current comparison on the intended applications and models with recorded transcripts and repeated cases. Use upstream changes as test hypotheses, not proof that local behavior improved. No cross-provider runtime or educational outcome experiment was performed for this report.

## Complete PR title inventory

“Targeted diff review” means relevant file patches only. “Related; metadata screen only” is a candidate or contextual precedent, not an endorsement. “No direct transfer selected” records triage rather than proof of irrelevance. Full original bodies are retained in the companion JSON.

| PR | State | Title | Screening |
| --- | --- | --- | --- |
| [#1](https://github.com/mattpocock/skills/pull/1) | closed | Add frontmatter to skills missing YAML metadata | related; metadata screen only |
| [#2](https://github.com/mattpocock/skills/pull/2) | closed | Enhance SKILL.md with metadata and instructions | related; metadata screen only |
| [#4](https://github.com/mattpocock/skills/pull/4) | closed | update write-a-prd with name and description | related; metadata screen only |
| [#5](https://github.com/mattpocock/skills/pull/5) | closed | Add metadata and instructions for write-a-prd skill | related; metadata screen only |
| [#7](https://github.com/mattpocock/skills/pull/7) | closed | feat: improve skill scores across 11 skills | related; metadata screen only |
| [#8](https://github.com/mattpocock/skills/pull/8) | closed | feat: add native Claude Code marketplace support | related; metadata screen only |
| [#22](https://github.com/mattpocock/skills/pull/22) | closed | Improve grill-me guidance and broaden its sweet spot | related; metadata screen only |
| [#25](https://github.com/mattpocock/skills/pull/25) | closed | feat(tolling) convert from gh to az devops cli for interactions | no direct transfer selected |
| [#26](https://github.com/mattpocock/skills/pull/26) | closed | Update SKILL.md | related; metadata screen only |
| [#27](https://github.com/mattpocock/skills/pull/27) | closed | feat: two-tier repo-aware git guardrails | no direct transfer selected |
| [#28](https://github.com/mattpocock/skills/pull/28) | closed | [Security] Add security lens, priority ordering, and challenge behavior to grill-me skill | no direct transfer selected |
| [#30](https://github.com/mattpocock/skills/pull/30) | closed | update skills for jira and bdd workflows | no direct transfer selected |
| [#32](https://github.com/mattpocock/skills/pull/32) | closed | Add Claude code official marketplace and plugins support | related; metadata screen only |
| [#34](https://github.com/mattpocock/skills/pull/34) | closed | Publish remaining local Hermes skills to wiki | no direct transfer selected |
| [#39](https://github.com/mattpocock/skills/pull/39) | closed | Refine grill-me skill  | related; metadata screen only |
| [#40](https://github.com/mattpocock/skills/pull/40) | closed | refactor: restructure repo as enterprise plugin marketplace | related; metadata screen only |
| [#41](https://github.com/mattpocock/skills/pull/41) | closed | Add marketplace.json for plugin discovery | related; metadata screen only |
| [#42](https://github.com/mattpocock/skills/pull/42) | closed | Update SKILL.md | related; metadata screen only |
| [#43](https://github.com/mattpocock/skills/pull/43) | closed | Task/update ideation | no direct transfer selected |
| [#46](https://github.com/mattpocock/skills/pull/46) | closed | Make the write-a-skill line-limit consistent | related; metadata screen only |
| [#48](https://github.com/mattpocock/skills/pull/48) | closed | Fix formatting and wording in SKILL.md | related; metadata screen only |
| [#50](https://github.com/mattpocock/skills/pull/50) | closed | Enhance interview instructions with assumption verification | related; metadata screen only |
| [#51](https://github.com/mattpocock/skills/pull/51) | closed | Document the missing installable skills in the README | related; metadata screen only |
| [#52](https://github.com/mattpocock/skills/pull/52) | closed | Fix documentation for skills naming consistency | related; metadata screen only |
| [#53](https://github.com/mattpocock/skills/pull/53) | closed | add feature-complete skill | no direct transfer selected |
| [#56](https://github.com/mattpocock/skills/pull/56) | closed | feat: support native GitHub sub-issues for /to-issues skill | no direct transfer selected |
| [#57](https://github.com/mattpocock/skills/pull/57) | closed | fix: support both bun.lock and bun.lockb for Bun detection | no direct transfer selected |
| [#58](https://github.com/mattpocock/skills/pull/58) | closed | feat(grill-me): enforce numbered Q&A with recommended answers | related; metadata screen only |
| [#59](https://github.com/mattpocock/skills/pull/59) | closed | feat(to-issues): attach child issues as native sub-issues | no direct transfer selected |
| [#60](https://github.com/mattpocock/skills/pull/60) | closed | fix(setup-pre-commit): support both bun.lock and bun.lockb for Bun detection | no direct transfer selected |
| [#61](https://github.com/mattpocock/skills/pull/61) | closed | feat(to-issues): attach child issues as native sub-issues | no direct transfer selected |
| [#62](https://github.com/mattpocock/skills/pull/62) | closed | Add skill: max-prd-loop | no direct transfer selected |
| [#64](https://github.com/mattpocock/skills/pull/64) | closed | Update README.md | no direct transfer selected |
| [#65](https://github.com/mattpocock/skills/pull/65) | closed | fix: correct bun lockfile extension from bun.lockb to bun.lock | no direct transfer selected |
| [#66](https://github.com/mattpocock/skills/pull/66) | closed | feat(to-issues): attach child issues as native sub-issues via API | no direct transfer selected |
| [#67](https://github.com/mattpocock/skills/pull/67) | closed | Create SECURITY.md for security policy | no direct transfer selected |
| [#74](https://github.com/mattpocock/skills/pull/74) | closed | Fix npx command paths in README | related; metadata screen only |
| [#75](https://github.com/mattpocock/skills/pull/75) | closed | fix typo in readme | no direct transfer selected |
| [#81](https://github.com/mattpocock/skills/pull/81) | closed | Separate content skills from backlog backend (#80) | related; metadata screen only |
| [#90](https://github.com/mattpocock/skills/pull/90) | merged | Add setup-matt-pocock-skills; rename github-triage; migrate skills to vague prose | related; metadata screen only |
| [#291](https://github.com/mattpocock/skills/pull/291) | merged | Split skills into model-invoked vs user-invoked | related; metadata screen only |
| [#345](https://github.com/mattpocock/skills/pull/345) | merged | chore: version skills | no direct transfer selected |
| [#347](https://github.com/mattpocock/skills/pull/347) | merged | chore: version skills | related; metadata screen only |
| [#353](https://github.com/mattpocock/skills/pull/353) | merged | chore: version skills | no direct transfer selected |
| [#393](https://github.com/mattpocock/skills/pull/393) | merged | tdd: reshape into reference-only with pre-agreed seams | targeted diff review |
| [#394](https://github.com/mattpocock/skills/pull/394) | merged | feat(review): always-on Fowler smell baseline in the Standards axis | related; metadata screen only |
| [#395](https://github.com/mattpocock/skills/pull/395) | merged | docs(link-skills): mark as a dev-only script | related; metadata screen only |
| [#398](https://github.com/mattpocock/skills/pull/398) | merged | Generalize decision-mapping beyond engineering | no direct transfer selected |
| [#401](https://github.com/mattpocock/skills/pull/401) | merged | Add Task ticket type to decision-mapping skill | no direct transfer selected |
| [#402](https://github.com/mattpocock/skills/pull/402) | merged | docs: rework the skill docs-page template | related; metadata screen only |
| [#403](https://github.com/mattpocock/skills/pull/403) | merged | docs: pages for the remaining 22 promoted skills | related; metadata screen only |
| [#404](https://github.com/mattpocock/skills/pull/404) | merged | docs: end the build chain at implement, not tdd | related; metadata screen only |
| [#405](https://github.com/mattpocock/skills/pull/405) | merged | Rename review skill to code-review, promote to engineering | related; metadata screen only |
| [#406](https://github.com/mattpocock/skills/pull/406) | merged | ask-matt: map the full skill set, add router maintenance rule | targeted diff review |
| [#408](https://github.com/mattpocock/skills/pull/408) | merged | chore: add implement skill to public plugin set | related; metadata screen only |
| [#409](https://github.com/mattpocock/skills/pull/409) | merged | Add the research skill | related; metadata screen only |
| [#410](https://github.com/mattpocock/skills/pull/410) | closed | v1.1: planning-skills unification (breaking) + wayfinder graduation | no direct transfer selected |
| [#412](https://github.com/mattpocock/skills/pull/412) | merged | Rename decision-mapping skill to wayfinder | no direct transfer selected |
| [#413](https://github.com/mattpocock/skills/pull/413) | merged | feat(wayfinder): make the map collaborative via the issue tracker | no direct transfer selected |
| [#419](https://github.com/mattpocock/skills/pull/419) | merged | refactor(wayfinder): make the map an index, not a store | no direct transfer selected |
| [#420](https://github.com/mattpocock/skills/pull/420) | merged | fix(wayfinder): rename "Two branches" to "Two modes" | no direct transfer selected |
| [#421](https://github.com/mattpocock/skills/pull/421) | merged | Add claude-handoff skill (in-progress) | no direct transfer selected |
| [#422](https://github.com/mattpocock/skills/pull/422) | merged | wayfinder: refer to maps and tickets by name, not id | no direct transfer selected |
| [#424](https://github.com/mattpocock/skills/pull/424) | closed | wayfinder: recheck claims before showing the frontier in Handoff | no direct transfer selected |
| [#425](https://github.com/mattpocock/skills/pull/425) | merged | wayfinder: remove the Handoff ceremony | no direct transfer selected |
| [#428](https://github.com/mattpocock/skills/pull/428) | merged | wayfinder: reframe description around planning big work | no direct transfer selected |
| [#433](https://github.com/mattpocock/skills/pull/433) | merged | grilling: add confirmation gate and grill leading word | related; metadata screen only |
| [#434](https://github.com/mattpocock/skills/pull/434) | merged | docs: fix tdd skill reference to code-review skill | related; metadata screen only |
| [#435](https://github.com/mattpocock/skills/pull/435) | merged | wayfinder: prefer native blocking, and say why | no direct transfer selected |
| [#436](https://github.com/mattpocock/skills/pull/436) | merged | wayfinder: claim by assigning the ticket, not a label | no direct transfer selected |
| [#455](https://github.com/mattpocock/skills/pull/455) | merged | Reframe wayfinder around "destination" as the leading word | no direct transfer selected |
| [#456](https://github.com/mattpocock/skills/pull/456) | merged | wayfinder: split the map catch-all into Not yet specified / Out of scope | no direct transfer selected |
| [#459](https://github.com/mattpocock/skills/pull/459) | merged | to-issues: prefer native sub-issues; reference /prototype code explicitly | no direct transfer selected |
| [#460](https://github.com/mattpocock/skills/pull/460) | merged | wayfinder: restore no-fog early exit | no direct transfer selected |
| [#461](https://github.com/mattpocock/skills/pull/461) | merged | wayfinder/grilling: stop the agent grilling itself | related; metadata screen only |
| [#462](https://github.com/mattpocock/skills/pull/462) | merged | wayfinder: reassert planning-only purpose | no direct transfer selected |
| [#463](https://github.com/mattpocock/skills/pull/463) | merged | writing-great-skills: add Negation failure mode | targeted diff review |
| [#464](https://github.com/mattpocock/skills/pull/464) | merged | v1.1: planning-skills unification (breaking) + wayfinder graduation | related; metadata screen only |
| [#469](https://github.com/mattpocock/skills/pull/469) | merged | to-issues: slice wide refactors by expand–contract | no direct transfer selected |
| [#472](https://github.com/mattpocock/skills/pull/472) | merged | fix(wayfinder): resolve issue-tracker doc via the CLAUDE.md pointer, not a hardcoded path | targeted diff review |
| [#488](https://github.com/mattpocock/skills/pull/488) | merged | prototype: keep the prototype as a primary source | targeted diff review |
| [#502](https://github.com/mattpocock/skills/pull/502) | merged | Friendlier setup flow + one-file-per-ticket local tracker | related; metadata screen only |
| [#503](https://github.com/mattpocock/skills/pull/503) | merged | chore: version skills | no direct transfer selected |
| [#504](https://github.com/mattpocock/skills/pull/504) | merged | fix(to-tickets): remove stray </content> tag | targeted diff review |
| [#505](https://github.com/mattpocock/skills/pull/505) | merged | Add setup-ts-deep-modules skill (in-progress) | no direct transfer selected |
| [#506](https://github.com/mattpocock/skills/pull/506) | closed | fix(to-tickets): publish one local file per ticket, not a single tickets.md | related; metadata screen only |
| [#522](https://github.com/mattpocock/skills/pull/522) | closed | Gabimoncha/codex port | related; metadata screen only |
| [#532](https://github.com/mattpocock/skills/pull/532) | merged | grilling: reword the primitive for general use | related; metadata screen only |
| [#533](https://github.com/mattpocock/skills/pull/533) | merged | improve-codebase-architecture: scope the scan to where change is landing (YAGNI) | no direct transfer selected |
| [#534](https://github.com/mattpocock/skills/pull/534) | merged | Name the wayfinder unit a "decision ticket" | no direct transfer selected |
| [#535](https://github.com/mattpocock/skills/pull/535) | merged | ask-matt: give /wayfinder real routing help | related; metadata screen only |
| [#536](https://github.com/mattpocock/skills/pull/536) | merged | feat: ship the skill set as a native Claude Code plugin (v1.2) | related; metadata screen only |
| [#537](https://github.com/mattpocock/skills/pull/537) | closed | wayfinder: run research inline as a subagent, not as a ticket | no direct transfer selected |
| [#538](https://github.com/mattpocock/skills/pull/538) | merged | wayfinder: burn research tickets down with subagents | no direct transfer selected |
| [#539](https://github.com/mattpocock/skills/pull/539) | merged | fix: finish promoted-bucket wiring for resolving-merge-conflicts and implement | related; metadata screen only |
| [#551](https://github.com/mattpocock/skills/pull/551) | merged | feat: add Codex agents/openai.yaml metadata to every skill | targeted diff review |
| [#565](https://github.com/mattpocock/skills/pull/565) | open | refactor(plugin): self-maintaining directory form for plugin skills | related; metadata screen only |
| [#572](https://github.com/mattpocock/skills/pull/572) | merged | Add to-questionnaire skill (in-progress) | no direct transfer selected |
| [#586](https://github.com/mattpocock/skills/pull/586) | merged | batch-grill-me: granular fact-finding, don't block the round | no direct transfer selected |
| [#593](https://github.com/mattpocock/skills/pull/593) | merged | Release v1.2 | related; metadata screen only |
| [#647](https://github.com/mattpocock/skills/pull/647) | open | feat(spawn): generalise claude-handoff into agent-agnostic spawn skill | related; metadata screen only |
| [#650](https://github.com/mattpocock/skills/pull/650) | merged | feat!: rename writing-great-skills → writing-for-agents and restructure | targeted diff review |
| [#679](https://github.com/mattpocock/skills/pull/679) | merged | Graduate to-questionnaire into the Productivity bucket | no direct transfer selected |
| [#680](https://github.com/mattpocock/skills/pull/680) | merged | Graduate wizard into the Engineering bucket | no direct transfer selected |
| [#681](https://github.com/mattpocock/skills/pull/681) | merged | docs: split install instructions by audience | related; metadata screen only |
| [#682](https://github.com/mattpocock/skills/pull/682) | merged | feat(writing-for-agents): add the *cache* leading word for environment truth | targeted diff review |
| [#734](https://github.com/mattpocock/skills/pull/734) | merged | docs: finish the to-prd → to-spec rename in shipped text | related; metadata screen only |
| [#749](https://github.com/mattpocock/skills/pull/749) | merged | docs: tell one true install story (official marketplace) | related; metadata screen only |
| [#750](https://github.com/mattpocock/skills/pull/750) | merged | feat: give ask-matt the phase boundary decision tree | related; metadata screen only |
| [#751](https://github.com/mattpocock/skills/pull/751) | merged | feat: add wait-what, the verbosity fire extinguisher | related; metadata screen only |
| [#752](https://github.com/mattpocock/skills/pull/752) | merged | chore: remove six unused skills and the personal bucket | related; metadata screen only |
| [#753](https://github.com/mattpocock/skills/pull/753) | closed | docs: drop the Quickstart block from all 24 pages | no direct transfer selected |
| [#754](https://github.com/mattpocock/skills/pull/754) | merged | docs: drop the Quickstart block from all 25 pages | related; metadata screen only |
| [#755](https://github.com/mattpocock/skills/pull/755) | merged | docs: rewrite the grill-me page around what people get wrong | related; metadata screen only |
| [#757](https://github.com/mattpocock/skills/pull/757) | merged | docs: remove the source link from every skills page | no direct transfer selected |
| [#758](https://github.com/mattpocock/skills/pull/758) | merged | docs: rewrite the writing-for-agents page around what people get wrong | related; metadata screen only |
| [#759](https://github.com/mattpocock/skills/pull/759) | merged | docs: make Common questions and It's working if part of the page standard | related; metadata screen only |
| [#760](https://github.com/mattpocock/skills/pull/760) | merged | docs: drop the fire-extinguisher metaphor from wait-what | no direct transfer selected |
| [#761](https://github.com/mattpocock/skills/pull/761) | merged | docs: rewrite every skills page to the four-section standard | related; metadata screen only |
| [#762](https://github.com/mattpocock/skills/pull/762) | merged | skill: make wizard model-invoked | related; metadata screen only |
| [#763](https://github.com/mattpocock/skills/pull/763) | merged | chore: condense changesets and drop docs-only entries | no direct transfer selected |
| [#764](https://github.com/mattpocock/skills/pull/764) | merged | docs: drop the human-in-the-loop lecture from the wizard page | no direct transfer selected |
| [#765](https://github.com/mattpocock/skills/pull/765) | merged | docs: link first use of AI Coding Dictionary terms | no direct transfer selected |
| [#766](https://github.com/mattpocock/skills/pull/766) | merged | fix: make writing-for-agents model-invokable in Codex | targeted diff review |
| [#767](https://github.com/mattpocock/skills/pull/767) | merged | docs: write the pages in neutral third person | related; metadata screen only |
| [#768](https://github.com/mattpocock/skills/pull/768) | merged | chore: version skills | no direct transfer selected |
| [#769](https://github.com/mattpocock/skills/pull/769) | merged | chore: sync the plugin version from package.json on release | related; metadata screen only |
| [#779](https://github.com/mattpocock/skills/pull/779) | merged | fix: make diagnosing-bugs redact secrets | targeted diff review |
| [#781](https://github.com/mattpocock/skills/pull/781) | merged | fix: make subagent dispatch harness-neutral | targeted diff review |
| [#782](https://github.com/mattpocock/skills/pull/782) | merged | chore: version skills | no direct transfer selected |
| [#783](https://github.com/mattpocock/skills/pull/783) | merged | refactor(wizard): remove the minutes estimate | related; metadata screen only |
| [#788](https://github.com/mattpocock/skills/pull/788) | merged | docs(grill-me): drop the "holds decisions" phrasing | no direct transfer selected |
| [#807](https://github.com/mattpocock/skills/pull/807) | open | refactor: flatten skills/ and adopt Agent Plugins 1.0 | related; metadata screen only |
| [#848](https://github.com/mattpocock/skills/pull/848) | merged | domain-modeling: trigger on CONTEXT.md / ADR writes | related; metadata screen only |
| [#849](https://github.com/mattpocock/skills/pull/849) | open | chore: version skills | no direct transfer selected |
| [#876](https://github.com/mattpocock/skills/pull/876) | open | rename CONTEXT.md/CONTEXT-MAP.md convention to GLOSSARY.md/GLOSSARY-MAP.md | related; metadata screen only |
| [#878](https://github.com/mattpocock/skills/pull/878) | merged | Standardize cross-skill invocation on "call the Skill tool" phrasing | targeted diff review |
| [#879](https://github.com/mattpocock/skills/pull/879) | merged | Remove em-dashes from grilling skill | no direct transfer selected |
| [#880](https://github.com/mattpocock/skills/pull/880) | merged | Stop skills from calling other user-invoked skills | targeted diff review |
| [#889](https://github.com/mattpocock/skills/pull/889) | closed | Stub: retro skill — raw idea dump | no direct transfer selected |
| [#891](https://github.com/mattpocock/skills/pull/891) | merged | Remove single-writer section from grill-with-docs docs | no direct transfer selected |
| [#904](https://github.com/mattpocock/skills/pull/904) | merged | wait-what: follow CONTEXT-MAP.md to the right CONTEXT.md | related; metadata screen only |
| [#905](https://github.com/mattpocock/skills/pull/905) | merged | Remove all em-dashes from the repo | targeted diff review |
| [#911](https://github.com/mattpocock/skills/pull/911) | merged | Fix invalid YAML front matter in six SKILL.md files | targeted diff review |
| [#917](https://github.com/mattpocock/skills/pull/917) | merged | grilling: separate questions in a round with an HR | related; metadata screen only |
| [#926](https://github.com/mattpocock/skills/pull/926) | merged | Add implement-spec skill (in-progress) with its bucket docs | no direct transfer selected |
| [#1025](https://github.com/mattpocock/skills/pull/1025) | merged | link-skills: stop linking misc/ into local skill directories | related; metadata screen only |
| [#1083](https://github.com/mattpocock/skills/pull/1083) | merged | retro: push mechanical coding-standards findings toward deterministic checks | targeted diff review |
| [#1092](https://github.com/mattpocock/skills/pull/1092) | merged | Add the pr skill (in-progress): reference for a fast-to-review PR body | targeted diff review |
