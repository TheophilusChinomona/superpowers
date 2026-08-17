---
name: plan-eng-review
description: Use when an implementation plan needs architecture and reliability review
---

# Plan Engineering Review

Inspect an approved design or implementation plan for architectural soundness, operational risk, and testable behavior. Treat missing boundaries and unspecified failure paths as findings rather than filling them in silently.

## When to Use

- A user asks for an architecture, engineering, technical, or implementation-plan review.
- A plan is about to move into implementation and needs a second pass over data flow, failure modes, security, and coverage.
- A `writing-plans` output introduces a new interface, service, datastore, dependency, or operational path.

Do not use this as a substitute for `office-hours` when the problem is unclear, or for `plan-design-review` and `plan-devex-review` when their specialist lenses are the main concern.

## Review Lens

Inspect every applicable concern:

- **Architecture and data flow:** components, boundaries, interfaces, ownership, state transitions, trust boundaries, dependencies, migrations, and a concise request-to-storage-to-response flow.
- **Failure modes:** timeouts, retries, partial writes, duplicate delivery, stale data, concurrency, rate limits, backpressure, degraded dependencies, rollback, and recovery.
- **Null and error handling:** missing records, malformed input, absent configuration, empty collections, expired credentials, unexpected response shapes, and errors at every boundary. Do not accept an implicit happy path.
- **Security:** authentication, authorization, tenant isolation, secret handling, injection, sensitive logging, replay, abuse, and security regressions. Identify fail-open paths explicitly; permissions and validation must fail closed where safety requires it.
- **Testing and coverage:** unit, integration, contract, end-to-end, migration, negative, failure-injection, security, and regression tests. Tie tests to risks, not only to lines of code.
- **Observability and operations:** useful logs, metrics, traces, alerts, runbooks, SLO impact, capacity, performance, deployment, rollback, and operational cost. New operational burden must be named.

## Procedure

1. State the plan, design, constraints, and existing behavior reviewed. If a required artifact is absent, record it as an open decision or critical finding. Completion criterion: review scope and evidence sources are explicit.
2. Trace the primary data flow and each trust boundary. Use a small text diagram when it makes ownership or failure propagation clearer. Completion criterion: inputs, transformations, persistence, outputs, and authorization points are accounted for.
3. Walk through normal, null, error, retry, timeout, partial, and recovery paths. Explicitly check fail-open behavior, missing null/error handling, and tenant or permission boundaries when relevant. Completion criterion: each applicable risk has a mitigation and a test or a named gap.
4. Check testing, security, observability, and operational cost against the risks found. Do not approve a security-sensitive change without relevant regression coverage. Completion criterion: coverage is mapped to critical failure modes.
5. List required plan changes and hand the approved direction to `writing-plans`. Do not edit code or the plan during review unless the user explicitly asks for that separate action. Completion criterion: a verdict and actionable follow-ups are present.

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

Use `APPROVE` only when applicable architecture, failure, security, testing, observability, and cost concerns are addressed. Use `APPROVE-WITH-NITS` for non-blocking gaps. Use `REQUEST-CHANGES` for an unsafe boundary, unhandled critical failure path, absent security regression coverage, or an architecture that cannot be operated or tested.

## Safety Boundary

This skill does not automatically commit, push, deploy, open pull requests, install runtimes, or mutate production. Do not commit, push, deploy, open pull requests, install runtimes, or mutate production while using it. It may inspect repository context and propose changes, but it must not apply implementation edits during a review by default.
