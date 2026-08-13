---
name: hermes-cron-management
description: Manage Hermes cron jobs with clear, safe workflows.
version: 0.1.0
author: Theophilus Chinomona, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [hermes, cron, scheduling, automation]
    related_skills: [using-superpowers]
---

# Hermes Cron Management Skill

Use Hermes' native cron interfaces to inspect, create, edit, pause, resume,
run, remove, and audit scheduled jobs. Prefer the `cronjob` tool for actions
from an agent session; use the `terminal` tool with the `hermes cron` CLI when
the user explicitly needs a shell command or when a complete table is easier
to inspect.

## When to Use

- The user asks to list, organize, create, change, pause, resume, run, or
  delete Hermes scheduled jobs.
- The user asks whether a cron job is active, what it last did, or why it did
  not run.

Don't use this skill for operating-system Task Scheduler or external cron
implementations unless the user explicitly asks for those.

## Prerequisites

- A configured Hermes profile and access to its cron store.
- For `cronjob`, use the current profile unless the user names another one.
- Never guess a job ID. List jobs first and use the returned ID.

## Quick Reference

Agent tool:

- `cronjob(action="list")`
- `cronjob(action="create", schedule=..., prompt=..., name=..., repeat=...)`
- `cronjob(action="update", job_id=..., schedule=..., prompt=..., ...)`
- `cronjob(action="pause", job_id=...)`
- `cronjob(action="resume", job_id=...)`
- `cronjob(action="run", job_id=..., prompt=...)`
- `cronjob(action="remove", job_id=...)`

CLI through `terminal`:

- `hermes cron list --all`
- `hermes cron create --help`
- `hermes cron edit --help`
- `hermes cron pause --help`
- `hermes cron resume --help`
- `hermes cron run --help`
- `hermes cron remove --help`
- `hermes cron runs --help`
- `hermes cron status`

## Procedure

1. **Discover.** For an inventory, call `cronjob(action="list")`. For a shell
   view, run `hermes cron list --all` through `terminal`. Capture each job's
   ID, name, schedule, enabled state, and next/last run fields.
2. **Organize.** Present jobs in a stable order: enabled state, next run,
   then name. Group paused/disabled jobs separately. Do not claim a job is
   missing until both the default list and an all-jobs list have been checked.
3. **Create.** Confirm the schedule and the exact prompt/action. Call
   `cronjob(action="create", schedule=..., prompt=..., name=...)`. Include
   `repeat` only when the user asks for a finite number of runs. Report the
   returned job ID.
4. **Change.** List first, select the exact job ID, then call
   `cronjob(action="update", job_id=..., ...)`. Preserve unspecified fields;
   do not overwrite a job with guessed defaults.
5. **Pause or resume.** List first, then call `cronjob(action="pause", job_id=...)`
   or `cronjob(action="resume", job_id=...)`. Verify with another list call.
6. **Run now.** Use `cronjob(action="run", job_id=...)` only when the user
   requests an immediate run. This schedules the next tick; it is not a
   promise that delivery has already completed. Inspect execution history
   afterward with `hermes cron runs` through `terminal` when needed.
7. **Remove.** Treat removal as destructive. Verify the selected job's name,
   schedule, and prompt before calling `cronjob(action="remove", job_id=...)`.
   Re-list afterward and report the result.
8. **Verify.** For any mutation, perform a fresh list/status check and report
   actual tool output. If a job failed, inspect `hermes cron runs` and do not
   invent a cause.

## Pitfalls

- `cronjob(action="run")` fires in the background and returns before the run
  finishes; do not report completion from the trigger alone.
- `--all` is required to include disabled jobs in CLI inventory output.
- Job IDs are opaque and must come from a live list operation.
- Cron sessions use the configured profile and delivery target; do not expose
  credentials or copy secrets into prompts.
- A schedule can be valid while its delivery target or script fails; inspect
  execution history to distinguish those cases.

## Verification

A management operation is complete only when the mutation returned without an
error and a subsequent list/status/history check confirms the expected state.
For a full inventory, verify that the number of displayed jobs matches the
`--all` listing and that every job is represented exactly once.
