# Skill: Mismatch Loop

**Invocation:** "mismatch loop", "run a mismatch pass", "let's pick off
some mismatches"

> ## ⛔ STOP — HARD GATE BEFORE ANY EDIT
>
> **No edit to `germanic.txt`, `*.tsv`, or any pipeline file may be
> proposed until a draft of the §17.10.X DEV_NOTES section for this
> iteration exists on disk.**
>
> The reasoning, sources, and proposed change MUST be written into
> `Germanic/docs/DEV_NOTES.md` first — not just discussed in chat.
> Source-audit notes typed into the chat thread are NOT a substitute
> for the DEV_NOTES draft. (See "Anti-patterns" at the end.)
>
> Recommended SQL gate at the start of each iteration:
>
> ```sql
> INSERT INTO todos (id, title, description) VALUES
>   ('loop-NN-devnotes',  'Draft §17.10.X for [PROTOFORM]', '...'),
>   ('loop-NN-implement', 'Apply rule/TSV change for [PROTOFORM]', '...'),
>   ('loop-NN-verify',    'Rebuild + report + commit',    '...');
> INSERT INTO todo_deps (todo_id, depends_on) VALUES
>   ('loop-NN-implement', 'loop-NN-devnotes'),
>   ('loop-NN-verify',    'loop-NN-implement');
> ```
>
> Do not mark `loop-NN-devnotes` done until the section is appended to
> `DEV_NOTES.md` and (preferably) committed. Do not start
> `loop-NN-implement` until then.

The mismatch loop is the project's standard work cycle: pick a
PROTOFORM that the FST gets wrong, decide what's wrong, fix it
Lautgesetzlich-ly, prove the fix doesn't regress anything else, write
it up, commit. Repeat. The mismatch count is the project's headline
metric.

Closely related skills (read them too):

- `skills/be-lautgesetzlich.md` — the *philological* discipline that
  governs *which kind* of fix is allowed (phonology > analogy > target
  retargeting; chronology first; sources before guesses).
- `skills/fst-build-and-tokenize.md` — the *mechanical* discipline:
  how to rebuild bins, how to read `+?` and `[carry]`, how to add a
  `pgrmWeakTailVowel` clause.
- `skills/sync-trace-report.md` — when the trace report has drifted
  out of sync with the real pipeline.

This skill is the *workflow* that ties them together.

---

