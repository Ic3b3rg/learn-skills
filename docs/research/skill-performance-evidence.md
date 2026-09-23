# Evidence about agent-skill performance

Retrieved 2026-09-23. This supplements the pedagogical research: evidence that retrieval helps learners does not establish that a particular Markdown prompt improves an agent. This is a targeted review of named primary sources, not a systematic review of every publication.

## Official OpenAI guidance

OpenAI's January 2026 skill-evaluation article recommends measurable outcomes, process adherence, style and efficiency checks, with captured trajectories and artifacts. It includes positive, implicit and negative activation cases. This supports maintaining a small replayable test set, rather than treating YAML validation or reading instructions as an execution benchmark. [Official article](https://developers.openai.com/blog/eval-skills)

The September 11, 2026 authoring article recommends short, discriminating descriptions and conditional resource loading, and warns that elaborate procedures can overconstrain stronger models. It explicitly discusses differences between models. This is model-sensitive vendor guidance, not a universal instruction to remove the pedagogical constraints that define this product. [Official article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)

The evaluation guide recommends task-specific data, human-calibrated grading, edge cases and continued measurement. Its explanation of variability is incompatible with claiming guaranteed perfect behavior from a finite test suite. [Official evaluation guide](https://developers.openai.com/api/docs/guides/evaluation-best-practices)

## Empirical studies

These are academic preprints in the inspected arXiv records. No peer-reviewed publication status was established during this audit. Full-text methods and limitations were consulted; the numerical results below belong to each stated setup, not to learn-skills.

| Primary source and version | Finding relevant to authoring | Limit on the inference |
| --- | --- | --- |
| [SkillsBench v4, June 14, 2026](https://arxiv.org/html/2602.12670v4) | Paired evaluation on 87 tasks reports an average gain from 33.9% to 50.5%; focused skill packages do better than exhaustive ones in the authors' analysis. | Terminal/container tasks, selected models and harnesses. The paper acknowledges context-length confounding and incomplete ecological validity. This is not evidence for the same gain in tutoring. |
| [SWE-Skills-Bench v1, March 16, 2026](https://arxiv.org/html/2603.15401v1) | Among 49 skills over 565 task instances, 39 show no pass-rate improvement; average success changes from 89.8% to 91.0%, with token overhead and some regressions. | Its experimental setup uses Claude Code with Haiku 4.5. A domain-specific software benchmark cannot establish all-provider behavior or learning outcomes. |
| [Agent Skills Can Be Harmful v1, August 12, 2026](https://arxiv.org/html/2608.11888v1) | Differential analysis identifies 307 functional or efficiency failures; excessive verification and heavy implementation procedures are important categories. | Attribution includes manual judgment and the data come from two benchmarks. This warns against indiscriminate procedural additions; it does not show that this repository's citation discipline should be removed. |
| [Signal or Noise? v1, August 24, 2026](https://arxiv.org/html/2608.23067v1) | Web-development experiments include length-matched controls and component ablations; effects differ by model, and average functional performance declines in the tested conditions. | Seed variation is material; the benchmark excludes human interventions and does not measure every quality dimension, including visual fidelity. Its anti-pattern findings should not become a universal writing prescription. |

Version discipline matters: the current SkillsBench paper differs from older summaries using 86 tasks and a 16.2-point gain. Do not mix results from different revisions. The v4 table above follows its current abstract and full text. [Version history](https://arxiv.org/abs/2602.12670)

## Application to this repository

The following are our deductions, not measured outcomes:

1. Keep the learner-first constraints because they define the requested product; assess how reliably each model follows them instead of deleting them to chase generic coding throughput.
2. Evaluate discovery separately from execution. An explicitly injected skill cannot demonstrate correct automatic selection.
3. Compare the original and revised skills on identical source fixtures, prompts and model settings; include a no-skill control when measuring the benefit of the skill itself.
4. Preserve raw transcripts, tool calls, written artifacts, installed-resource hashes, model/application versions, time and token costs. Repeat runs to expose variability.
5. Use human judgment for whether a hint gives away an answer or a question tests transfer. Simple text matching cannot establish these properties.
6. Separate adherence and learning benefit. Successful agent execution is not a controlled study of retention or transfer in human learners.

## Remaining confidence gap

Current evidence is strongest for parsing/resource repairs, weaker for instruction-following improvements, and insufficient to establish comparative model performance or educational efficacy. The previous independent checks were instruction traces with simulated requests, not recorded full client runs. Neither the repository's validators nor the cited literature fills that gap.

For an initial evaluation dataset, use one ordinary request, one boundary/non-trigger request, and one failure/exception case per skill. This suggested 27-case starting point is a project testing choice, not a scientifically sufficient sample size. Expand it using observed failures; do not translate a perfect result on that set into a claim of 100% reliability.
