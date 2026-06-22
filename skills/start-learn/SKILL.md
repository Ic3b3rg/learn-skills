---
name: start-learn
description: Entry point to learn-skills. Asks one question — what to learn — then auto-detects Scenario A (understand existing code or topic) or Scenario B (learn from scratch) and acts accordingly. Scenario A: selects and runs the right dialogic skill, declaring the choice. Scenario B: creates a teaching workspace with CURRICULUM.md, HTML lessons, glossary, and resources. Use when the user says "help me start", "I want to learn", "where do I begin", "start-learn", or when invoked without a specific methodology in mind.
---

# Start Learn

> Speak to the user in their language; these instructions are in English for the agent.

Single-question entry point. One ask — then act. No interview, no menu.

## Quick start

```
User: /start-learn
Agent: What do you want to learn?
       (Give me a file/PR to understand, or a topic you want to learn from scratch.)
```

The agent reads the answer, infers Scenario A or B, declares the assumption, and proceeds. If wrong, the user corrects in one word.

## Auto-detection

Read [FLOWS.md](FLOWS.md) for the full detection logic, skill-mapping table (Scenario A), and step-by-step workspace protocol (Scenario B).

Summary:
- **Scenario A** — user mentions existing code, file, PR, or wants to deepen a topic with a codebase already in mind → select the right dialogic skill, declare the choice + a one-line reason, and run it. The user can redirect at any time.
- **Scenario B** — user names a topic they want to learn from zero → create a teaching workspace, generate CURRICULUM.md, produce HTML lessons on demand.

Always declare the assumption:
> *"Starting from the hypothesis that you're learning X from scratch — correct me if wrong."*

## Workspace (Scenario B only)

See [WORKSPACE.md](WORKSPACE.md) for the full directory structure, file purposes, and workspace detection rule.

The workspace path is chosen by the user in plain text (no tool). Access in subsequent sessions: `cd` into the folder. Detection signal for all workspace-aware skills: presence of `CURRICULUM.md` in cwd.

## Baseline handoff

In both scenarios, state the inferred level explicitly at the end:
> *"I'll carry this baseline (estimated: X) to `/assess` when you run it later — progress will be measurable."*

## Anti-patterns

- **Don't ask more than one question upfront** — the whole point is zero boilerplate; if you need more context, ask *after* you've started, not before.
- **Don't decide silently** — always declare the assumed scenario before acting; one wrong assumption costs one correction, not a lost session.
- **Don't dispatch silently** — auto-selecting the methodology is the behaviour (ADR 0004), but always declare the choice + a one-line reason before running, because an undeclared switch hides the meta-decision the user has the right to override.
- **Don't make the user choose between named methodologies** — the audience doesn't know the skills by name; offering "explain-and-check or ask-me-questions?" asks for an expert choice they can't make. Pick one, run it, let the user redirect.
- **Don't auto-dispatch in Scenario B** — selection-and-run applies to Scenario A methodologies; Scenario B still ends with "say 'next lesson' when ready" so the user paces content delivery.
- **Don't generate all lessons upfront** — one lesson at a time, on demand, so each can adapt to progress recorded in `learning-records/`.
- **Don't invent resource URLs** — populate RESOURCES.md via web search; if unavailable, name sources without URLs and flag "verify the link."

## Governing principles (this skill satisfies all five)

1. **Agent withholds** — withholds *content* (lessons deliver only when requested; sessions make the student speak first). Selects the *methodology* on the user's behalf (ADR 0004) — meta-choice, not content.
2. **Student speaks first** — all choices (workspace path, curriculum approval, lesson request) originate from the user.
3. **Artefact is the judge** — Scenario A: reads real code/docs before proposing. Scenario B: every lesson cites a primary source.
4. **Source fidelity** — web search before content; no parametric knowledge asserted without citation. Policy: [../../docs/sources.md](../../docs/sources.md).
5. **Exit is a transfer test** — Scenario A: user's confirmation of the next skill is the exit. Scenario B: each lesson ends with a practice section the user completes.
