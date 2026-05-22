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

1. **Frame.** State the mode, the artefact, and (code-mode) the one concrete event whose trace you'll follow. Wait for the user to confirm or pick a different event.
2. **Project read (topic-mode only).** Read `package.json` / lockfile / `pyproject.toml` / `Gemfile` to identify the version of the topic in use. If the project doesn't pin it, ask the user explicitly. Never assume a default.
3. **Student speaks first.** Ask the user to explain end-to-end. **Do not** produce your own explanation. **Do not** interrupt. **Do not** validate intermediate parts as they speak. Let them finish.
4. **Verify against the artefact.** Read the code (Read tool) or docs (WebFetch / context7). Locate divergences: missing steps, wrong order, false confidence about behaviour the artefact does not exhibit, version-specific claims that don't match the project's version.
5. **Surface gaps as questions, never answers.** Never say "you missed X." Ask a question whose correct answer requires X. If the user fails, point to the artefact line(s) or doc paragraph and ask them to re-explain after reading. **Never** fill in the gap yourself.
6. **Cite.** Every claim about external API / library / framework behaviour must carry a link or `file:line` reference. If no source is found, declare uncertainty. **Never** assert from memory.
7. **Transfer-test exit.** Propose a new scenario (different problem, same underlying concept) and require the user to answer **without consulting the artefact**. The session ends only when they pass.

### Code-mode rule (trace-oriented)

Code-mode explanations must follow a concrete execution path, not abstract concepts.

- ❌ "This module handles payments and uses a strategy pattern."
- ✅ "When the user clicks Pay, the request goes to `payment.ts:42`, which validates the cart, then calls..."

If the user starts conceptually, redirect immediately: ask them to pick one concrete event and walk what happens, step by step, from there.

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

## Governing principles (this skill satisfies all five)

1. **Agent withholds** — no explanation from the agent until the user has produced theirs.
2. **Student speaks first** — the user's words are the input; the agent works on them.
3. **Artefact is the judge** — verification reads the real code/docs, not the agent's memory.
4. **Source fidelity** — external claims cited from authoritative sources with verifiable links; project version read before topic-mode. Policy: [../../docs/sources.md](../../docs/sources.md).
5. **Exit is a transfer test** — the session ends on a passed new-scenario question, not on "I get it."
