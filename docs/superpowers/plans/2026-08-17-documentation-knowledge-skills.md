# Documentation and Knowledge Skills Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans for small and medium plans, or superpowers:subagent-driven-development when the plan is large enough that per-task subagents and review repay their cost. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add `document-release`, `document-generate`, `learn`, and `diagram` skills that keep project knowledge accurate and durable in the Sentio-OS PARA vault without leaking secrets or replacing repository source of truth.

**Architecture:** The four skills are Markdown workflows. Documentation skills inspect verified project files and write concise, cited notes. `learn` records durable lessons in Sentio-OS and distinguishes project knowledge from user memory. `diagram` produces a source-first diagram artifact and records the source plus rendered outputs when local rendering tools are available.

**Tech Stack:** Markdown, Agents Skills frontmatter, Python contract tests, Mermaid, Excalidraw JSON, Sentio-OS Markdown.

**Spec:** `docs/superpowers/specs/2026-08-17-first-wave-skills-integration.md`

## Global Constraints

- Sentio-OS path for this machine: `C:\Users\Givemore\Desktop\Sentio-OS`.
- The vault is a knowledge layer, not a replacement for repository code or formal project source files.
- Never copy credentials, `.env` contents, tokens, or private keys into Sentio-OS.
- No automatic commits, pushes, deploys, PRs, runtime installs, or production mutations.
- If Sentio-OS is missing, report the missing path and ask before creating a different vault.
- Durable notes must distinguish observed facts, interpretation, recommendation, unknowns, and source links.

---

### Task 1: Write the red contract test and pressure prompts

**Files:**
- Create: `tests/skills/test_documentation_knowledge_contracts.py`
- Create: `tests/explicit-skill-requests/prompts/document-release-please.txt`
- Create: `tests/explicit-skill-requests/prompts/document-generate-please.txt`
- Create: `tests/explicit-skill-requests/prompts/learn-please.txt`
- Create: `tests/explicit-skill-requests/prompts/diagram-please.txt`

**Interfaces:**
- Produces the contract every documentation/knowledge skill must satisfy before authoring.

- [ ] **Step 1: Write the failing static test**

```python
from pathlib import Path
import re

ROOT = Path(__file__).parents[2]
SKILLS = {
    "document-release": "Sentio-OS",
    "document-generate": "source of truth",
    "learn": "durable",
    "diagram": "Mermaid",
}


def test_documentation_skills_are_not_yet_satisfied():
    for name, required_term in SKILLS.items():
        path = ROOT / "skills" / name / "SKILL.md"
        assert path.is_file(), f"missing {path}"
        text = path.read_text(encoding="utf-8")
        assert re.search(r"^name: " + re.escape(name) + r"$", text, re.M)
        assert re.search(r"^description: Use when", text, re.M)
        assert required_term.lower() in text.lower()
        assert "secret" in text.lower() or "credential" in text.lower()
        assert "do not commit" in text.lower()
```

- [ ] **Step 2: Run the red test**

Run: `python -m pytest tests/skills/test_documentation_knowledge_contracts.py -q`

Expected: FAIL because the four skill files do not exist.

- [ ] **Step 3: Create the four pressure prompts**

Prompts must test: post-release docs with an unverified claim, generation from a repository containing `.env` files, learning from a one-off transient failure, and a diagram request with incomplete relationships.

- [ ] **Step 4: Run the baseline without the new skills**

Use a clean agent session and capture whether it invents documentation, copies secrets, stores transient facts as durable learning, or emits a diagram without an editable source.

---

### Task 2: Add `document-release`

**Files:**
- Create: `skills/document-release/SKILL.md`

**Interfaces:**
- Consumes: a verified completed change, diff, tests, release notes, and the relevant project README.
- Produces: updated project documentation plus a concise Sentio-OS release note with evidence and links.

- [ ] **Step 1: Normalize the upstream source**

Read `https://raw.githubusercontent.com/garrytan/gstack/main/document-release/SKILL.md`. Remove gstack preamble, telemetry, update checks, and automatic commit behavior.

- [ ] **Step 2: Define the evidence-first workflow**

Require the agent to inspect `git diff`, test output, changed routes/APIs, and existing docs before writing. Every claim must cite a file path, command output, or source URL. The skill must say what to do when verification is unavailable: mark the claim unverified rather than guessing.

- [ ] **Step 3: Define Sentio-OS placement**

Write project-specific release context under the matching folder in `C:\Users\Givemore\Desktop\Sentio-OS\01-Projects\`. Use date-prefixed Markdown and link the repository source path. Do not copy the entire diff.

- [ ] **Step 4: Run the explicit trigger test**

Run: `bash tests/explicit-skill-requests/run-test.sh document-release tests/explicit-skill-requests/prompts/document-release-please.txt 5`

Expected: PASS with the skill loaded before file changes.

---

### Task 3: Add `document-generate`

**Files:**
- Create: `skills/document-generate/SKILL.md`

**Interfaces:**
- Consumes: a repository or module path and available source/docs.
- Produces: documentation grounded in inspected code, with missing information called out explicitly.

- [ ] **Step 1: Normalize the upstream source**

Read `https://raw.githubusercontent.com/garrytan/gstack/main/document-generate/SKILL.md`. Keep its inventory-first behavior and remove runtime-specific commands.

