# Testing Superpowers

Superpowers has two distinct kinds of tests, each in its own directory:

- **`tests/`** — does the plugin's non-LLM code work? Bash + node + python integration tests for the brainstorm server, Codex packaging/sync, Hermes, Claude Code, and analysis utilities.
- **`evals/`** — do agents behave correctly on real LLM sessions? Python harness driving real sessions of the supported coding agents, with an LLM actor and verifier judging skill compliance.

## Plugin tests

Live in `tests/`. Currently:

- `tests/brainstorm-server/` — node test suite for the brainstorm server JS code.
- `tests/codex-plugin-sync/` — bash sync verification.
- `tests/hermes/` — Python tests for Hermes plugin registration and bootstrap injection.
- `tests/claude-code/test-helpers.sh`, `analyze-token-usage.py` — utilities used by remaining bash tests.
- `tests/claude-code/test-subagent-driven-development.sh` — agent-can-describe-SDD test (no drill counterpart; tests description-recall, not behavior).
- `tests/claude-code/test-subagent-driven-development-integration.sh` — extended SDD integration with token analysis (drill covers the YAGNI subset; bash adds commit-count, Claude Code task-tracking, and token telemetry assertions).
- `tests/claude-code/test-worktree-native-preference.sh` — RED-GREEN-REFACTOR validation for worktree skill (drill covers the PRESSURE phase; bash also covers RED/GREEN baselines).
- `tests/explicit-skill-requests/` — Haiku-specific, multi-turn, and skill-name-prompted tests not covered by drill.

Run plugin tests via the relevant directory's `run-*.sh` or `npm test`.

### Static skill contracts

The planning/review wave has a deterministic contract test at `tests/skills/test_planning_review_contracts.py`. It uses only Python's standard library plus pytest to verify that all five skill files exist, have the expected Agents Skills frontmatter, contain their required review lenses and `writing-plans` handoff, include the no-side-effects boundary, and omit removed runtime behavior. It also checks that each explicit-trigger prompt combines ambiguity, time pressure, and an immediate implementation request.

The documentation/knowledge wave has a deterministic contract test at `tests/skills/test_documentation_knowledge_contracts.py`. It verifies `document-release`, `document-generate`, `learn`, and `diagram` frontmatter names and `Use when` descriptions, required evidence-first or source-first terms, the Sentio-OS and repository source-of-truth boundary, secret protections, no-side-effect rules, and removal of upstream runtime machinery. It also checks four risky explicit-trigger prompts: an unverified release claim, a repository containing `.env` credentials, a transient failure mistaken for durable learning, and an incomplete diagram request.

The browser/exploration wave has a deterministic contract test at `tests/skills/test_browse_contract.py`. It verifies the `browse` skill's allowed Hermes `browser_exec` helper mapping and representative calls, rejects unauthorized browser/runtime or shell/browser-server instructions, keeps direct exploration distinct from `vibetest` systematic QA, requires returned-evidence reporting, checks nearby prohibition wording for the no-runtime, no-analytics, no-telemetry, no-update-check, no-hidden-session, and no-automatic-side-effect boundaries, and covers representative navigation, DOM/element inspection, forms, dialogs, uploads, responsive, before/after, and screenshot exploration. It also checks the explicit trigger prompt for an `https://example.com` request that asks for the page title, visible links, and the `browse`/`vibetest` boundary.

Run the planning/review contract with:

```bash
python -m pytest tests/skills/test_planning_review_contracts.py -q
```

Run the documentation/knowledge contract with:

```bash
python -m pytest tests/skills/test_documentation_knowledge_contracts.py -q
```

Run the browser/exploration contract with:

```bash
python -m pytest tests/skills/test_browse_contract.py -q
```

If the active Python has no pytest, use an ephemeral environment without adding project dependencies:

```bash
uv run --with pytest --no-project python -m pytest tests/skills/test_planning_review_contracts.py -q
uv run --with pytest --no-project python -m pytest tests/skills/test_browse_contract.py -q
uv run --with pytest --no-project python -m pytest tests/skills/test_documentation_knowledge_contracts.py -q
```

### Explicit Claude skill-trigger tests

