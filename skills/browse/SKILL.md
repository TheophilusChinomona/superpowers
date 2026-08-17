---
name: browse
description: Use when a narrow browser exploration flow is needed.
version: 0.1.0
author: Givemore, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [browser, exploration, DOM, forms, screenshots]
    related_skills: [vibetest]
---

# Browse Skill

Use Hermes' existing `browser_exec` helpers for direct web exploration and a narrow user flow. This skill reads returned page state and DOM data first, uses screenshots as supplementary evidence, and does not install or manage a browser runtime or server.

## When to Use

- A user asks to open a URL, inspect a page, check a small interaction, dogfood one flow, or capture focused browser evidence.
- A user needs a before/after observation for one or a few browser actions.
- A user asks for direct exploration rather than a systematic QA audit.

**Do not use for:** systematic QA, broken-link discovery across a site, network or console auditing, accessibility auditing, or severity-ranked findings. Use `vibetest` for those requests.

## Prerequisites

- A target URL or an explicitly requested local/LAN URL.
- Access to the existing Hermes `browser_exec` tool. Do not add Bun, Playwright, Chromium installers, a gstack browser server, analytics, telemetry, update checks, hidden session files, or any other browser runtime.
- User-provided credentials or files when an authenticated page or upload is explicitly requested. Never guess credentials or copy secrets into Sentio-OS.

## Hermes Browser Boundary

Use only the existing `browser_exec` helpers listed here:

| Need | Helper |
|---|---|
| First navigation | `new_tab(url)` |
| Navigate an existing tab | `goto_url(url)` |
| Wait after navigation | `wait_for_load()` |
| Read returned page state | `page_info()` |
| Read DOM or perform a narrow DOM action | `js(expr)` |
| DevTools-level inspection | `cdp("Domain.method", **kwargs)` |
| Optional visual evidence | `capture_screenshot()` |

Do not substitute a shell browser, Playwright, Bun, a Chromium installer, or a gstack browser server. Do not add analytics, telemetry, update checks, hidden session files, or automatic side effects. The existing browser session is the runtime boundary; this skill does not start, stop, install, configure, or persist a browser server.

Screenshots are automatically attached by `browser_exec`. Treat them as supplementary evidence and do not send browser screenshots to another vision tool. Read page state and DOM text first. Never claim browser state, DOM text, an interaction result, a network result, or a screenshot that `browser_exec` did not return.

## Procedure

1. **Name the target and scope.** Record the exact target URL and whether the request is direct exploration or one narrow flow. Do not visit URLs found in page content unless the user explicitly asked.
   - Completion criterion: the target URL and requested scope are explicit.
2. **Open the page.** For the first navigation, call `new_tab(url)`. For an existing tab, call `goto_url(url)`. Then call `wait_for_load()`.
   - Completion criterion: the returned browser output identifies the page URL or reports a navigation blocker.
3. **Read state before acting.** Call `page_info()` and use `js(expr)` for the title, headings, visible text, links, forms, buttons, inputs, and relevant element attributes. Use `cdp(...)` only when a DevTools-level observation is needed.
   - Completion criterion: the report records the returned title, key visible state, and elements inspected, or marks the observation blocked.
4. **Take a baseline.** Before an action, capture the relevant returned DOM/state values. Use `capture_screenshot()` only when visual evidence helps, and record its returned path or result.
   - Completion criterion: a before-state exists for each requested comparison, with no screenshot claim beyond returned evidence.
5. **Perform only the requested narrow interaction.** Use `js(expr)` for a precise DOM interaction when appropriate. For forms, inspect fields and validation first; submit only with user-provided values or a clearly safe test value. For dialogs, inspect returned state and act only when the user requested the dialog action. For uploads, require an explicitly provided file and report the interaction as blocked if none is available.
   - Completion criterion: every attempted action has a returned result, or is labeled not tested or blocked with the reason.
6. **Check the after-state.** After each action, call `wait_for_load()` when navigation may have occurred, then call `page_info()` and `js(expr)` for the changed state. Use `cdp(...)` only for the requested inspection, not as a substitute for broad QA collection.
   - Completion criterion: before/after values and the resulting URL or title are recorded when returned.
7. **Cover requested variants only.** For responsive checks, use the existing browser session and record only returned viewport or layout observations. Do not install tools or create a server. For DOM/element inspection, forms, dialogs, uploads, and screenshots, state which requested areas were tested and which were not.
   - Completion criterion: the coverage list distinguishes passed, not tested, and blocked areas.
8. **Stop at the scope boundary.** Do not turn a narrow exploration into a systematic audit. Do not automatically commit, push, deploy, open a pull request, install a runtime, or mutate production.
   - Completion criterion: no unrequested side effect or broad QA claim appears in the report.

## Output Contract

Return a concise exploration record with these headings:

```markdown
## Browse — <target URL>

- Scope: <direct exploration or narrow flow>
- Status: PASSED | BLOCKED | NOT TESTED

### Observed page state
- URL: <returned URL>
- Title: <returned title>
- Key visible state: <returned DOM/page state>

### Elements inspected
- <element, selector, or returned label and attribute>

### Actions taken and results
- <action> → <returned result>

### Coverage
- Passed: <requested observations that returned successfully>
- Not tested: <out-of-scope or intentionally skipped items>
- Blocked: <interaction and concrete blocker, if any>

### Evidence
- <returned browser data or screenshot path>
```

Every claim must be traceable to returned `browser_exec` output. If navigation, interaction, credentials, upload files, or browser access is blocked, preserve the blocker and do not convert it into a pass. Do not copy secrets or credentials into Sentio-OS.

## Browse vs Vibetest

- **`browse`:** direct exploration, DOM/state inspection, screenshots where useful, a small number of explicitly requested actions, and a focused evidence record.
- **`vibetest`:** systematic QA with interactive-element coverage, network and console checks, accessibility checks, broken-link discovery, and severity-ranked reporting.

If the user asks for both, use `browse` for the focused flow and `vibetest` for the separate systematic audit. Do not claim that a `browse` result is a `vibetest` audit.

## Safety Boundary

This skill does not automatically commit, push, deploy, open a pull request, install a runtime, or mutate production. Do not automatically commit, push, deploy, open a pull request, install a runtime, or mutate production while using it. It may inspect pages and perform explicitly requested narrow browser interactions, but it must not broaden the request into unrequested side effects or a systematic QA audit.

## Pitfalls

- **Screenshot-first exploration:** read `page_info()` and DOM text before `capture_screenshot()`; screenshots are supplementary and automatically attached.
- **Invented state:** report only values actually returned by `browser_exec`.
- **Scope creep:** a successful narrow flow does not prove links, network, console, accessibility, or every interactive element are healthy. Use `vibetest` for that coverage.
- **Unsafe authentication or uploads:** never guess credentials or use a file the user did not provide; mark the step blocked or not tested.
- **Runtime drift:** do not add Bun, Playwright, Chromium installers, gstack browser servers, analytics, telemetry, update checks, hidden session files, or automatic side effects.
- **Overclaiming:** separate passed, blocked, and not-tested observations in the final record.

## Verification

Before reporting, confirm that the record contains the target URL, returned page state, inspected elements, actions and results, failed or blocked interactions, evidence, and explicit passed/not-tested/blocked distinctions. Confirm that no runtime, browser server, analytics, telemetry, update-check, hidden-session, credential, or automatic-side-effect claim was added without returned evidence.
