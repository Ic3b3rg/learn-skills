---
name: active-recall
description: Forces the user to retrieve knowledge from memory before consulting any source, then verifies what they produced against the real artefact (code, tests, official documentation). Use when the user wants to test what they have actually learned about a topic or a piece of code, to consolidate knowledge after a learning session, after a few days have passed since they last touched a subject, or anytime they say "let me see if I remember", "test my recall", "let's check what I retained", "active-recall this".
---

# Active Recall

> Speak to the user in their language; these instructions are in English for the agent.

The user retrieves what they know **without looking** at code, notes, or docs first; the agent then verifies the retrieval against the real artefact and surfaces the gaps. Retrieval-before-consultation is the entire point — opening the source first turns recall into recognition, which is a different and weaker learning act.

## Quick start

```
User: /active-recall src/auth/session.ts
Agent: Close the file before answering. I won't ask you anything until you confirm
       it's closed.
       Tell me from memory: what does this module export, and what does each export do?
       Don't worry about being exhaustive — just write what you actually remember.
```

After the user produces their recall, the agent opens the file, compares what was retrieved against what is there, and questions only the gaps.

## Workflows

### Mode detection

Inspect the argument:
- **Code-mode** — argument is a file, directory, or PR/diff the user has previously worked on. Artefact = the local code.
- **Topic-mode** — argument is a topic name the user has previously studied. Artefact = external documentation + the project's actual stack version.

If the argument refers to something the user has clearly never seen, redirect: this skill is for retrieving prior learning, not first contact. Suggest `/feynman` or `/elaboration` instead.

### Session protocol

1. **Source closed.** Explicitly instruct the user to close the file / put the docs away / not look anything up. Wait for confirmation. This is the single most violated rule in self-study and the skill must enforce it.
2. **Ask a retrieval-shaped question.** Not "tell me about X" (too open, the user fills space). Use concrete prompts: *"name the three things this module exports"*, *"list the steps of the request flow you remember"*, *"give me the signature of the main function and what it returns."* Specific shapes force commitment.
3. **Project read (topic-mode only).** Before verification, read `package.json` / lockfile / `pyproject.toml` to anchor on the version actually used. Never compare the recall against generic knowledge.
4. **Verify against the artefact.** Read the code (Read tool) or docs (WebFetch / context7). Mark what the user got correct, what they missed entirely, and what they recalled *wrong* (those are the most dangerous — confident false memories).
5. **Triage the gaps.** Categorize: (a) detail forgotten (cheap to relearn), (b) structure misremembered (concept-level gap), (c) confidently wrong (false memory — needs explicit correction with evidence).
6. **Targeted re-retrieval, not re-reading.** Don't dump the correct answer. For each gap, ask a follow-up question that *requires* the right answer to satisfy. Only if the user still cannot retrieve, point at the file:line or doc paragraph and ask them to read and then re-retrieve later (close again, answer again).
7. **Cite.** Every external claim about API / library behaviour must carry a link or `file:line` reference. If no source is found, declare uncertainty.
8. **Transfer-test exit.** Ask one question about a scenario the user has *not* seen but that requires the same retrieved knowledge to answer. They must answer with the source still closed. Only then is the session complete.

### Suggested next

When the session closes, propose one follow-up:

- High rate of confident false memories → `/feynman` to rebuild the model
- Many forgotten details, structure intact → `/anki-cards` to capture for next time
- Structural gaps → `/elaboration` to reconnect to prior knowledge
- Wants durable notes → `/zettelkasten`
- Wants to confirm a level → `/assess`

## Anti-patterns

- **Don't let the user peek at the source before retrieving** — recognition triggered by exposure is a fundamentally weaker learning act than retrieval from memory; the moment the source is open, the experiment is contaminated.
- **Don't ask open prompts that let the user wander** ("tell me about X") — open prompts let the user fill space with what they remember confidently; forced-shape prompts ("name three", "give the signature", "list the steps in order") commit them to specific claims that can be verified.
- **Don't fill in a missed detail by stating it** — handing the answer over collapses the active retrieval back into passive recognition; point at the line, close the source again, re-retrieve.
- **Don't treat a confident wrong answer as "almost right"** — false memories are more dangerous than missing ones because the user reasons from them later; flag them explicitly with the citation that contradicts them.
- **Don't accept "yes I remember now" as exit after seeing the answer** — exposure-triggered recognition is not retrieval. Exit is a passed transfer test with the source closed, on a scenario the user has not just seen.

## Governing principles (this skill satisfies all five)

1. **Agent withholds** — no information from the agent until the user has retrieved.
2. **Student speaks first** — the user's retrieval is the input.
3. **Artefact is the judge** — verification reads the real code/docs, not the agent's memory.
4. **Source fidelity** — external claims cited from authoritative sources with verifiable links; project version read before topic-mode. Policy: [../../docs/sources.md](../../docs/sources.md).
5. **Exit is a transfer test** — session ends on a passed new-scenario question, source closed.