- [ ] **Step 2: Define the generation workflow**

Require: inventory files, identify the audience, trace public entry points and dependencies, distinguish observed behavior from inference, write the smallest useful document, and verify every path/link before completion.

- [ ] **Step 3: Add the secret boundary**

Require excluding `.env`, credentials, tokens, private keys, generated secrets, and sensitive logs. If the source cannot be documented safely, report the boundary instead of copying it.

- [ ] **Step 4: Run the explicit trigger test**

Run: `bash tests/explicit-skill-requests/run-test.sh document-generate tests/explicit-skill-requests/prompts/document-generate-please.txt 5`

Expected: PASS and no secret content copied into generated notes.

---

### Task 4: Add `learn`

**Files:**
- Create: `skills/learn/SKILL.md`

**Interfaces:**
- Consumes: a verified recurring lesson, source evidence, project identity, and the failure or success that produced it.
- Produces: a durable learning note in Sentio-OS with context, evidence, reusable rule, scope, and review date.

- [ ] **Step 1: Normalize the upstream source**

Read `https://raw.githubusercontent.com/garrytan/gstack/main/learn/SKILL.md`. Preserve show/add/search behavior conceptually, but use Sentio-OS Markdown rather than gstack's JSONL storage.

- [ ] **Step 2: Define durable-learning criteria**

Save only lessons that are reusable beyond the current turn. A note must include: project, date, observed evidence, lesson, application boundary, and related source links. One-off progress, temporary TODOs, and stale task state stay out of durable learning.

- [ ] **Step 3: Define placement and correction behavior**

Place project lessons under the relevant `01-Projects/<Project>/` folder and cross-project patterns under `03-Resources/`. If a lesson is superseded, mark it superseded and link the replacement; do not silently erase history.

- [ ] **Step 4: Run the explicit trigger test**

Run: `bash tests/explicit-skill-requests/run-test.sh learn tests/explicit-skill-requests/prompts/learn-please.txt 5`

Expected: PASS with a durable note shape and no unsupported conclusion.

---

### Task 5: Add `diagram`

**Files:**
- Create: `skills/diagram/SKILL.md`

**Interfaces:**
- Consumes: an English architecture/process description or Mermaid source.
- Produces: Mermaid source, an editable Excalidraw JSON artifact when requested, and rendered SVG/PNG only when a verified local renderer is available.

- [ ] **Step 1: Normalize the upstream source**

Read `https://raw.githubusercontent.com/garrytan/gstack/main/diagram/SKILL.md`. Remove gstack-only shell helpers and automatic file-opening behavior.

- [ ] **Step 2: Define source-first output**

Require the editable source to be emitted before rendered output. Use Mermaid for simple diagrams. Use Excalidraw JSON for hand-editable visual diagrams. Put artifacts under the relevant Sentio-OS project folder and link them from its README.

- [ ] **Step 3: Define renderer detection**

Check for an available Mermaid renderer before claiming SVG/PNG output. If no renderer exists, save the source and state that rendering was not run; do not invent a rendered artifact.

- [ ] **Step 4: Run the explicit trigger test**

Run: `bash tests/explicit-skill-requests/run-test.sh diagram tests/explicit-skill-requests/prompts/diagram-please.txt 5`

Expected: PASS and an explicit source-first output contract.

---

### Task 6: Turn the red test green and document the wave

**Files:**
- Modify: `tests/skills/test_documentation_knowledge_contracts.py`
- Modify: `README.md:91-101`
- Modify: `docs/testing.md:8-21`

**Interfaces:**
- Consumes: all four skills and their explicit trigger prompts.
- Produces: deterministic contract coverage and plugin documentation.

- [ ] **Step 1: Run the static contract test**

Run: `python -m pytest tests/skills/test_documentation_knowledge_contracts.py -q`

Expected: PASS for all four skills.

- [ ] **Step 2: Document the skills and Sentio-OS boundary**

Add the four skills to the README's skill categories. Explain that Sentio-OS stores durable context while repositories remain code source of truth.

- [ ] **Step 3: Run targeted verification**

Run: `python -m pytest tests/hermes -q && git diff --check && git diff -- skills tests/skills tests/explicit-skill-requests README.md docs/testing.md`

Expected: Hermes tests pass, no whitespace errors, and no unrelated runtime or integration files appear.

- [ ] **Step 4: Stop for review before any commit or push**

Present generated note examples, secret-boundary evidence, diagram artifact evidence, and test results. Do not commit or push automatically.
