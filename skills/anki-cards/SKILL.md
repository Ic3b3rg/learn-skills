---
name: anki-cards
description: Produces ASCII flashcards (question on the front, answer on the back, separated by a fold marker) for active-recall practice on a topic or piece of code. Each card targets one atomic fact, anchored to a citation. The user generates the question phrasing; the agent verifies the answer against the real artefact. Use when the user wants reusable retrieval material after a learning session, when capturing facts from a /feynman or /active-recall session, or anytime they say "give me flashcards", "make Anki cards", "anki this", "I want to drill this".
---

# Anki Cards

> Speak to the user in their language; these instructions are in English for the agent.

A generative skill that produces a markdown file of ASCII flashcards under `learn/anki/`. Each card is one atomic fact, with a clearly-folded answer. Cards are a *vehicle* for active-recall practice — see [ADR 0001](../../docs/adr/0001-evidence-based-core-and-editorial-concepts.md) — not a methodology in themselves. This skill produces the artefact; `/active-recall` is the methodology that uses it.

## Quick start

```
User: /anki-cards src/auth/session.ts
Agent: Project read first. Stack: TypeScript + NextAuth 5.0.
       Cards will be saved to learn/anki/session-cards.md. I'll prompt you for
       the question phrasing on each card; I'll verify and write the answer.
       Tell me the first thing you want to be able to recall from memory.
```

The file is plain markdown. Compatible with eye-review and with simple Anki importers via copy-paste; we don't generate `.apkg` binaries.

## Workflows

### Mode detection

Inspect the argument:
- **Code-mode** — argument is a file or PR. Cards target *facts about this code* (invariants, signatures, behaviour edges).
- **Topic-mode** — argument is a concept. Cards target *facts about the topic* at the project's stack version.

### Card and file format

See [CARD-FORMAT.md](CARD-FORMAT.md) for the exact card block, file structure, and the three non-negotiable properties (atomic, question-from-user, cited). Default file size: **5–15 cards**.

### Generation protocol

1. **Project read.** Read `package.json` / lockfile / `pyproject.toml`. Cards must reflect the actual version in use.
2. **Read the artefact (code-mode) or fetch the docs (topic-mode).** No card is written if the answer cannot be sourced.
3. **Ask the user for the first question front.** Examples of good prompts:
   - *"What's one thing about this code you'd want to recall a week from now without looking?"*
   - *"What's the first specific fact about this topic you want to drill?"*
4. **Atomicity check.** If the front contains "and" or multiple clauses, ask the user to split.
5. **Source the answer.** Read code (Read tool) or docs (WebFetch / context7) to write a verified back. Cite. **Never** write an answer from memory.
6. **Loop.** Continue until the user says stop, or 15 cards, whichever first.
7. **Write the file** to `learn/anki/<slug>-cards.md` using the Write tool.
8. **Offer the follow-up.** After saving, suggest: *"Run `/active-recall learn/anki/<slug>-cards.md` when you want to practise these."*

### Using the cards later

This skill doesn't *practise* the cards — it only generates them. Practice happens via `/active-recall` on the file. The agent reading the cards file should treat each Front as a recall prompt and verify the user's answer against the Back + citation.

## Anti-patterns

- **Don't author question fronts for the user** — the user phrases what they want to recall, because *what they choose to be tested on* is itself diagnostic information about their model; agent-authored fronts collapse retrieval into recognition.
- **Don't write answers from memory** — every back is sourced before being written, otherwise the card becomes a durable carrier of borrowed confidence that the user will absorb on every review.
- **Don't write compound cards** (two facts in one) — compound cards make it impossible to distinguish "knew one fact and guessed the other" from "knew both"; atomicity is what makes recall signal interpretable.
- **Don't generate without citations because "it's basic"** — cite anyway; cards are durable, and basic-looking facts often turn out to be the version-specific ones that drift over time.
- **Don't put the answer above the fold** — the `<details>` fold is the entire point of the format; visible answers turn cards into reading material, which doesn't drive retrieval.
- **Don't write more than 15 cards in one session** — fatigue produces lower-quality phrasing, which produces lower-quality recall later; the user pays the cost on every future review.

## Governing principles (this skill satisfies all five)

1. **Agent withholds** — answers folded; the user produces the front phrasing.
2. **Student speaks first** — the user's recall need is the input.
3. **Artefact is the judge** — every back is verified against the real code/docs.
4. **Source fidelity** — every back ends with a citation to an authoritative source; stack version anchored before generation. Policy: [../../docs/sources.md](../../docs/sources.md).
5. **Exit is a transfer test** — the cards themselves *are* transfer-test fuel for `/active-recall` later.
