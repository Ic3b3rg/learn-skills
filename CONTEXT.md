# Context — learn-skills

This repo will host a set of agent skills that package **known pedagogical methodologies** (Feynman, active recall, Socratic dialogue, Anki, Bloom's taxonomy, learn-by-doing, ...) as agent workflows applied to code.

The motivation is anti-surrender: closing the comprehension gap that opens between a human and a codebase when an LLM has done work on the human's behalf. But the *mechanism* is not a generic "intervention pattern" — it's a deliberate borrowing of methods that pedagogy and cognitive science have already validated. The skill set is, in effect, **a learning toolbox for the post-LLM era**.

Canonical use case: after an LLM has completed a task (a PR, a refactor, a feature), or after a code review, the human invokes one of these skills on a specific topic / file / module to **rebuild understanding** that was bypassed during generation.

It is *not* a generalist SDLC skill set (that's [Addy Osmani's agent-skills](agent-skills-main/)). The two layers compose: Addy's skills cover *how to build*, this repo covers *how to learn what was built*.

The reference text for the anti-surrender framing is Addy Osmani's _Cognitive Surrender_ (May 2026), which builds on Shaw & Nave's Wharton paper _Thinking — Fast, Slow, and Artificial_, the MIT _Your Brain on ChatGPT_ paper, the Anthropic skill-formation paper, and the arXiv _Cognitive Agency Surrender_ paper. The methodologies themselves are pre-LLM (Feynman, Bloom, Anki, etc.) — the contribution is *applying them to code through an LLM agent*.

---

## Glossary

### Cognitive offloading
Delegating execution to the AI **while keeping ownership of the answer**. The human still constructs an independent expectation, judges the AI's output against it, and intervenes when it doesn't match. Healthy posture. The calculator, the search engine, the GPS.

### Cognitive surrender
The state in which **the AI's output silently becomes the human's output**, with no independent view ever formed to compare it against. There is "nothing to override, because you never formed an independent view." Pathological posture. From Shaw & Nave (Wharton, 2026).

> **Diagnostic:** the line between offloading and surrender feels identical from the inside. The only reliable signal is whether the human can reconstruct the *why* of a decision after the agent has left the room.

### Borrowed confidence
The effect where an AI's high baseline confidence **transfers to the human** without the underlying reasoning. In Shaw & Nave, participants' self-rated confidence rose when AI was available, even on trials where the AI was wrong 50% of the time. In software: "we use a debounce of 300ms here" reads as institutional knowledge even when the model invented the number.

### Cognitive debt
Short-term cognitive gain paid back with compounding long-term cost — borrowed from "technical debt." Each act of surrender is a tiny loan; the interest is paid when something breaks and the mental model needed to fix it isn't there. Coined in the MIT _Your Brain on ChatGPT_ paper.

### Comprehension debt
The widening gap between **how much code exists in a system** and **how much of it any human genuinely understands**. The structural consequence of accumulated cognitive surrender. Distinct from cognitive debt: cognitive debt is the *mechanism* (per-decision), comprehension debt is the *bill* (system-wide).

### Mutual amplification
Andy Clark's term for the *cooperation* mode with AI, opposed to delegation. A loop where the human's prompts sharpen the model's output, which sharpens the human's next prompts, which sharpens the human's model of the problem. End-of-session test: did the human end with a sharper or fuzzier mental model than they started with?

### Scaffolded cognitive friction
Deliberately introduced moments of resistance that **interrupt heuristic acceptance** of AI output. From the arXiv _Cognitive Agency Surrender_ paper. Examples: a required design doc before generation, a confirmation step before merge, a checklist before deploy. Friction is the price of staying on the offloading side.

