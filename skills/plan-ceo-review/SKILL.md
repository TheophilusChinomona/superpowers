---
name: plan-ceo-review
description: Use when a product plan needs rigorous user-value and scope review
---

# Plan CEO Review

Review an approved problem frame, design, or implementation plan from the product-owner's perspective. Challenge whether the work creates meaningful user value, whether the scope is coherent, and whether the work should exist before anyone edits the plan or code.

## When to Use

- A user asks for a strategy, product, scope, ambition, or founder-mode review.
- A plan has attractive features but weak evidence of user value, differentiation, or sequencing.
- A design is ready for `writing-plans` but needs a final product challenge first.

Do not use this to replace `office-hours` when the problem or success condition is still unknown, or to replace engineering, design, or DevEx review for their specialist concerns.

## Review Lens

Inspect the plan in this order:

1. **User value:** Who is the target user, what painful job or outcome matters, what happens today, and what evidence supports the claim? Distinguish a user problem from an internal preference or feature request.
2. **Should this work exist:** Test the problem's urgency, frequency, willingness to change, timing, and the cost of doing nothing. State plainly when the evidence does not justify building.
3. **Scope:** Identify the smallest coherent slice that proves the outcome. Challenge feature piles, vague audiences, premature platform work, and scope that cannot be completed or evaluated together.
4. **Differentiation:** Explain why this approach is meaningfully better or more specific than the status quo and credible alternatives. Do not call novelty differentiation without a user-observable advantage.
5. **Sequencing:** Check prerequisites, learning order, reversible versus expensive decisions, and what should be validated before investment. Recommend cuts, deferrals, or a stronger next slice when appropriate.

## Procedure

1. State the context and artifacts reviewed. If the problem, user, or success condition is missing, record that as a critical finding instead of inventing it. Completion criterion: the review boundary is explicit.
2. Separate evidence from assumptions and evaluate each review lens above. Cite the plan section or stated fact when available; label an inference as an inference. Completion criterion: every major scope item has a value and sequencing rationale or a finding.
3. Rank findings as critical findings or warnings. A critical finding blocks approval; a warning needs attention but does not block the stated outcome. Completion criterion: each finding has impact and a concrete recommendation.
4. List open decisions that require the user's choice. Do not silently add or remove scope, and do not edit a plan or code while review is in progress. Completion criterion: unresolved choices are visible and assigned to the user.
5. Convert accepted decisions into required plan changes and hand the revised direction to `writing-plans`. Completion criterion: the next planning step is named and no implementation action was taken.

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

Use `APPROVE` only when the plan is coherent and the critical risks are addressed. Use `APPROVE-WITH-NITS` when the outcome and scope are sound but non-blocking clarifications remain. Use `REQUEST-CHANGES` when user value, scope, differentiation, sequencing, or whether the work should exist is unresolved.

## Safety Boundary

This skill does not automatically commit, push, deploy, open pull requests, install runtimes, or mutate production. Do not commit, push, deploy, open pull requests, install runtimes, or mutate production while using it. It reviews and proposes plan changes; it does not apply edits without explicit user direction.
