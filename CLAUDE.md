# Superpowers Lite — Contributor Guidelines

This fork keeps the reusable Superpowers workflow while intentionally supporting only Claude Code, Codex, and Hermes Agent. The goal is a smaller, clearer plugin with less harness-specific indirection.

## Supported integrations

- Claude Code via `.claude-plugin/`
- Codex App and CLI via `.codex-plugin/`
- Hermes Agent via `.hermes-plugin/`

Do not add or restore integration files for Cursor, Devin, Kimi Code, OpenCode, Pi, Gemini CLI, Antigravity, Factory Droid, GitHub Copilot CLI, Grok Build CLI, or other unsupported harnesses unless the project scope is explicitly changed first.

## Working in this repository

- Read `AGENTS.md`, this file, and the relevant skill before changing code or skills.
- Keep changes focused on one real problem.
- Preserve the shared skills under `skills/` and avoid harness-specific branching in skill content.
- Prefer the smallest implementation that solves the problem.
- Do not add third-party runtime dependencies without explicit approval.
- Do not commit, push, or open a pull request unless explicitly asked.
- Never read, print, or commit secrets such as `.env` files or credentials.

## Skill changes

Skills shape agent behavior and must be treated like code. When modifying a skill:

1. Read the complete skill and its linked references.
2. Follow the repository's skill-authoring and evaluation guidance.
3. Preserve deliberate terminology and behavior-shaping language unless there is evidence for a change.
4. Run the relevant tests or evaluations.
5. Review the complete diff before delivery.

## Verification

Before claiming a change is complete:

- Check `git diff` and `git status`.
- Run targeted tests for the changed integration or skill.
- Validate JSON, YAML, shell, and Python files with the repository's available checks.
- Search for stale references to removed harnesses when removing an integration.
- Report actual command results; do not infer success from code inspection alone.

## Pull requests

If a pull request is requested, read `.github/PULL_REQUEST_TEMPLATE.md` first and complete every section with specific, truthful information. Include the problem, the approach, tests run, and the supported integration scope. Show the complete diff for human review before submission.

Unless the project direction changes, pull requests for this fork should target the branch specified by the fork owner rather than assuming upstream's branch policy.
