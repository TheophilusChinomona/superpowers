# First-Wave Skills Integration Specification

- **Status:** Approved for implementation
- **Date:** 2026-08-17
- **Project:** Superpowers Lite

## Goal

Add a focused first wave of planning, documentation, knowledge, diagram, and browser-exploration workflows while keeping Superpowers Lite lean, harness-neutral, and safe by default.

## Approved skills

Planning and review:

- `office-hours`
- `plan-ceo-review`
- `plan-eng-review`
- `plan-design-review`
- `plan-devex-review`

Documentation and knowledge:

- `document-release`
- `document-generate`
- `learn`

Visual output:

- `diagram`

Browser:

- `browse`

## Integration boundaries

- Existing Superpowers Lite engineering skills remain canonical.
- New skills complement rather than replace `brainstorming`, `writing-plans`, `vibetest`, verification, review, and branch-finishing workflows.
- `browse` is Hermes-native and uses `browser_exec`; it does not import Bun, Playwright, a gstack browser server, telemetry, update checks, or hidden session machinery.
- `browse` means direct exploration and interaction. `vibetest` remains the systematic QA audit with network, console, accessibility, and severity reporting.
- Documentation and learning skills write durable project context to `C:\Users\Givemore\Desktop\Sentio-OS` when it is available. They must never copy credentials, `.env` contents, or tokens.
- No skill may commit, push, deploy, open a PR, install a runtime, or mutate production by default.
- Imported material is normalized into Superpowers Lite's `SKILL.md` format and is not copied with third-party installers or lifecycle machinery.

## Upstream source provenance

The selected source skill documents are in the gstack repository:

- `https://raw.githubusercontent.com/garrytan/gstack/main/office-hours/SKILL.md`
- `https://raw.githubusercontent.com/garrytan/gstack/main/plan-ceo-review/SKILL.md`
- `https://raw.githubusercontent.com/garrytan/gstack/main/plan-eng-review/SKILL.md`
- `https://raw.githubusercontent.com/garrytan/gstack/main/plan-design-review/SKILL.md`
- `https://raw.githubusercontent.com/garrytan/gstack/main/plan-devex-review/SKILL.md`
- `https://raw.githubusercontent.com/garrytan/gstack/main/document-release/SKILL.md`
- `https://raw.githubusercontent.com/garrytan/gstack/main/document-generate/SKILL.md`
- `https://raw.githubusercontent.com/garrytan/gstack/main/learn/SKILL.md`
- `https://raw.githubusercontent.com/garrytan/gstack/main/diagram/SKILL.md`
- `https://raw.githubusercontent.com/garrytan/gstack/main/browse/SKILL.md`

## Independent delivery plans

1. `docs/superpowers/archive/plans/2026-08-17-planning-review-skills.md`
2. `docs/superpowers/archive/plans/2026-08-17-documentation-knowledge-skills.md`
3. `docs/superpowers/archive/plans/2026-08-17-hermes-native-browse.md`

## Verification Record

- **Date:** 2026-08-18
- **Status:** Verified; linked implementation plans are complete and ready to archive with this specification.
- **Coverage:** All ten approved skills and the integration boundaries in this specification were implemented, statically verified, reviewed, and documented.
- **Observed verification:** Skill contracts — 8 passed; `git diff --check` — passed; Hermes — 18 passed and 1 known unrelated bootstrap assertion failure; browser smoke evidence — passed.
- **Blocked verification:** Claude explicit-trigger checks remain blocked because the account is out of usage; no blocked check is represented as a pass.
- **Archive decision:** Move this specification to `docs/superpowers/archive/specs/` with `git mv` together with the three linked plans in `docs/superpowers/archive/plans/`, then verify repository and vault links.
