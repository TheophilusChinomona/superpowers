---
name: vibetest
description: Use when asked to vibetest a website or run automated browser QA to find UI bugs, broken links, failed network calls, console errors, accessibility issues, or functional problems on a live, localhost, or LAN site
---

# Vibetest

## Overview

Drive a real browser through a site, exercising its interactive elements, and report the bugs you find — broken links, failing forms, failed network calls, console/JS errors, and accessibility problems — ranked by severity.

**Core principle:** navigate, enumerate every interactive element, test each one, and for every failure record the concrete element → action → observed result. Also watch Chrome DevTools (network + console) so silent failures — a 500 API call, a 404 asset, an uncaught JS exception — are caught, not just visual breakage.

No Gemini key, no `vibetest` package, and no separate Chromium install are required. Use the browser you already have: the `browser_exec` tool drives local Chrome for `localhost`/LAN URLs and routes public URLs to a cloud browser automatically.

## When to Use

- The user asks to "vibetest" a site, run browser QA, or check a website for bugs/broken links/network failures/JS errors.
- Smoke-testing a just-built (vibe-coded) page before showing it off — live URL or `localhost`.

**Don't use when:** a single, specific interaction is all that's needed (just drive the browser once), or when the target is unreachable from both local Chrome and the cloud browser.

## How to Run

Work text-first (the model cannot see screenshots): read page state, DOM, and DevTools signals — don't rely on images.

### 0. Install the network + console collector (before first navigation)

Inject a persistent collector so JS exceptions, unhandled rejections, and `console.error` calls during page load are captured. Do this once, before any navigation; it re-arms automatically on every subsequent document.

```python
cdp("Page.addScriptToEvaluateOnNewDocument", source="""
window.__vibetestErrors = [];
window.addEventListener('error', e => window.__vibetestErrors.push('window.onerror: ' + e.message));
window.addEventListener('unhandledrejection', e => window.__vibetestErrors.push('unhandledrejection: ' + ((e.reason && e.reason.message) || String(e.reason))));
const __ce = console.error.bind(console);
console.error = (...a) => { window.__vibetestErrors.push('console.error: ' + a.map(String).join(' ')); __ce(...a); };
""")
```

### 1. Open the URL

`new_tab(url)` (first navigation) or `goto_url(url)`, then `wait_for_load()`.

### 2. Read the page

`page_info()` for state, then `js()` to extract DOM text: headings, nav, links (`[...document.querySelectorAll('a')].map(a => a.href+' | '+a.textContent)`), buttons, forms, inputs.

### 3. Enumerate interactive elements

Links, buttons, form fields, dropdowns, menus. Group them into test areas (header nav, main content, forms, footer).

### 4. Test each element

- Links: click (or `js("document.querySelector('…').click()")`), check the result — 404, error page, wrong destination, dead redirect.
- Buttons: click, confirm a response happens.
- Forms: submit with valid input, then invalid/empty — record error handling, validation, confirmation.
- Navigation: exercise header/footer/sidebar links.

### 5. Network & console audit (after load, and after each interaction)

```python
# Failed resource loads (status >= 400) — catches 404 assets, 500 API calls
print(js("JSON.stringify(performance.getEntriesByType('resource').map(r=>({n:r.name.replace(location.origin,'').slice(0,80), s:r.responseStatus||0})).filter(r=>r.s>=400))"))
# Main document status
print(js("JSON.stringify({navStatus: (performance.getEntriesByType('navigation')[0]||{}).responseStatus || -1})"))
# Collected console errors / JS exceptions / unhandled rejections
print(js("JSON.stringify(window.__vibetestErrors || [])"))
```

Any resource with `s >= 400`, a `navStatus >= 400`, or a non-empty `__vibetestErrors` is a finding — record the exact URL/message. Re-check after each form submit or button click that is supposed to trigger a network call (the Performance API resets per document, so it reflects the current page's requests).

### 6. Check accessibility

Missing `alt` on images, unlabeled inputs (`label`/`aria-label`), empty link text, missing headings.

### 7. Report

Consolidated list ranked high/medium/low (format below).

### localhost / LAN

`localhost:3000`, `127.0.0.1`, `192.168.x.x` etc. work directly — the browser harness drives local Chrome. Cloud providers auto-route away from private addresses.

### Parallel coverage (optional)

For a large site, split areas into `delegate_task` subagents (each drives its own browser over one section) and merge their reports. For a small site, test inline — one browser, sequential checks, no subagent overhead.

## Report Format

```markdown
## Vibetest — <url>

### High severity
- <element/request> — <action> — <observed result>   (e.g. POST /api/cart returned 500)

### Medium severity
- …

### Low severity
- …
```

Each finding names the exact element/URL, the action taken, and the observed result (status code, error message). Never write a vague "broken link" — say which link and what happened.

## Common Mistakes

- **Skipping the DevTools audit** — a visually fine page can still be failing silently (500s, missing assets, uncaught exceptions). Always run step 5.
- **Reporting without evidence** — a finding needs element/URL + action + result.
- **Screenshot-driven testing** — the model can't see images; read `page_info()` / `js()` text and the DevTools signals instead.
- **Installing the collector after navigating** — it must be installed before the first load to catch load-time errors.
- **Reaching `localhost` from a cloud browser** — let the local-Chrome path handle private URLs.
- **Installing Chromium/Playwright** — unnecessary; the browser tool drives the existing Chrome.
- **Missing the a11y pass** — alt text, labels, and contrast are part of vibetest, not an afterthought.
