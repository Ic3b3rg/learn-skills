# Learn Skills

**Understand the code you ship.**

Nine agent skills for learning from your codebase or studying a new topic. Explain what you understand, practise retrieving it, work through exercises, and get feedback checked against real code and documentation.

Start with `start-learn` if you are unsure which workflow to use. It chooses an approach for existing code or helps you create a learning workspace for a new topic. You can redirect it at any time.

[Get started](#get-started) · [Choose a skill](#choose-a-skill) · [Examples](#examples) · [Learning workspace](#learning-workspace) · [Compatibility](#compatibility) · [Contributing](#contributing-and-validation)

## Get started

You need an agent application that supports skills and can read the files you want to study. Generating exercises, notes, or lessons also needs file-writing access. External verification uses documentation access when available; unavailable sources should be disclosed rather than invented.

### Codex

Run in your terminal:

```bash
codex plugin marketplace add Ic3b3rg/learn-skills
codex plugin add learn-skills@learn-skills
codex plugin list
```

Start a new Codex thread in your project, then send:

```text
$start-learn I want to understand src/orders/payment.ts.
```

### Claude Code

Run inside Claude Code:

```text
/plugin marketplace add Ic3b3rg/learn-skills
/plugin install learn-skills@ic3b3rg-learn-skills
```

Then send:

```text
/learn-skills:start-learn I want to understand src/orders/payment.ts.
```

Replace the example path with a file in your project. **Learn Skills is the plugin name; `start-learn` is the entry skill.** There is no `/learn-skills` command by itself.

## Choose a skill

Use `$name` in Codex or `/learn-skills:name` with the Claude Code plugin.

| You want to… | Skill | What happens |
| --- | --- | --- |
| Find a starting point | `start-learn` | Routes an existing-code goal to a suitable skill, or sets up a workspace for learning from scratch. |
| Check your explanation | `explain-and-check` | You explain first; the agent checks your account against the source and probes gaps. |
| Test what you remember | `quiz-me` | You close the source, confirm you are ready, and answer from memory before verification. |
| Connect a new idea to familiar ones | `connect-to-what-you-know` | You propose analogies; the agent checks their structure and where they break. |
| Reason through a problem | `ask-me-questions` | Guides you with one question at a time, with explicit exceptions for citations and safety. |
| Practise by doing | `learn-by-doing` | Creates 3–7 exercises with folded solutions, then verifies the attempts you submit. |
| Keep reusable notes | `linked-notes` | Captures individual ideas in your own words, with citations and links you approve. |
| Create recall material | `flashcards` | Builds cards from learner-authored questions with verified, folded answers. |
| Find gaps after studying | `assess` | Reports a demonstrated level, concrete gaps, and a suggested next skill; no 1–100 score. |

You can invoke any skill directly. The router is a convenience, not a required first step.

## Examples

These are example prompts and expected workflows, not transcripts of measured client runs.

### Understand code an agent just wrote

```text
$explain-and-check src/orders/payment.ts
```

The agent reads the relevant source and asks you to explain it. It checks your explanation, targets a misconception with a question, and asks you to apply the corrected understanding to a new case. You supply the explanation before receiving feedback.

### Get hands-on exercises

```text
$learn-by-doing src/orders/payment.ts
Create exercises that help me understand the payment flow.
```

The skill reads the project and source, then writes a Markdown exercise file with solutions inside `<details>` sections. Code-based sets include a debugging task. Submit an attempt when ready: feedback identifies a pass, partial answer, or failure with a source reference; a failed attempt gets a targeted question and a retry.

A small source file is included for trying this workflow:

```text
$learn-by-doing evals/fixtures/code/discount.js
```

### Learn a topic from scratch

```text
$start-learn I want to learn Rust ownership from scratch.
I know TypeScript and want to understand borrowing errors.
```

The agent asks where to create the workspace and proposes a curriculum. After you approve it, request `next lesson` to generate one HTML lesson at a time. Lessons include practice and source references; later lessons can use recorded progress.

### Check what stuck

```text
$quiz-me src/orders/payment.ts
```

Close the source when asked and confirm before answering. For a broader assessment after studying, use:

```text
$assess payment processing
```

Assessment labels describe performance on the sampled tasks. They are not a certification of overall ability.

For Claude Code, replace the prefix, for example:

```text
/learn-skills:learn-by-doing src/orders/payment.ts
```

## Learning workspace

For learning from scratch, `start-learn` creates a workspace at a path you choose:

```text
my-learning-workspace/
├── MISSION.md          # Your goal and constraints
├── CURRICULUM.md       # Editable lesson roadmap
├── NOTES.md            # Preferences and agent notes
├── RESOURCES.md        # Knowledge sources and community resources
├── lessons/            # HTML lessons generated on request
├── reference/
│   └── glossario.html  # Glossary expanded with lessons
├── learning-records/   # Assessment records
├── notes/             # Atomic notes
├── flashcards/        # Recall material
└── exercises/         # Practice sets
```

Enter that directory before starting a later session. Workspace-aware skills detect `CURRICULUM.md` in the current directory; they do not automatically find or switch to another workspace.

A checked curriculum item means its lesson was **generated**, not that you mastered it. You can edit and reorder the curriculum. Lessons are generated on demand rather than all at once.

### Where files go

| Output | In an ordinary project | Inside a learning workspace |
| --- | --- | --- |
| Exercises | `learn/<slug>-exercises.md` | `exercises/<slug>-exercises.md` |
| Notes | `learn/notes/<slug>.md` | `notes/<slug>.md` |
| Flashcards | `learn/flashcards/<slug>-cards.md` | `flashcards/<slug>-cards.md` |
| Assessment records | No records written | `learning-records/NNNN-<topic>-assessment.md` |

Generating a file is only preparation. Learning is assessed through the answers and attempts you bring back to the session.

## How the workflows work

- **Your attempt comes first.** Explain, recall, make an analogy, or solve an exercise before feedback.
- **Sources ground the feedback.** Code, tests, and authoritative documentation at the project's relevant versions take precedence over an agent's confidence.
- **Questions target gaps.** Workflows use focused prompts and retries rather than immediately giving away a solution.
- **Application matters.** Relevant workflows ask you to use an idea in a new situation; merely producing notes or cards does not demonstrate transfer.
- **You control the pace.** Request lessons and submit answers when ready. The instructions are in English; dialogue follows your language.

The methods draw on research into self-explanation, retrieval practice, analogy, and formative assessment. That research does **not** establish the effectiveness of this exact package, its question counts, or every model that runs it. See the [per-skill evidence review](docs/research/per-skill-quality.md) for primary sources and limits.

There is no review scheduler, spaced-repetition engine, or monolithic numeric learning score. See the [scope decision](docs/adr/0002-no-scheduling-no-monolithic-scores.md).

## Compatibility

The repository includes plugin packaging for **Codex** and **Claude Code**. The skill folders also carry their own reference files and source policy for standalone installation.

| Application | Project skill directory | Invocation |
| --- | --- | --- |
| Codex | `.agents/skills/` | `$skill-name` |
| Claude Code | `.claude/skills/` | `/skill-name` for standalone skills; `/learn-skills:skill-name` for this plugin |
| GitHub Copilot in VS Code | `.github/skills/` or `.agents/skills/` | Application-specific activation |
| Gemini CLI | `.gemini/skills/` or `.agents/skills/` | Application-specific activation |
| Cursor | `.cursor/skills/` or `.agents/skills/` | Application-specific activation |

Copy **complete skill folders**, including reference files and `SOURCES.md`, into the host's supported directory. Install all nine if you want `start-learn` to route between workflows. Optional `agents/openai.yaml` files supply Codex UI metadata.

These discovery paths are documented by the applications; they are not a claim that this package has passed runtime tests on every client or model. See the [compatibility research and official sources](docs/research/skill-portability.md#application-compatibility).

### Local development installation

```bash
git clone https://github.com/Ic3b3rg/learn-skills.git
cd learn-skills
```

For Claude Code:

```bash
claude --plugin-dir .
```

For Codex:

```bash
codex plugin marketplace add .
codex plugin add learn-skills@learn-skills
codex plugin list
```

Start a new session after installation.

## Troubleshooting

**The plugin is installed, but a command is missing.** Start a new thread or restart the application. Check the command prefix above. In Codex, use `codex plugin list` to check installation.

**The Claude Code marketplace command fails because SSH is unavailable.** Use HTTPS:

```text
/plugin marketplace add https://github.com/Ic3b3rg/learn-skills.git
/plugin install learn-skills@ic3b3rg-learn-skills
```

**`start-learn` reports a missing workflow.** Install the full set of skill folders. The router needs the selected skill's instructions to run it.

**Files appear under `learn/` instead of the workspace folders.** Check your current directory. Workspace detection requires `CURRICULUM.md` there.

**A source cannot be verified.** Provide the relevant file or documentation, or enable the required access. The workflow should disclose missing evidence rather than manufacture a citation.

**Codex exits with `spawn ... vendor/.../codex/codex ENOENT`.** The error points to the CLI executable path. Check `which codex` and `codex --version`. If you installed Codex globally through npm, reinstall that installation:

```bash
npm uninstall -g @openai/codex
npm install -g @openai/codex@latest
```

Refresh your shell's command cache (`rehash` in zsh, `hash -r` in bash), then retry `codex --version` and `codex plugin list`.

## Contributing and validation

Keep changes focused on the existing learning behavior unless you are explicitly proposing a methodology change. Repository documents are in English. See [CLAUDE.md](CLAUDE.md) for authoring conventions.

After editing the canonical source policy in `docs/sources.md`, regenerate bundled copies:

```bash
python3 scripts/sync_source_policy.py
```

Run the structural validator and regression suite with Ruby and Python 3; both use standard libraries:

```bash
ruby scripts/validate_skills.rb
python3 -m unittest discover -s tests -v
```

The validator checks YAML, names, descriptions, the local line cap, local resource closure, policy synchronization, router targets, optional Codex metadata, and JSON syntax. The [GitHub workflow](.github/workflows/validate-skills.yml) runs the checks on pushes and pull requests.

Behavioral evaluation has [27 prepared cases](evals/README.md): positive, negative, and edge scenarios for each skill. To prepare a fresh test workspace:

```bash
python3 scripts/prepare_eval.py quiz-me-positive --output /tmp/learn-skills-quiz-run
```

Choose a new output path for each run. Preparation copies inputs and records hashes; **it does not execute a model**. Follow the evaluation guide to run an isolated client session and record results. Structural checks alone do not establish cross-provider reliability or learning outcomes.

## Design and research

- [Project context](CONTEXT.md): motivation, vocabulary, and design history.
- [Architecture decisions](docs/adr/): scope and workflow choices.
- [Source policy](docs/sources.md): how evidence is selected and verified.
- [Portability audit](docs/research/skill-portability.md): packaging and application compatibility.
- [Per-skill evidence](docs/research/per-skill-quality.md): pedagogical research and its limits.
- [Ecosystem comparison](docs/research/ecosystem-crosscheck.md): lessons from other skill repositories.
- [Matt Pocock PR coverage](docs/research/matt-pr-coverage.md): reviewed changes, relevant findings, and coverage limits.
- [Performance evidence](docs/research/skill-performance-evidence.md): why model-level evaluation remains necessary.
- [Validation record](docs/skill-quality-validation.md): implemented corrections and verification scope.

Inspired by [Matt Pocock's skills](https://github.com/mattpocock/skills), [Addy Osmani's agent-skills](https://github.com/addyosmani/agent-skills), and [Superpowers](https://github.com/obra/superpowers). This is an independent project; inspiration does not imply endorsement.

Version 0.3.0. Structural validation and regression tests are available; measured learning outcomes and a completed cross-provider behavioral benchmark are not.
