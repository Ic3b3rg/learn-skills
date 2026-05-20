# Note format reference

Detailed reference for the Zettel format produced by `/zettelkasten`. The SKILL.md links here when writing notes.

## File location

Every Zettel file lives at `learn/zettel/<kebab-slug>.md`. Slugs are kebab-case, derived from the title. If a slug collides with an existing file, append a numeric suffix (`-2`, `-3`).

## Note format

```md
---
title: <single-sentence statement of the idea>
date: YYYY-MM-DD
tags: [<topic>, ...]
links:
  - [[other-note-slug]]
  - [[another-note-slug]]
---

<2–6 sentences in the user's own words. One idea. No more.>

## Why this matters

<1–2 sentences: where this idea applies, what it lets you do or avoid.>

## Sources

- `<file:line>` or [doc link](url) — what the source establishes
- `<file:line>` or [doc link](url) — what the source establishes
```

## Three non-negotiable properties

- **Atomic.** One idea per file. If a draft contains "and also...", split it.
- **In the user's words.** The agent never writes the body. If the user dictates literal docs prose, the agent pushes back: *"rephrase that in your own words — otherwise it's a quote, not a Zettel."*
- **Cited.** Every claim about external behaviour must point to an artefact or a doc. Quotes are allowed in the Sources section, not in the body.
