---
name: vibetest
description: Use when asked to vibetest a website or run automated browser QA to find UI bugs, broken links, accessibility issues, or functional problems on a live, localhost, or LAN site
---

# Vibetest

## Overview

Drive a real browser through a site, exercising its interactive elements, and report the bugs you find — broken links, failing forms, JS errors, and accessibility problems — ranked by severity.

**Core principle:** navigate, enumerate every interactive element, test each one, record the concrete element → action → observed-result for anything that breaks.

No Gemini key, no `vibetest` package, and no separate Chromium install are required. Use the browser you already have: the `browser_exec` tool drives local Chrome for `localhost`/LAN URLs and routes public URLs to a cloud browser automatically.

## When to Use

- The user asks to "vibetest" a site, run browser QA, or check a website for bugs/broken links/a11y issues.
- Smoke-testing a just-built (vibe-coded) page before showing it off — live URL or `localhost`.

**Don't use when:** a single, specific interaction is all that's needed (just drive the browser once), or when the target is unreachable from both local Chrome and the cloud browser.

## How to Run

Work text-first (the model cannot see screenshots): read the page state and DOM, don't rely on images.

1. **Open the URL** — `new_tab(url)` (first navigation) or `goto_url(url)`, then `wait_for_load()`.
2. **Read the page** — `page_info()` for state, then `js()` to extract the DOM text: headings, nav, links (`[...document.querySelectorAll('a')].map(a => a.href+' | '+a.textContent)`), buttons, forms, inputs.
3. **Enumerate interactive elements** — links, buttons, form fields, dropdowns, menus. Group them into test areas (header nav, main content, forms, footer).
4. **Test each element**:
   - Links: click (or `js("document.querySelector('…').click()")`), check the result — 404, error page, wrong destination, dead redirect.
   - Buttons: click, confirm a response happens.
   - Forms: submit with valid input, then with invalid/empty input — record error handling, validation, confirmation.
   - Navigation: exercise header/footer/sidebar links.
5. **Check accessibility** — missing `alt` on images, unlabeled inputs (`label`/`aria-label`), empty link text, missing headings.
6. **Report** a consolidated list ranked high/medium/low severity (format below).

### localhost / LAN

`localhost:3000`, `127.0.0.1`, `192.168.x.x` etc. work directly — the browser harness drives the local Chrome. Cloud providers are auto-routed away from private addresses, so a cloud browser is never asked to reach your machine.

### Parallel coverage (optional)

For a large site, split the areas into `delegate_task` subagents (each drives its own browser over one section) and merge their reports. For a small site, test inline — one browser, sequential checks, no subagent overhead.

## Report Format

```markdown
## Vibetest — <url>

### High severity
- <element> — <action> — <observed result>   (e.g. "Contact Us" link — clicked — redirected to 404)

### Medium severity
- …

### Low severity
- …
```

Each finding must name the exact element, the action taken, and the observed result. Never write a vague "broken link" — say which link and what happened.

## Common Mistakes

- **Reporting without evidence** — a finding needs the element + action + result you actually observed.
- **Screenshot-driven testing** — the model can't see images; always read `page_info()` / `js()` text.
- **Reaching `localhost` from a cloud browser** — don't route a private URL through the cloud; let the local-Chrome path handle it.
- **Installing Chromium/Playwright** — unnecessary; the browser tool drives the existing Chrome.
- **Missing the a11y pass** — alt text, labels, and contrast are part of vibetest, not an afterthought.
