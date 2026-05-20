---
name: elaboration
description: Builds durable understanding by forcing the user to connect a new concept to things they already know — analogies to other languages, prior patterns, similar abstractions in different domains. The agent never volunteers the analogy; the user produces it, the agent stress-tests it. Use when the user is learning something new and wants to anchor it to existing knowledge, when reading code that uses an unfamiliar pattern, when a concept "isn't sticking", or anytime they say "what does this remind me of?", "connect this to what I know", "elaborate on this", "elaboration this".
---

# Elaboration

> Speak to the user in their language; these instructions are in English for the agent.

The user is asked to **produce the analogies and connections themselves** — "this is like X in Python", "this resembles the visitor pattern", "this is the same shape as Y in our codebase." The agent then stress-tests those connections against the actual artefact and against the actual analogue. Wrong analogies are more dangerous than missing ones, because they install false structure in the user's mental model.

## Quick start

```
User: /elaboration "React Server Components"
Agent: Project read first. Your package.json pins React 19.0.0; I'll cite docs for
       that version.
       Now your turn: what does "React Server Components" remind you of? Anything
       from another framework, another language, or another part of this codebase?
       Give me one or two analogies before I say anything.
```

After the user produces analogies, the agent verifies each one: where the analogy holds, where it breaks, and what consequence that has for the user's mental model.

## Workflows

### Mode detection

Inspect the argument:
- **Code-mode** — argument is a file, function, or pattern in the project. Artefact = the local code + docs of the libraries it uses.
- **Topic-mode** — argument is a concept name. Artefact = external documentation + the project's stack version.

### Session protocol

1. **Frame.** Restate the concept the user wants to elaborate on. Wait for confirmation. State whether the verification will read code, external docs, or both.
2. **Project read (topic-mode only).** Read `package.json` / lockfile / `pyproject.toml` to identify the version. If the topic doesn't appear anywhere in the project, ask the user whether to anchor on the latest stable version or a specific one.
3. **Student produces analogies first.** Ask the user for one to three analogies / connections / parallels — to other languages, other frameworks, other patterns, other parts of the codebase, even other domains entirely. **Do not** offer analogies of your own. **Do not** hint. Wait for the user.
4. **Stress-test each analogy.** For each connection the user gave:
   - **Where does the analogy hold?** Identify the shared structure. Confirm it with reference to the artefact.
   - **Where does it break?** Find the specific point where the parallel fails. Cite the line / docs / version-specific detail that makes it fail.
   - **What's the consequence?** If the user reasons from this analogy in code, where will it lead them wrong? This is the surrender risk — false analogies install confident wrong models.
5. **Surface the gap as a question, not a fix.** If the user's analogy is broken in an important way, don't say "actually it's like Z instead." Ask: *"given X in the artefact, can the analogy to Python decorators still account for this behaviour?"* Let the user repair their own model.
6. **Optional bridge.** If the user has no analogies and is stuck, offer **one** structural question (not an analogy): *"think of any time you've seen a function that takes another function and returns a modified one — does anything come to mind?"* Bridges are scaffolds, not answers.
7. **Cite.** Every claim about how a framework / library / language feature behaves carries a link or `file:line` reference. Cross-language claims (e.g. "Python decorators do X") must be cited to the relevant docs at the relevant version.
8. **Transfer-test exit.** Pose a scenario where the analogy *would* tempt the user toward a wrong answer if it were fully right. They must answer correctly, naming where the analogy breaks. Only then is the session complete.

### Suggested next

When the session closes, propose one follow-up:

- The user wants to verify the model holds end-to-end → `/feynman`
- Wants to capture the analogy + its break-point as a durable artefact → `/zettelkasten`
- Wants to fix specific facts that came up → `/anki-cards`
- Wants to confirm a level → `/assess`

## Anti-patterns

- **Don't offer your own analogy before the user does** — the user's structure is exactly what we're testing; if you produce the analogy, you've replaced their mental model with yours and there's nothing left to diagnose.
- **Don't let a broken analogy pass because "the user mostly gets it"** — the break-point is precisely where false reasoning will originate later, when the user applies the analogy beyond its range; naming the break is the entire surrender-resistant move.
- **Don't bridge too early when the user is silent** — handing them a structural question before they've tried sets a lower ceiling on what they were capable of producing; one full attempt first, then a single structural bridge if needed.
- **Don't compare to "the general idea" of a language feature** instead of its behaviour at a real version — "Python `@property`" means different things in 2.7 vs 3.12; generic analogies install confidently wrong structural beliefs.
- **Don't produce the analogy *and* its break-point in the same breath** — that collapses the diagnostic into a monologue; the user has to *walk* one step at a time for the cognitive work to happen.

## Governing principles (this skill satisfies all five)

1. **Agent withholds** — no analogies from the agent until the user has produced theirs.
2. **Student speaks first** — the user's connections are the input.
3. **Artefact is the judge** — every analogy is checked against the real code/docs, not asserted from memory.
4. **Source fidelity** — analogues across languages/frameworks cited at the relevant version, from authoritative sources only. Policy: [../../docs/sources.md](../../docs/sources.md).
5. **Exit is a transfer test** — session ends on a scenario where the analogy's break-point matters.
