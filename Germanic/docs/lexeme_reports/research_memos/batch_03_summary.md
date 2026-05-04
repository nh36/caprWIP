# Batch 03 summary

## Rows memoed

1. **2013 fire / fȳre** — **Lane 1** (`known_unmodelled`)
2. **2087 knob / cnobba** — **Lane 2** (`reconstructed_oe`)
3. **1946 berry / berġes** — **Lane 3** (`late_analogy`)
4. **1949 bier / bǣr** — **Lane 4** (`regular` with non-empty `NOTE`)

## Ready for final report

- **Ready:** 1946 berry / berġes; 1949 bier / bǣr
- **Not yet ready:** 2013 fire / fȳre; 2087 knob / cnobba

## Rows needing paradigm probes

- **Needs paradigm probe:** 2013 fire / fȳre; 1946 berry / berġes
  - For **1946**, the existing nom.sg./gen.sg. probe is already sufficient.
  - For **2013**, the current probe is too narrow and should be expanded beyond the dat.sg.-only pilot.
- **No paradigm probe needed:** 2087 knob / cnobba; 1949 bier / bǣr

## Rows recommending TSV changes

- **2013 fire / fȳre** — TSV `PROTO`, TSV `NOTE`
- **2087 knob / cnobba** — TSV `PROTO`, TSV `PROTOFORM`, TSV `COUNTERPART`, TSV `DERIVATION_CLASS`, TSV `NOTE`
- **1946 berry / berġes** — TSV `NOTE`
- **1949 bier / bǣr** — TSV `NOTE`

## Rows recommending DEV_NOTES or dossier cleanup

- **2013 fire / fȳre** — light `DEV_NOTES` cleanup to mark the old retarget-to-`fȳr` state as superseded
- **2087 knob / cnobba** — `DEV_NOTES` cleanup plus `docs/references/README_knob.md` revision
- **1946 berry / berġes** — clearer marking of stale berry history in `DEV_NOTES.md` and `analysis/final_vowel_missing_analysis.md`
- **1949 bier / bǣr** — optional light cleanup of stale `*barwōn` diagnostic prose

## Lane usage

- No lane was exhausted or skipped.
- No refill rule was needed.
- The round again followed the preferred one-per-lane layout exactly.

## Systematic workflow issues noticed

- **Some rows are not merely memo-ready; they are row-redesign-ready.** `2087 knob / cnobba` is the clearest case so far: the memo points toward a likely retargeting rather than a simple lexeme-report write-up.
- **Lexeme-headword vs derivational-input conflation is still recurring.** `2013 fire / fȳre` and `1946 berry / berġes` both needed explicit memo-stage correction of `PROTO` versus `PROTOFORM`.
- **Packets still over-surface historical debugging states.** This remains manageable, but it means memo authors must keep doing substantial repo follow-up instead of trusting packet weighting alone.
- **Supplementary lexical tables remain useful but weak.** In this round they were consistently secondary to repo-local dictionaries, reference extracts, and DEV_NOTES chronology.

Batch 03 is complete. The rollout continues to the next four-row round.
