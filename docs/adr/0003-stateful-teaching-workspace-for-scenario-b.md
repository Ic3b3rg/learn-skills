# Stateful teaching workspace for Scenario B (learn-from-scratch flow)

**Date:** 2026-06-16
**Status:** Accepted

## Context

learn-skills was designed around Scenario A: the user has code written by an LLM and needs to rebuild understanding. All skills were stateless dialogic sessions — invoke, run, done.

Scenario B (learn a topic from scratch) existed as a use case in CONTEXT.md but had no dedicated infrastructure. Users invoked the same stateless skills (quiz-me, connect-to-what-you-know, etc.) in topic-mode, but there was no persistent workspace, no curriculum, no accumulated resources. Each session started from scratch.

An existing teaching-workspace pattern demonstrated a compelling approach for Scenario B: a persistent directory (MISSION.md, lessons, learning-records, RESOURCES.md, reference/*.html) that accumulates across sessions over weeks of study. This pattern directly addresses Scenario B's needs — learning a language, a framework, or a skill over time.

The question was whether to integrate this pattern without violating the existing architecture.

## Decision

Add a **stateful teaching workspace** activated by `start-learn` when it detects Scenario B intent.

### Auto-detection over menu

`start-learn` asks one question: "what do you want to learn?". The LLM infers Scenario A vs B from the answer and declares its assumption explicitly ("starting from the hypothesis that you're at zero — correct me if wrong"). No interview, no menu.

Rationale: fewer questions = less boilerplate, the LLM handles ambiguity gracefully by surfacing its assumption, and the user corrects in one word if wrong.

### Workspace path chosen conversationally

The workspace path is asked in plain text — no tool, no fixed location. The user specifies it (e.g. `~/learning/chess/`), the agent creates the workspace there. Access in subsequent sessions is via `cd` into the directory.

Alternatives rejected:
- **Fixed path (`~/.claude/learn/`)**: breaks when the user has multiple LLM tools — each would create its own fixed path, polluting `~/.claude/`, `~/.gemini/`, etc.
- **Inside the code repo**: pollutes the repo's git status with MISSION.md, lesson files, etc.
- **Argument per invocation**: verbose, friction every time.

`cd`-based access requires zero infrastructure and works across all LLMs and environments.

### Upfront curriculum, on-demand content

`start-learn` generates `CURRICULUM.md` as the first workspace artefact — a roadmap of planned lessons with `[ ]`/`[x]` markers. The user can edit, reorder, expand, or prune it freely. Lesson HTML files are generated one at a time as the user advances, not all upfront.

Rationale: the map gives orientation and lets the user shape the learning path; on-demand generation allows each lesson to adapt to progress captured in `learning-records/`.

### HTML lessons with adaptive practice formats

Each lesson is a self-contained HTML file: explanation → adaptive practice → primary source + link to next lesson. Practice format adapts to topic:

- SVG diagrams for spatial topics (chess boards, flowcharts)
- Code editor (`<textarea>`) for programming
- Traditional A-B-C-D for languages and theory
- Sequence display for procedural skills (Rubik's, algorithms)

Multiple-choice answers are always equal in length — no formatting clues. Structure is fixed; format is adaptive.

### Five skills become workspace-aware

`start-learn`, `assess`, `linked-notes`, `flashcards`, `learn-by-doing` read and write workspace files (CURRICULUM.md, learning-records/, reference/, RESOURCES.md). Dialogic skills (`explain-and-check`, `quiz-me`, `connect-to-what-you-know`, `ask-me-questions`) remain stateless — they work without a workspace and are embedded as techniques inside HTML lessons.

### Glossario automatic in Scenario B

`reference/glossario.html` is auto-built by the agent as terms are introduced in lessons. In Scenario A, the user builds their own glossary if desired — the student-speaks-first principle requires the student to produce the definition, not the agent.

### Resources via web search with fallback

`RESOURCES.md` is populated using web search: Knowledge (official docs, books) and Wisdom (community forums, local classes). If web search is unavailable, the agent names known high-trust sources without inventing URLs and flags "verify the link yourself." Never asserts sources from parametric memory alone.

## Consequences

- `start-learn/INTERVIEW.md` is removed — the 5-question interview is superseded by single-question auto-detection.
- `start-learn/` gains three reference files: `FLOWS.md` (both flows), `WORKSPACE.md` (workspace structure), `LESSON-FORMAT.md` (HTML template + adaptive formats).
- The "no automatic router" principle from ADR 0001 is preserved: `start-learn` orchestrates the workspace, not the skills. It never auto-dispatches another skill — the user still decides when to open a lesson.
- ADR 0002's rejection of scheduling state is preserved: the workspace stores progress (what was learned), not scheduling (when to resurface it). No spaced-repetition engine.
