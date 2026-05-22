# Evidence-based core, with Bloom/SOLO as editorial concepts (and as the `assess` scale)

The set is built around methodologies with strong empirical support in the learning-sciences literature — **explain-and-check, quiz-me, connect-to-what-you-know** as the core; **ask-me-questions, learn-by-doing, linked-notes, flashcards** as secondary. **Bloom's taxonomy and SOLO are NOT skills**: they are editorial concepts the project uses internally to help users pick, *and* the discrete scale `/assess` reports on. The reason for this dual role: a taxonomy is a *map for thinking about learning*, not a protocol you run, so packaging it as an invocable skill would either duplicate other skills or build a meta-router we explicitly rejected.

## Considered options

- **Flashcards as a peer methodology.** Rejected. Flashcards are a *vehicle* for retrieval practice (`/quiz-me`) + spaced repetition, not a methodology in their own right. We keep `/flashcards` as a secondary *generative* skill (it produces flashcards), but the methodology being practised is retrieval.
- **Bloom as a peer skill (`/bloom`).** Rejected. Bloom is a taxonomy of cognitive levels (remember → … → create). Forcing it into a skill either duplicates the others (Bloom-level "remember" ≈ `/flashcards`) or builds a meta-router that decides per level — which would violate the no-router principle (see [ADR 0002](0002-no-scheduling-no-monolithic-scores.md)).
- **A larger set including spaced repetition and interleaving.** Rejected — see [ADR 0002](0002-no-scheduling-no-monolithic-scores.md).

## Consequences

- Bloom and SOLO are used internally **as a chooser**: "want to *remember*? → `/flashcards`; *understand*? → `/explain-and-check`; *apply* / *create*? → `/learn-by-doing`."
- `/assess` outputs are expressed in Bloom or SOLO levels (user picks at `/start-learn` time). The taxonomy is reused as the assessment scale rather than as a skill.
- Adding a new skill in the future requires demonstrating it is (a) a *methodology* (not a vehicle, not a taxonomy) and (b) backed by evidence, not folk pedagogy.
