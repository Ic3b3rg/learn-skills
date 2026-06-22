# Agent selects the methodology (reverses the no-router decision)

**Date:** 2026-06-19
**Status:** Accepted (supersedes the "no automatic router" decision recorded in the CONTEXT.md decisions log on 2026-05-19, and referenced by [ADR 0001](0001-evidence-based-core-and-editorial-concepts.md) and [ADR 0003](0003-stateful-teaching-workspace-for-scenario-b.md))

## Context

The original architecture (2026-05-19) banned an orchestrating router: `start-learn` *proposed* a methodology and the user *decided* by typing the slash command. The stated rationale was that "the cognitive cost of explicitly choosing the methodology is a feature, not friction" — picking the method was treated as part of principle 1 (the agent withholds).

Field use exposed the flaw. The target audience — developers rebuilding understanding of LLM-written code — **does not know the methodologies by name**. This is already acknowledged in the 2026-05-21 renaming decision, which stripped the pedagogical names (feynman, zettelkasten, …) precisely because they were opaque to this audience. Asking that same audience to choose between `explain-and-check` and `ask-me-questions` is asking for an expert decision they have no basis to make. The "friction is a feature" claim only holds when the chooser is competent to choose; here the friction is a barrier, not scaffolding.

A real session made this concrete: `start-learn` presented a fork of two named skills, the user couldn't tell them apart, and the choice became dead weight at the very start of the session.

## Decision

**The agent selects the methodology and runs it**, instead of proposing and waiting for the user to type the command.

`start-learn` (and any entry into the suite) now: detects the goal from the user's request, **declares the chosen methodology and the one-line reason, and dispatches it**. The user can redirect at any point ("no, just ask me questions") — selection is not a lock.

### What is reversed, and what is not

The reversal is **narrow and surgical**. It applies only to the *meta-choice of methodology*. It does **not** touch content-withholding.

- **Reversed:** the 2026-05-19 rule that the user must choose the methodology. The agent now chooses.
- **Untouched — principle 1 at the substance level:** inside every session, the agent still volunteers no explanation, answer, or framing before the user has produced theirs. `explain-and-check` still makes the student speak first; `quiz-me` still demands retrieval before the source. Auto-selecting *which method runs* is not the same as auto-supplying *the understanding the method exists to build*.

The 2026-05-19 framing conflated these two. This ADR separates them: principle 1 governs **content**, not **method selection**.

### Invocation mechanics

All skills remain **model-invoked** (descriptions retained) so the agent can dispatch them. This keeps every skill independently discoverable by natural language and pays the context-load cost of the descriptions — accepted as the price of auto-selection. `disable-model-invocation` is **not** used.

## Consequences

- `start-learn`'s "Don't auto-dispatch another skill" anti-pattern is removed; auto-dispatch is now the intended behaviour.
- The user keeps the override: the agent announces its choice before running, and switches methodology on request. Declaration + redirectability replace the confirm gate.
- README (`/start-learn` row, "what NOT to do" list), `CLAUDE.md` (Boundaries), and `FLOWS.md` (Scenario A protocol) are updated to describe selection-and-dispatch.
- ADR 0003's workspace orchestration is unaffected — Scenario B already had `start-learn` driving the workspace; Scenario A now matches that level of agency for methodology choice.
- Context-load cost of keeping all descriptions model-invoked is accepted; the alternative (a user-invoked router cutting context load) was rejected because it reintroduces the manual-choice barrier this ADR removes.
