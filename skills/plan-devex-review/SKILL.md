---
name: plan-devex-review
description: Use when a plan needs developer setup, feedback-loop, and recovery review
---

# Plan Developer Experience Review

Review a developer-facing plan from clean checkout through first success, everyday feedback, debugging, upgrade, and failure recovery. Treat contributor time, dependency burden, and undocumented assumptions as product constraints.

## When to Use

- A user asks for a developer-experience, onboarding, API, CLI, SDK, library, or contributor-workflow review.
- A plan changes setup, commands, dependencies, test workflows, documentation, or local tooling.
- A project assumes a global dependency, hidden environment value, tribal debugging knowledge, or a happy-path setup.

Use `writing-plans` after the review to turn accepted improvements into small implementation tasks.

## Review Lens

Inspect the complete developer journey:

1. **Setup:** clean checkout, supported versions, prerequisites, configuration, credentials without secret leakage, platform differences, deterministic install, and a first successful command.
2. **Feedback loops:** time to first result, useful progress, local iteration speed, watch mode or focused checks where appropriate, and whether failures point to the next action.
3. **Test commands:** canonical commands, test scope, fixtures and services, required environment, expected duration, deterministic behavior, and how to run one focused test before the full suite.
4. **Debugging:** logs, error messages, reproduction steps, source maps or traces when relevant, health checks, diagnostic commands, and a path from symptom to likely cause.
5. **Contributor documentation:** quickstart, architecture context, conventions, common workflows, release/upgrade notes, troubleshooting, ownership, and documentation that matches the actual commands.
6. **Dependency burden:** direct and transitive cost, global versus project-local tools, version drift, platform-specific friction, supply-chain exposure, and whether each dependency earns its maintenance cost.
7. **Failure recovery:** interrupted setup, stale generated state, unavailable services, partial migrations, failed tests, bad configuration, rollback, reset, and how a contributor returns to a known-good state.

## Procedure

1. State the contributor persona, starting state, target workflow, and artifacts reviewed. If the plan assumes a tool, credential, or command that is not documented, record it as a finding. Completion criterion: the journey boundary is explicit.
2. Walk the journey in order: discover, install, first success, real change, focused test, full test, debug, recover, and upgrade. Mark every hidden assumption and wait point. Completion criterion: each stage has a command or a documented reason it is out of scope.
3. Evaluate feedback quality and failure recovery. Prefer project-local, reproducible commands over machine-global state; never copy secrets into examples or docs. Completion criterion: the most likely setup and test failures each have an actionable recovery path.
4. Rank dependency and documentation gaps by contributor impact and maintenance cost. Do not install runtimes or edit files while reviewing. Completion criterion: required plan changes name the owner-facing action and its verification.
5. Hand accepted improvements to `writing-plans`. Completion criterion: the verdict, next planning step, and unresolved decisions are explicit.

## Required Output

Use these headings exactly:

```markdown
## Context reviewed
## Strengths
## Critical findings
## Warnings
## Open decisions
## Required plan changes
## Verdict
[APPROVE | APPROVE-WITH-NITS | REQUEST-CHANGES]
```

Use `APPROVE` only when setup, feedback loops, test commands, debugging, contributor documentation, dependency burden, and failure recovery are workable for the target persona. Use `APPROVE-WITH-NITS` for non-blocking documentation polish. Use `REQUEST-CHANGES` when a clean contributor cannot reach first success, reproduce tests, debug failures, or recover without undocumented help or an unjustified dependency.

## Safety Boundary

This skill does not automatically commit, push, deploy, open pull requests, install runtimes, or mutate production. Do not commit, push, deploy, open pull requests, install runtimes, or mutate production while using it. It reviews and proposes developer-workflow changes; it does not install dependencies or apply code edits by default.
