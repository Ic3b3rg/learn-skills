# Levels — assessment scales and verdict format

Detailed reference for the **Session protocol** of `/assess`. The SKILL.md links here when running the assessment.

## Session protocol

1. **Frame.** Restate object, scale (Bloom default unless overridden), and rules: sources closed, no consulting between questions. Wait for confirmation.
2. **Recall baseline.** If `/start-learn` recorded a baseline self-assessment, state it. This makes any later delta visible. If no baseline exists, ask the user for one (1–5 self-rating) before starting.
3. **Project read (topic-mode only).** Read `package.json` / lockfile / `pyproject.toml` for the version in use. Assess against that version, not generic knowledge.
4. **Ask 4–6 questions of ascending cognitive demand** (see Bloom or SOLO mapping below). Each question targets one level. Stop early if the user fails two consecutive levels.
5. **Verify each answer against the artefact.** Read the code (Read tool) or docs (WebFetch / context7). Mark each answer **pass / partial / fail**, with the specific divergence noted.
6. **Map performance to a level.** Reach a level only when the user passes all questions up to and including it. A partial at level L means the user is at L−1 with a specific gap *toward* L.
7. **Produce the verdict block** in the exact format below.

## Bloom mapping (default)

- **L1 — Remember**: name / list / state the basic facts.
- **L2 — Understand**: explain in your own words why X works.
- **L3 — Apply**: solve a small, mechanical problem using the concept.
- **L4 — Analyze**: compare two designs and identify the trade-off.
- **L5 — Evaluate**: judge a design choice in this codebase, justify with cited reasoning.
- **L6 — Create**: design a new component / pattern using the concept correctly.

## SOLO mapping (if chosen)

Prestructural → Unistructural (one point) → Multistructural (several disconnected points) → Relational (points connected) → Extended abstract (generalises beyond the case).

## Verdict block — exact format

```
Topic: <topic>
Scale: Bloom (or SOLO)
Baseline (from /start-learn): <self-rated 1-5 or "not provided">
Verified level: <Bloom level name, e.g. "Apply (L3)">
Gaps:
  - <concrete gap 1, with file:line or doc reference>
  - <concrete gap 2>
  - <concrete gap 3, if any>
Suggested next: /<skill> <arguments>
```

**Never** include a numeric score. **Never** round levels (no "2.5"). A user is *at* a level or *not yet at* a level.

## `--detailed` mode (optional)

If the user passes `--detailed`, additionally produce a 4-axis rubric (Recall / Trace / Transfer / Teach-back, each 1–3). Use it as colour, never as a replacement for the Bloom/SOLO level.
