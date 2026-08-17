---
name: document-release
description: Use when a shipped change needs evidence-based documentation updates.
---

# Document Release

Use this workflow after a verified change has shipped or is ready for release documentation. It audits the repository's documentation against the actual diff, tests, routes, and public behavior, then writes concise project context. Repository files remain the source of truth; Sentio-OS is a linked knowledge layer, not a copy of the code.

## When to Use

- A user asks to update, sync, or document what changed after a release.
- A completed change may have stale README, architecture, contribution, API, route, or changelog documentation.
- A release needs a concise, evidence-linked project note in Sentio-OS.

Do not use this to invent release notes from an unverified claim, replace code review, or generate missing documentation without first auditing the shipped surface. Use `document-generate` for substantial new documentation discovered as a gap.

## Prerequisites

- Identify the repository and the change or release being documented.
- Confirm the relevant diff, test output, changed routes or APIs, and existing docs can be inspected.
- Check whether `C:\Users\Givemore\Desktop\Sentio-OS` exists. If it is missing, report the missing path and ask before creating or using another vault; do not substitute another vault.
- Never read, print, or copy credentials or equivalent sensitive material, including secrets, `.env` contents, tokens, private keys, or sensitive logs.

## Evidence Contract

Every factual claim must cite one of:

- a repository-relative file path and relevant symbol or heading;
- a command and its observed output;
- a verified test result;
- a source URL supplied or inspected during the task.

Label claims as **Verified**, **Inferred**, or **Unverified**. If a test, route, diff, or source cannot be checked, write `Unverified: ...` and explain what is missing. Never turn an assumption into a release fact.

## Procedure

1. **Establish the scope.** Read the complete relevant README, architecture, contributing, release, and API documentation before editing. Inspect repository status, the target diff, changed-file list, commits, and the base branch when available. Completion criterion: the files, commits, and public surfaces under review are named.
2. **Build the evidence map.** Inspect `git diff`, run the repository's documented tests or inspect fresh test output, and review changed routes, APIs, commands, configuration, public skills, and user-visible behavior. Record what is verified, inferred, and unavailable. Completion criterion: every release claim has an evidence source or an explicit unverified label.
3. **Build a Diataxis coverage map.** For each changed public surface, record whether reference, how-to, tutorial, and explanation coverage exists. Reference describes facts and options; how-to describes a task; tutorial teaches a newcomer; explanation records why. Flag zero-coverage items and suggest `document-generate`; do not silently generate a missing page from the coverage map.
4. **Check diagram drift.** If documentation contains Mermaid or text diagrams, compare their entities and flows with changed modules, routes, and dependencies. Flag renamed, moved, split, or removed entities. Do not rewrite a diagram without evidence for the intended shape.
5. **Apply only safe documentation edits.** Correct factual paths, counts, examples, links, lists, and behavior that the evidence proves. Ask before narrative or philosophy changes, security-sensitive wording, large rewrites, new TODOs, or version bumps. Read a file completely before editing it. Preserve the content and history of changelog entries; polish wording only and never replace the file.
6. **Write project context.** When Sentio-OS is available, write a date-prefixed Markdown note under `Sentio-OS/01-Projects/<Project>/`. Keep it concise: summary, verified evidence, unverified items, user impact, repository links, and follow-up documentation gaps. Link to repository paths instead of copying the entire diff. Do not create a different vault when the configured path is absent.
7. **Verify the result.** Re-read every modified documentation file, verify every relative path and Markdown link, rerun applicable tests, and check that the note contains no secret material. Report changed files and evidence. Completion criterion: each modified file is accounted for and all remaining uncertainty is visible.

## Release Note Shape

```markdown
# Release context: <project> — <YYYY-MM-DD>

## Summary
- <user-visible change> [Verified: repo/path or command]

## Evidence
- Verified: <test or command output, with path/link>
- Inferred: <interpretation, with supporting evidence>
- Unverified: <claim not checked and why>

## Documentation coverage
- Reference: <path or gap>
- How-to: <path or gap>
- Tutorial: <path or gap>
- Explanation: <path or gap>

## Follow-up
- <smallest next documentation action>
```

## Safety Boundary

This skill does not automatically perform side effects. Do not automatically commit. Do not automatically push. Do not automatically deploy. Do not automatically open a pull request. Do not automatically install a runtime. Do not automatically mutate production while using it. It may inspect and edit documentation when requested, but it must not apply code or production changes.

## Upstream Source

Normalized from the exact upstream document: https://raw.githubusercontent.com/garrytan/gstack/main/document-release/SKILL.md
