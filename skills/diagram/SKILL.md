---
name: diagram
description: Use when a process or architecture needs an editable diagram.
---

# Diagram

Turn a verified description into an editable, source-first diagram. Mermaid remains the default source for simple flows and architecture; provide editable Excalidraw JSON only when the user explicitly requests an editable hand-drawn visual artifact. Render SVG or PNG only after a local renderer is verified; never pretend that an unrendered source is a finished image.

## When to Use

- A user asks to make, draw, create, or explain a process, architecture, flowchart, or dependency diagram.
- A repository or project needs a durable visual artifact linked from its documentation.
- A user wants to revise an existing diagram from its editable source.

Do not invent missing nodes, relationships, ownership, or data flow. If the request is incomplete, state the unknowns and ask focused questions before finalizing the diagram.

## Prerequisites

- Identify the diagram subject, audience, source evidence, and desired format.
- Check whether `C:\Users\Givemore\Desktop\Sentio-OS` exists before writing durable project artifacts. If it is missing, report the missing path and ask before creating or using another vault; do not substitute another vault.
- Prefer repository paths and inspected code as the source of truth for architecture. Never read, print, or copy credentials or equivalent sensitive material, including secrets, `.env` contents, tokens, private keys, or sensitive logs.
- Do not install a runtime or renderer as part of this workflow.

## Source-First Contract

1. Emit the editable source before any rendered output.
2. Use Mermaid source for simple flowcharts, pipelines, hierarchies, sequence diagrams, and state diagrams. Prefer `graph LR` for flows and `graph TD` for hierarchies; keep labels short and put detail on edges.
3. Emit Excalidraw JSON only when the user explicitly requests an editable hand-drawn scene. Renderer support for conversion does not by itself authorize Excalidraw JSON. State when a diagram type is not Excalidraw-editable.
4. Render SVG and PNG only when a verified local Mermaid renderer is available. If there is no renderer, save or show the source and report `No renderer verified; rendering was not run.`
5. Treat the source as the single source of truth for revisions. Change the source, then re-render; never edit a rendered image as if it were the model.

## Procedure

1. **Clarify the model.** Extract nodes, relationships, direction, boundaries, inputs, outputs, and audience from the request and inspected source. For an incomplete request, list missing relationships and ask the smallest useful question instead of guessing. Completion criterion: each drawn relationship is either evidenced or explicitly accepted by the user.
2. **Choose the format.** Use Mermaid for a simple or code-review-friendly diagram. Use Excalidraw JSON for editable visual layout when requested. Split diagrams when a single view would exceed a readable number of nodes; explain the split. Completion criterion: format and scope are recorded.
3. **Write the source first.** Create the Mermaid source, or the requested Excalidraw JSON, in the relevant project artifact location. For durable Sentio-OS context, use `C:\Users\Givemore\Desktop\Sentio-OS\01-Projects\<Project>\diagrams\` and link the artifact from that project's README. Keep repository code and architecture claims traceable to repository paths. Completion criterion: the editable source exists and is readable before rendering begins.
4. **Detect a renderer.** Check for a local renderer using available local or repository tooling without installing anything. Confirm that the renderer can process this diagram type. If it is absent or fails, stop at source delivery and report the limitation honestly. Completion criterion: any claimed SVG or PNG has a renderer check and observed output behind it.
5. **Render and validate.** When available, render SVG and PNG from the source. For a flowchart, generate Excalidraw JSON only when the user explicitly requested it and the conversion succeeds. If parsing fails, show the error, fix the source, and retry; do not deliver a broken rendered artifact. Completion criterion: each delivered artifact opens or parses successfully, or is clearly labeled unrendered.
6. **Deliver with links.** List the source, optional Excalidraw JSON, and verified SVG/PNG paths. Link the source from the relevant README or documentation index. For a user revision, edit the source and repeat renderer verification. Completion criterion: the user can find the editable source and understands any renderer limitation.

## Format Guidance

| Need | Preferred output | Boundary |
|---|---|---|
| Simple flow or architecture | Mermaid source | Keep relationships evidence-based. |
| Hand-editable visual scene | Excalidraw JSON plus source | Do not claim editability if conversion was not verified. |
| Documentation image | Verified SVG, optionally PNG | Never fabricate a render or use a CDN fallback. |
| Incomplete request | Source only after clarification, or an explicit draft with unknowns | Do not silently fill gaps. |

## Safety Boundary

This skill does not automatically perform side effects. Do not automatically commit. Do not automatically push. Do not automatically deploy. Do not automatically open a pull request. Do not automatically install a runtime. Do not automatically mutate production while using it. It does not automatically open files or applications. It may write requested diagram artifacts, but it must not change implementation or production configuration.

## Upstream Source

Normalized from the exact upstream document: https://raw.githubusercontent.com/garrytan/gstack/main/diagram/SKILL.md
