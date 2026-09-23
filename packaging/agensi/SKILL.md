---
name: learn-skills
description: "Guides learning from code or a new topic through explanation, recall, analogies, questions, exercises, notes, flashcards, and assessment. Use when the user wants to understand code, practise a concept, check learning, or start a learning workspace."
---

# Learn Skills

Speak in the user's language. This is one self-contained skill with nine internal workflows, not a plugin requiring other installed skills.

## Choose and load a workflow

If the user names a workflow, read its linked file and follow it. Otherwise read `start-learn`; ask what they want to learn only if the request does not already say. Declare the chosen approach briefly and proceed, except in questions-only mode: start with its first question and omit a declarative announcement. The user may redirect.

| Goal | Workflow to read |
| --- | --- |
| Choose an approach or learn from scratch | [start-learn](references/start-learn.md) |
| Check the user's explanation of code or a concept | [explain-and-check](references/explain-and-check.md) |
| Test recall from memory | [quiz-me](references/quiz-me.md) |
| Connect new concepts to prior knowledge | [connect-to-what-you-know](references/connect-to-what-you-know.md) |
| Reason through questions only | [ask-me-questions](references/ask-me-questions.md) |
| Create and verify practical exercises | [learn-by-doing](references/learn-by-doing.md) |
| Capture ideas in the user's words | [linked-notes](references/linked-notes.md) |
| Create reusable recall cards | [flashcards](references/flashcards.md) |
| Assess demonstrated understanding and gaps | [assess](references/assess.md) |

Read [SOURCES.md](references/SOURCES.md) before source verification. Each workflow includes its own format and protocol references as sections; read the relevant sections when instructed. Do not load unrelated workflows.

## Internal routing

A workflow's mention of another skill means reading that workflow from the table above and continuing in this session. No separate installation, slash command, shell command, or subagent is required. Examples written as `learn-skills: quiz-me <topic>` describe a user request to this skill, not executable commands.

When `start-learn` selects a Scenario A workflow, read and run it immediately. For Scenario B, preserve workspace-path selection, mission confirmation, curriculum approval, and user-requested lessons. Suggest a practice workflow without starting it until requested. When a user accepts a suggested follow-up, load that workflow rather than restarting the interview.

Resolve instruction resources relative to this installed skill directory, even after changing the working directory. Resolve generated learning files relative to the user's project or chosen workspace. Never write learner output into the installed skill directory. If a packaged reference is inaccessible, identify it and request access; do not invent the workflow.

## Preserve the learning contract

Follow the selected workflow's attempt-before-feedback gates, source checks, retry rules, output paths, and stopping conditions. Recall and assessment wait for source-closed confirmation. Exercise solutions remain folded. Workspace detection uses `CURRICULUM.md` in the current working directory. A generated lesson is not evidence of mastery. Assessment uses the existing discrete levels and gap list, never a percentage score. Do not add review scheduling.
