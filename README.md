# learn-skills

A set of agent skills that package **evidence-backed pedagogical methodologies** — Feynman, active recall, elaboration, Socratic dialogue, learn-by-doing, Zettelkasten, Anki flashcards — as workflows applied to code.

Motivation: closing the comprehension gap that opens between a human and a codebase when an LLM has done the work on the human's behalf. This is the **anti-surrender** layer that sits next to [Addy Osmani's agent-skills](https://github.com/addyosmani/agent-skills) — those cover *how to build*, this covers *how to learn what was built*.

Read [CONTEXT.md](CONTEXT.md) for the full design rationale, vocabulary, and decisions log. Read [docs/adr/](docs/adr/) for the load-bearing architectural decisions.

---

## Quickstart

```bash
# 1. Install in Claude Code
/plugin marketplace add Ic3b3rg/learn-skills
/plugin install learn-skills@ic3b3rg-learn-skills
```

Then, from any Claude Code session:

```
# An LLM just wrote code for you and you want to actually understand it?
/feynman path/to/that-file.ts

# Don't know where to start?
/start-learn

# Want to check what you've actually learned?
/assess "event sourcing"
```

Three commands cover most situations. The other six skills (`active-recall`, `elaboration`, `socratic`, `learn-by-doing`, `zettelkasten`, `anki-cards`) are discoverable from `/start-learn` or from [The skill set](#the-skill-set) below.

---

## Why this exists

LLMs often write good code. The risk isn't bad code — it's that **the human's understanding shrinks while the codebase grows**. Four sources converging on this:

- **Addy Osmani — *Cognitive Surrender*** ([blog](https://addyosmani.com/blog/cognitive-surrender/)) — distinguishes *offloading* (keep the what) from *surrender* (the AI's output silently becomes yours). Identifies the gap; this repo packages the remedy.
- **Shaw & Nave (Wharton)** — with AI available, participants accepted wrong answers **73% of the time**; confidence rose even on wrong trials.
- **MIT — *Your Brain on ChatGPT*** ([arXiv:2506.08872](https://arxiv.org/abs/2506.08872)) — measured reduced neural connectivity and weaker memory in AI-assisted writers. Coined "cognitive debt."
- **Anthropic — *AI assistance & coding skills*** ([research](https://www.anthropic.com/research/AI-assistance-coding-skills)) — engineers using AI to **generate** code scored **17% lower** on comprehension than those using it for **conceptual inquiry**. *Same tool, opposite outcomes.* This is why every skill here forces inquiry over generation.

---

## When to use these skills

Two canonical scenarios:

| Scenario | You just... | Reach for |
|----------|-------------|-----------|
| **A** — Understand code an LLM wrote | merged a PR / accepted a refactor / let an agent close a task | `/feynman <file>`, `/elaboration <file>`, `/zettelkasten <file>` |
| **B** — Learn a topic from scratch | started studying an unfamiliar library, pattern, or domain | `/elaboration <topic>`, `/active-recall <topic>`, `/learn-by-doing <topic>` |

Not sure where to start? Run `/start-learn` — it interviews you in a handful of questions and **proposes** the right skill. You always make the final call.

---

## The skill set

### Meta
- **`/start-learn`** — Interview-guided entry point. Asks what you want to learn and how, then proposes a skill. Never picks for you.
- **`/assess`** — Formative assessment. Produces a Bloom (or SOLO) level + concrete gap list + suggested next skill. **Never a 1-100 score.**

### Session methodologies (dialogic)
- **`/feynman`** — Explain it in your own words; the agent stress-tests against the code.
- **`/active-recall`** — Retrieve from memory before consulting the source.
- **`/elaboration`** — Connect the new concept to existing knowledge by force of question.
- **`/socratic`** — The agent only asks; never tells.

### Generative methodologies (artefact-producing)
- **`/learn-by-doing`** — Produces a file of exercises (solutions hidden).
- **`/zettelkasten`** — Produces atomic, linked notes for durable knowledge.
- **`/anki-cards`** — Produces ASCII flashcards for active-recall practice.

### Editorial concepts (not skills, but used by `/assess`)
- **Bloom's taxonomy** — remember → understand → apply → analyze → evaluate → create.
- **SOLO taxonomy** — prestructural → unistructural → multistructural → relational → extended abstract.

---

## Methodological roots

Nothing here is invented. Each skill repackages a protocol that pedagogy has already validated:

- `/feynman` ← **Feynman Technique** — Richard Feynman's habit of teaching to learn.
- `/active-recall` ← **Testing Effect** — Roediger & Karpicke (2006); retrieval beats re-reading.
- `/elaboration` ← **Elaborative Interrogation** — Pressley et al. (1987).
- `/socratic` ← **Socratic Method** — Plato's dialogues.
- `/learn-by-doing` ← **Learning by Doing** (Dewey, 1916) + **Deliberate Practice** (Ericsson).
- `/zettelkasten` ← **Zettelkasten** — Niklas Luhmann.
- `/anki-cards` ← **Spaced retrieval** — Ebbinghaus' forgetting curve; Leitner system.
- Bloom (concept) ← **Bloom's Taxonomy** — Benjamin Bloom (1956).
- SOLO (concept) ← **SOLO Taxonomy** — Biggs & Collis (1982).

The contribution of this repo is the **application**: each method is reshaped to obey the [five operating principles](#the-five-operating-principles) so it stays effective when an agent is in the loop.

---

## The five operating principles

Every skill in this repo obeys all five. A skill that breaks one is suspect.

1. **The agent withholds.** Your current understanding is the starting material, not the agent's prior knowledge.
2. **The student speaks first.** You explain; the agent stress-tests.
3. **The artefact is the judge.** Verification comes from the code, not from the agent's confidence.
4. **Source fidelity.** External knowledge is verified against real documentation and the project's actual versions. No memorised defaults.
5. **Exit is a transfer test.** A session ends when you demonstrate the understanding on a new problem, not when you say "I get it."

---

## Out of scope (on purpose)

- **Spaced repetition.** Temporal state management is a separate project; we don't build it here.
- **Interleaving as a skill or flag.** Surfaces as a tip — declare multiple topics up front and the agent will alternate naturally.
- **Automatic skill routers.** `/start-learn` *proposes*; the agent never auto-dispatches based on inferred context.
- **Monolithic 1-100 scores.** Discrete levels (Bloom/SOLO) + gap lists only.

See [docs/adr/0002-no-scheduling-no-monolithic-scores.md](docs/adr/0002-no-scheduling-no-monolithic-scores.md) for the full rationale.

---

## Install

### Claude Code (plugin marketplace)

```bash
/plugin marketplace add Ic3b3rg/learn-skills
/plugin install learn-skills@ic3b3rg-learn-skills
```

If you don't have SSH keys set up on GitHub and the marketplace command fails, use the explicit HTTPS form:

```bash
/plugin marketplace add https://github.com/Ic3b3rg/learn-skills.git
/plugin install learn-skills@ic3b3rg-learn-skills
```

### Local / development

```bash
git clone https://github.com/Ic3b3rg/learn-skills.git
claude --plugin-dir /path/to/learn-skills
```

### Other platforms

Skills are plain markdown files with YAML frontmatter, so any Claude / agent platform that supports the open Agent Skills format can use them. Drop the contents of `skills/` into your platform's skills directory. See [CLAUDE.md](CLAUDE.md) for the operating conventions and [docs/sources.md](docs/sources.md) for the verification policy each skill enforces.

---

## Status

Early stage (v0.1.0). The design is settled (see [CONTEXT.md](CONTEXT.md) and the ADRs in [docs/adr/](docs/adr/)); all 9 skills are written and validated. Real-world iteration begins next.
