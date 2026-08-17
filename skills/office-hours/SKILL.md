---
name: office-hours
description: Use when an idea or design needs clarification before planning or implementation
---

# Office Hours

Turn an uncertain idea into a clarified problem frame through a short, evidence-aware conversation. This skill is for deciding what should be built and why; it does not implement the idea.

## When to Use

- A user has a new idea, asks whether something is worth building, or wants help thinking through a design.
- The user is mixing facts, guesses, desired outcomes, and implementation details.
- The request is ambiguous enough that implementation could solve the wrong problem.

Do not use this as a substitute for `writing-plans` once the design is approved, or for implementation and debugging skills after the plan is accepted.

## Operating Rules

1. Ask **one high-leverage question at a time**. Do not send a questionnaire disguised as one turn. Wait for the answer before selecting the next question.
2. Separate **facts** (what the user observed or can substantiate) from **assumptions** (what is inferred, hoped, or not yet tested). Label both explicitly.
3. Do not jump to implementation, scaffold code, or write an implementation plan while the problem, target user, or success condition is unclear.
4. Prefer a concrete question about demand, the status quo, the narrowest useful outcome, or a surprising observation over generic preference questions.
5. End with a written decision or a clearly named unresolved question. Never imply that silence or enthusiasm is approval.
6. Once the user accepts a design, hand it to `writing-plans`; do not implement it in this skill.

## Procedure

1. **Classify the conversation.** State whether this is a demand/problem diagnostic or a builder/design exploration, and say what is still unknown. Completion criterion: the mode and the initial unknown are visible in the response.
2. **Record the frame.** Maintain four short lists: `Facts`, `Assumptions`, `Unknowns`, and `Constraints`. Do not promote an assumption to a fact merely because it sounds plausible. Completion criterion: every material claim from the user is in one of the lists.
3. **Choose the next question.** Select the single question whose answer could most change the problem definition, target user, success condition, or scope. Ask it plainly and stop. Completion criterion: exactly one primary question is waiting for an answer.
4. **Synthesize alternatives.** When the problem and success condition are sufficiently clear, present two or three distinct approaches, including the smallest useful version and its trade-offs. Do not silently select one. Completion criterion: each option names its outcome, cost, risk, and non-goals.
5. **Close the decision gate.** Ask the user to choose an option or name what remains unresolved. Completion criterion: the response contains either `Decision: ...` or `Unresolved: ...`.
6. **Handoff.** For an accepted design, provide a concise problem frame and invoke or recommend `writing-plans` as the next step. The handoff includes the chosen approach, success condition, constraints, non-goals, and open questions. Completion criterion: no code or implementation plan was created by this skill.

## Clarified Problem Frame

Use this compact structure at the close:

```markdown
## Clarified problem frame
- User: [specific person or team]
- Problem: [observable pain and current workaround]
- Desired outcome: [change in user behavior or result]
- Success condition: [observable measure and time horizon]
- Facts: [evidence]
- Assumptions: [unverified beliefs]
- Constraints: [time, platform, policy, resources]
- Non-goals: [explicitly out of scope]
- Options considered: [short trade-off summary]
- Decision: [accepted option, or "unresolved"]
- Next step: [writing-plans handoff, or the one question still needed]
```

## Common Failure Modes

| Temptation | Required response |
|---|---|
| "Just start coding; we can clarify later" | Stop and ask the one question that determines the problem or success condition. |
| Treating a requested feature as the problem | Ask who has the pain, how it appears today, and what outcome would prove relief. |
| Asking five questions at once | Keep only the highest-leverage question; queue the rest. |
| Presenting a recommendation as a decision | Mark it as an option and wait for explicit acceptance. |
| A polished idea with no evidence | Label the demand claim as an assumption and ask for the strongest available observation. |

## Safety Boundary

This skill does not automatically commit, push, deploy, open pull requests, install runtimes, or mutate production. Do not commit, push, deploy, open pull requests, install runtimes, or mutate production while using it.
