---
type: decision
status: approved
created: 2026-08-17
tags:
  - assistant
  - obsidian
  - workflow
---

# Assistant output vault

## Decision

Use `docs/assistant/` as the durable, Obsidian-readable workspace for important assistant outputs in the Superpowers Lite repository.

The folder is intended to be opened directly in Obsidian as a vault. It remains inside the repository so notes can be reviewed, versioned, and shared with the project.

## Structure

- `INDEX.md` — entry point and navigation
- `active/` — evolving investigations and open questions
- `decisions/` — approved choices and conventions
- `research/` — source-backed findings and comparisons
- `archive/` — superseded but still useful notes

## Naming

Durable notes use date-prefixed names:

`YYYY-MM-DD-short-topic-name.md`

## Note contract

Notes use lightweight YAML frontmatter with at least:

- `type`
- `status`
- `created`
- `tags`

Related notes use Obsidian wikilinks such as `[[INDEX]]` and `[[research/topic]]`.

## Consequences

- Important reasoning is no longer trapped in chat history.
- Obsidian can provide navigation and backlinks over the repository notes.
- Formal plans and specifications remain in `docs/superpowers/`; the assistant vault links to them rather than replacing them.
- Temporary experiments remain outside the vault unless explicitly promoted.
