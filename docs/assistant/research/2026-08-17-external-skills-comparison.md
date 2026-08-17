---
type: research
status: open
created: 2026-08-17
tags:
  - superpowers
  - gstack
  - hallmark
  - taste-skill
  - plugin-design
---

# External skills comparison: gstack, Hallmark, Taste Skill

## Sources

- [gstack](https://github.com/garrytan/gstack)
- [Hallmark](https://github.com/nutlope/hallmark)
- [Taste Skill](https://github.com/Leonxlnx/taste-skill)
- [Taste Skill website](https://www.tasteskill.dev/)

All three projects present MIT licensing in their published source material. License compatibility does not remove the need to preserve attribution and review imported instructions before integration.

## Observed roles

### gstack

A broad product-delivery operating system for Claude Code and other agent hosts. Its catalog covers product discovery, scope review, engineering review, design review, DX review, code review, browser QA, security, documentation, release, retrospectives, diagrams, and memory.

High-value candidates:

- `office-hours`
- `plan-ceo-review`
- `plan-eng-review`
- `plan-design-review`
- `plan-devex-review`
- `spec`
- `cso`
- `document-release`
- `document-generate`
- `learn`
- `retro`
- `diagram`

Overlap candidates that should be adapted rather than duplicated:

- `investigate` with `systematic-debugging`
- `review` with `requesting-code-review`
- `qa` with `vibetest`
- `ship` with `finishing-a-development-branch`

Operational or host-specific commands should be deferred until their side effects and Hermes compatibility are explicitly reviewed:

- deployment and merge commands
- browser-cookie setup
- agent tunneling and pairing
- automatic update and telemetry behavior

### Hallmark

A design-quality protocol with four modes:

- default design flow
- `audit`
- `redesign`
- `study`

Notable rules include structural variety, honest content, locked tokens, responsive checks, complete interaction states, focus accessibility, pre-emit self-critique, and explicit safety rails for existing projects. Hallmark is the strongest candidate for a shared design-quality layer.

### Taste Skill

A frontend visual-quality catalog. Its main default skill infers design direction and tunes variance, motion, and density. Other skills cover redesigns, minimalist UI, output completeness, image-to-code, image generation, and visual style variants.

Best candidates for selective adaptation:

- `design-taste-frontend`
- `redesign-existing-projects`
- `minimalist-ui`
- selected output-completeness rules

Defer by default:

- `gpt-taste`, because its mandatory GSAP, randomization, and AIDA rules are too prescriptive for a general plugin
- image-generation skills, because they are a separate capability and require an image-generation workflow
- importing every visual style variant, because that would create skill sprawl

## Recommendation

Keep Superpowers Lite's existing engineering workflow as the canonical core. Add selected gstack product, architecture, security, documentation, and research workflows. Use Hallmark as the main design-quality protocol and borrow focused Taste rules for frontend visual judgment.

Normalize imported Markdown into the repository's shared `skills/` format. Do not copy third-party installers blindly: each source targets different hosts, paths, dependencies, and lifecycle behaviors.

No plugin implementation has been approved yet; this note records the research and the proposed direction only.
