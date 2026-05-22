# Interview — question bank and skill-mapping table

Detailed reference for the **Interview protocol** of `/start-learn`. The SKILL.md links here when conducting the interview.

## Interview protocol

Ask **one question at a time**. Wait for the answer before moving on. Cap at 7 questions total. Each question carries its own purpose; never skip the purpose-bearing ones (Q1, Q2, Q3, Q6).

**Q1 — Object of study (required).** *"A file/folder/PR you want to understand, or a topic name you want to learn?"* — disambiguates Scenario A (existing code) vs B (topic from scratch).

**Q2 — Self-rated baseline (required).** *"On a 1-to-5 scale, how would you rate your current understanding of this?"* — captured for `/assess` to use later as the comparison baseline.

**Q3 — Goal shape (required).** *"At the end of the session, do you want (a) to verify you understand it deeply, (b) to retrieve what you already knew, (c) to anchor it to things you know, (d) to capture it for later, or (e) to practise applying it?"* — maps onto methodology family.

**Q4 — Resources (optional).** *"Any specific resources you want to use? URL, file, video, book?"* — accept multiple, of any type. Skip if Q1 already gave a project file.

**Q5 — Output preference (optional).** *"Do you want to walk away with a durable artefact (notes, flashcards, exercise file), or is in-session understanding enough?"* — picks generative vs dialogic.

**Q6 — Assessment scale (required for downstream `/assess`).** *"For future progress checks, do you prefer Bloom (remember → … → create) or SOLO (prestructural → … → extended abstract) levels? Default Bloom if unsure."*

**Q7 — Stack version (only when ambiguous).** *"Your project pins X version of [library]; should we anchor to that, or to a different version?"* — only ask if the project context is unclear.

## Skill-mapping table

Use this as a guide. **Never automatic** — always present as a proposal.

| Goal in Q3 | Scenario A (code) → | Scenario B (topic) → |
|---|---|---|
| (a) verify deep understanding | `/explain-and-check <file>` | `/explain-and-check <topic>` |
| (b) retrieve prior knowledge | `/quiz-me <file>` | `/quiz-me <topic>` |
| (c) anchor to existing knowledge | `/connect-to-what-you-know <file>` | `/connect-to-what-you-know <topic>` |
| (d) capture for later | `/linked-notes <file>` or `/flashcards <file>` | `/linked-notes <topic>` or `/flashcards <topic>` |
| (e) practise applying it | `/learn-by-doing <file>` | `/learn-by-doing <topic>` |

If the user wants only questions (no agent answers at all), propose `/ask-me-questions` regardless of goal.

## Recommendation block format

```
Based on your answers:
  - Object: <object>
  - Baseline: <1-5> on <scale>
  - Goal: <goal>
  - Resources: <list or "none">
  - Assessment scale: <Bloom | SOLO>

I recommend → /<skill-name> <arguments>
Why: <one or two sentences mapping the answers to this skill's strengths.>

Alternatives:
  - /<alt-1> — <when this would be a better fit>
  - /<alt-2> — <when this would be a better fit>

Confirm (run as-is), swap (pick an alternative), or refine (change arguments)?
```
