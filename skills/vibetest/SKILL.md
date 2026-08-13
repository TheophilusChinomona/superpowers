---
name: vibetest
description: Use when asked to vibetest a website, or to run automated multi-agent QA against a live or localhost site to find UI bugs, broken links, accessibility issues, and other functional problems
---

# Vibetest

## Overview

Run automated QA by launching several Browser-Use agents against a URL, each testing a different slice of the page, then consolidate their findings into a severity-ranked bug report.

**Core principle:** scout the page, fan out N agents to test different elements, summarize the reports into high/medium/low-severity findings with specific steps and observed results.

## When to Use

- The user asks to "vibetest" a site, run browser QA, or check a website for bugs/broken links/a11y issues.
- You want automated regression smoke-testing of a just-built (vibe-coded) page, live URL or `localhost`.

**Don't use when:** the task needs a single specific interaction test (drive one browser yourself instead), or when no `GOOGLE_API_KEY` / Gemini access is configured (vibetest's agents run on Gemini).

## Prerequisites

- Python 3.11+.
- `GOOGLE_API_KEY` set in the environment (Gemini 2.0 flash / 1.5 flash). **Not** `BROWSER_USE_API_KEY` — vibetest uses the open-source `browser-use` library with local Playwright browsers, not Browser Use Cloud.
- The `vibetest` package installed, with Playwright Chromium downloaded.
- The vibetest MCP server registered with the harness (Hermes: `hermes mcp`; Claude Code: `claude mcp add vibetest ...`).

## How to Run

vibetest exposes two MCP tools:

1. `start(url, num_agents=3, headless=false)` — spawns the QA swarm and returns a `test_id`.
2. `results(test_id)` — returns the consolidated report with severity breakdown.

### Parameters

| Param | Default | Notes |
|---|---|---|
| `url` | — | Required. `https://…`, `localhost:3000`, etc. |
| `num_agents` | `3` | More agents = broader coverage (capped at 10 concurrent). |
| `headless` | `false` | `true` for no visible browser windows. |

### Flow

1. Call `start` with the target URL and desired agent count; capture the `test_id`.
2. Poll `results(test_id)` until the report is ready.
3. Read the report: `high_severity` / `medium_severity` / `low_severity`, `total_issues`, and per-issue descriptions (element tested + action + observed result).

## Common Mistakes

- **Wrong key** — vibetest reads `GOOGLE_API_KEY` (Gemini); `BROWSER_USE_API_KEY` (cloud) will not work. They are different products.
- **Treating it as Browser Use Cloud** — vibetest drives local Playwright Chromium via the open-source `browser-use` package; it does not use the cloud SDK or API v4.
- **Returning the raw agent dumps** — always use `results()` for the consolidated, deduplicated, severity-classified report rather than the per-agent transcripts.
- **Forgetting Chromium** — `playwright install chromium` must have been run, or every agent errors at launch.
