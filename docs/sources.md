# Verification Sources — Policy

Operational policy for how skills in this repo verify claims made by the user (and by themselves) against external knowledge. Companion to **Principle 4: Source fidelity** in [CONTEXT.md](../CONTEXT.md). Linked from every skill that performs verification.

The premise: when the user demonstrates knowledge by explaining, retrieving, analogising, or producing an answer, the agent's verification cannot rest on the agent's own training. It must rest on **a real source the user can open and read for themselves**. Otherwise the verdict is just one model's confidence transferred to the user — the textbook surrender pattern, applied at the verification layer.

## What counts as an authoritative source

In priority order. Use the highest-priority source available; degrade only when necessary.

### Tier 1 — Canonical, version-pinned
- **Official documentation** at the version actually used in the project (read manifest files first).
- **Source code of the library / framework / language itself** at the pinned version (release tags, not `main`).
- **Standards & specs**: RFCs, W3C / WHATWG / ECMAScript specs, language reference manuals.
- **Project's own code** — when verifying a claim about the user's codebase, the code on disk is the source.

### Tier 2 — Authoritative secondary
- Release notes / changelogs of the relevant version.
- Anthropic / OpenAI / vendor documentation for the AI / SDK / API in question.
- Peer-reviewed academic papers for theoretical or pedagogical claims.

### Tier 3 — Use with explicit caveat
- Conference talks / official blog posts from project maintainers (e.g. React team blog) — note date + version.
- Type definitions / `.d.ts` files in well-maintained `@types` packages.

### Not authoritative (do NOT cite as verification)
- StackOverflow answers, blog tutorials, Medium posts, YouTube tutorials.
- LLM-generated content (including the agent's own prior turns).
- Outdated docs for older versions when the project uses a newer one.
- Anyone's "best practices" article, no matter how popular.

These can be useful as *starting points* for the user's learning, but they cannot serve as the **judge** in a verification step.

## How to cite

Every external claim that contributes to the verification must carry **a link** the user can open. The link is what makes the verdict *auditable*.

### Format

- **Local code**: `path/to/file.ts:42-58` — line-precise, copy-pasteable into the editor.
- **Web sources**: `[anchor text](https://url)` — always linked, never mentioned by name only.
- **Multi-source**: list each one; do not aggregate ("the docs say X" with no link is borrowed confidence).

### Where to look up

Use available retrieval tools, in this order:

1. **Read** for local code.
2. **context7** for indexed library docs at the pinned version — fast, version-aware.
3. **WebFetch** for direct URL retrieval when the user provides one.
4. **WebSearch** only when the canonical URL is unknown and must be discovered.

### Anti-pattern: silent assertion

The single most common failure mode is the agent making a confident claim about external behaviour without a link, because *"I know this one."* That confidence is exactly what the user is supposed to be checking *against* the source. Stating it as fact short-circuits the verification.

If the agent can't find a source for a claim, the correct move is **declare uncertainty**, not assert from memory:

> "I expected `signIn()` to return a Promise<Session> but I couldn't confirm this in the v5 docs I have access to — can you point me to the function signature? Until then, treat this verification as open."

## Version matters more than people assume

A correct claim at v4 of a library is a wrong claim at v5. Before any topic-mode verification:

1. Read the project's manifest (`package.json`, lockfile, `pyproject.toml`, `Gemfile`, ...) to identify the pinned version.
2. Anchor citations to **that** version's documentation.
3. If the project doesn't pin the topic (e.g. user asks about "decorators" with no language context), **ask which version** to anchor on. Never assume.

## When to invite the user to read the source

After verification, when a gap is identified, the agent should **link the source paragraph or file:line** and invite the user to read it before re-explaining. This is the difference between "you got it wrong" and "here is the source — see if your model still holds after reading."

The point is not that the agent has the answer. The point is that **the source has the answer, and the user can reach it directly**. The agent is the index, not the oracle.
