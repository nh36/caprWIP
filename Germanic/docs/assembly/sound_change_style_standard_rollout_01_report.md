# Sound-change style standard rollout 01 report

## Summary

- The sound-change half was regenerated before and after the rollout with:
  - `bash Germanic/docs/assembly/build_sound_change_volume.sh`
  - `bash Germanic/docs/assembly/build_sound_change_volume_docker.sh`
  - `python3 Germanic/tools/audit_sound_change_report_style.py`
- Regeneration succeeded for:
  - `Germanic/docs/assembly/sound_change_volume_alpha_01.md`
  - `Germanic/docs/assembly/sound_change_volume_alpha_01.tex`
  - `Germanic/docs/assembly/sound_change_volume_alpha_01.pdf`
  - `Germanic/docs/sound_changes/change_reports/sound_change_half_coverage_report.md`
  - `Germanic/docs/sound_changes/change_reports/sound_change_style_audit.md`
- The final style audit now reports **42 reports checked, 42 reports clean**.
- The rollout revised **40 manifest-backed report files** (`pilot/` + `full/`).

## Pilot models used

The style standard was derived from the existing pilot/full report pattern, with
these files used as the explicit reference set:

- `pilot/016-020-early-vocalic-final-corridor.md`
- `full/014-015-opening-vowel-prelude.md`
- `full/018-stressed-monosyllable-o-raising-note.md`
- `full/035-037-prefix-and-compound-adjustments.md`
- `full/058-oe-nasal-dissimilation-residual-note.md`
- `full/069-early-o-shortening-context-note.md`
- `full/081-083-j-strengthening-vocalization-and-ei-contraction-bridge.md`

## STYLE_STANDARD.md

`Germanic/docs/sound_changes/change_reports/STYLE_STANDARD.md` now fixes:

- the required section sequence;
- the function of each section;
- the distinction between source tradition and CAPR implementation;
- wording rules for strong local, broad/far, boundary-limited, runner-bounded,
  negative, and technical-marker chronology evidence;
- grouped-report hierarchy rules for centers, flanks, followers, and residual
  members;
- cross-reference phrasing that keeps outward links as cross-references rather
  than larger chapter claims;
- typography rules for change IDs, rule names, linguistic forms, citations, and
  raw FOMA syntax.

## Audit script

`Germanic/tools/audit_sound_change_report_style.py` now checks every manifest-
backed pilot/full report for:

- the required `###` / `####` heading scaffold;
- missing, duplicated, unexpected, or empty sections;
- project-facing wording drift;
- chronology overclaiming in bounded or runner-limited units;
- raw FOMA syntax outside fenced `foma` blocks;
- formatting drift in exact identifiers and rule-label usage.

The script writes `Germanic/docs/sound_changes/change_reports/sound_change_style_audit.md`.

## Coverage and regeneration status

The final regenerated coverage report still states:

- ordinary chronology-card sound changes covered: **70/70**;
- covered by pilot/full production reports: **70**;
- covered by scaffold placeholders: **0**;
- grouped into multi-change units: **48 changes across 20 units**;
- every ordinary chronology card represented somewhere in the assembled half: **yes**.

The build completed without manifest/scaffold mismatch errors, so manifest/
scaffold alignment still passes.

## Human-review status

- Units left for human review by the final audit: **none**.
- Further literary refinement is optional, but no report is currently outside the
  accepted style standard.

## Scope confirmation

- No FST rules were changed.
- No TSV data files were changed.
- No chronology-card files were changed.
- No source dossiers or book dossiers were substantively changed.
- The changes in this pass are confined to the sound-change report layer, its
  schema/readme/supporting style docs, the new audit script, and regenerated
  assembly outputs.