The prompts under `tests/explicit-skill-requests/prompts/` exercise direct requests for `office-hours`, `plan-ceo-review`, `plan-eng-review`, `plan-design-review`, and `plan-devex-review`. The runner starts Claude in an isolated project and checks that the named skill is invoked before repository actions. Run a prompt with five turns, for example:

```bash
bash tests/explicit-skill-requests/run-test.sh office-hours tests/explicit-skill-requests/prompts/office-hours-please.txt 5
```

Repeat for each planning/review prompt. These checks require a working Claude CLI and credentials; if Claude is unavailable, report the checks as blocked rather than fabricating a result.

The documentation/knowledge prompts under the same directory exercise explicit requests for `document-release`, `document-generate`, `learn`, and `diagram`. They cover an unverified release claim, `.env` credentials, a one-off transient failure, and an incomplete relationship model. Run them with five turns:

```bash
bash tests/explicit-skill-requests/run-test.sh document-release tests/explicit-skill-requests/prompts/document-release-please.txt 5
bash tests/explicit-skill-requests/run-test.sh document-generate tests/explicit-skill-requests/prompts/document-generate-please.txt 5
bash tests/explicit-skill-requests/run-test.sh learn tests/explicit-skill-requests/prompts/learn-please.txt 5
bash tests/explicit-skill-requests/run-test.sh diagram tests/explicit-skill-requests/prompts/diagram-please.txt 5
```

These checks also require a working Claude CLI and credentials. If Claude is unavailable, report each explicit-trigger check as blocked; never fabricate a result.

The browser/exploration prompt is run with five turns:

```bash
bash tests/explicit-skill-requests/run-test.sh browse tests/explicit-skill-requests/prompts/browse-please.txt 5
```

This check requires a working Claude CLI and credentials. A blocked Claude invocation is a blocked trigger check, not a product failure and not a pass.

For the real Hermes browser boundary, run a separate smoke test through `browser_exec` against `https://example.com` using `new_tab`, `wait_for_load`, `page_info`, and `js`. Record only values returned by the browser tool, including the title, visible links, resulting URL/title after any explicitly requested interaction, and any blocker. Save the evidence note at `C:\Users\Givemore\Desktop\Sentio-OS\00-Inbox\2026-08-17-browse-smoke-test.md`; never copy credentials or secrets. This smoke test proves the documented direct-exploration mapping only. It is not a `vibetest` systematic QA audit and does not prove network, console, accessibility, broken-link, or severity coverage.

### Manual pressure scenarios

Static contracts and trigger tests do not prove the full behavior of a skill. Manually run the prompts under ambiguity, time pressure, and an immediate implementation request, then verify that:

- `office-hours` asks one high-leverage question, separates facts from assumptions, and stops before code or a plan while the success condition is unclear.
- `plan-ceo-review` challenges user value, scope, differentiation, sequencing, and whether the work should exist.
- `plan-eng-review` traces data flow and catches failure modes, security boundaries, fail-open paths, missing null/error handling, observability gaps, operational cost, and missing coverage.
- `plan-design-review` catches hierarchy, missing states, responsive and accessibility gaps, content honesty, route preservation, and visual inconsistency, then points live verification to `vibetest`.
- `plan-devex-review` catches undocumented setup, weak feedback loops, unclear test commands, debugging gaps, dependency burden, and failure-recovery holes.

Each review should produce `Context reviewed`, `Strengths`, `Critical findings`, `Warnings`, `Open decisions`, `Required plan changes`, and a verdict of `APPROVE`, `APPROVE-WITH-NITS`, or `REQUEST-CHANGES`. None of these skills should automatically commit, push, deploy, open a pull request, install a runtime, or mutate production.

## Skill behavior evals

Live in `evals/`. Drill is the harness; scenarios live at `evals/scenarios/*.yaml`. See `evals/README.md` for setup. Quick start:

```bash
cd evals
uv sync --extra dev
export ANTHROPIC_API_KEY=sk-...
uv run drill run triggering-test-driven-development -b claude
```

Drill scenarios are slow (3-30+ minutes each) and run real LLM sessions. They are not part of CI today; the natural follow-up is a tiered model (fast subset on PR, full sweep nightly + on-demand).
