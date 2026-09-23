# Per-skill quality research

Research date: 2026-09-23. Scope: the nine local learning skills, their operational instructions, and ADRs 0001–0004. This report complements [the portability audit](skill-portability.md). It proposes editorial and operational improvements; it does not validate these LLM workflows experimentally or authorize a new teaching methodology.

## Evidence and scope

The research below uses original research papers on publisher or author-institution sites and authoritative National Academies reports. Evidence about a learning mechanism is not evidence that this exact skill, question count, taxonomy mapping, model, or provider produces the same outcome. Authoritative syntheses are identified as such, not presented as individual experiments. No learner study or cross-provider execution was performed for this report.

Preserve the project's choices: student production before feedback; source verification; individual workflow exceptions; discrete Bloom/SOLO output and gap lists; no review scheduler; automatic Scenario A dispatch; user-paced Scenario B lessons. Research can improve the accuracy of explanatory prose without silently changing those choices. Implementation suggestions below are deductions from comparing the sources with the local instructions, not conclusions reported by the papers.

## 1. ask-me-questions

**Relevant evidence.** Chi et al. (2001) studied human tutoring and an intervention that suppressed tutor explanations and feedback while encouraging prompts. Students learned as effectively under that interactive condition; the authors discuss constructive student activity and scaffolding. This supports investigating learner construction through questions. It does not establish a universal questions-only requirement for all learners or topics. [Original paper and abstract](https://onlinelibrary.wiley.com/doi/abs/10.1207/s15516709cog2504_1)

**Preserving improvement.** Align every example with the existing one-question-at-a-time rule. The anti-pattern replacement currently combines “What pattern…” and “What would you guess…” in one turn. Show the first question, wait, then the second. Describe the posture as questions-only **with the two named exceptions**, so the opening summary does not compete with citation and safety clauses. Retain the user-requested switch to explanation.

**Behavioral check.** An ordinary session asks one question without a declarative hint; a citation request declares the exception, supplies the source, and returns to questions. A user's stop ends the session.

**Deferred.** Whether prolonged frustration should trigger a new hint policy or another exception is a pedagogical decision. The tutoring paper does not settle it.

## 2. explain-and-check

**Relevant evidence.** Chi et al. (1994) found greater gains from prompted self-explanation than repeated reading in a small study of students learning the circulatory system. This supports asking learners to construct explanations; it does not validate this skill's exact sequence, developer audience, or one-question transfer criterion. [Original paper and abstract](https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1803_3)

**Preserving improvement.** Keep the distinction between an underivable prerequisite and the conclusion being tested adjacent to the withholding instruction. Clarify that file-role framing may require silent inspection before the student's explanation; it must not expose the mechanism. State completion as the existing sequence: transfer answer, learner-drawn trace, verification. Avoid summarizing completion as merely the learner saying they understand.

**Behavioral check.** A missing local symbol definition receives the permitted one-sentence prerequisite; a missing reasoning step receives a question, not the agent's solution. The final diagram is produced by the learner.

**Deferred.** Adding worked explanations or changing the transfer threshold would change the protocol. One successful new example is evidence about that example, not proof of durable mastery across contexts.

## 3. quiz-me

**Relevant evidence.** Roediger and Karpicke (2006) compared studying and retrieval for prose passages: restudying had an immediate-test advantage, whereas testing improved delayed retention. This supports retrieval before consultation when practising recall. It does not justify saying all recognition or rereading is inherently inferior in every setting. [Original paper, author's laboratory](https://learninglab.psych.purdue.edu/downloads/2006/2006_Roediger_Karpicke_PsychSci.pdf)

**Preserving improvement.** Split the quick-start transcript at the existing source-closed confirmation gate: agent asks the learner to close the file, learner confirms, agent asks recall. The current example promises to wait and then immediately asks the question. Keep the order of learner attempt, source verification, targeted retry, and new-scenario exit explicit. Describe recognition as failing this task's recall criterion, rather than universally useless learning.

**Behavioral check.** No recall prompt arrives before confirmation. A confident wrong answer is checked against a source. “I remember now” after rereading does not replace the source-closed transfer answer.

**Deferred.** Scheduled repetition, prescribed delays, or a changed correction strategy are outside the preservation scope and ADR 0002.

## 4. connect-to-what-you-know

**Relevant evidence.** Gentner, Loewenstein, and Thompson (2003) studied analogical encoding in negotiation: comparing cases supported abstraction and transfer. The paper explicitly distinguishes comparison between examples from invoking a familiar base-domain analogy. This is related evidence for structural comparison, not direct validation of learner-generated software analogies or a strict ban on tutor examples. [Original paper, author's institution](https://groups.psych.northwestern.edu/gentner/papers/GentnerLoewensteinThompson03.pdf)

**Preserving improvement.** Use a compact internal verification checklist for each supplied analogy: shared relation, breakpoint, consequence, source. Retain learner-first generation and the one permitted structural bridge after an attempt. Clarify that citations must establish both sides of a cross-language comparison, including relevant version differences.

**Behavioral check.** The agent never proposes the initial analogy; a plausible but broken analogy triggers a repair question and a transfer example testing its boundary.

**Deferred.** Offering worked analogies, paired comparison tasks, or more scaffolding could be useful experiments but would change the chosen method. Do not claim the existing one-to-three analogy range has empirical optimization behind it.

## 5. assess

**Relevant evidence.** The National Research Council's *Knowing What Students Know* treats assessment as reasoning from observations, using a model of cognition and an interpretation method. That supports tying a judgment to tasks and evidence. It does not validate this repository's four-to-six-question interview as a calibrated measurement instrument or its highest-passed-level algorithm. [Authoritative assessment report](https://www.nationalacademies.org/read/10019/chapter/3)

**Preserving improvement.** Make the visible checklist refer to the selected taxonomy; its current Remember–Create labels are Bloom-specific despite SOLO being first-class. Preserve the exact verdict format and mappings in `LEVELS.md`. Make evidence timing consistent: verify internally as answers arrive, preserve the no-hints/no-partial-credit-narration rule, and cite evidence in the verdict. Treat the label as the level demonstrated on the sampled tasks, not a global certification of the person.

**Behavioral check.** Run Bloom and SOLO fixtures, including missing sources and two consecutive failures. Unsourced questions are dropped; the next skill follows the dominant gap; no monolithic numeric score appears.

**Deferred.** Recalibrating taxonomies, changing stop rules, resolving unrepresented edge cases in the level model, or adding confidence intervals requires a separate assessment design decision. A discrete label alone does not remove measurement uncertainty. The ADR claim that assessment literature does not use monolithic scales should not be repeated as a universal fact; the no-score rule can stand as a product choice.

## 6. flashcards

**Relevant evidence.** Retrieval experiments support practising recall, not merely owning a card deck. Roediger and Karpicke (2006) studied prose retrieval, not this Markdown format, student-authored fronts, or a fifteen-card cap. The project's distinction between generating cards and using them for retrieval is therefore useful. [Original retrieval study](https://learninglab.psych.purdue.edu/downloads/2006/2006_Roediger_Karpicke_PsychSci.pdf)

**Preserving improvement.** Resolve the output directory once from workspace mode and reuse it in the saved-path message and follow-up invocation. Keep user-authored fronts, verified backs, citations, and folds. Describe the fifteen-card limit as the existing session limit, without an unsupported claim that fatigue necessarily starts there. Check the rendered example actually places the answer inside `<details>`.

**Behavioral check.** A workspace session writes to `flashcards/` and recommends practising that actual file. No front or back is silently fabricated; no answer appears above the fold.

**Deferred.** Deck scheduling, importer guarantees, learner-independent front generation, and adaptive card counts change scope or behavior. Generating a deck is not itself a passed transfer test.

## 7. learn-by-doing

**Relevant evidence.** Freeman et al. (2014) synthesized 225 studies of undergraduate STEM courses and found improved outcomes under active learning compared with traditional lecturing. This supports active participation broadly, but it is a meta-analysis of varied classroom interventions, not a trial of these generated exercises. [Authors' published meta-analysis](https://doi.org/10.1073/pnas.1319030111)

**Preserving improvement.** Make paths in the checklist honor the existing workspace override. Treat three-to-seven exercises as the chosen bounded output and E4 as the required code-mode task; remove unsupported superlatives about debugging always having the highest transfer signal. Preserve solution folds, source grounding, collision handling, and learner control over progression. Make generating an exercise file distinct from verifying completed answers.

**Behavioral check.** A three-exercise code-mode output still includes the required debug task. The file contains no exposed solutions, and a failed answer receives a targeted question plus evidence rather than a spoiler.

**Deferred.** Changing the exercise ladder, adding fully worked examples, or adapting limits by fatigue would change the protocol. Neither the seven-exercise cutoff nor the mandatory debug ranking follows from the cited study.

## 8. linked-notes

**Relevant evidence.** Self-explanation research supports constructive generation, but it does not establish that any paraphrase proves understanding. Karpicke and Blunt (2011) found retrieval practice outperformed elaborative concept mapping in their science-text experiments, including inference questions. This cautions against treating note or graph production as equivalent to demonstrated retrieval; it is not evidence that linked notes lack value. [Original experiment, author's laboratory](https://learninglab.psych.purdue.edu/downloads/2011/2011_Karpicke_Blunt_Science.pdf)

**Preserving improvement.** Use the resolved notes directory when suggesting links: the protocol currently names `learn/notes/` even though workspace mode uses `notes/`. Clarify that final files include only user-accepted links; preserve the prohibition on rewriting existing note bodies. State that a paraphrase is an observed learner contribution, rather than automatically a transfer demonstration. Keep source verification and user wording separate responsibilities.

**Behavioral check.** Given existing workspace notes, suggestions inspect `notes/`; rejected links remain absent; citations are verified; the agent formats the learner's prose without replacing it.

**Deferred.** Adding a new retrieval or transfer exam before saving notes would change the artifact-generation workflow. Atomicity, wikilinks, and no-index notes are organizational choices, not experimentally established optimal learning formats.

## 9. start-learn

**Relevant evidence.** *How People Learn II* concludes that the usefulness of learning strategies depends on prior knowledge, material, goals, and context. This supports attending to the learner's situation. It does not validate this router's one-question classifier or establish that an inferred baseline measures ability. [Authoritative National Academies report](https://www.nationalacademies.org/read/24783/chapter/2)

**Preserving improvement.** Repair metadata syntax and keep the initial single-question flow. Explicitly load the selected installed workflow through the current client's supported mechanism, state choice and reason, and allow redirection. Keep inferred baseline, self-rating, and demonstrated assessment results distinct in wording. Add the direct lesson-format reference where lessons are generated. Correct the stale summary that calls user confirmation of the next skill the Scenario A exit: ADR 0004 requires automatic selection and dispatch.

**Behavioral check.** Existing code triggers a declared methodology and execution, not a selection menu. From-scratch learning creates the agreed workspace, waits for curriculum approval, and delivers lessons on request. A missing target skill is reported truthfully rather than imitated from memory.

**Deferred.** New diagnostic interviews, mastery-based progression, adaptive routing models, and automatic lesson generation would alter the intentionally simple entry point.

## Implementation boundary

The safest quality pass is to align examples with existing rules, fix paths and invocation assumptions, preserve exceptions beside the rules they qualify, and separate scientific motivation from local editorial choices. Use the skill-creator workflow to make triggers, resources, and completion observable; do not infer pedagogical success from a shorter prompt or passing static validation.

For subsequent evaluation, retain one representative positive scenario per skill plus negative and edge cases. Record the installation, model/application, source availability, actual turns, generated files, and which invariants passed. Behavioral comparisons can establish instruction adherence on those cases. Measuring learning benefit or equivalence across populations requires a different study.
