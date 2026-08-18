# Planning and Review Skills Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans for small and medium plans, or superpowers:subagent-driven-development when the plan is large enough that per-task subagents and review repay their cost. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add five harness-neutral planning and review skills that improve product framing, architecture, design, and developer-experience decisions without replacing Superpowers Lite's existing planning workflow.

**Architecture:** Each skill is a self-contained `SKILL.md` under `skills/`. `office-hours` produces a clarified problem frame; the four review skills consume an approved problem or plan and return findings, decisions, and required follow-ups. They invoke existing `brainstorming` and `writing-plans` concepts by reference, but they do not edit code or run side-effecting commands by default.

**Tech Stack:** Markdown, Agents Skills frontmatter, Python contract tests, Claude explicit-skill request runner.

**Spec:** `docs/superpowers/archive/specs/2026-08-17-first-wave-skills-integration.md`

## Global Constraints

- Existing Superpowers Lite engineering skills remain canonical.
- New skills complement rather than replace `brainstorming` and `writing-plans`.
- No automatic commits, pushes, deploys, PRs, runtime installs, or production mutations.
- Imported source is normalized into Superpowers Lite `SKILL.md` files.
- Upstream provenance is recorded in `docs/superpowers/specs/2026-08-17-first-wave-skills-integration.md` and Sentio-OS.

---

### Task 1: Write the red contract test and pressure prompts

**Files:**
- Create: `tests/skills/test_planning_review_contracts.py`
- Create: `tests/explicit-skill-requests/prompts/office-hours-please.txt`
- Create: `tests/explicit-skill-requests/prompts/plan-ceo-review-please.txt`
- Create: `tests/explicit-skill-requests/prompts/plan-eng-review-please.txt`
- Create: `tests/explicit-skill-requests/prompts/plan-design-review-please.txt`
- Create: `tests/explicit-skill-requests/prompts/plan-devex-review-please.txt`

**Interfaces:**
- Produces the contract that every planning skill must satisfy before its body is authored.

- [ ] **Step 1: Write the failing static test**

```python
from pathlib import Path
import re

ROOT = Path(__file__).parents[2]
SKILLS = {
    "office-hours": "clarified problem frame",
    "plan-ceo-review": "scope",
    "plan-eng-review": "architecture",
    "plan-design-review": "design",
    "plan-devex-review": "developer experience",
}


def frontmatter(text):
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert match, "skill must have YAML frontmatter"
    return match.group(1)


def test_planning_skill_contracts_are_not_yet_satisfied():
    for name, required_term in SKILLS.items():
        path = ROOT / "skills" / name / "SKILL.md"
        assert path.is_file(), f"missing {path}"
        text = path.read_text(encoding="utf-8")
        fm = frontmatter(text)
        assert f"name: {name}" in fm
        assert "description: Use when" in fm
        assert required_term in text.lower()
        assert "do not commit" in text.lower()
        assert "writing-plans" in text
```

- [ ] **Step 2: Run the test to verify the red state**

Run: `python -m pytest tests/skills/test_planning_review_contracts.py -q`

Expected: FAIL because the five new skill files do not exist.

- [ ] **Step 3: Add five pressure prompts**

Each prompt must combine ambiguity, time pressure, and a request to start implementation immediately. The expected behavior is explicit skill loading first, one decision at a time for `office-hours`, and findings before edits for review skills.

- [ ] **Step 4: Run one baseline fresh-agent attempt without the new skill files**

Use the prompt text in a clean agent session and save the response under `Sentio-OS/00-Inbox/` as a baseline. Record whether the agent skipped clarification, accepted scope without challenge, or edited before review.

---

### Task 2: Add `office-hours`

**Files:**
- Create: `skills/office-hours/SKILL.md`

**Interfaces:**
- Consumes: the user's rough idea and any existing project context.
- Produces: a concise problem frame containing user, problem, desired outcome, constraints, non-goals, options, decision, and next step.

- [ ] **Step 1: Normalize the upstream source**

Read `https://raw.githubusercontent.com/garrytan/gstack/main/office-hours/SKILL.md`. Preserve the useful two-mode concept, but remove gstack preamble, telemetry, update checks, runtime paths, and host-specific tool declarations.

- [ ] **Step 2: Write the minimal skill contract**

The skill must require:

1. Ask one high-leverage question at a time.
2. Separate facts from assumptions.
3. Refuse to jump to implementation while the problem or success condition is unclear.
4. End with a written decision or a clearly named unresolved question.
5. Hand an approved design to `writing-plans` rather than implementing it.

- [ ] **Step 3: Run the explicit trigger test**

Run: `bash tests/explicit-skill-requests/run-test.sh office-hours tests/explicit-skill-requests/prompts/office-hours-please.txt 5`

Expected: PASS with an explicit `office-hours` skill invocation and no code-changing tool before invocation.

- [ ] **Step 4: Run the pressure scenario with the new skill**

Expected: the response asks focused questions, names assumptions, and does not create code or a plan until the problem frame is accepted.

---

### Task 3: Add `plan-ceo-review` and `plan-eng-review`

**Files:**
- Create: `skills/plan-ceo-review/SKILL.md`
- Create: `skills/plan-eng-review/SKILL.md`

**Interfaces:**
- Consumes: an approved design or implementation plan.
- Produces: actionable findings, explicit decisions, and a revised scope or architecture recommendation.

