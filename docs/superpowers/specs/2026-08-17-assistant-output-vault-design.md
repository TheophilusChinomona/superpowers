# Assistant output vault design

- **Status:** Approved for implementation
- **Date:** 2026-08-17
- **Scope:** Durable assistant outputs for the Superpowers Lite repository

## Context

Important reasoning currently exists only in chat history. The user wants a filesystem-backed workspace that can be opened in Obsidian so assistant outputs and human review share a durable source of truth.

The repository already contains formal plans and specifications under `docs/superpowers/`. The new workspace should complement those documents rather than replace them.

The assistant vault index is available at [docs/assistant/INDEX.md](../../assistant/INDEX.md).

## Goals

1. Provide one obvious folder for durable assistant outputs.
2. Make the folder easy to open directly as an Obsidian vault.
3. Keep notes searchable, linkable, and reviewable in Git.
4. Separate evolving work, approved decisions, research, and historical material.
5. Keep the convention small enough to use consistently.

## Non-goals

- Do not create a separate database or application.
- Do not move existing formal plans or specifications.
- Do not add an Obsidian plugin dependency.
- Do not automatically save every chat message.
- Do not commit changes without an explicit user request.

## Structure

```text
docs/assistant/
├── INDEX.md
├── active/
├── decisions/
├── research/
└── archive/
```

Each directory has a README explaining its purpose. Git tracks the section guides and notes; empty directories do not need separate placeholders.

## Note format

Durable notes use Markdown with lightweight YAML frontmatter:

```yaml
---
type: research
status: active
created: YYYY-MM-DD
tags:
  - assistant
---
```

Required fields are `type`, `status`, `created`, and `tags`. Notes should use date-prefixed filenames: `YYYY-MM-DD-short-topic-name.md`.

## Linking

`INDEX.md` is the entry point. Related notes use Obsidian wikilinks. Formal plans and specs remain in their existing locations and may be linked from the assistant index.

## Workflow

1. Create or update an `active/` note while a topic is being explored.
2. Record source-backed findings in `research/`.
3. Record approved choices in `decisions/`.
4. Link the durable result from `INDEX.md`.
5. Move superseded drafts to `archive/` when retaining them is useful.
6. Keep temporary experiments outside the vault unless deliberately promoted.

## Verification

The implementation is complete when:

- `docs/assistant/INDEX.md` exists and links to each section.
- Each section has a README.
- The current folder decision is recorded in `decisions/`.
- The external skills comparison is recorded in `research/`.
- The formal specification links to the new workspace.
- Git status shows only the intended documentation files as untracked or modified.
