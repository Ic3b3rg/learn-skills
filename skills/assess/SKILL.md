---
name: assess
description: "Assesses demonstrated understanding with Bloom or SOLO levels, concrete gaps, and a next learning step. Use when the user requests a formative assessment, asks \"where am I at?\", or wants their current level checked after studying."
---

# Assess

> Speak to the user in their language; these instructions are in English for the agent.

A short, structured assessment that returns a **discrete level** on a named taxonomy (Bloom or SOLO), a **concrete gap list**, and a **suggested next skill** to close the most material gap. A monolithic 0–100 number is **not** an output of this skill, by design — see [ADR 0002](https://github.com/Ic3b3rg/learn-skills/blob/master/docs/adr/0002-no-scheduling-no-monolithic-scores.md).

## Quick start

```
User: /assess "event sourcing"
Agent: I'll use Bloom unless you prefer SOLO, with 4–6 questions of increasing demand.
       Close the code and docs and confirm before we begin.
User: Closed. Bloom is fine.
Agent: Your earlier baseline was 2/5. Answer without consulting sources:
       Q1 (Remember): What is stored in an event stream?
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
- [ ] Question sequence follows the chosen scale in LEVELS.md
- [ ] Each answer verified against the artefact
- [ ] Questions asked in ascending cognitive demand
- [ ] Stopped after two consecutive fails, if reached
- [ ] No more than six questions asked
- [ ] Partial answers recorded as gaps toward the next level
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
5. **Verify each answer against the artefact** — local code or authoritative documentation using available retrieval tools. Pass / partial / fail with cited evidence.
6. **Map performance to a level** — highest level fully passed; a partial at L means the user is at L−1 with a gap *toward* L.
7. **Produce the verdict block** in the exact format defined in [LEVELS.md](LEVELS.md). Never a numeric score; never a rounded level.

`--detailed` adds a 4-axis rubric (Recall / Trace / Transfer / Teach-back, 1–3 each) as colour, not replacement.

### Choosing the suggested next skill

Pick by **dominant gap**, not by lowest level: structural → `/explain-and-check` or `/connect-to-what-you-know`; factual → `/quiz-me` (capture with `/flashcards`); can't apply → `/learn-by-doing`; can't connect → `/connect-to-what-you-know`; solid, wants record → `/linked-notes`.

### Source fidelity

Every verification reads the real artefact; every external claim carries `file:line` or a doc link. If an answer cannot be sourced, **drop the question** rather than score from memory.

### Workspace mode

If `CURRICULUM.md` exists in cwd: read `learning-records/` first and state prior progress (*"Last session: Apply (L3)"*). After verdict, write `learning-records/NNNN-<topic>-assessment.md` (frontmatter: `date`/`topic`/`level`; body: gap list; N = highest existing + 1). Absent: no records touched.

## Anti-patterns

- **Don't produce a 1-100 score** — a single number creates false precision, false closure ("78, good enough"), and applies borrowed confidence to the verdict itself; this is the failure mode the skill exists to refuse. See [ADR 0002](https://github.com/Ic3b3rg/learn-skills/blob/master/docs/adr/0002-no-scheduling-no-monolithic-scores.md).
- **Don't round a level** ("Apply-ish", "halfway between Apply and Analyze") — rounding reintroduces the false-precision problem on a smaller scale; levels are discrete because the diagnostic value is in the *next* level the user can't reach, not in fractional progress.
- **Don't skip the baseline** — without it the verdict is a snapshot with no story, and the user has no way to tell if learning happened or stagnated.
- **Don't ask 12 questions** — cap at 6; cognitive fatigue erodes the signal, and answers from a tired user describe their tiredness, not their understanding.
- **Don't choose the suggested-next from the lowest level reached** — the dominant *gap* determines the next skill (a user at L3 with a factual gap needs `/quiz-me`, not `/connect-to-what-you-know`); routing by level is a shortcut that misses the texture.
- **Don't read docs / code *with* the user to "fairly verify"** — joint reading collapses the assessment into a learning session, eliminating the diagnostic value; the user keeps the source closed and the agent judges.

## Governing principles (this skill satisfies all five)

1. **Agent withholds** — no hints, no partial credit narration during the assessment.
2. **Student speaks first** — every level is verified on what the user produces.
3. **Artefact is the judge** — verification reads the real code/docs.
4. **Source fidelity** — version anchoring + citation to authoritative sources on every external claim. Before verifying, read [SOURCES.md](SOURCES.md).
5. **Exit is a transfer test** — the L3+ questions *are* transfer tests; the verdict is built on them.
