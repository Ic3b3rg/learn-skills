# Card format reference

Detailed reference for the card and file format produced by `/anki-cards`. The SKILL.md links here when generating cards.

## Card format

Every card is one block in the file:

```md
## Card N — <short slug>

**Front**
<question, ideally specific and answerable in 1–3 lines>

<details>
<summary>Answer</summary>

**Back**
<answer, 1–3 lines, ending with a citation: `file:line` or [doc link](url)>
</details>

---
```

### Three non-negotiable properties

- **Atomic.** One fact per card. *"What does `signIn` return?"* is one card. *"What does `signIn` do and when do you use it?"* is two — split.
- **Question from the user.** The user phrases the front; the agent verifies the back. Letting the agent invent the front collapses retrieval into recognition.
- **Cited.** Every back ends with a `file:line` reference or a verified doc link.

## File format

```md
# Anki Cards: <topic or file>

Generated: YYYY-MM-DD · Stack: <stack + versions>

## Card 1 — <slug>
...

## Card 2 — <slug>
...
```

Default file size: **5–15 cards**. Below 5 isn't worth a file; above 15 is fatigue territory in a single session.
