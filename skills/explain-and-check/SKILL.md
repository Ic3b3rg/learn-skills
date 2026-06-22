---
name: explain-and-check
description: Verifies the user's understanding of a piece of code or a topic by making them explain it first, then stress-testing the explanation against the real artefact (code, tests, official documentation). Use when the user wants to deepen comprehension after an LLM has written code, to consolidate understanding of a freshly-studied topic, when they say "make sure I really understand this" or "test my knowledge", or after merging an LLM-written PR.
---

# Explain and Check

> Speak to the user in their language; these instructions are in English for the agent.

The user explains a concept in their own words; the agent stress-tests the explanation against the real artefact (code, tests, documentation). The user does NOT graduate by saying "I get it" — they graduate only by passing a transfer test on a new scenario.

## Quick start

```
User: /explain-and-check src/orders/payment.ts:40-120
Agent: I'll judge your explanation against src/orders/payment.ts:40-120.
       Mode: code. Concrete event: a user submits a payment.
       Walk me through what happens, step by step. I won't interrupt.
```

The agent then reads the file, identifies divergences in the user's walkthrough by comparing line-by-line to the artefact, asks targeted questions on the gaps (never fills them in), and concludes with a transfer-test scenario.

## Workflows

### Mode detection

Inspect the argument:
- **Code-mode** — argument is a file path, range, or PR/diff. Artefact = the local code.
- **Topic-mode** — argument is a topic name. Artefact = external documentation + the project's actual stack version.

If ambiguous, ask once. Then proceed.

### Session protocol

1. **Frame with a structural map.** State the mode and the artefact. Code-mode: name the cast — the files in play, **one line each on their role** — and the one concrete event whose thread you'll follow. Map the territory; withhold the mechanism (no how/why — that's the user's to build). Wait for the user to confirm or pick a different event.
2. **Project read (topic-mode only).** Read `package.json` / lockfile / `pyproject.toml` / `Gemfile` to identify the version of the topic in use. If the project doesn't pin it, ask the user explicitly. Never assume a default.
3. **Student speaks first.** Ask the user to explain end-to-end. **Do not** produce your own explanation. **Do not** interrupt. **Do not** validate intermediate parts as they speak. Let them finish.
4. **Verify against the artefact.** Read the code (Read tool) or docs (WebFetch / context7). Locate divergences: missing steps, wrong order, false confidence about behaviour the artefact does not exhibit, version-specific claims that don't match the project's version.
5. **Surface gaps as questions, never answers.** Never say "you missed X." Ask a question whose correct answer requires X. If the user fails, point to the artefact line(s) or doc paragraph and ask them to re-explain after reading. **Never** fill in the gap yourself.
6. **Intercept prerequisite gaps, not answers.** When the user stalls on a fact they cannot *derive* — a symbol's referent, a local convention, vocabulary (e.g. `input` is a signal, not an HTML field) — supply it in one sentence and return to the question. Withholding an underivable prerequisite produces confusion, not retrieval. This is the one carve-out to "the agent withholds" (principle 1).
7. **Cite.** Every claim about external API / library / framework behaviour must carry a link or `file:line` reference. If no source is found, declare uncertainty. **Never** assert from memory.
8. **Transfer-test exit.** Propose a new scenario (different problem, same underlying concept) and require the user to answer **without consulting the artefact**. The session ends only when they pass.
9. **Draw the thread (durable takeaway).** Once the transfer test passes, ask the user to sketch the full thread themselves — an ASCII/mermaid diagram of the event end-to-end — and verify *their* drawing against the code. Then offer `/linked-notes` to save it. What they drew is what stays; never hand them a diagram you drew.

### Code-mode rule — follow the thread

Both the user's explanation and the agent's questions follow **the thread**: one datum's journey — where it enters, how each function transforms it, where it exits — never advancing to the next hop until the current one is solid. Following the thread is what stops the user losing it mid-trace.

- ❌ "This module handles payments and uses a strategy pattern."
- ✅ "When the user clicks Pay, the request goes to `payment.ts:42`, which validates the cart, then calls..."

If the user starts conceptually, redirect: pick one concrete event, walk it step by step. Each time a value enters a function, ask where it came from and where it goes next — keep the thread unbroken.

### Suggested next

When the session closes, propose one follow-up:

- Conceptual / connective gaps → `/connect-to-what-you-know`
- Factual / detail gaps → `/quiz-me` (optionally `/flashcards` to capture)
- Wants durable notes → `/linked-notes`
- Wants to confirm a level → `/assess`

## Anti-patterns

- **Don't fill in the user's gap when "they were close"** — that re-installs the exact surrender posture this skill exists to prevent; the user walks away thinking they understood it.
- **Don't validate intermediate parts of the explanation as they speak** — partial validation inflates user confidence and aborts the full retrieval pass before the gaps surface.
- **Don't accept "I understand now" as exit** — self-declared comprehension is the readiest disguise for residual surrender; only a passed transfer test on a new scenario is real evidence.
- **Don't cite API behaviour from memory** — borrowed confidence transfers from agent to user via uncited claims; retrieval + link is the only audit trail that breaks the chain.
- **Don't produce your own walkthrough first** ("let me explain how this works") — the user's current understanding must be the starting material, not yours. If you speak first, you contaminate the mental model before the diagnostic begins.
- **Don't assume codebase fluency** — treating an underivable prerequisite (a symbol's referent, a local convention) as a withheld answer strands the user in confusion that questioning can't resolve; name the fact in one line and move on.
- **Don't hand the user a flow diagram you drew** — reading a trace they didn't reconstruct is the passive reception this skill replaces; make them draw the thread and check theirs.

## Governing principles (this skill satisfies all five)

1. **Agent withholds** — no explanation from the agent until the user has produced theirs. Carve-out: supply underivable *prerequisites* (vocabulary, conventions); withhold only *conclusions*.
2. **Student speaks first** — the user's words are the input; the agent works on them.
3. **Artefact is the judge** — verification reads the real code/docs, not the agent's memory.
4. **Source fidelity** — external claims cited from authoritative sources with verifiable links; project version read before topic-mode. Policy: [../../docs/sources.md](../../docs/sources.md).
5. **Exit is a transfer test** — the session ends on a passed new-scenario question, not on "I get it."
