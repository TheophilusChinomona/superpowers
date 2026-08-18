# Hermes-Native Browse Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans for small and medium plans, or superpowers:subagent-driven-development when the plan is large enough that per-task subagents and review repay their cost. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a lightweight `browse` skill that uses Hermes' existing `browser_exec` tool for direct web exploration while keeping `vibetest` as the systematic QA audit workflow.

**Architecture:** `skills/browse/SKILL.md` documents a text-first browser procedure using `new_tab`, `goto_url`, `wait_for_load`, `page_info`, `js`, `cdp`, and `capture_screenshot` through `browser_exec`. It explicitly avoids Bun, Playwright, gstack servers, telemetry, update checks, hidden sessions, and automatic side effects. Its output is an exploration record, not a severity-ranked QA report.

**Tech Stack:** Markdown, Agents Skills frontmatter, Hermes `browser_exec`, Python contract tests, explicit Claude skill-trigger tests.

**Spec:** `docs/superpowers/archive/specs/2026-08-17-first-wave-skills-integration.md`

## Global Constraints

- Use Hermes-native `browser_exec`; do not add Bun, Playwright, Chromium installers, or a gstack browser runtime.
- Keep `browse` distinct from `vibetest`: exploration versus systematic QA.
- Read page state and DOM text first; screenshots are supplementary evidence.
- Never claim a page state, network result, or screenshot that was not returned by the browser tool.
- Do not log in with guessed credentials or copy secrets from pages into Sentio-OS.
- No automatic commits, pushes, deploys, PRs, runtime installs, or production mutations.

---

### Task 1: Write the red contract test and browser prompt

**Files:**
- Create: `tests/skills/test_browse_contract.py`
- Create: `tests/explicit-skill-requests/prompts/browse-please.txt`

**Interfaces:**
- Produces the contract that the skill is Hermes-native and does not import gstack runtime behavior.

- [ ] **Step 1: Write the failing static test**

```python
from pathlib import Path

ROOT = Path(__file__).parents[2]


def test_browse_is_hermes_native_and_distinct_from_vibetest():
    path = ROOT / "skills" / "browse" / "SKILL.md"
    assert path.is_file()
    text = path.read_text(encoding="utf-8").lower()
    for term in ("browser_exec", "page_info", "new_tab", "js", "cdp"):
        assert term in text
    assert "vibetest" in text
    assert "playwright" in text and "do not" in text
    assert "bun" in text and "do not" in text
    assert "telemetry" in text and "do not" in text
```

- [ ] **Step 2: Run the red test**

Run: `python -m pytest tests/skills/test_browse_contract.py -q`

Expected: FAIL because `skills/browse/SKILL.md` does not exist.

- [ ] **Step 3: Write the explicit prompt**

The prompt must ask the agent to browse `https://example.com`, report the page title and visible links, and explain the difference between `browse` and `vibetest`.

- [ ] **Step 4: Run the baseline without the skill**

Use a clean agent session and record whether it invents browser APIs, installs Playwright, or reports page state without a browser result.

---

### Task 2: Write the Hermes-native skill contract

**Files:**
- Create: `skills/browse/SKILL.md`

**Interfaces:**
- Consumes: a URL, local/LAN URL, or a requested direct browser interaction.
- Produces: a concise exploration report containing URL, observed page state, actions, results, evidence, and blockers.

- [ ] **Step 1: Normalize the upstream source**

Read `https://raw.githubusercontent.com/garrytan/gstack/main/browse/SKILL.md`. Keep its direct interaction coverage—navigation, elements, forms, dialogs, uploads, responsive checks, screenshots, and before/after state—but remove its preamble, gstack config, analytics, telemetry, session files, update checks, and shell runtime.

- [ ] **Step 2: Define the Hermes tool mapping**

The skill must use:

- `new_tab(url)` for first navigation
- `goto_url(url)` for an existing tab
- `wait_for_load()` after navigation
- `page_info()` for page state
- `js(expr)` for DOM extraction and interaction when appropriate
- `cdp(...)` for DevTools-level inspection
- `capture_screenshot()` when visual evidence is useful

State that browser screenshots are automatically attached by the tool and must not be sent to another vision tool.

