# OE paradigm probe skill

## Purpose

Use this skill when a lexeme report depends on comparing multiple candidate
Proto-Germanic paradigm cells against the OE target.

## What the probe must record

- which cells were generated;
- which cells were omitted and why;
- whether the morphology was hand-specified or template-generated;
- whether ProtoGate was bypassed;
- whether the winning form is unique.

## Current implementation policy

- Start with **minimal hand-specified templates** for pilot entries.
- Do not over-engineer a full Proto-Germanic morphology generator before the
  schema and pilot reports are stable.
- Use the existing deterministic OE FST stack as the evaluation target.

## Markdown output

Paradigm probes should emit a LaTeX-friendly Markdown table like:

| Cell | Candidate input | FST output | Match? | Comment |
|:---|:---|:---|:---|:---|

Use short comments and keep prose outside the table.

