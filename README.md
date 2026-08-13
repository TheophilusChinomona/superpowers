# Superpowers Lite

Superpowers Lite is a focused software-development methodology for coding agents. It keeps the reusable skills and runtime bootstrap while supporting only three integrations:

- Claude Code
- Codex (App and CLI)
- Hermes Agent

This fork intentionally removes integrations for other coding-agent harnesses so the repository stays smaller, easier to maintain, and easier to understand.

## How it works

When you start building something, the skills guide the agent through a deliberate workflow instead of jumping straight into code:

1. **Brainstorming** refines the idea and records an approved design.
2. **Git worktrees** isolate implementation work and verify a clean baseline.
3. **Writing plans** turns the design into small, executable tasks.
4. **TDD** enforces the RED-GREEN-REFACTOR cycle.
5. **Execution workflows** implement tasks with review and verification.
6. **Finishing a branch** verifies the result and presents the next delivery option.

The bootstrap is loaded automatically by the supported integrations. You do not need to manually invoke the first skill.

## Installation

Install separately in each coding-agent harness you use.

### Claude Code

Install from Anthropic's official marketplace:

```text
/plugin install superpowers@claude-plugins-official
```

Or register and install from the Superpowers marketplace:

```text
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

### Codex App

1. Open **Plugins** in the Codex app sidebar.
2. Find **Superpowers** in the Coding section.
3. Click **+** and follow the installation prompts.

### Codex CLI

Open the plugin interface:

```text
/plugins
```

Search for `superpowers`, then select **Install Plugin**.

### Hermes Agent

Install the plugin from this repository:

```bash
hermes plugins install obra/superpowers --enable
```

Restart active Hermes sessions after installing. If a long session compacts before the bootstrap is reloaded, start a fresh session.

## Basic workflow

The core skills are designed to work together:

1. `brainstorming`
2. `using-git-worktrees`
3. `writing-plans`
4. `subagent-driven-development` or `executing-plans`
5. `test-driven-development`
6. `requesting-code-review`
7. `finishing-a-development-branch`

Use the workflow that fits the task. The skills are guidance for disciplined development, not a requirement to use every stage for every change.

## What's inside

### Skills

- **Planning:** `brainstorming`, `writing-plans`, `executing-plans`
- **Implementation:** `test-driven-development`, `subagent-driven-development`
- **Debugging:** `systematic-debugging`, `verification-before-completion`
- **Collaboration:** `dispatching-parallel-agents`, `requesting-code-review`, `receiving-code-review`
- **Git:** `using-git-worktrees`, `finishing-a-development-branch`
- **Meta:** `using-superpowers`, `writing-skills`

### Runtime integrations

- `.claude-plugin/` — Claude Code plugin metadata
- `.codex-plugin/` — Codex plugin metadata
- `.hermes-plugin/` — Hermes Agent plugin and bootstrap
- `hooks/` — shared Claude/Codex session-start hook support
- `skills/` — the shared skills library

## Philosophy

- Test-driven development
- Systematic investigation over guesswork
- Simple designs and minimal complexity
- Evidence before claims
- Reusable, harness-neutral skills

## Testing

Plugin-infrastructure tests live under `tests/`. Run the relevant test suite for the integration you changed. Skill-behavior evaluations, when available, live under `evals/`.

For more details, see [`docs/testing.md`](docs/testing.md).

## Contributing to this fork

Keep changes focused and preserve the small supported-integration surface. Before submitting a change:

1. Read [`CLAUDE.md`](CLAUDE.md) and [`AGENTS.md`](AGENTS.md).
2. Describe the real problem the change solves.
3. Keep unrelated harness integrations and dependencies out of core.
4. Run targeted tests and report the results.
5. Review the complete diff before committing or opening a pull request.

## License

MIT License — see [`LICENSE`](LICENSE).
