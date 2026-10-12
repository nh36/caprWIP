# Batch 10 summary

## Rows memoed

1. **2184 shove / sċēaf** — **Lane 3** (`late_analogy`)
2. **1968 breast / brēost** — **Lane 4** (`early_analogy`)
3. **2203 span / spanne** — **refill** from the next highest-risk available lane (`late_analogy`), because **lane 1 and lane 2 were exhausted**
4. **2250 thistle / þistles** — **refill** from the next highest-risk available lane (`late_analogy`), because **lane 1 and lane 2 were exhausted**

## Ready for final report

- **Ready:** 1968 breast / brēost; 2203 span / spanne
- **Not yet ready:** 2184 shove / sċēaf; 2250 thistle / þistles

## Rows needing paradigm probes

- **Needs paradigm probe:** 2184 shove / sċēaf; 2203 span / spanne; 2250 thistle / þistles
  - `shove` still needs a reusable built-in probe covering infinitive, 1/3 sg. preterite, pret. plural, and past participle.
  - `span` already has a sufficient built-in probe, but it remains a paradigm-cell row and should still be tracked as such.
  - `thistle` already has an initial probe, but it should be expanded to include nominative `*θístilaz` and another oblique/plural control cell.
- **No paradigm probe needed:** 1968 breast / brēost

## Rows recommending TSV changes

- **1968 breast / brēost** — TSV `NOTE`
- **2250 thistle / þistles** — TSV `NOTE`

## Rows recommending DEV_NOTES or dossier cleanup

- **1968 breast / brēost** — clarify stale March-April 2026 column-history wording in `DEV_NOTES`
- **2184 shove / sċēaf** — optionally mark old 3pl `*skúbun -> sċufon` resolution more explicitly as superseded
- **2203 span / spanne** — clean stale `*spannăi` and stale row-number references in `DEV_NOTES` / `prosodic_tier_research.md`
- **2250 thistle / þistles** — clarify superseded March-2026 thistle history and the stale `*θístilaz` vs `*θéstilaz` wording in `DEV_NOTES`

## Lane usage

- **Lane 1 and lane 2 were exhausted.**
- Lane 3 and lane 4 were filled normally.
- Refill rule used: the third and fourth slots were filled from the next highest-risk remaining category, yielding two additional `late_analogy` rows (`2203 span / spanne`, `2250 thistle / þistles`).

## Systematic workflow issues noticed

- **The remaining queue continues to be mostly paradigm-cell work.** Batch 10 again became three `late_analogy` rows plus one lane-4 row because the higher-risk non-regular lanes are exhausted.
- **Probe quality is now uneven rather than simply missing.** `span` is already in good shape, `thistle` has a starter probe that needs widening, and `shove` still lacks a reusable built-in spec.
- **Some rows are now mainly documentation-cleanup cases.** `breast` is analytically settled; what remains is making sure packets and future reports do not overread stale column-history material as current guidance.

Batch 10 is complete. The rollout continues to the next four-row round.