## The loop, at a glance

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Read the mismatch report; pick a candidate              │
│ 2. Triage: TSV bug? Data exception? Phonology? Analogy?    │
│ 3. Trace the candidate stage by stage; isolate the failure │
│ 4. Consult sources before proposing a fix (be-lautgesetz.) │
│ 5. Write up the diagnosis + plan in DEV_NOTES first        │
│ 6. Implement the fix (one rule change OR one TSV edit)     │
│ 7. Rebuild bins (fst-build-and-tokenize)                   │
│ 8. Re-run mismatch report; verify count drops, no new      │
│    regressions in unrelated rows                            │
│ 9. Trace the candidate end-to-end; confirm clean derivation │
│10. Commit (single focused commit; descriptive message)     │
│11. Push                                                    │
└─────────────────────────────────────────────────────────────┘
```

Stop after each iteration. Don't bundle multiple fixes into one
commit; each candidate gets its own DEV_NOTES section and its own
commit so future you can revert one thing without reverting another.

---

## 1. Read the report and pick a candidate

```bash
python3 Germanic/tools/oe_mismatch_report.py
head -80 Germanic/docs/debug_snapshots/oe_mismatch_report.txt
```

The report has four sections you care about:

1. **INTERVENTION SUMMARY** — counts by category. Use this to size
   the work.
2. **CORE BUCKETS** — clearly phonological misses (breaking,
   palatalisation, long-vowel, etc.). These are usually the ripest
   fruit.
3. **OTHER SUB-BUCKETS** — finer-grained categorisation
   (`vowel_quality__u_lowering_exception`, `cons_mismatch__þ_vs_d__intervocalic`,
   etc.).
4. **DETAILED EXAMPLES** — the actual `*proto -> got (expected …)`
   lines, plus the bucket script's own >> ISSUE / >> LIKELY / >> ACTION
   commentary.

### How to choose a candidate

In rough order of preference:

| Priority | Bucket signal | Why |
|----------|---------------|-----|
| ⭐⭐⭐ | `TSV/data fixes needed` (intervention summary) | Cheapest; PROTOFORM clearly wrong, no FST change. |
| ⭐⭐⭐ | Single bucket containing one item, especially a CORE bucket | Single, well-isolated failure ⇒ low risk of side effects. |
| ⭐⭐  | Bucket containing 2–4 related items | Same root cause ⇒ one fix clears multiple. Higher payoff. |
| ⭐⭐  | `_exception` buckets if you have a hypothesis | Often a chronology problem. |
| ⭐   | `_other`, `cons_mismatch__*` | Often idiosyncratic; harder to fix without regression. |
| ✗   | Anything already in `Documented exceptions` | Don't touch unless re-opening it. |

Avoid big buckets (e.g. `final_vowel_missing__weak_noun_like (4)` if
you have no theory) early — they may turn out to require a structural
change you don't want to commit to in a single iteration.

---

## 2. Triage the candidate

Quick gate questions (in order):

1. **Is the PROTOFORM itself reasonable?** Sanity check against
   Kroonen / R/T / Orel. If the PROTOFORM is unreconstructable,
   that's a TSV/data fix.
2. **Is the OE target attested in the form claimed?** Check
   Bosworth-Toller, Hall, Campbell. Sometimes the target is wrong.
3. **Is `+?` (no output)?** Tokenisation problem — go straight to
   `skills/fst-build-and-tokenize.md` §6 (pgrmWeakTailVowel).
4. **Is the output the right *shape* but with one wrong segment?**
   Phonology rule problem — proceed to step 3 (trace).
5. **Is the output something completely unexpected?** Probably a
   rule fires at the wrong stage; trace will show.

### Honest framings the loop demands

- "It's regular sound change" vs "it's analogy". Reading
  `skills/be-lautgesetzlich.md` is **not** optional here — it's the
  project's policy on which kind of fix is even permitted.
- "Phonology change" vs "PROTOFORM retargeting" vs "OE target
  retargeting". All three are sometimes correct. The right one is the
  one supported by the philological literature.
- "Fix one rule" vs "rule X needs reordering". Reordering is much
  riskier than adding a clause; it ripples across the whole pipeline.

---

## 3. Trace the candidate

Use the stage-by-stage tracer:

```bash
python3 Germanic/tools/oe_full_trace_report.py
grep -A 40 'YOUR_PROTOFORM' Germanic/docs/debug_snapshots/oe_full_trace_report.txt
```

What to look for:

- The first stage at which the form *diverges from your expectation*.
  That's the rule (or absence of rule) to scrutinise.
- `[carry]` at every stage = tokenisation failed; not a phonology
  problem (see fst-build-and-tokenize §5).
- `[carry]` at one specific stage = that rule didn't fire on a
  legitimate input. Check that rule's environment in `germanic.txt`.
- Output unchanged across many stages until one big jump = a single
  rule did all the (correct or incorrect) work; that's where to look.

Print or paste the trace into your DEV_NOTES section. The trace is
the evidence.

---

## 4. Consult sources first

Before proposing a fix, search for the relevant phenomenon in:

```bash
grep -inE 'YOUR_TERM|YOUR_PHENOMENON' docs/references/*.txt
```

Catalogue (already maintained in `Germanic/docs/REFERENCES.md`):

- **First-pass authorities**: Hogg vol. 1, Ringe-Taylor vol. 2,
  Ringe vol. 1.
- **OE handbooks**: Campbell, Brunner, Luick, Bülbring.
- **Etymological dictionaries**: Kroonen, Orel, Seebold, Bosworth-
  Toller, Hall.

If two sources disagree, that's interesting and goes into DEV_NOTES.
If sources are silent, that's also interesting (and a warning).

The discipline:

- A fix you can support with at least one explicit citation is
  preferred to a fix that is "phonologically reasonable".
- A fix that contradicts the consensus is a red flag — write up *why*
  you're departing.
- "Analogical" claims must cite the source making the analogy claim
  (not just hand-wave). If the sources don't say "analogical", default
  to phonological treatment.

---

## 5. Write up DEV_NOTES first (before any code change)

Open `Germanic/docs/DEV_NOTES.md`. Find the most recent §17.10.x
section. Add §17.10.(x+1) with:

```markdown
### §17.10.X Case N — [PROTOFORM] → [target] ([one-line summary])

**Mismatch as observed** (from oe_mismatch_report.txt):

```
*PROTOFORM -> GOT (expected EXPECTED)
>> ISSUE: ...
```

**Trace** (relevant excerpt from oe_full_trace_report.txt):

```
ProtoInput:                  *…
StageThatMatters:            *…
…
```

**Source audit:**

- Campbell §X — quote/paraphrase
- R/T vol. 2 §X — quote/paraphrase
- ...

**Diagnosis**: [what the trace plus sources say is wrong]

**Plan**: [exactly what change to make, where, and why]

**Risk assessment**: [what could regress; how to verify it doesn't]
```

Commit this DEV_NOTES update *before* the implementation commit. That
way the research is in git history even if the implementation later
turns out to be wrong.

---

## 6. Implement the fix

Make the *minimum* change that the plan calls for. Resist scope creep.

Common fix patterns:

| Pattern | Where | Risk |
|---------|-------|------|
| TSV cell edit (PROTOFORM, TOKENS, target) | `Germanic/data/germanic-aligned-final.tsv` | Lowest |
| Add `pgrmWeakTailVowel` clause for new paradigm cell | `germanic.txt` ~line 365–438 | Low |
| Add a new rule clause (`X -> Y || A _ B`) | `germanic.txt` rule body | Medium |
| Add a brand-new `define` and slot it into composite | `germanic.txt` + `EnglishProtoToOE` body + sandbox + tracer | High |
| Reorder rules in composite | `EnglishProtoToOE` body + sandbox + tracer | Highest |

Anything Medium-or-higher should also update
`Germanic/fsts/old_english_sandbox.txt` and verify with
`skills/sync-trace-report.md`.

---

## 7. Rebuild bins

```bash
bash Germanic/tools/rebuild_oe_bins.sh 2>&1 | tee /tmp/build.log
grep -iE "should consist of at most 40 character" /tmp/build.log   # MUST be empty
```

If the warning fires, see `skills/sync-trace-report.md` step 3.

---

## 8. Re-run the mismatch report

```bash
python3 Germanic/tools/oe_mismatch_report.py
head -1 Germanic/docs/debug_snapshots/oe_mismatch_report.txt
```

Three possibilities:

1. **Count went down**: ✓ continue.
2. **Count unchanged**: the fix didn't take effect on the target row,
   or it fixed one and broke one. Diff before/after (e.g. cache the
   old report at `/tmp/old.txt`) and inspect.
3. **Count went up**: regression. Stop. Diff the report. Either fix
   the regression in the same iteration or revert.

A drop of 1 is fine and normal. A drop of 2+ from a single fix is
suspicious — verify the secondary drops are *correct* fixes, not
accidental rule shadowing.

---

## 9. Trace the candidate end-to-end

```bash
python3 Germanic/tools/oe_full_trace_report.py
grep -A 40 'YOUR_PROTOFORM' Germanic/docs/debug_snapshots/oe_full_trace_report.txt
```

Verify the derivation now matches the philological story you wrote
in DEV_NOTES.

---

## 10. Commit

One commit per fix. Message format:

```
[scope]: [one-line summary] (mismatches N → N-1)

DEV_NOTES §17.10.X — [Case label].

[2-3 sentences explaining what changed and why, in the abstract.]

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
```

Stage:

- `Germanic/data/germanic-aligned-final.tsv` (if TSV change)
- `Germanic/fsts/germanic.txt` (if rule change)
- `Germanic/fsts/old_english_sandbox.txt` (if sandbox needed sync)
- `Germanic/fsts/old_english.bin` (foma-built; commit alongside source)
- `backend/*.bin` (commit alongside source — see fst-build-and-tokenize §1)
- `Germanic/docs/DEV_NOTES.md` (the §17.10.X writeup)
- `Germanic/docs/debug_snapshots/oe_mismatch_report.txt`
- `Germanic/docs/debug_snapshots/oe_full_trace_report.txt`

If DEV_NOTES was already committed in step 5 separately (preferred),
just add a one-line forward reference: "Implementation of §17.10.X."

---

## 11. Push

```bash
git push
```

---

## Stop conditions for the loop

A single sitting should usually be one to three iterations. Stop if:

- The next candidate would require structural reordering — write a
  plan in DEV_NOTES and pause for review.
- Two consecutive iterations introduced regressions.
- The mismatch count goes *up* with no explanation.
- A bucket reveals a phenomenon you don't have sources for. Pause and
  research first; don't guess.

When you stop, the working tree should be clean (everything committed
and pushed) and the mismatch report's headline number should reflect
the current state.

---

## Anti-patterns

- **Bundling fixes**: one commit covering three unrelated rows. Makes
  it impossible to revert one without losing the others.
- **Skipping DEV_NOTES**: implementation lands without a written
  rationale. Two months later no one (including you) remembers why.
- **"Just try it"**: making a rule change without first reading the
  cited section of the relevant grammar.
- **Ignoring `+?` candidates as "phonology bugs"**: they're almost
  always tokenisation. See fst-build-and-tokenize §5.
- **Calling everything analogical**: see `be-lautgesetzlich.md` —
  default is phonological; analogy must be explicitly cited.
- **Touching a "documented exception" bucket without re-opening it**:
  these were closed for a reason; the reason should be in DEV_NOTES.
  Re-read the original closure note before reopening.
- **Reordering rules to fix one form**: high regression risk. If
  reordering really is the answer, it deserves its own multi-iteration
  research arc, not a quick mismatch-loop pass.

---

## Quick reference — useful commands

```bash
# State
head -1 Germanic/docs/debug_snapshots/oe_mismatch_report.txt
git status --short

# Pick a candidate
sed -n '1,80p' Germanic/docs/debug_snapshots/oe_mismatch_report.txt

# Trace one form
python3 Germanic/tools/oe_full_trace_report.py
grep -A 40 'YOUR_PROTOFORM' Germanic/docs/debug_snapshots/oe_full_trace_report.txt

# Apply a single PGmc → OE
echo 'PROTOFORM_NO_LEADING_STAR' | docker compose exec -T backend \
    bash -lc 'cd /usr/app && flookup -i old_english.bin'

# Source search
grep -inE 'YOUR_TERM' docs/references/*.txt | head

# Rebuild
bash Germanic/tools/rebuild_oe_bins.sh

# Re-verify
python3 Germanic/tools/oe_mismatch_report.py
head -1 Germanic/docs/debug_snapshots/oe_mismatch_report.txt
```
