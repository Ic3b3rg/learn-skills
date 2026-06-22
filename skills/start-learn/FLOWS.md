# Flows — Scenario A and Scenario B detail

Reference for the **flow logic** of `/start-learn`. SKILL.md links here after auto-detection.

## Auto-detection

The agent reads the user's answer and infers the flow:

| Scenario A signals | Scenario B signals |
|---|---|
| Mentions a file, PR, repo, diff | Mentions a topic, language, new skill |
| "understand this code", "what does this do" | "learn from scratch", "I know nothing about X" |
| Context: an active codebase is open | Context: no existing artefact |

If ambiguous, the agent declares its assumption and proceeds:
> *"Starting from the hypothesis that you want to learn X from scratch — tell me if I'm wrong."*

---

## Scenario A — Understand existing code/topic

**Trigger**: the user mentions existing code or wants to deepen something in an active project.

### Protocol

1. **Declare the assumption** ("Scenario A: you're working on existing code") and ask for one-word confirmation if ambiguous.
2. **Estimate the level** from the answer: do they already have a base? are they expert? Use it to pick from the skill-mapping table.
3. **Select, declare, run.** Pick the single best-fit skill from the table, state the choice + a one-line reason, and run it. Do **not** present a menu and do **not** wait for the user to type the command — the audience doesn't know the methodologies by name (ADR 0004). The user can redirect at any point ("no, just ask me questions").
4. **Baseline handoff**: state the estimated level explicitly so `/assess` can measure the delta later.

### Skill-mapping table

| User's goal | Skill to run |
|---|---|
| Verify they really understood | `/explain-and-check <file-or-topic>` |
| Test what they remember | `/quiz-me <file-or-topic>` |
| Anchor to prior knowledge | `/connect-to-what-you-know <file-or-topic>` |
| Capture durable notes | `/linked-notes <file-or-topic>` |
| Capture flashcards | `/flashcards <file-or-topic>` |
| Practise with exercises | `/learn-by-doing <file-or-topic>` |
| Questions only, no answers | `/ask-me-questions <file-or-topic>` |

---

## Scenario B — Learn from scratch

**Trigger**: the user wants to learn something new with no existing artefact.

### Protocol

#### Step 1 — Workspace
Ask in plain text (no tool):
> *"Where do you want to create the workspace? (e.g. `~/learning/chess/` or `~/Documents/rust-ownership/`)"*

Create the folder and write `MISSION.md` (3–5 lines: why, success, constraints, out of scope). Show it to the user and wait for confirmation or correction.

#### Step 2 — Curriculum
Generate a curriculum of 8–12 lessons ordered by increasing difficulty. Show the list to the user and wait for approval/edits before writing `CURRICULUM.md`.

`CURRICULUM.md` format:
```markdown
# Curriculum: <topic>
- [ ] Lesson 1 — <title>
- [ ] Lesson 2 — <title>
...
```

The user can reorder, prune, or add lessons freely.

#### Step 3 — Resources
Search the web for authoritative sources on the topic. Write `RESOURCES.md` with two sections:
- `## Knowledge` — official docs, books, courses
- `## Wisdom` — community, forums, local classes

Fallback if web search is unavailable: names of known sources without inventing URLs, flagged *"verify the link"*.

#### Step 4 — First lesson on demand
Tell the user: *"Curriculum ready. Say 'next lesson' when you want to start."*

When the user asks for the first lesson:
1. Read the first `[ ]` line in `CURRICULUM.md`.
2. Find the primary source for the topic (web search or docs).
3. Generate the HTML file following the template in [LESSON-FORMAT.md](LESSON-FORMAT.md).
4. Mark the lesson `[x]` in `CURRICULUM.md`.
5. Update `reference/glossario.html` with the lesson's new terms.
6. Tell the user how to open the HTML file.

Repeat from point 1 for each subsequent lesson.

#### Scenario B rules

- **Don't generate all lessons upfront** — only the one requested, so each lesson can adapt to the accumulated learning-records.
- **Every lesson starts from the primary source** — no parametric-memory content without a verifiable citation.
- **The glossary is built incrementally** — add only the terms introduced in the current lesson.
- **Don't auto-dispatch other skills in Scenario B** — if the user wants `/quiz-me` or `/linked-notes` on the lesson just read, propose the command but don't invoke it automatically. (Scenario A's selection-and-run, ADR 0004, applies to methodology choice on existing code, not to pacing lesson delivery.)
