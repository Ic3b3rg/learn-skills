# Workspace — directory structure and file purposes

Reference for the **Scenario B workspace** created by `/start-learn`. The user chooses the path in plain text; in later sessions, they access it by using `cd` to enter the directory.

## Directory structure

```
workspace-root/
  MISSION.md            ← why the user wants to learn this topic
  CURRICULUM.md         ← lesson roadmap, editable by hand
  NOTES.md              ← user preferences and agent notes
  RESOURCES.md          ← Knowledge sources + community Wisdom
  lessons/
    0001-name.html      ← lessons generated on demand
    0002-name.html
  reference/
    glossario.html      ← glossary built one lesson at a time
  learning-records/
    0001-slug.md        ← progress record after each assessment
  notes/                ← atomic notes from /linked-notes (workspace mode)
  flashcards/           ← card files from /flashcards (workspace mode)
  exercises/            ← exercise files from /learn-by-doing (workspace mode)
```

## Key files

**`CURRICULUM.md`** — editable roadmap. Format:

```markdown
# Curriculum: <topic>
- [ ] Lesson 1 — Title
- [x] Lesson 2 — Title   ← already generated
- [ ] Lesson 3 — Title
```

The agent marks `[x]` when it generates the HTML file. The user can freely reorder, add, or remove lines.

**`MISSION.md`** — a goal in 3–5 lines: why, what counts as success, constraints, and what is out of scope. Written by the agent after the first exchange and confirmed by the user.

**`RESOURCES.md`** — populated through web search. Two sections: `## Knowledge` (official docs, books) and `## Wisdom` (community, forums, courses). If web search is unavailable, list source names without URLs and flag them with "verify the link."

**`reference/glossario.html`** — each lesson automatically adds its new terms. The file is a printable HTML page, updated incrementally.

## Workspace detection

Workspace-aware skills (assess, linked-notes, flashcards, learn-by-doing) detect the workspace by checking for `CURRICULUM.md` in the current directory. If present → workspace mode. If absent → legacy mode (the existing `learn/` paths).

## The `cd` rule

The user must be inside the workspace before invoking any workspace-aware skill. There is no automatic routing: the user is responsible for navigating to the correct directory.
