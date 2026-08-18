# Archived Plans and Specifications

This directory contains completed plan/spec pairs that passed the SDD/TDD Plan/Spec Completion Gate.

- `docs/superpowers/archive/plans/` — archived implementation plans from `docs/superpowers/plans/`
- `docs/superpowers/archive/specs/` — archived specifications from `docs/superpowers/specs/`

## Archive policy

A plan and its linked spec are moved here only after verified completion. The final verification record stays in the plan and records the commands, observed results, spec coverage, unresolved findings, and any accepted environmental blockers. Archive moves use `git mv` and preserve the original filenames.

Do not archive documents with unresolved Critical or Important findings, unrecorded blockers, or unchecked plan/spec requirements. The repository remains the source of truth; update repository and vault links when a pair is archived.