### Anti-rationalization table
A design pattern (from Addy's Agent Skills) that **pairs each common excuse for skipping a workflow step with a pre-written rebuttal**. "This task is too simple to need a spec." → "Acceptance criteria still apply." Pre-writes the rebuttal to the rationalization the human (or the agent) will produce when tired.

### Surrender artifact
Evidence that a past decision was a surrender, surfaced now. Canonical example: "you find yourself defending a design choice in a meeting and you can't reconstruct why it was made, only that the agent suggested it and it seemed reasonable."

### Posture
The human's *stance* toward the AI in a given interaction — offloading vs surrender. The article's central claim: the tool is the same in both cases; only the posture differs. Skills in this repo intervene on **posture**, not on tool capability.

### Conceptual inquiry mode vs generation mode
Two distinct ways of using the agent on the same task. *Generation mode*: "write the code." *Conceptual inquiry mode*: "explain the tradeoffs / interrogate the design / teach me the library." Anthropic's skill-formation paper: generation-mode users scored 17% lower on follow-up comprehension; inquiry-mode users held their ground. Same tool, opposite cognitive outcomes.

---

## Canonical use cases

Two scenarios that drive the design. Every skill must be useful in at least one of these; ideally in both, with explicit per-scenario behaviour.

### Scenario A — Understand code an LLM just wrote

The user has shipped a PR / accepted a refactor / let an agent close a task. The artefact exists; the mental model does not. The user invokes a skill on a file, a diff, or a region of code to **rebuild what the LLM bypassed**.

Defining traits:
- Input is concrete and bounded (a file, a PR, a function, a module).
- The artefact already exists and is the source of truth.
- Risk = the user "felt like it made sense" while reading — classic cognitive surrender.
- Typical skills: feynman (in code mode), elaboration (cross-language analogy), zettelkasten (durable notes), anki-cards (key invariants).

### Scenario B — Learn a topic from scratch

The user wants to take on an unfamiliar topic / library / pattern. No code yet, or only exploratory code. They study, gather resources, then test themselves.

Defining traits:
- Input is a topic, not an artefact (often only a name and a goal).
- The "source of truth" is external (docs, books, the user's own study notes), not internal code.
- Risk = the user lets the LLM read for them, ends up with a fluent summary and no transferable understanding.
- Typical skills: elaboration (anchor to prior knowledge), active-recall (after study), learn-by-doing (apply on a contrived problem), feynman (in topic mode), zettelkasten / anki-cards (capture).

### Code-mode rule (applies to Scenario A)

When any skill operates on existing code, the user's explanation must be **trace-oriented**, not concept-oriented. The agent's first prompt is shaped as a concrete execution path, e.g.:

> *"When the user clicks the [Pay] button, walk me through what happens. Don't describe the components — describe the journey of the request."*

Concept-first explanations ("this class handles payments") are *exactly* the form LLMs default to and the form that leaves the user feeling-but-not-knowing. Trace-first explanations expose every step where the user has to say "uh, I'm not sure what happens here" — those are the surrender hotspots.

## Operating philosophy

Four principles, derived from designing the Feynman skill, that apply across the entire skill set. Any new skill that violates one of these is suspect and must be re-examined.

### 1. The agent withholds

The agent does not volunteer its own explanation, answer, or framing first. On every interaction, the human's current understanding must be the **starting material**. If the agent speaks first on the substance, it inoculates the human with borrowed framing before the human knows whether they had any framing at all. This is the borrowed-confidence effect from Shaw & Nave, reapplied to learning.

Practical consequence: the first non-meta turn in every skill belongs to the human, not the agent.

### 2. The student speaks first

The human's spoken/written explanation is the input. Skills are not "ask the agent to explain X to me" — they are "I explain X, the agent stress-tests me." This inverts the default LLM interaction.

Practical consequence: skills begin with a prompt to the human ("explain it in your words"), not with the agent producing content.

### 3. The artefact is the judge

When the student's explanation needs to be checked against a source of truth, the source is **the code itself** (and its tests, types, git history, comments) — not the agent's prior knowledge of how things "usually" work. The agent's role is to read the real artefact and surface where the student's mental model diverges from it. This is what makes the methodology surrender-resistant: the verdict comes from the system, not from the agent's confidence.

Practical consequence: skills explicitly Read files/diffs/tests as the verification step, instead of relying on the model's internal knowledge.

### 4. Source fidelity

When a skill operates on knowledge that lives outside the user's head, the agent must consult and cite the **real source**, not its own memory. This is the principle "the artefact is the judge" applied beyond local code, to the wider world.

Three operative rules:

1. **Project read before topic-mode.** Before any topic-mode session, the agent reads the project's manifest files (`package.json`, lockfile, `pyproject.toml`, `Gemfile`, etc.) to identify the versions and stack in use. If the project context is ambiguous or the topic doesn't map to anything in the project, the agent **asks**. Never assumes a default. A React 16 explanation in a React 19 codebase is a canonical surrender failure.

2. **Citation discipline — official / authoritative sources only.** Every claim about external API / library / framework behaviour must be paired with a verifiable link to a Tier 1 or Tier 2 source as defined in [docs/sources.md](docs/sources.md): canonical docs at the pinned version, source code, RFCs / W3C / language specs, peer-reviewed papers. Tutorials, blog posts, and Stack Overflow are **not** valid judges. If no authoritative source can be found, the agent **declares uncertainty** instead of asserting from memory. The user must be able to open the link, read the source, and verify the verdict independently.

3. **Polymorphic resources.** Skills must accept arbitrary input resource types: URL, local file path, video reference, book identifier, doc link. Internally these all normalise to "source." The skill cites and references them by location and (where retrievable) date / version.

This rule binds **all skills that operate in topic-mode**, and **all sessions that cite external knowledge** regardless of mode. Detailed policy (what counts as authoritative, how to cite, what to do when no source can be found) lives in [docs/sources.md](docs/sources.md).

### 5. Exit is a transfer test

A session does not end when the student says "I get it." A session ends when the student demonstrates the understanding on a *new* problem — a variant scenario, a different audience, a related edge case — produced by the agent and answered by the student **without consulting the code**. Self-declared comprehension is the readiest disguise for residual surrender; transfer is the cheapest objective signal of real comprehension.

Practical consequence: every skill specifies a transfer-test design, not a "satisfied?" prompt, as its termination condition.

---

## Skill taxonomy

The set is organised by **family**, because the family dictates the shape of the SKILL.md. A skill must belong to exactly one family.

### Onboarding / meta
Skills that orchestrate the user's relationship with the set, without working directly on a topic. Two skills, one at the entry, one at the exit.

- `start-learn` — interview-guided starter. Asks the user a small number of questions (intent, scenario A vs B, current self-rated knowledge, preferred output) and then **proposes** the most suitable skill + arguments. Golden rule: the user always has the final word on the skill chosen; the agent only proposes. Side-effect: the baseline self-assessment captured here becomes the reference point for `assess`.

- `assess` — formative assessment skill, invoked after one or more learning sessions. Verifies the user's current level **on a discrete scale** (Bloom or SOLO), produces a **concrete gap list**, and suggests the next skill + arguments to close the gap. Output is *never* a 1-100 score: a monolithic number produces false precision, false closure, and borrowed confidence applied to the verdict itself. Instead: discrete Bloom level + gap inventory + suggested-next. Detailed mode (multi-axis rubric: Recall / Trace / Transfer / Teach-back, each 1-3) available as a flag, not default.

### Session methodologies (dialogic)
Conversational protocols. Output = comprehension internalised by the human. No persistent artefact required. The agent and the human exchange turns under the operating philosophy above.

- `feynman` — explain in your own words, the agent stress-tests against the code
- `active-recall` — retrieve from memory before consulting the source
- `elaboration` — connect the new concept to existing knowledge by force of question
- `socratic` — the agent asks only, never tells (secondary; overlaps elaboration)

### Generative methodologies (artefact-producing)
Produce a reusable file. The artefact is the durable output and lives in the repo after the session ends.

- `learn-by-doing` — produces a file of exercises (with hidden solutions)
- `zettelkasten` — produces atomic, linked notes for durable knowledge
- `anki-cards` — produces flashcards in ASCII format (a *vehicle* for active-recall, not a methodology in its own right; offered as a skill because the artefact-production step is non-trivial)

### Editorial concepts (NOT skills, but reused as assessment scales)
Frameworks the project uses to *explain itself* in README/CONTEXT and to help users *choose* a skill — and **also reused as the measurement scale by `assess`**. Not invocable as skills.

- **Bloom's taxonomy** — remember → understand → apply → analyze → evaluate → create. The README maps each skill to the Bloom levels it best serves. `assess` outputs a Bloom level, not a 1-100 score.
- **SOLO taxonomy** — prestructural → unistructural → multistructural → relational → extended abstract. Alternative lens; `assess` can output either Bloom or SOLO depending on the user's preference at `start-learn` time.

## Distinction: methodology vs vehicle vs concept

A persistent source of confusion in this domain. The repo's vocabulary fixes the three terms:

- **Methodology** — *what* you do to learn (e.g. active recall, elaboration). Becomes a skill if it's an evidence-backed protocol the agent can run.
- **Vehicle** — *the form the methodology's output takes* (e.g. flashcards are a vehicle for active recall; a Zettel note is a vehicle for elaboration). May or may not warrant its own skill, depending on how much work the vehicle production is.
- **Editorial concept** — a *map for thinking about learning* (Bloom, SOLO). Never a skill. Lives in README and helps users pick.

When in doubt, ask: "is this *what I do*, *what comes out*, or *how I think about it*?"

## Decisions log

- **2026-05-19** — Scope shifted from "anti-surrender intervention patterns" to "pedagogical methodologies as skills." Generic interventions rejected as too vague.
- **2026-05-19** — Operating philosophy fixed (four principles above) using Feynman as the tracer-bullet methodology. Any future skill must satisfy all four.
- **2026-05-19** — Skill core built around **evidence-backed methodologies**: active recall, elaboration, Feynman. Socratic, learn-by-doing, Anki-cards, Zettelkasten kept as secondary skills. Bloom and SOLO demoted to editorial concepts (not skills).
- **2026-05-19** — Initially adopted three-family taxonomy (session / generative / scheduling). Dropped to **two families** (session / generative) after deciding to exclude scheduling methodologies entirely. Spaced repetition rejected: temporal state management is out of scope for this side project and likely to swallow it. Interleaving rejected as a skill or modifier: surfaces as a tip in the README only.
- **2026-05-19** — Identified two canonical use cases (Scenario A: understand LLM-written code; Scenario B: learn a topic from scratch). Each skill must serve at least one. The trace-oriented "code-mode rule" added as a binding constraint for Scenario A.
- **2026-05-19** — Architecture: **one slash command per skill, no orchestrating router**. Composition lives in README recipes, not in code. Rationale: a meta-router that picks a methodology *for* the user violates principle 1 (the agent withholds). The cognitive cost of explicitly choosing the methodology is a feature, not friction.
- **2026-05-19** — Language: **everything in English** (SKILL.md, README, in-skill prompts). The agent translates the user-facing dialogue to the user's language at runtime. Rationale: domain vocabulary is English-native; English maximises distribution; agent bilingualism is free.
- **2026-05-19** — Added `start-learn` as an **interview-guided onboarding skill** (NOT an automatic router). Golden rule: the final choice of skill is always declared by the user, never by the agent. Reopens nothing of the "no router" decision because the difference is binary: a router *decides*, `start-learn` *proposes*. Side-benefit: the self-assessment collected in `start-learn` becomes the baseline against which `assess` measures progress.
- **2026-05-19** — Added **source-fidelity** as principle 4 of the operating philosophy (renumbered: source fidelity = 4, exit is transfer test = 5). Three operative rules: project read before topic-mode, citation discipline, polymorphic resources. Reason: the principle "artefact is the judge" needed an explicit extension beyond local code to external knowledge sources. Without it, topic-mode sessions are surrender-vulnerable on the field being studied.
- **2026-05-19** — Added `assess` as the second meta skill. **Rejected the user's original request for a 1-100 score** with three reasons: false precision, false closure, borrowed confidence applied to the verdict. Adopted instead a discrete Bloom/SOLO level + concrete gap list + suggested-next-skill. Multi-axis rubric (Recall/Trace/Transfer/Teach-back) available as `--detailed` mode, not default. Bloom/SOLO get reused: editorial concept *and* assessment scale.

## Non-goals

- Replacing or competing with [Addy Osmani's agent-skills](agent-skills-main/). Those are the SDLC layer. This repo sits **next to** them and operates on the human's understanding of the artefacts produced.
- General "AI safety" or model-side interventions (extended thinking, constitutional AI). Those live inside the model and are Anthropic's territory.
- Generic "anti-surrender intervention patterns" (withholding, friction gates, adversarial pairing, surrender surfacing). Those were considered and rejected as too generic. The skills in this repo are **specific pedagogical methodologies**, not generic posture interventions.
- Productivity maximisation. Learning often *adds* time. The pitch is sustained capability, not throughput.
