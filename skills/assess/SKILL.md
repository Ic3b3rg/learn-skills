---
name: assess
description: Performs a formative assessment of the user's current understanding of a topic or piece of code. Output is ALWAYS a discrete Bloom or SOLO level + a concrete gap list + a suggested next skill — NEVER a 1-100 score (false precision, false closure, borrowed confidence). Use when the user wants to check their current level, after one or more learning sessions, at the end of a study sprint, or anytime they say "test me", "where am I at", "how well do I know X", "assess this".
---

# Assess

> Speak to the user in their language; these instructions are in English for the agent.

A short, structured assessment that returns a **discrete level** on a named taxonomy (Bloom or SOLO), a **concrete gap list**, and a **suggested next skill** to close the most material gap. A monolithic 0–100 number is **not** an output of this skill, by design — see [ADR 0002](../../docs/adr/0002-no-scheduling-no-monolithic-scores.md).

## Quick start

```
User: /assess "event sourcing"
Agent: I'll assess your level on event sourcing on the Bloom scale (or SOLO if you
       prefer). I'll ask 4–6 questions of increasing cognitive demand. Answer
       without consulting code or docs — close them now.
       Baseline from /start-learn (if available): self-rated 2/5.
       Q1 (remember): Name the four most basic invariants of an event-sourced
       aggregate.
```

After the questions, the agent verifies answers against the artefact (code + docs), maps performance to a Bloom/SOLO level, lists concrete gaps, and recommends one next skill.

## Workflows

### Mode detection

Inspect the argument:
- **Code-mode** — argument is a file, directory, or PR. Artefact = local code.
- **Topic-mode** — argument is a topic name. Artefact = external docs + project's actual stack version.

### Default scale

Default to **Bloom** unless `/start-learn` recorded a SOLO preference, or the user states a preference now. Both scales are first-class; the user picks.

### Session checklist (copy into your reply and tick as you go)

```
Assessment progress:
- [ ] Mode detected (code / topic) and stated
- [ ] Scale chosen (Bloom default unless SOLO requested)
- [ ] Baseline recalled from /start-learn (or asked now)
- [ ] Source-closed rule confirmed with user
- [ ] Project read (topic-mode only)
- [ ] Q1 (Remember) asked + answered + verified against artefact
- [ ] Q2 (Understand) asked + answered + verified
- [ ] Q3 (Apply) asked + answered + verified
- [ ] Q4 (Analyze) — stop if two consecutive fails
- [ ] Q5 (Evaluate) — only if Q4 passed
- [ ] Q6 (Create) — only if Q5 passed
- [ ] Level mapped (highest level fully passed)
- [ ] Gaps listed concretely with file:line or doc refs
- [ ] Suggested next skill identified by *dominant gap*, not by level
- [ ] Verdict block printed in the exact required format
- [ ] No numeric score produced (anti-pattern check)
```

### Session protocol

Read [LEVELS.md](LEVELS.md) for the full Bloom/SOLO mappings and the exact verdict block format. Summary of the 7 steps:

1. **Frame** — restate object, scale, sources-closed rule. Wait for confirmation.
2. **Recall baseline** from `/start-learn` (or ask for it now: 1–5 self-rating).
3. **Project read** (topic-mode only) — anchor on the version in `package.json` / lockfile / etc.
4. **Ask 4–6 questions of ascending cognitive demand** — one per Bloom/SOLO level; stop after two consecutive fails.
5. **Verify each answer against the artefact** — code via Read, docs via WebFetch / context7. Pass / partial / fail with cited evidence.
6. **Map performance to a level** — highest level fully passed; a partial at L means the user is at L−1 with a gap *toward* L.
7. **Produce the verdict block** in the exact format defined in [LEVELS.md](LEVELS.md). Never a numeric score; never a rounded level.

`--detailed` adds a 4-axis rubric (Recall / Trace / Transfer / Teach-back, 1–3 each) as colour, not replacement.

### Choosing the suggested next skill

Pick by **dominant gap**, not by lowest level: structural → `/feynman` or `/elaboration`; factual → `/active-recall` (capture with `/anki-cards`); can't apply → `/learn-by-doing`; can't connect → `/elaboration`; solid, wants record → `/zettelkasten`.

### Source fidelity

Every verification reads the real artefact; every external claim carries `file:line` or a doc link. If an answer cannot be sourced, **drop the question** rather than score from memory.

## Anti-patterns

- **Don't produce a 1-100 score** — a single number creates false precision, false closure ("78, good enough"), and applies borrowed confidence to the verdict itself; this is the failure mode the skill exists to refuse. See [ADR 0002](../../docs/adr/0002-no-scheduling-no-monolithic-scores.md).
- **Don't round a level** ("Apply-ish", "halfway between Apply and Analyze") — rounding reintroduces the false-precision problem on a smaller scale; levels are discrete because the diagnostic value is in the *next* level the user can't reach, not in fractional progress.
- **Don't skip the baseline** — without it the verdict is a snapshot with no story, and the user has no way to tell if learning happened or stagnated.
- **Don't ask 12 questions** — cap at 6; cognitive fatigue erodes the signal, and answers from a tired user describe their tiredness, not their understanding.
- **Don't choose the suggested-next from the lowest level reached** — the dominant *gap* determines the next skill (a user at L3 with a factual gap needs `/active-recall`, not `/elaboration`); routing by level is a shortcut that misses the texture.
- **Don't read docs / code *with* the user to "fairly verify"** — joint reading collapses the assessment into a learning session, eliminating the diagnostic value; the user keeps the source closed and the agent judges.

## Governing principles (this skill satisfies all five)

1. **Agent withholds** — no hints, no partial credit narration during the assessment.
2. **Student speaks first** — every level is verified on what the user produces.
3. **Artefact is the judge** — verification reads the real code/docs.
4. **Source fidelity** — version anchoring + citation to authoritative sources on every external claim. Policy: [../../docs/sources.md](../../docs/sources.md).
5. **Exit is a transfer test** — the L3+ questions *are* transfer tests; the verdict is built on them.
