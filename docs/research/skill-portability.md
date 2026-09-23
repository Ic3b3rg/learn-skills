# Skill portability research

Research date: 2026-09-23. Local baseline: `bbfd0916ce6a8b3318dc6de7728821e832d53d51`. Matt Pocock repository inspected at `c55ee46073ed923f86ce59a5eb3b6d895095d1b7`.

## Finding

The nine learning workflows can retain their content and intended behavior while improving parsing, packaging, discovery, and wording. The clearest defect is invalid YAML in `start-learn`; the clearest portability weakness is that every skill depends on a source-policy file outside its installable folder. These are local static findings, not claims that every client currently fails. No provider runtime or learning session was exercised for this report.

The scope below distinguishes the **agent application** (Claude Code, Codex, Copilot, Gemini CLI, Cursor) from the underlying model. Shared file-format support does not establish identical model behavior, permission handling, tool availability, or packaging. Recommendations are proposals; this research changes no skill.

## What the official guidance actually says

The Agent Skills standard requires a folder containing `SKILL.md`, with YAML `name` and `description`. Names must match the enclosing folder and satisfy the documented lowercase naming rules; descriptions have a 1,024-character limit. The standard describes full-body loading on activation, recommends under 500 lines and under 5,000 tokens for instructions, and recommends relative, shallow references. Optional `compatibility` describes actual environment requirements; `allowed-tools` is experimental and varies by implementation. These are format and authoring rules, not an execution guarantee. [Agent Skills specification](https://agentskills.io/specification)

Anthropic recommends concise instructions, descriptions covering purpose and triggering situations, third-person descriptions, and details disclosed through references when needed. It loads metadata initially, the body when relevant, and resources on demand. Its guidance recommends a body under 500 lines and tests against the models intended for use, including real scenarios and at least three evaluations. It also recommends observing missed references and unwanted activation. [Anthropic authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

Consequently, the local 100-line limit can remain an editorial constraint, but its rationale should change. [CLAUDE.md](../../CLAUDE.md) says Claude previews with `head -100` and cannot see later instructions during discovery. The sources above do not establish that mechanism; they describe metadata-first discovery and subsequent full-body loading. Do not extend all skills to 500 lines simply because a larger recommendation exists.

## Application compatibility

This table records documented support, not successful installation of this repository.

| Application | Documented route | What remains application-specific |
| --- | --- | --- |
| Claude Code | Personal/project `.claude/skills/<name>/SKILL.md`; plugin skills under `skills/`. | Direct `/name` invocation differs from plugin `/plugin-name:skill-name`; invocation controls, subprocess contexts and dynamic injection are extensions. [Claude Code skills](https://code.claude.com/docs/en/skills) |
| Codex | Repository and user `.agents/skills`; plugins for reusable distribution. | Explicit `$skill` invocation; optional `agents/openai.yaml` controls presentation and invocation. `allow_implicit_invocation` defaults to true; false prevents implicit activation. [OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills) |
| GitHub Copilot in VS Code | Project `.github/skills`, `.claude/skills`, `.agents/skills`; personal `.copilot/skills`, `.claude/skills`, `.agents/skills`. | The documentation also describes Copilot CLI and cloud-agent support, but does not replace testing each surface. Name/folder alignment matters. [VS Code skills](https://code.visualstudio.com/docs/agent-customization/agent-skills) |
| Gemini CLI | User/workspace `.gemini/skills` or `.agents/skills`; `gemini skills install` and `link`. | Activation has a consent step. Its `/skills` commands manage skills; do not assume Claude-style direct `/quiz-me` dispatch. [Gemini management](https://geminicli.com/docs/cli/using-agent-skills/), [activation tool](https://geminicli.com/docs/tools/activate-skill/) |
| Cursor | Project/user `.agents/skills` and `.cursor/skills`, with Claude/Codex directories also supported. | Local discovery is distinct from cloud synchronization: documented user-skill sync applies to `.cursor/skills`, not `.agents/skills`. [Cursor skills](https://cursor.com/docs/skills) |

Recommendation: retain one canonical skill body per methodology, keep optional provider metadata separate, and document provider-specific installation/invocation. Do not introduce five copies of each pedagogical workflow. A Claude or Codex plugin manifest is not evidence that another application's installer consumes that manifest.

## Local findings and conservative changes

### 1. Invalid frontmatter: confirmed

[start-learn/SKILL.md](../../skills/start-learn/SKILL.md) contains unquoted `Scenario A:` and `Scenario B:` text in a plain YAML description. Ruby's standard YAML parser reports a mapping error; the other eight skill frontmatter blocks parse successfully. Reproduction, requiring no dependency installation:

```sh
ruby -ryaml -e 'Dir["skills/*/SKILL.md"].sort.each { |p| begin; YAML.safe_load(File.read(p).split("---", 3)[1]); puts "OK #{p}"; rescue Psych::SyntaxError => e; puts "INVALID #{p}: #{e.message.lines.first.strip}"; end }'
```

Observed error: `mapping values are not allowed in this context at line 3 column 211`. Quote the existing description or use a folded YAML scalar, preserving its wording. Validate extracted frontmatter with a real YAML parser; checking only the opening `---` cannot catch this failure. This check is a syntax reproduction, not a complete schema validator.

Other local checks: all nine skill files meet the repository's 100-line cap; all nine `agents/openai.yaml` files parse and contain interface metadata without an explicit invocation policy; all four plugin/marketplace manifests parse as JSON. All Markdown link targets checked in `SKILL.md` exist in the full checkout. These results establish syntax and checkout integrity only, not schema compliance or successful installation.

### 2. Resources outside the skill folder: confirmed structural dependency

All nine `SKILL.md` files link `../../docs/sources.md`. Some also link ADRs outside their folders. These links resolve in the full checkout, but copying an individual skill folder does not copy those targets. Evidence: [source policy](../sources.md), [quiz-me](../../skills/quiz-me/SKILL.md), [assess](../../skills/assess/SKILL.md), [learn-by-doing](../../skills/learn-by-doing/SKILL.md), [flashcards](../../skills/flashcards/SKILL.md).

Preserve the full operational source policy in any distributed skill that needs it. One option is generated, byte-checked bundled copies from the canonical policy; another is a package layout whose installer demonstrably preserves the shared target. Distinguish operative policy from historical rationale: ADR links can become stable repository links without making their explanatory text part of every invocation. Test both the full package and a single copied skill in a temporary directory. Do not silently shorten the source hierarchy while fixing its location.

### 3. Named tools: confirmed wording, runtime effect untested

Several skills and [docs/sources.md](../sources.md) name `Read`, `WebFetch`, `WebSearch`, or `context7`. Replace mandatory tool names with the capabilities already intended: read local files, retrieve version-pinned official documentation, fetch the supplied URL, search for the canonical source when necessary. Context7 can remain an optional example. Preserve retrieval order, citations, version anchoring, and the existing uncertainty fallback. This changes the mechanism's wording, not the verification standard.

### 4. Discovery versus cross-skill execution

[start-learn](../../skills/start-learn/SKILL.md) must select and run a methodology in Scenario A; [ADR 0004](../adr/0004-agent-selects-methodology.md) explicitly establishes this. Preserve automatic selection and user redirection. The portable instruction should name the target workflow and require its instructions to be loaded using the client's supported mechanism, rather than assuming literal slash-command text executes everywhere. Keep invocation metadata consistent across the body, Claude frontmatter, and Codex `agents/openai.yaml`.

This is a regression concern, not a confirmed local disabled-invocation bug. An individually installed `start-learn` also needs its target skills available; document that dependency and give a truthful missing-target response. Do not replace a missing workflow with an invented approximation or switch Scenario A to a user-selection menu.

### 5. References and wording

[start-learn/SKILL.md](../../skills/start-learn/SKILL.md) directly points to `FLOWS.md` and `WORKSPACE.md`, while the lesson-format instructions are reached through another reference. Add a direct conditional pointer to [LESSON-FORMAT.md](../../skills/start-learn/LESSON-FORMAT.md) at the point where lesson generation is introduced. Translate existing Italian passages in workspace/lesson references into English without changing their requirements, following the repository convention. Neither change requires a new methodology.

Some apparent duplication contains useful exceptions. Before compressing anything, map each requirement to its surviving location. In particular, preserve the one-sentence prerequisite intervention in `explain-and-check`, the explicit exceptions to questions-only behavior in `ask-me-questions`, and the distinction between generated curriculum material and demonstrated mastery. [Explain-and-check](../../skills/explain-and-check/SKILL.md), [ask-me-questions](../../skills/ask-me-questions/SKILL.md), [start-learn flows](../../skills/start-learn/FLOWS.md)

## Matt Pocock: lessons backed by actual changes

The authoritative repository is [mattpocock/skills](https://github.com/mattpocock/skills). Its current [writing-for-agents](https://github.com/mattpocock/skills/blob/c55ee46073ed923f86ce59a5eb3b6d895095d1b7/skills/productivity/writing-for-agents/SKILL.md) favors clear steps, observable completion, explicit reference triggers, colocated rules, and one authoritative home per meaning. Apply those editorial ideas selectively; its invocation choices are not universal requirements for this project's automatic router.

| Verified upstream event | Relevant lesson here |
| --- | --- |
| [PR #911](https://github.com/mattpocock/skills/pull/911), merged 2026-08-19, fixes [issue #907](https://github.com/mattpocock/skills/issues/907), closed as completed. Unquoted colon-space descriptions broke YAML and caused installer discovery to skip six skills; quoting preserved wording. | An exact structural analogue of `start-learn`. Parse Markdown frontmatter, not merely standalone `.yaml` files. The upstream PR does not prove that our repository has been run through the same installer. |
| [PR #781](https://github.com/mattpocock/skills/pull/781), merged 2026-08-06, removes Claude-specific `Agent` and agent-type names while retaining parallel delegation requirements. | Direct precedent for replacing tool identifiers with capabilities without changing the workflow. Local analogy: source retrieval tool names. |
| [PR #766](https://github.com/mattpocock/skills/pull/766), merged 2026-08-05, closes [issue #748](https://github.com/mattpocock/skills/issues/748). Renamed skill metadata retained an old display name and disabled implicit invocation; the fix removed the stale policy. | Validate metadata together with descriptions and routing after renames. Preventive here; no equivalent local false policy was established. |
| [PR #880](https://github.com/mattpocock/skills/pull/880), merged 2026-08-15, fixes calls to user-invoked targets after invocation wording was standardized. | A mechanically consistent rewrite can still break dispatch. Preserve this project's model-invoked target skills and test Scenario A. Do not copy a user-only router policy into `start-learn`. |

These entries were checked through GitHub's first-party API for bodies and merge timestamps; #907 and #748 were additionally checked for closed/completed status. An open PR, a closed-but-unmerged PR, or a PR's unchecked test-plan item is not evidence of a shipped fix or successful runtime test.

## Preservation and verification plan

Recommended order, without expanding functionality:

1. Repair YAML with unchanged text; add deterministic frontmatter/name/reference checks.
2. Make the distributed resources complete and document actual application installation paths.
3. Replace tool-name assumptions, clarify dispatch, add direct reference pointers, and translate existing reference text.
4. Only then simplify repetitive prose, reviewing a before/after requirement map.

The invariant map should cover: all nine names and triggering intentions; language adaptation; code/topic mode selection; source and version policy; student-first sequencing; each workflow's permitted explanations and exceptions; output formats; assessment levels and no monolithic score; workspace paths/state; one-lesson-at-a-time delivery; transfer tests; and Scenario A routing versus Scenario B pacing. Do not treat a shortened file as evidence that its behavior survived.

Run structural checks on each isolated installable skill, including every referenced operational resource. Check optional metadata syntax and invocation consistency, not only JSON manifests. Keep the 100-line repository cap until deliberately revising that local convention.

Then run the same small scenario set before and after on each claimed application/model combination: (a) a recall session that withholds the source until the learner answers; (b) a from-scratch workspace creating only the requested lesson; (c) automatic Scenario A routing; (d) absent web retrieval with honest uncertainty; (e) questions-only behavior and its explicit exceptions; (f) taxonomy assessment retaining discrete levels. Include negative trigger prompts and missing-dependency cases. Record application/model version, install method, resources read, and observed output against the invariant map. These runs are proposed and **not performed** here.

Static validity can establish that files parse and resources ship. Only those behavioral checks can support a claim that the intended functionality remains equivalent across applications and models.
