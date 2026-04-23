# Skill: Sync Trace Report

**Invocation:** "sync trace report"

Bring the OE stage-by-stage tracer (`Germanic/tools/oe_full_trace_report.py`)
and the sandbox composition (`Germanic/fsts/old_english_sandbox.txt`) back
into exact agreement with the main pipeline
(`EnglishProtoToOE` in `Germanic/fsts/germanic.txt`, currently around
lines 2671-2818). Without this synchronisation the trace report is worse
than useless — it silently lies about what the real pipeline does.

## Why this skill exists

Three recurring failure modes:

1. **Silent sandbox drift.** Someone reorders or adds a rule to
   `EnglishProtoToOE` without mirroring it in `old_english_sandbox.txt`.
   The trace then shows a derivation that no real run actually produces.
2. **Tracer STAGES list drift.** The `STAGES` list in
   `oe_full_trace_report.py` stops matching the sandbox save order, so
   bins are read under the wrong label.
3. **foma 40-character name limit.** `define NAME …;` silently truncates
   network names longer than 40 characters (emits only a *warning*:
   `Network name 'X' should consist of at most 40 characters.`). The
   subsequent `regex NAME;` then matches `NAME` as a **literal string**,
   producing a 2-state 1-arc 1-path FST (~150 bytes on disk, gzipped).
   All downstream bins are poisoned by this. The symptom in the trace is
   a run of `[carry]` labels or suspicious "reverts".

## Procedure

1. **Read the main composite.** Look at the `define EnglishProtoToOE (…)`
   block in `Germanic/fsts/germanic.txt`. Write down the exact sequence
   of `.o. RuleName` lines — this is the ground truth.

2. **Diff the sandbox.** Compare the `OESandboxAfterX = OESandboxAfterPrev .o. X`
   chain in `Germanic/fsts/old_english_sandbox.txt` against the main
   composite. For every difference (missing rule, extra rule, wrong
   order, renamed rule) fix the sandbox — not the main pipeline. The
   main pipeline is the authority.

3. **Check every sandbox definition name for the 40-char limit.** Any
   `define OESandboxAfterFooBar` where `OESandboxAfterFooBar` exceeds
   40 characters will silently corrupt bins. Abbreviate. Examples that
   have already bitten us:

   | Too long (>40)                                   | Abbrev form                              |
   |--------------------------------------------------|------------------------------------------|
   | `OESandboxAfterUnstressedLongVowelShortening`    | `OESandboxAfterUnstressedLongVowShort`   |
   | `OESandboxAfterFinalGeminateSimplification`      | `OESandboxAfterFinalGemSimplif`          |
   | `OESandboxAfterPWGmcSurvivingBimoricOUnrounding` | `OESandboxAfterSurvivingBimoricOUnround` |

   Rule of thumb: `OESandboxAfter` is 14 chars, so the rule-name part
   can be at most 26 chars.

4. **Update the save-bin section** at the bottom of
   `old_english_sandbox.txt` so every new or renamed `OESandboxAfterX`
   has its corresponding `clear stack; regex …; save stack …bin` block
   in the correct order.

5. **Update the tracer STAGES list.** In
   `Germanic/tools/oe_full_trace_report.py`, the
   `STAGES: List[Tuple[str, str]]` constant (around line 40) must have
   one entry per save in the sandbox, in the same order. The tuple is
   `(label, bin_filename)`. The label is free-form (displayed in
   output); the filename must match the `save stack …bin` exactly.

6. **Rebuild the bins.** From the repo root:
   ```
   bash Germanic/tools/rebuild_oe_bins.sh
   ```
   Takes a few minutes via `docker compose exec backend`.

7. **Check for the 40-character warning** in the rebuild output:
   ```
   bash Germanic/tools/rebuild_oe_bins.sh 2>&1 | grep -iE "40 character|should consist"
   ```
   Output **must** be empty. If not, abbreviate the named defs and
   rebuild.

8. **Sanity-check bin sizes** (the real bins live in `backend/` at repo
   root, *not* in `Germanic/fsts/` — those are tiny stubs):
   ```
   ls -la backend/old_english_sandbox_after_*.bin | awk '{print $5, $NF}' | sort -n | head
   ```
   Every bin should be several kB at minimum. Sub-200-byte bins mean a
   collapsed (name-limit-poisoned) FST.

9. **Run a trace on a representative word** and eyeball the output:
   ```
   python3 Germanic/tools/oe_full_trace_report.py --output /tmp/trace.txt
   ```
   Verify the sandbox's last pre-`ProtoToOE` stage output equals the
   `ProtoToOE` stage output for at least one representative word.
   Divergence = the sandbox is still out of sync; do not declare victory.

10. **Run the mismatch report** to confirm no regression:
    ```
    python3 Germanic/tools/oe_mismatch_report.py
    head -1 Germanic/docs/debug_snapshots/oe_mismatch_report.txt
    ```

11. **Commit.** Single commit, message roughly:
    ```
    Sync OE trace report: mirror sandbox to main EnglishProtoToOE

    <list the specific rules that moved / were added / were renamed>

    Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
    ```

## Key invariants

- `Germanic/fsts/germanic.txt` `EnglishProtoToOE` is the authority.
- `Germanic/fsts/old_english_sandbox.txt` must compose the same rules in
  the same order.
- `Germanic/tools/oe_full_trace_report.py` `STAGES` must list the
  sandbox's saved bins in the same order with matching filenames.
- No sandbox `define` name may exceed 40 characters.
- The real bins are in `backend/` at the repo root. `Germanic/fsts/*.bin`
  are (mostly) not used by the tracer.

## Known trap: "intentionally divergent" sandbox comments

Past commits have left comments like "CRITICAL: OEMedUnstressedULowering
runs HERE (not in Stage 11!)" claiming the sandbox is intentionally
different from main. **Do not trust these.** Every known case has turned
out to be the sandbox being stale, not a deliberate design choice. Sync
to main and verify with a trace on a representative word.