- [ ] **Step 1: Normalize both upstream sources**

Read the exact upstream files named in the spec. Remove interactive-tool declarations that are not available across supported hosts. Keep the distinct lenses:

- CEO: user value, scope, differentiation, sequencing, and whether the work should exist.
- Engineering: architecture, data flow, failure modes, testing, security, observability, and operational cost.

- [ ] **Step 2: Encode the review output contract**

Both skills must output:

- Context reviewed
- Strengths
- Critical findings
- Warnings
- Open decisions
- Required plan changes
- Verdict: `APPROVE`, `APPROVE-WITH-NITS`, or `REQUEST-CHANGES`

`plan-eng-review` must explicitly inspect security regressions, fail-open paths, missing null/error handling, and test coverage when those concerns apply.

- [ ] **Step 3: Run both explicit trigger tests**

Run:

```bash
bash tests/explicit-skill-requests/run-test.sh plan-ceo-review tests/explicit-skill-requests/prompts/plan-ceo-review-please.txt 5
bash tests/explicit-skill-requests/run-test.sh plan-eng-review tests/explicit-skill-requests/prompts/plan-eng-review-please.txt 5
```

Expected: both pass and invoke the named skill before repository actions.

- [ ] **Step 4: Run the combined pressure scenario**

Use a plan with attractive product scope but a hidden tenant-isolation failure. Expected: CEO review challenges unnecessary scope; engineering review identifies the security boundary and requests a test before approval.

---

### Task 4: Add `plan-design-review` and `plan-devex-review`

**Files:**
- Create: `skills/plan-design-review/SKILL.md`
- Create: `skills/plan-devex-review/SKILL.md`

**Interfaces:**
- Consumes: a design or implementation plan, existing UI constraints when available, and the target developer workflow.
- Produces: design findings or developer-experience findings with a verdict and concrete plan changes.

- [ ] **Step 1: Normalize the upstream sources**

Read the exact upstream files named in the spec. Keep the review lenses but remove gstack-only runtime behavior.

- [ ] **Step 2: Define the design review contract**

Require checks for information hierarchy, states, responsive behavior, accessibility, content honesty, route preservation, and visual consistency. Point to `vibetest` for live interaction verification rather than duplicating its browser audit.

- [ ] **Step 3: Define the DevEx review contract**

Require checks for setup, local feedback loops, test commands, debugging paths, contributor documentation, dependency burden, and failure recovery.

- [ ] **Step 4: Run both explicit trigger tests**

Run:

```bash
bash tests/explicit-skill-requests/run-test.sh plan-design-review tests/explicit-skill-requests/prompts/plan-design-review-please.txt 5
bash tests/explicit-skill-requests/run-test.sh plan-devex-review tests/explicit-skill-requests/prompts/plan-devex-review-please.txt 5
```

Expected: both pass with no premature code-changing tool use.

- [ ] **Step 5: Run the pressure scenario**

Give the design reviewer a polished but incomplete interface plan with no empty, loading, error, focus, or mobile states. Give the DevEx reviewer a setup plan that assumes an unavailable global dependency. Expected: both request concrete changes instead of approving visual polish or undocumented setup.

---

### Task 5: Turn the red test green and document the first wave

**Files:**
- Modify: `tests/skills/test_planning_review_contracts.py`
- Modify: `README.md:91-101`
- Modify: `docs/testing.md:8-21`

**Interfaces:**
- Consumes: all five skill files and the explicit trigger prompts.
- Produces: deterministic contract coverage and discoverable documentation.

- [ ] **Step 1: Run the static contract test**

Run: `python -m pytest tests/skills/test_planning_review_contracts.py -q`

Expected: PASS for all five skills.

- [ ] **Step 2: Add the skills to the README categories**

List the five skills under Planning and Review, and state that they complement the existing `brainstorming` and `writing-plans` workflow.

- [ ] **Step 3: Document the test tiers**

Update `docs/testing.md` to distinguish static skill contracts from explicit Claude skill-trigger tests and manual pressure scenarios.

- [ ] **Step 4: Run the targeted suite and inspect the diff**

Run: `python -m pytest tests/hermes -q && git diff --check && git diff -- skills tests/skills tests/explicit-skill-requests README.md docs/testing.md`

Expected: Hermes tests pass, no whitespace errors, and the diff contains only the planning/review wave.

- [ ] **Step 5: Stop for review before any commit or push**

Present the five skill files, test outputs, and the pressure-scenario findings. Do not commit or push automatically.

## Verification Record

- **Date:** 2026-08-18
- **Status:** Verified; ready to archive.
- **Plan/spec coverage:** All five planning/review skills, their static contract, trigger prompts, README/testing documentation, no-side-effect boundaries, and review output contracts were implemented and reviewed.
- **Observed verification:** `uv run --with pytest --no-project python -m pytest tests/skills -q` — 8 passed; `git diff --check` — passed; Hermes — 18 passed and 1 known unrelated bootstrap assertion failure.
- **Blocked verification:** Claude explicit-trigger checks remain blocked because the account is out of usage; they are not represented as passes.
- **Review status:** Task review, fix review, final whole-branch review, and final scoped re-review found no unresolved Critical or Important findings.
- **Archive decision:** Move this plan to `docs/superpowers/archive/plans/` and the linked first-wave spec to `docs/superpowers/archive/specs/` with `git mv`, then verify repository and vault links.