- [ ] **Step 3: Define the output contract**

Require:

- Target URL
- Page title and key visible state
- Interactive elements inspected
- Actions taken and observed results
- Failed or blocked interactions
- Evidence paths or returned browser data
- Clear distinction between “not tested,” “blocked,” and “passed”

- [ ] **Step 4: Define the vibetest boundary**

Use `browse` for direct exploration or a narrow flow. Use `vibetest` when the user asks for systematic QA, broken-link discovery, network/console audit, accessibility audit, or severity-ranked findings.

- [ ] **Step 5: Run the explicit trigger test**

Run: `bash tests/explicit-skill-requests/run-test.sh browse tests/explicit-skill-requests/prompts/browse-please.txt 5`

Expected: PASS and no runtime installation before skill invocation.

---

### Task 3: Run a real browser smoke test

**Files:**
- No repository file changes.
- Evidence: save the returned report under `C:\Users\Givemore\Desktop\Sentio-OS\00-Inbox\2026-08-17-browse-smoke-test.md`.

**Interfaces:**
- Consumes: the new `browse` skill and Hermes `browser_exec`.
- Produces: verified evidence that the documented tool mapping works.

- [ ] **Step 1: Open the public test page**

Use `browser_exec` with `new_tab("https://example.com")`, then `wait_for_load()` and `page_info()`.

- [ ] **Step 2: Extract the visible contract**

Use `js()` to read `document.title`, the main heading, and all visible link labels/hrefs. Record only returned values.

- [ ] **Step 3: Test one interaction**

Follow the page's visible link, wait for load, and record the resulting URL and title. If the link is unavailable or the page is blocked, record the blocker instead of fabricating a pass.

- [ ] **Step 4: Save the evidence note**

Write the URL, timestamp, actions, returned observations, and any blocker to the specified Sentio-OS Inbox note. Do not store credentials or unrelated page content.

---

### Task 4: Turn the red test green and document the boundary

**Files:**
- Modify: `tests/skills/test_browse_contract.py`
- Modify: `README.md:91-101`
- Modify: `docs/testing.md:8-21`

**Interfaces:**
- Consumes: `skills/browse/SKILL.md` and the smoke-test evidence.
- Produces: deterministic contract coverage and discoverable documentation.

- [ ] **Step 1: Run the static contract test**

Run: `python -m pytest tests/skills/test_browse_contract.py -q`

Expected: PASS.

- [ ] **Step 2: Document the skill categories**

Add `browse` under browser/exploration in the README and state that `vibetest` remains the systematic QA skill.

- [ ] **Step 3: Run targeted verification**

Run: `python -m pytest tests/hermes -q && git diff --check && git diff -- skills/browse tests/skills/test_browse_contract.py tests/explicit-skill-requests/prompts/browse-please.txt README.md docs/testing.md`

Expected: Hermes tests pass, no whitespace errors, and no Bun/Playwright dependency files appear.

- [ ] **Step 4: Stop for review before any commit or push**

Present the smoke-test evidence and the contract-test output. Do not commit or push automatically.

## Verification Record

- **Date:** 2026-08-18
- **Status:** Verified; ready to archive.
- **Plan/spec coverage:** Hermes-native `browse`, browser helper mapping, direct-exploration/vibetest boundary, returned-evidence contract, smoke evidence, static contracts, trigger prompt, README/testing documentation, and review findings were implemented and reviewed.
- **Observed verification:** `uv run --with pytest --no-project python -m pytest tests/skills -q` — 8 passed; `git diff --check` — passed; Hermes — 18 passed and 1 known unrelated bootstrap assertion failure; browser smoke against `https://example.com` succeeded with returned evidence saved in Sentio-OS.
- **Blocked verification:** Claude explicit-trigger check remains blocked because the account is out of usage; it is not represented as a pass.
- **Review status:** Task review, fix review, final whole-branch review, and final scoped re-review found no unresolved Critical or Important findings.
- **Archive decision:** Move this plan to `docs/superpowers/archive/plans/` and the linked first-wave spec to `docs/superpowers/archive/specs/` with `git mv`, then verify repository and vault links.
