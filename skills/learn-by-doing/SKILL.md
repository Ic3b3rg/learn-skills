---
name: learn-by-doing
description: Generates a file of practical exercises (with solutions hidden behind a clearly marked fold) that target the user's understanding of a topic or piece of code. The user solves the exercises themselves; the agent verifies their solutions against the real artefact. Use when the user wants to consolidate by practising, after a learning session that left only conceptual understanding, when "I get it in theory but I want to try", or anytime they say "give me exercises", "let me try", "learn by doing", "practise this".
---

# Learn By Doing

> Speak to the user in their language; these instructions are in English for the agent.

A generative skill: produces a markdown file under `learn/` containing 3–7 graded exercises plus a hidden solutions section. The user attempts the exercises; the agent verifies each answer against the real code/docs when the user submits them. The artefact (the exercises file) persists in the project and can be reopened later — see [ADR 0002](../../docs/adr/0002-no-scheduling-no-monolithic-scores.md) for why we don't schedule those reopenings.

## Quick start

```
User: /learn-by-doing src/orders/payment.ts
Agent: Project read first. Stack: TypeScript + Express 4.21, ESM modules.
       I'll generate 5 exercises of ascending difficulty, save them to
       learn/payment-exercises.md, and hide solutions behind a fold.
       Bring me each answer when you're ready — I'll verify against payment.ts.
```

After generation, the user works through the file, brings answers back into the conversation, and the agent verifies.

## Workflows

### Mode detection

Inspect the argument:
- **Code-mode** — argument is a file, function, or PR. Exercises target *this* code (refactor, extend, recreate from spec, find the bug).
- **Topic-mode** — argument is a topic. Exercises target *applying the concept* (implement, design, choose between alternatives) within the project's actual stack.

### Session checklist (copy into your reply and tick as you go)

```
Generation:
- [ ] Project read complete (stack + versions identified)
- [ ] Artefact read (code-mode) or docs fetched (topic-mode)
- [ ] 3–7 exercises drafted with ascending difficulty (E1 → E7 ladder)
- [ ] E4 (Debug) included when code-mode
- [ ] Every solution traces to file:line or cited doc
- [ ] Solutions folded under <details> tag (none above the fold)
- [ ] File written to learn/<slug>-exercises.md
- [ ] Filename + path confirmed with user before write if collision

Per-answer verification (each time the user brings an answer):
- [ ] User's answer read carefully (not skimmed)
- [ ] Verified against artefact with file:line or doc citation
- [ ] Marked pass / partial / fail with evidence
- [ ] On fail: one targeted question + line reference + retry (no spoiler)
- [ ] On pass: user decides whether to proceed to next exercise
```

### Generation protocol

Read [EXERCISES.md](EXERCISES.md) for the full generation reference (exercise ladder E1–E7 + file format). Summary of the steps:

1. **Project read** — identify stack + versions from manifest files; never use a generic version.
2. **Read artefact / fetch docs** — every solution must trace to a citation.
3. **Pick 3–7 exercises** from the ladder (E1 Reproduce → E7 Teach). Include E4 (Debug) in code-mode.
4. **Write the file** to `learn/<slug>-exercises.md` with solutions folded under `<details>`.

### Verification protocol (when the user brings an answer)

1. **Read the user's answer.** Do not skim — read it like a code review.
2. **Verify against the artefact** (Read tool for code, WebFetch / context7 for docs). Mark **pass / partial / fail** with the specific divergence.
3. **Cite.** Every claim about "the correct answer" carries a `file:line` or a doc link.
4. **If failed, do not reveal the solution.** Ask one targeted question and point at the relevant artefact line(s). Let the user retry.
5. **If passed, move to the next exercise** (the user decides when).

### File hygiene

- Exercises files live in `learn/` at the project root.
- One file per session (don't merge into an existing file — the user might want different sets for different goals).
- File names: `learn/<slug>-exercises.md`, slug derived from topic or source file.
- The `learn/` folder is the only persistent state any skill writes. Do not add metadata files, indexes, or schedules.

## Anti-patterns

- **Don't put solutions above the fold, even partially** — visible solutions defeat the entire skill, because the act that produces learning is the user *attempting* before consulting; one peek collapses recall into recognition.
- **Don't write solutions the agent invented from memory** — every solution must trace to the artefact, otherwise the user gets verified against the agent's confidence rather than the real source; that's borrowed confidence at the verification layer.
- **Don't write generic exercises** ("implement quicksort") — exercises must use *this* stack at *this* version on *this* problem, otherwise the transfer doesn't connect to the work the user actually does.
- **Don't reveal the answer when the user is stuck** — the productive struggle is the learning signal; offer a targeted question + line reference + retry, and let the user re-attempt with the source closed again.
- **Don't generate more than 7 exercises in one file** — past 7, fatigue dominates and exercise quality drops; the user answers shallower and learns less per exercise.
- **Don't skip E4 (debug) in code-mode** — debug exercises produce the highest transfer signal because they require a working mental model to even identify the broken assumption.

## Governing principles (this skill satisfies all five)

1. **Agent withholds** — solutions folded; verification asks before telling.
2. **Student speaks first** — the user produces every answer.
3. **Artefact is the judge** — every solution and every verification is grounded in real code/docs.
4. **Source fidelity** — stack version read before generation; every solution carries a citation to an authoritative source. Policy: [../../docs/sources.md](../../docs/sources.md).
5. **Exit is a transfer test** — the last exercises (E5–E7) are transfer-tests by construction.
