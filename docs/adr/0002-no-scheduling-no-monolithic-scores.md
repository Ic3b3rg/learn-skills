# No scheduling methodologies; no monolithic `/assess` scores

Two related exclusions, both rejecting features that are natural to ask for but harmful to include.

**No spaced repetition / interleaving as skills.** These methodologies operate *across* sessions and require persistent temporal state (a schedule file, a review queue, a notion of "due today"). Building that state layer is a sub-project unto itself — file format, intervals (SM-2, FSRS, Anki), missed-review handling, eventual sync — that would swallow the focus of a side-project skill set. We surface interleaving as a *tip* in the README ("declare multiple topics at session start, the agent will alternate") and we offer no spaced-repetition skill at all.

**No 1-100 numeric scores in `/assess`.** A single number produces *false precision* (73 vs 74 means nothing but reads as if it does), *false closure* ("I'm at 78, good enough" is exactly the surrender posture the skill set fights), and *borrowed confidence applied to the verdict itself* (the user accepts the number with no leverage to contest it). The pedagogical-assessment literature does not use monolithic scales; it uses discrete-level taxonomies (Bloom, SOLO) or multi-axis rubrics. We do too.

## Considered options

- **Build a minimal spaced-repetition layer (just a markdown schedule file).** Rejected: even a minimal layer raises decisions on intervals, location in the user's filesystem, integration with git, what counts as a "missed review." All of these creep. The marginal value over "user re-runs `/active-recall` when they want" is not worth the surface area.
- **Output `/assess` as `<level> + <0-100 score>`.** Rejected: the number does the dominant work in the user's mind (numbers are sticky), so the discrete level becomes decorative. Worse of both worlds.
- **Output `/assess` only as Bloom level, no gap list.** Rejected: a level alone is information ("you are at Apply"); a gap list is *action* ("you can't articulate why optimistic vs pessimistic locking matters here"). The action is the value.

## Consequences

- The skill set is **stateless across sessions** by design. Any persistence is a side-effect of a skill writing a file (e.g. `/zettelkasten` produces a note, `/learn-by-doing` produces an exercise file), never a hidden state machine the agent maintains.
- `/assess` always outputs: **discrete Bloom or SOLO level + gap list + suggested next skill**. A `--detailed` flag enables a 4-axis rubric (Recall / Trace / Transfer / Teach-back, each 1-3) as an opt-in.
- "Where's spaced repetition?" will be a frequently-asked question. The README's *Out of scope* section answers it pre-emptively and points here.
