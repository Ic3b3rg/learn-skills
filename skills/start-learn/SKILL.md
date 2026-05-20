---
name: start-learn
description: Interview-guided entry point to the learn-skills set. Asks the user a small set of questions (intent, scenario, self-rated baseline, preferred output, assessment scale) and then PROPOSES the most suitable skill plus arguments to invoke next. The user always has the final word — the agent never auto-dispatches another skill. Use when the user is unsure which learning skill applies, says "help me start", "where do I begin", "I want to learn but don't know how", "start-learn", or when invoked without a specific methodology in mind.
---

# Start Learn

> Speak to the user in their language; these instructions are in English for the agent.

The user's entry point when they want to learn but don't yet know which methodology fits. The agent runs a short interview (5–7 questions max), captures a baseline self-assessment, then **proposes** the most appropriate skill + arguments. The user accepts, swaps, or refines. The agent never invokes another skill automatically.

## Quick start

```
User: /start-learn
Agent: A few quick questions to point you to the right skill. I'll propose at the
       end — you'll always have the final call.

       Q1 of 6: What do you want to learn? Give me either:
         - a file/folder/PR you want to understand (Scenario A: existing code), or
         - a topic name (Scenario B: a concept from scratch).
```

After the interview, the agent prints a recommendation block (with rationale + alternatives) and waits for the user to confirm or change.

## Workflows

### Session checklist (copy into your reply and tick as you go)

```
Interview progress:
- [ ] Q1: object of study confirmed (file/folder/PR or topic name)
- [ ] Q2: baseline self-rating captured (1–5)
- [ ] Q3: goal shape selected (verify / retrieve / anchor / capture / practise)
- [ ] Q4 (opt): resources noted
- [ ] Q5 (opt): output preference (artefact / in-session)
- [ ] Q6: assessment scale chosen (Bloom default, or SOLO)
- [ ] Q7 (only if ambiguous): version anchoring confirmed
- [ ] Recommendation block printed with 1 main + 2 alternatives
- [ ] User confirmed / swapped / refined
```

### Interview protocol

Read [INTERVIEW.md](INTERVIEW.md) for the full 7-question bank, the recommendation block format, and the goal → skill mapping table.

Operating rules:
- **One question at a time**, wait for the answer, cap at 7.
- Required: Q1 (object), Q2 (baseline 1–5), Q3 (goal), Q6 (Bloom/SOLO scale).
- Optional: Q4 (resources), Q5 (output preference), Q7 (only when project context is ambiguous).
- After the interview, print the recommendation block from [INTERVIEW.md](INTERVIEW.md) with one main proposal + 1–2 alternatives. Wait for the user to confirm / swap / refine.

### Baseline handoff

State explicitly in the recommendation block: *"I'll pass this baseline (<1-5> on <scale>) to `/assess` when you run it later, so progress is measurable."* This makes the connection visible.

## Anti-patterns

- **Don't ask more than 7 questions** — past 7, the user starts pattern-matching to "say yes and move on", which converts the interview from anti-surrender into surrender-by-fatigue.
- **Don't decide for the user** — even when the right skill is obvious, auto-invoking violates principle 1 and turns the entry point into a router; *always propose, always wait, always let the user type the final command*.
- **Don't skip Q2 (baseline)** — without it, `/assess` later has no reference to compare against; progress becomes invisible and surrender becomes harder to detect.
- **Don't recommend without showing the alternatives** — a recommendation that hides the alternatives forces the user to accept blind; seeing the trade-off is what makes the choice metacognitive.
- **Don't ask Q7 when the project clearly pins the version** — reading manifest files is the agent's job, not the user's; making the user answer something the codebase already states is a small but real form of surrender from the agent's side.

## Governing principles (this skill satisfies all five)

1. **Agent withholds** — proposes, never decides.
2. **Student speaks first** — every choice originates from the user's answers.
3. **Artefact is the judge** — reads project files before suggesting a version-specific topic.
4. **Source fidelity** — version anchoring happens here, before any downstream skill runs. Policy: [../../docs/sources.md](../../docs/sources.md).
5. **Exit is a transfer test** — the "exit" of `start-learn` is the user's explicit confirmation of the next skill to run; nothing happens silently.
