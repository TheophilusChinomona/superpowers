---
name: agency-agent-routing
description: Use when a task needs a domain specialist (backend, frontend, database, security, testing, design, planning, marketing) and you must pick the right Agency agent to load inline or delegate to, or when assembling a team of specialists for a scenario
---

# Agency Agent Routing

## Overview

Route each task to the right Agency specialist instead of doing it as a generalist. A curated roster of specialists lives in `agents/<slug>.md` at the plugin root; this skill tells you which one to pick and how to hand the work to it.

**Core principle:** Classify the task, select the matching specialist, then either load its persona inline (cheap, no subagent) or delegate to it as a subagent (isolated context) — never both, never neither.

## When to Use

- A task clearly belongs to a domain with a named specialist (backend, frontend, database, auth, security, testing, design, planning).
- The work benefits from a specialist's standards, checklists, and deliverables rather than generic effort.
- You are coordinating multiple specialists across phases (plan → build → review → gate).
- A scenario (feature, MVP, audit) needs a specific assembled team.

**Don't use when:**

- The work is trivial or mechanical — do it inline yourself. Routing a specialist for a one-line fix is overhead.
- The task spans domains so tightly that one specialist's lens would miss context — handle it yourself or split it deliberately.

## Routing Procedure

1. **Classify** the task into one division and one specialist slot (see the table).
2. **Select** the specialist by slug.
3. **Hand off** in one of two ways:
   - **Load (inline):** adopt the specialist's persona and standards for the current turn. Use for advice, design, review, and small focused work. No subagent is spawned.
   - **Delegate (subagent):** spawn an isolated subagent carrying the specialist's full instructions plus the task. Use when the work is large enough to flood your context, or runs in parallel with other work.
4. **Pass full context.** Specialists know nothing about your session. Hand over the goal, the relevant files/errors, and any outputs from earlier specialists verbatim.

## Routing Table (curated roster)

| Division | Specialist (slug) | Route to when the task is |
|---|---|---|
| project-management | `senior-project-manager` | Scope, task breakdown, sprint/phase planning |
| project-management | `experiment-tracker` | A/B test design, experiment planning |
| engineering | `software-architect` | System design, architecture decisions |
| engineering | `backend-architect` | API + database + scale design |
| engineering | `api-platform-engineer` | API contracts, gateways, versioning |
| engineering | `database-optimizer` | Query/index performance, slow queries |
| engineering | `database-reliability-engineer` | Migrations, consistency, HA, backups |
| engineering | `identity-access-engineer` | Auth (JWT/OAuth), RBAC, multi-tenancy |
| engineering | `senior-developer` | Complex implementation, hard bugs |
| engineering | `rapid-prototyper` | Fast first-version iteration |
| engineering | `frontend-developer` | React/UI implementation |
| engineering | `devops-automator` | CI/CD, pipelines, automation |
| engineering | `sre-site-reliability-engineer` | Reliability, observability, on-call |
| engineering | `code-reviewer` | Code review, defect triage |
| engineering | `technical-writer` | Docs, runbooks, ADRs |
| security | `security-architect` | Security design, defense-in-depth |
| security | `application-security-engineer` | App-level vulns, authn/z review |
| testing | `api-tester` | API/integration tests |
| testing | `test-automation-engineer` | Test suites, CI test automation |
| testing | `reality-checker` | Production readiness, milestone gates |
| testing | `evidence-collector` | Quality verification, evidence capture |
| design | `ui-designer` | Design system, components, UX |
| marketing | `growth-hacker` | Launch plan, GTM, user acquisition |

## Team Compositions

Assemble these teams when the scenario matches. Load/delegate each specialist for its own phase; pass outputs verbatim between them.

**Enterprise feature development** — `senior-project-manager` (planning) → `senior-developer` (implementation) + `ui-designer` (components) → `evidence-collector` (verification) → `reality-checker` (production gate), with `experiment-tracker` for any A/B work.

**Startup MVP** — `frontend-developer` (app) + `backend-architect` (API/DB) + `rapid-prototyper` (first version) in parallel, `growth-hacker` (launch plan) alongside, `reality-checker` gating each milestone.

**Backend feature (e.g. ERP)** — `backend-architect` or `senior-developer` (implement) + `database-optimizer` (queries/migrations) + `identity-access-engineer` (auth/tenancy) → `api-tester` (integration) + `code-reviewer` (review) → `reality-checker` (gate).

## Dispatch per Harness

Speak in actions ("load the specialist", "delegate to the specialist"); each harness resolves them to its own mechanism.

- **Hermes Agent** — preferred: the `agency-agents-router` plugin. `agency_agents_search` to find a specialist (full 270 roster), then `agency_agents_load` (inline) or `agency_agents_delegate` (subagent). Offline fallback for the curated set: read `agents/<slug>.md` at the plugin root and adopt it.
- **Claude Code** — read `agents/<slug>.md` at the plugin root and adopt the specialist for the turn; if the specialists are installed as Claude sub-agents (`~/.claude/agents/`), dispatch with the Task tool using the agent's frontmatter `name`.
- **Codex** — read `agents/<slug>.md` and adopt inline, or use Codex's subagent mechanism with the specialist's `name`.

The curated `agents/` directory is the offline, self-contained roster. Hermes additionally has the full Agency roster through its router plugin; Claude Code and Codex see only what is in `agents/` unless the full roster is installed separately.

## Common Mistakes

- **Routing to a generalist** when a named specialist exists — check the table first.
- **Delegating for trivial work** — a subagent pays a context build plus a review pass; load inline for anything small.
- **Loading the whole roster** — never preload all specialists; pull only the ones the current phase needs.
- **Skipping context handoff** — specialists share no memory; paste prior outputs, files, and errors verbatim.
- **Picking a vague specialist** — if two slots could apply, pick the more specific one and say why.
