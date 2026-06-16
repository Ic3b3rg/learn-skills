# learn-skills

A set of agent skills that package **evidence-backed pedagogical methodologies** as workflows applied to code: explain-and-check, quiz-me, connect-to-what-you-know, ask-me-questions, learn-by-doing, linked-notes, flashcards.

Motivation: closing the comprehension gap that opens between a human and a codebase when an LLM has done the work on the human's behalf. This is the **anti-surrender** layer that sits next to [Addy Osmani's agent-skills](https://github.com/addyosmani/agent-skills) — those cover *how to build*, this covers *how to learn what was built*.

Read [CONTEXT.md](CONTEXT.md) for the full design rationale, vocabulary, and decisions log. Read [docs/adr/](docs/adr/) for the load-bearing architectural decisions.

---

## Quickstart

```bash
/plugin marketplace add Ic3b3rg/learn-skills
/plugin install learn-skills@ic3b3rg-learn-skills
```

**The easiest way to begin**: run `/start-learn`. Tell it what you want to learn — it figures out the right approach and acts. You always make the final call.

```
/start-learn
```

If you already know what you need:

```
# Understand code an LLM just wrote
/explain-and-check path/to/that-file.ts

# Check what you've actually learned
/assess "event sourcing"
```

The other six skills (`quiz-me`, `connect-to-what-you-know`, `ask-me-questions`, `learn-by-doing`, `linked-notes`, `flashcards`) are listed below — or just run `/start-learn` and let the interview surface the right one.

---

## Why this exists

LLMs often write good code. The risk isn't bad code — it's that **the human's understanding shrinks while the codebase grows**. Four sources converging on this:

- **Addy Osmani — *Cognitive Surrender*** ([blog](https://addyosmani.com/blog/cognitive-surrender/)) — distinguishes *offloading* (keep the what) from *surrender* (the AI's output silently becomes yours). Identifies the gap; this repo packages the remedy.
- **Shaw & Nave (Wharton)** — with AI available, participants accepted wrong answers **73% of the time**; confidence rose even on wrong trials.
- **MIT — *Your Brain on ChatGPT*** ([arXiv:2506.08872](https://arxiv.org/abs/2506.08872)) — measured reduced neural connectivity and weaker memory in AI-assisted writers. Coined "cognitive debt."
- **Anthropic — *AI assistance & coding skills*** ([research](https://www.anthropic.com/research/AI-assistance-coding-skills)) — engineers using AI to **generate** code scored **17% lower** on comprehension than those using it for **conceptual inquiry**. *Same tool, opposite outcomes.* This is why every skill here forces inquiry over generation.

---

## When to use these skills

Not sure where to start? Run `/start-learn` — tell it what you want to learn and it takes it from there. You always make the final call.

Two canonical scenarios:

| Scenario | You just... | Reach for |
|----------|-------------|-----------|
| **A** — Understand code an LLM wrote | merged a PR / accepted a refactor / let an agent close a task | `/explain-and-check <file>`, `/connect-to-what-you-know <file>`, `/linked-notes <file>` |
| **B** — Learn a topic from scratch | want to learn a new language, framework, or skill from zero | `/start-learn` → creates a workspace with a curriculum, HTML lessons with quizzes, glossary, and curated resources |

---

## The skill set

### Find your starting point

| Command | What it does | When to use |
|---|---|---|
| `/start-learn` | Asks what you want to learn, then auto-detects the approach. **Scenario A** (existing code): proposes the right dialogic skill. **Scenario B** (from scratch): creates a workspace with `CURRICULUM.md`, HTML lessons, glossary, and `RESOURCES.md`. Never auto-dispatches. | Starting point for any learning session. |
| `/assess` | Produces a discrete level (Bloom or SOLO) + a concrete gap list + a suggested next skill. Never a 1-100 score. | After one or more sessions; you want to know what you actually retained. |

### Talk-it-through skills

| Command | What it does | When to use |
|---|---|---|
| `/explain-and-check` | You explain a topic or piece of code in your own words; the agent stress-tests your explanation against the real artefact (code, tests, docs). | After an LLM wrote code you accepted; you want to verify you really understand it. |
| `/quiz-me` | Forces you to retrieve knowledge from memory before consulting any source; the agent verifies what you produced against the real artefact. | After a learning session, or a few days later — you want to test what stuck. |
| `/connect-to-what-you-know` | You produce analogies between the new concept and things you already know; the agent stress-tests the analogies. | Learning something unfamiliar; you want to anchor it to prior knowledge. |
| `/ask-me-questions` | The agent only asks questions — never declares, never explains. You construct the insight yourself. | You want to reason something out rather than be told the answer. |

### Make-something skills

| Command | What it does | When to use |
|---|---|---|
| `/learn-by-doing` | Produces a file of exercises (solutions hidden) tailored to the topic or code you want to drill. | You want hands-on practice on a topic you're learning. |
| `/linked-notes` | Produces atomic markdown notes (one idea each, in your own words, cross-linked by topic) with citations to the source artefact. | You want a learning session to turn into durable, reusable knowledge. |
| `/flashcards` | Produces ASCII flashcards (question/answer separated by a fold marker) for retrieval practice. | You want reusable retrieval material to drill facts later. |

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
