---
name: document-generate
description: Use when a feature, module, or project needs grounded documentation.
---

# Document Generate

Research the whole source surface before writing the parts. This workflow produces structured documentation for a feature, module, or project using the Diataxis distinction between tutorial, how-to, reference, and explanation. Documentation must describe observed repository behavior accurately, call out inference, and never expose secrets.

## When to Use

- A user asks to generate, write, or explain documentation for a feature, module, command, API, or project.
- A release audit identifies a documentation gap.
- Existing docs do not explain public entry points, dependencies, configuration, examples, or failure behavior.

Do not use this to document credentials, private configuration, sensitive logs, or files that cannot be inspected safely. Do not replace repository source of truth with a generated note.

## Prerequisites

- Identify the target feature, module, repository, or coverage-map entities.
- Identify the intended audience and output location. Follow existing `docs/` and documentation-framework conventions when they exist.
- Check whether `C:\Users\Givemore\Desktop\Sentio-OS` exists before writing durable project context. If it is missing, report the missing path and ask before creating or using another vault; do not substitute another vault.
- Treat repositories as the source of truth for code and behavior.

## Research and Security Boundary

Inventory names and metadata first, then inspect only safe source files. Never read, print, or copy credentials or equivalent sensitive material, including secrets, `.env` files, tokens, private keys, generated secrets, and sensitive logs. Exclude those materials from examples, snippets, and notes. Do not copy a secret to prove that a configuration works. If safe documentation is impossible, report the boundary and the missing non-sensitive evidence.

Separate every statement into:

- **Observed fact:** directly supported by inspected code, tests, configuration examples, or docs.
- **Inference:** a reasoned interpretation that has supporting evidence but is not stated directly.
- **Unknown:** information not available or not verified.

## Procedure

1. **Define scope and audience.** Confirm whether the target is a feature, module, file, skill, or whole project. Identify reader experience, goal, and the smallest useful document set. If more than five new documents are needed, ask before creating them. Completion criterion: target, audience, output format, and non-goals are explicit.
2. **Inventory the source.** Use repository file inventory tools to map relevant directories while excluding build output, dependency trees, generated files, and secret-bearing paths. Record filenames and roles without copying sensitive contents. Completion criterion: the inventory names safe source, tests, docs, configuration examples, and entry points.
3. **Trace entry points and dependencies.** Read README and contributor guidance, project metadata, public entry files, target implementations end-to-end, tests, related modules, configuration examples, and relevant comments. Trace public commands, functions, options, routes, API endpoints, dependencies, dependents, edge cases, and design decisions. Completion criterion: the concept map identifies purpose, public surface, dependencies, dependents, edge cases, and design rationale.
4. **Partition the documentation.** Choose only the Diataxis quadrants the audience needs:
   - Tutorial: a newcomer reaches a working result in three steps or fewer.
   - How-to: an actionable task with prerequisites, exact steps, verification, and troubleshooting.
   - Reference: complete factual interfaces, types, defaults, constraints, and real examples.
   - Explanation: the problem, approach, trade-offs, and alternatives, without duplicating reference material.
   Completion criterion: each proposed document has one clear quadrant and purpose.
5. **Write from evidence.** Write reference material first, then explanation, how-to, and tutorial content as applicable. Use exact paths and commands only when verified. Preserve observed facts, label inference, and state unknowns instead of guessing. Completion criterion: every public claim and example links to its evidence or is marked unverified.
6. **Link and discover.** Add concise entry-point links in README or the existing docs index. Link reference to how-to, how-to to reference, and tutorials to both when those documents exist. Verify every path and Markdown link with repository inspection tools. Completion criterion: every new document is reachable from the documented entry point and no link points to a missing target.
7. **Review for safety and quality.** Re-read generated docs against implementation and tests. Check public-surface completeness, runnable examples, tutorial time to first result, troubleshooting, trade-offs, stale names, jargon, and secret boundaries. If Sentio-OS context is needed, write only a concise, evidence-linked note under `Sentio-OS/01-Projects/<Project>/`; do not duplicate the repository or copy the entire diff.
8. **Report.** List generated and updated paths, quadrant coverage, evidence checked, unknowns, and any blocked or unverified checks. Explain what was intentionally excluded for security or scope. Completion criterion: the report distinguishes generated facts from inference and names every remaining gap.

## Document Templates

### Reference

```markdown
# <Entity>

<What it is and when to use it.>

## API / Interface
<Verified public functions, commands, routes, options, types, defaults, and constraints.>

## Examples
<Examples that were checked against the repository.>

## Related
<Verified links to how-to, tutorial, or explanation documents.>
```

### How-to

```markdown
# How to <specific task>

<Expected outcome.>

## Prerequisites
## Steps
1. <Exact action>
2. <Exact action>

## Verification
<Command, test, or observable result.>

## Troubleshooting
<Observed failure modes and fixes.>
```

### Explanation

```markdown
# <Concept or design decision>
## The problem
## The approach
## Trade-offs
## Alternatives considered
```

### Tutorial

```markdown
# <What the reader will build>
## What you'll need
## Step 1
## Step 2
## Step 3
## What you built
```

## Safety Boundary

This skill does not automatically perform side effects. Do not automatically commit. Do not automatically push. Do not automatically deploy. Do not automatically open a pull request. Do not automatically install a runtime. Do not automatically mutate production while using it. It may write requested documentation, but it must not edit implementation or production configuration by default.

## Upstream Source

Normalized from the exact upstream document: https://raw.githubusercontent.com/garrytan/gstack/main/document-generate/SKILL.md
