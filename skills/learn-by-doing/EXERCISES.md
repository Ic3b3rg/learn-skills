# Exercises — generation reference

Detailed reference for the **Generation protocol** step of `learn-by-doing`. The SKILL.md links here when the agent is about to draft the exercises file.

## Generation protocol

1. **Project read.** Read `package.json` / lockfile / `pyproject.toml` / `Gemfile` to identify the stack and versions. Generated code in exercises and solutions must match the project's stack. Never use a generic version.
2. **Read the artefact (code-mode) or fetch the docs (topic-mode).** Exercises must be solvable; solutions must be verifiable. If the agent cannot cite a source for the solution, the exercise is dropped.
3. **Pick 3–7 exercises of ascending demand.** Use the ladder below.
4. **Write the file** at `exercises/<slug>-exercises.md` if `CURRICULUM.md` exists in the current directory; otherwise use `learn/<slug>-exercises.md`. Use the format below.

## Exercise ladder

The ladder maps onto Bloom's progression. Pick the 3–7 rungs most relevant to the user's level (from `/start-learn` baseline if available):

- **E1 — Reproduce.** Recreate a small piece of behaviour from a spec sentence.
- **E2 — Extend.** Add a small, isolated feature.
- **E3 — Refactor.** Improve a specified property (readability, performance, type-safety) without changing behaviour.
- **E4 — Debug.** Given a deliberately broken version, find and fix the bug. **Include this in code-mode** to test whether the learner can identify a broken assumption.
- **E5 — Apply elsewhere.** Use the same pattern in a different file / domain.
- **E6 — Design.** Make a choice between two plausible designs, justify with the project's constraints.
- **E7 — Teach.** Write a 5-line explanation that another developer could follow.

## File format

```md
# Exercises: <topic or file>

Generated: YYYY-MM-DD · Stack: <stack + versions>

## E1 — Reproduce
<prompt>

## E2 — Extend
<prompt>

...

---

## Solutions (folded — open only after attempting)

<details>
<summary>Open solutions</summary>

### E1
<solution, with `file:line` references or doc citations>

### E2
...
</details>
```

**The solutions fold is non-negotiable.** Putting solutions next to prompts destroys the skill.
