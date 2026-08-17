---
name: plan-design-review
description: Use when a plan with user-facing UI needs an interaction and visual review
---

# Plan Design Review

Review a UI or UX plan for understandable hierarchy, complete states, inclusive interaction, honest content, and consistency across routes and viewports. This is a plan review, not a replacement for live browser verification.

## When to Use

- A user asks for a design-plan, UX, interaction, or visual review before implementation.
- A plan adds or changes screens, routes, components, content, or responsive behavior.
- A polished mockup risks hiding missing loading, empty, error, focus, mobile, or accessibility behavior.

Use `vibetest` for live interaction, network, console, and accessibility verification after a runnable experience exists. Use `writing-plans` to turn accepted design decisions into implementation tasks.

## Review Lens

Inspect each applicable dimension:

1. **Information hierarchy:** What is seen first, second, and third? Are primary actions, navigation, status, and supporting detail distinguishable? Does the visual hierarchy serve the user's task rather than merely decorate it?
2. **States:** Specify loading, empty, error, success, partial, disabled, permission, offline, long-content, and first-use states as applicable. Include recovery actions and what remains usable.
3. **Responsive behavior:** Define intentional behavior for narrow, medium, and wide viewports: reflow, overflow, navigation, density, touch targets, and priority changes. "Stack on mobile" is not a complete rule.
4. **Accessibility:** Check keyboard order and focus visibility, semantics, labels, screen-reader announcements, contrast, motion preferences, zoom, target sizes, and non-pointer alternatives.
5. **Content honesty:** Ensure labels, status, progress, empty states, errors, and marketing claims tell the truth. Do not promise automation, security, speed, or completion the system cannot guarantee.
6. **Route preservation:** Check deep links, browser back/forward, refresh, query/filter state, redirects, unsaved changes, permissions, and restoration after an error.
7. **Visual consistency:** Check design tokens, spacing, typography, icon meaning, controls, focus/error treatment, motion, and reuse of existing patterns. Note intentional exceptions.

## Procedure

1. State the screens, routes, personas, constraints, and artifacts reviewed. If UI scope is implied but not specified, record the ambiguity. Completion criterion: every user-facing surface in the plan has a review boundary.
2. Trace the primary user journey and name the visual hierarchy at each step. Then enumerate applicable states and viewport changes. Completion criterion: the plan covers the happy path and the states most likely to change user behavior.
3. Check accessibility, content honesty, route preservation, and visual consistency against the interaction details. Record evidence or a concrete gap; do not infer that a polished visual has an accessible implementation. Completion criterion: each applicable lens has a finding or an explicit pass rationale.
4. List required plan changes before implementation. For live verification, point the implementer to `vibetest`; do not duplicate its browser audit in this skill. Completion criterion: findings are actionable and no UI code was edited.
5. Hand accepted design decisions to `writing-plans`. Completion criterion: the next step names the plan changes, verification path, and any unresolved decision.

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

Use `APPROVE` only when hierarchy, states, responsive behavior, accessibility, content honesty, route preservation, and visual consistency are addressed for the applicable surfaces. Use `APPROVE-WITH-NITS` for non-blocking polish. Use `REQUEST-CHANGES` for missing critical states, inaccessible interactions, misleading content, broken route behavior, or inconsistent patterns that would change usability.

## Safety Boundary

This skill does not automatically commit, push, deploy, open pull requests, install runtimes, or mutate production. Do not commit, push, deploy, open pull requests, install runtimes, or mutate production while using it. It reviews and proposes design changes only; it does not edit UI code or silently rewrite the plan.
