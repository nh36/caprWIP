# Agent routing

There is no generic mandatory step choreography, per-message response
format, probe ritual, or command-approval tier in this repository. (An old
workflow of that kind is archived, non-authoritative, at
`docs/archive/legacy-agent-workflow.md`.)

An explicit user request to complete a task — including completing,
committing and pushing a Germanic sound-change adjudication — **is** the
authorization for the edits, commits and pushes it requires. No further
approval gate applies.

## Germanic sound-change adjudication (the default active workstream)

Use the canonical `python3 Germanic/tools/adjudicate.py` interface.
Do not search the repository, inspect
Docker mounts, locate `.bin` files, or run `foma`/`flookup` by hand.

Start at `Germanic/docs/CURRENT_STATE.md` for the canonical commands and
`Germanic/docs/RESEARCH_ADJUDICATION_PROTOCOL.md` for the scientific procedure.
`Germanic/docs/README.md` routes all other tasks and distinguishes
SOURCE / GENERATED / ARCHIVE. Do not maintain another copy of that procedure here.

## Everything else

Follow `.github/copilot-instructions.md` and the user's instruction.
Anything that runs `foma`/`flookup` runs inside the backend container
(`docker compose exec -T backend ...`); for adjudication work this is
already encapsulated by `--evidence`.
