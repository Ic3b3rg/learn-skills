---
name: linked-notes
description: Produces atomic, linked markdown notes that capture one idea each, written in the user's own words, and cross-linked by topic. Each note carries a citation to the source artefact (code, docs, prior notes). Use when the user wants to turn a learning session into durable knowledge, when capturing insights from a /explain-and-check or /connect-to-what-you-know session, when "I want notes I can come back to", or anytime they say "save this as notes" or "make me notes".
---

# Linked Notes

> Speak to the user in their language; these instructions are in English for the agent.

A generative skill that turns a session's insight into a small set of **atomic notes** under `learn/notes/`, each capturing exactly one idea, written in the user's own words, with citations to the artefact and links to related notes. The notes outlast the session and compose into a growing knowledge base.

## Quick start

```
User: /linked-notes "event sourcing"
Agent: Project read first. Stack: TypeScript + EventStoreDB 23.x.
       I'll guide you through writing 3–6 atomic notes — one idea each, in your
       own words, with citations. You write; I check atomicity, drift, and
       citations. Start by telling me the first idea you want to capture.
```

After the session, files exist at `learn/notes/<slug>.md`, each containing one note with frontmatter, body, citations, and links to other notes.

## Workflows

### Mode detection

Inspect the argument:
- **Code-mode** — argument is a file or PR. Notes capture *what this code teaches* (patterns, invariants, surprises).
- **Topic-mode** — argument is a concept. Notes capture *one idea at a time* about the concept, anchored to the project's actual stack version.

### Note format

See [NOTE-FORMAT.md](NOTE-FORMAT.md) for the exact file location, frontmatter, body structure, and the three non-negotiable properties (atomic, in-the-user's-words, cited).

### Session protocol

1. **Project read** (topic-mode). Read `package.json` / lockfile to identify versions. Citations must match the version in use.
2. **One note at a time.** Ask the user for the first idea they want to capture. Single sentence, declarative, in their own words.
3. **Atomicity check.** Read what the user wrote. Does it contain more than one idea? If yes, ask which one to capture first; the rest become a queue for follow-up notes.
4. **Citation check.** For every claim in the note about *external* behaviour (an API behaves this way, a feature works like this), ask the user to supply or accept a citation (`file:line` or doc link). Use Read / WebFetch / context7 to verify the citation is accurate before writing it into the file.
5. **Wording check.** Compare the body to known docs/code. If it is a near-quote, ask the user to restate. Real notes are paraphrases — paraphrasing is itself an act of learning.
6. **Link suggestion (gentle).** After writing the note, check `learn/notes/` for existing notes with overlapping tags. Suggest 1–3 candidate links — the user accepts or rejects each. Never auto-link.
7. **Write the file.** Use the Write tool. Confirm filename and path with the user if it would collide with an existing slug.
8. **Loop or close.** Ask whether the user wants to capture another idea or close. If close, summarise: *N notes written, M new links."*

### Linking discipline

- Links are markdown wikilinks: `[[other-note-slug]]`.
- Bidirectional manually: if note A links to B, propose adding the reciprocal link to B.
- Don't create "index" notes. The folder structure + tags are the index.
- Don't backlink to source raw files: those belong in **Sources**, not in **links**.

### File hygiene

- Slugs are kebab-case, derived from the title. Collisions: append `-2`, `-3`.
- The agent never modifies an existing note's body in the same session — only adds links (with user confirmation).

### Workspace mode

If `CURRICULUM.md` exists in the current directory, the skill is running inside a Scenario B workspace. In workspace mode:
- Notes go to `notes/<slug>.md` (not `learn/notes/`).
- After each note, propose adding new terms to `reference/glossario.html`: *"This introduces the term X — add it to the glossary?"* The user decides; the agent writes the entry.

If `CURRICULUM.md` is absent (legacy mode), notes go to `learn/notes/` as before.

## Anti-patterns

- **Don't write compound notes** ("here's a note that covers X, Y, and Z") — non-atomic notes break the linking model and become unreusable; the act of forcing yourself to split them into atomic units is itself a learning act.
- **Don't author body prose for the user** — the agent prompts, verifies, formats; never writes the user's idea for them, because notes that aren't in the user's own words don't trigger the paraphrase-as-learning act that justifies the format.
- **Don't cite from memory** — every citation is verified against the real source before being written into the note, otherwise the durable artefact propagates borrowed confidence into the future.
- **Don't auto-link based on string match** — always propose, never auto-link; linking choices are the user's because the connections are *their* knowledge graph, not the agent's.
- **Don't mix atomic notes with raw notes or sketches** — atomic-only is what makes the collection composable; other captures (drafts, outlines, scratch) go elsewhere.

## Governing principles (this skill satisfies all five)

1. **Agent withholds** — the agent prompts, checks, formats; never authors body content.
2. **Student speaks first** — every note is the user's words.
3. **Artefact is the judge** — every citation verified against the real source before being written.
4. **Source fidelity** — version anchoring + citation to authoritative sources on every external claim. Policy: [../../docs/sources.md](../../docs/sources.md).
5. **Exit is a transfer test** — the *paraphrase* requirement (own words, not quotes) is itself a transfer demonstration.
