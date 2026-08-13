# SkillOpt-Inspired Skill Audit (Read-Only Baseline)

Static baseline audit. SkillOpt is primarily an optimization/evaluation framework; behavioral claims need task datasets, replay, and a held-out gate. No skill content was changed by this audit.

- Skills audited: **14**
- SKILL.md total lines: **3191**
- Supporting files: **36**
- Broken explicit local references: **0**
- Deleted-harness references in skills: **0**
- Exact duplicate long paragraphs: **0**

## Size and structure

| Skill | Lines | Bytes | Supporting files | Frontmatter | Description |
|---|---:|---:|---:|---|---|
| `brainstorming` | 250 | 15512 | 7 | yes | yes |
| `dispatching-parallel-agents` | 182 | 7038 | 0 | yes | yes |
| `executing-plans` | 69 | 2442 | 0 | yes | yes |
| `finishing-a-development-branch` | 225 | 7781 | 0 | yes | yes |
| `receiving-code-review` | 205 | 6203 | 0 | yes | yes |
| `requesting-code-review` | 95 | 2956 | 1 | yes | yes |
| `subagent-driven-development` | 580 | 33131 | 6 | yes | yes |
| `systematic-debugging` | 283 | 9465 | 10 | yes | yes |
| `test-driven-development` | 320 | 9015 | 1 | yes | yes |
| `using-git-worktrees` | 167 | 6813 | 0 | yes | yes |
| `using-superpowers` | 61 | 3016 | 2 | yes | yes |
| `verification-before-completion` | 120 | 3646 | 0 | yes | yes |
| `writing-plans` | 171 | 7265 | 1 | yes | yes |
| `writing-skills` | 463 | 17027 | 8 | yes | yes |

### Largest skills
- `subagent-driven-development` — 580 lines; prioritize for token-cost and behavioral evaluation
- `writing-skills` — 463 lines; prioritize for token-cost and behavioral evaluation
- `test-driven-development` — 320 lines; prioritize for token-cost and behavioral evaluation
- `systematic-debugging` — 283 lines; prioritize for token-cost and behavioral evaluation
- `brainstorming` — 250 lines; prioritize for token-cost and behavioral evaluation

## Findings

### Broken explicit local references
- None.

### Deleted-harness references inside skills
- None.

### Remaining non-supported harness mentions
- None.

## Prioritized audit queue

1. **P0 — Behavioral baseline:** define held-out tasks for `brainstorming`, `systematic-debugging`, `test-driven-development`, `writing-plans`, `subagent-driven-development`, and `verification-before-completion`; record baseline outcomes before edits.
2. **P1 — Compression:** `writing-skills` already split into references (679→463). Next candidates: `subagent-driven-development` (568) and `test-driven-development` (320).
3. **P1 — Subagent over-dispatch:** addressed for `subagent-driven-development`, `dispatching-parallel-agents`, `executing-plans`, and `writing-plans` (default is now inline; subagents gated on plan size).
4. **P1 — Workflow overlap:** compare `writing-plans`, `executing-plans`, `subagent-driven-development`, `requesting-code-review`, and `finishing-a-development-branch` for repeated gates.
5. **P2 — Small skills:** audit the remaining skills after the large-skill pass.

## Recommended next step

Run SkillOpt-style gated evaluation one skill at a time: baseline representative tasks, propose bounded edits, replay held-out tasks, and adopt only changes that preserve or improve the gate score. Keep each candidate change separately reviewable.
