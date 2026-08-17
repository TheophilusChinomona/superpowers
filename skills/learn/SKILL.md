---
name: learn
description: Use when a verified lesson should become reusable project knowledge.
---

# Learn

Capture only reusable lessons that remain useful beyond the current turn. This workflow shows, searches, adds, reviews, and supersedes Markdown learning notes in Sentio-OS. It does not turn transient progress into durable knowledge and it never replaces repository source of truth.

## When to Use

- A verified recurring pattern, pitfall, preference, architecture decision, or tool behavior should be reusable later.
- A user asks to show, search, add, prune, export, or review project learnings.
- A prior lesson must be corrected or superseded without silently erasing its history.

Do not use this for temporary progress, one-off TODOs, unverified guesses, session summaries, or a transient failure that has not recurred or produced a reusable rule. This skill does not implement code changes.

## Prerequisites

- Check whether `C:\Users\Givemore\Desktop\Sentio-OS` exists. If it is missing, report the missing path and ask before creating or using another vault; do not substitute another vault.
- Identify the project and the source evidence for each lesson.
- Never read, print, or copy credentials or equivalent sensitive material, including secrets, `.env` contents, tokens, private keys, or sensitive logs.
- Repositories remain the source of truth for implementation and current behavior; a learning note is a pointer and interpretation.

## Durable-Learning Gate

Save a lesson only when it is reusable beyond the current turn and supported by observed evidence. Before adding, ask:

1. Is this a recurring or broadly applicable pattern rather than a one-off event?
2. Can the observed evidence be linked without copying sensitive content?
3. Is the application boundary clear, including where the lesson does not apply?
4. Would a future agent act differently because of this note?

If any answer is no, do not create a durable note. Explain why it stays out of the knowledge base.

## Commands

- **Show recent:** list recent notes grouped by category, with source links.
- **Search:** search note titles, lessons, project names, and tags; show matching evidence and scope.
- **Add:** create a note only after the durable-learning gate passes.
- **Prune:** identify stale, contradictory, or unsupported notes and ask before changing them.
- **Export:** format selected notes as Markdown for a requested project document; do not silently append them elsewhere.
- **Stats:** summarize counts by project and category without exposing note contents that contain secrets.

## Procedure

1. **Classify the request.** Determine whether the user wants show, search, add, prune, export, or stats. For an add request, identify the project, date, evidence, proposed lesson, and application boundary. Completion criterion: the operation and scope are explicit.
2. **Check the durable-learning gate.** Reject temporary progress, one-off TODOs, transient failures, and unsupported conclusions. A transient failure becomes a lesson only after recurrence or a verified reusable cause and remedy are established. Completion criterion: the note is either accepted with evidence or explicitly rejected with a reason.
3. **Choose placement.** Project-specific lessons go under `C:\Users\Givemore\Desktop\Sentio-OS\01-Projects\<Project>\`. Cross-project patterns go under `C:\Users\Givemore\Desktop\Sentio-OS\03-Resources\`. Keep the repository path or URL in the source links. Completion criterion: placement matches scope.
4. **Write the Markdown note.** Use the required shape below. Keep it concise, link to repository evidence, and redact secrets rather than paraphrasing sensitive values. Completion criterion: project, date, observed evidence, lesson, application boundary, source links, and status are present.
5. **Review corrections safely.** If a note is stale or contradicted, mark it `Superseded` and link the replacement. Preserve the old note or its history; never silently erase a lesson. Completion criterion: the relationship between old and replacement notes is navigable.
6. **Verify and report.** Re-read the note, confirm links and placement, check for secret material, and report what was added, skipped, superseded, or left unverified. Completion criterion: no unsupported conclusion is presented as durable knowledge.

## Required Note Shape

```markdown
# Lesson: <short reusable title>

- Project: <project or Cross-project>
- Date: <YYYY-MM-DD>
- Status: Active | Superseded
- Category: Pattern | Pitfall | Preference | Architecture | Tool
- Source links: [repository path or URL], [test/issue/decision link]

## Observed evidence
<What was actually observed, with commands, tests, or paths.>

## Lesson
<Reusable rule stated without secret values.>

## Application boundary
<Where this applies, where it does not, and confidence or unknowns.>

## Related history
<Supersedes or is superseded by links; omit only when none exists.>
```

## Safety Boundary

This skill does not automatically perform side effects. Do not automatically commit. Do not automatically push. Do not automatically deploy. Do not automatically open a pull request. Do not automatically install a runtime. Do not automatically mutate production while using it. It may write requested knowledge notes, but it must not edit implementation or production configuration.

## Upstream Source

Normalized from the exact upstream document: https://raw.githubusercontent.com/garrytan/gstack/main/learn/SKILL.md
