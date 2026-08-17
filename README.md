# Superpowers Lite

Superpowers Lite is [theochinomona's](https://github.com/TheophilusChinomona) fork of [obra/superpowers](https://github.com/obra/superpowers), trimmed to a focused software-development methodology for coding agents. It keeps the reusable skills and runtime bootstrap while supporting only three integrations:

- Claude Code
- Codex (App and CLI)
- Hermes Agent

This fork intentionally removes integrations for other coding-agent harnesses (Cursor, Devin, Kimi, OpenCode, Gemini CLI, and others) so the repository stays smaller, easier to maintain, and easier to understand. It also adds a set of curated subagents (see [Subagents](#subagents) below) and a couple of extra skills (`vibetest`, `hermes-cron-management`) not present upstream.

Because this is a personal fork, it is **not** published on the official Claude Code or Codex marketplaces — install it by pointing your harness at this repository directly, as described below.

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

Install separately in each coding-agent harness you use. All three methods below point at this fork (`TheophilusChinomona/superpowers-lite`), not upstream `obra/superpowers` or any official marketplace.

### Claude Code

Register this repo as a marketplace, then install from it:

```text
/plugin marketplace add TheophilusChinomona/superpowers-lite
/plugin install superpowers-lite@superpowers-dev
```

`superpowers-dev` is the marketplace name and `superpowers-lite` is the plugin name, both declared in this repo's [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json).

For local development, clone the repo and add the local path instead:

```text
/plugin marketplace add /absolute/path/to/superpowers-lite
/plugin install superpowers-lite@superpowers-dev
```

### Codex CLI

Register this repo as a marketplace, then install from it:

```bash
codex plugin marketplace add TheophilusChinomona/superpowers-lite
codex plugin add superpowers-lite@superpowers-dev
```

`superpowers-dev` is the marketplace name declared in this repo's [`.agents/plugins/marketplace.json`](.agents/plugins/marketplace.json), which is what Codex reads (not `.claude-plugin/marketplace.json`, which is Claude Code's).

### Codex App

The Codex App's plugin browser only lists officially curated plugins, so a personal fork isn't installable through the sidebar UI. Use the Codex CLI commands above instead — the app and CLI share the same plugin config.

### Hermes Agent

Install the plugin directly from this fork:

```bash
hermes plugins install TheophilusChinomona/superpowers-lite --enable
```

Hermes prints a `doesn't contain plugin.yaml, plugin.json, or __init__.py` warning during install — that's a false positive from a shallow root-only check; the plugin's manifest lives under `.hermes-plugin/`, one level down, which is where Hermes' actual plugin loader looks. The install still succeeds (confirm with `hermes plugins list`).

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

Live under `skills/`:

- **Planning and Review:** `brainstorming`, `writing-plans`, `executing-plans`, `office-hours`, `plan-ceo-review`, `plan-eng-review`, `plan-design-review`, `plan-devex-review`
- **Implementation:** `test-driven-development`, `subagent-driven-development`
- **Debugging:** `systematic-debugging`, `verification-before-completion`
- **Collaboration:** `dispatching-parallel-agents`, `requesting-code-review`, `receiving-code-review`
- **Git:** `using-git-worktrees`, `finishing-a-development-branch`
- **Meta:** `using-superpowers`, `writing-skills`, `agency-agent-routing`
- **Documentation and Knowledge:** `document-release`, `document-generate`, `learn`
- **Visual Output:** `diagram` (source-first Mermaid and optional editable Excalidraw output)
- **Browser / Exploration:** `browse` (Hermes-native direct exploration via `browser_exec`; `vibetest` remains the systematic QA skill)
- **Fork additions:** `vibetest` (browser QA swarm), `hermes-cron-management`

Documentation, knowledge, and diagram skills may store concise, cited durable context or editable diagram sources under `C:\Users\Givemore\Desktop\Sentio-OS` when that path exists. If it is missing, they report the missing path and ask rather than substitute another vault. Repositories remain the source of truth for code and current behavior; these skills never read, print, or copy credentials or equivalent sensitive material, including secrets, `.env` contents, tokens, private keys, or sensitive logs.

### Subagents

`agents/` holds curated Claude Code sub-agent definitions not present upstream — role-specific personas (e.g. `backend-architect`, `security-architect`, `code-reviewer`, `test-automation-engineer`, `technical-writer`) you can invoke via the `Agent` tool for focused work outside the core skills workflow.

### Runtime integrations

- `.claude-plugin/` — Claude Code plugin and marketplace metadata for this fork
- `.codex-plugin/` — Codex plugin metadata
- `.hermes-plugin/` — Hermes Agent plugin and bootstrap
- `hooks/` — shared Claude/Codex session-start hook support
- `skills/` — the shared skills library
- `agents/` — curated Claude Code subagents (fork addition)

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
