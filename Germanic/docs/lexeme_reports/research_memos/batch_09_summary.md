# Batch 09 summary

## Rows memoed

1. **2140 night / niht** — **Lane 3** (`late_analogy`)
2. **1965 brand / brandes** — **Lane 4** (`early_analogy`)
3. **2152 rest / ræste** — **refill** from the next highest-risk available lane (`late_analogy`), because **lane 1 and lane 2 were exhausted**
4. **2183 shoulder / sċuldrum** — **refill** from the next highest-risk available lane (`late_analogy`), because **lane 1 and lane 2 were exhausted**

## Ready for final report

- **Ready:** none
- **Not yet ready:** 2140 night / niht; 1965 brand / brandes; 2152 rest / ræste; 2183 shoulder / sċuldrum

## Rows needing paradigm probes

- **Needs paradigm probe:** 2140 night / niht; 1965 brand / brandes; 2152 rest / ræste; 2183 shoulder / sċuldrum
  - `night` needs at least the nom.sg. `*náxtz -> neaht` versus dat.sg. `*náxti -> niht` contrast.
  - `brand` needs a simple nom.sg. `*brándaz -> brand` versus gen.sg. `*brándas -> brandes` audit probe.
  - `rest` needs nom.sg. `*rastō -> rast` plus the oblique singular cells that converge on `ræste`.
  - `shoulder` needs a reusable probe around the winning DatPl `*skúldramiz -> sċuldrum`, with comparison cells for singular `sċuldor` and weak-feminine `sċuldra` analyses.

## Rows recommending TSV changes

- **1965 brand / brandes** — TSV `PROTOFORM`, `COUNTERPART`, `DERIVATION_CLASS`, `NOTE`
- **2152 rest / ræste** — TSV `NOTE`
- **2183 shoulder / sċuldrum** — TSV `NOTE`

## Rows recommending DEV_NOTES or dossier cleanup

- **2140 night / niht** — stale row-number hit in `DEV_NOTES`
- **1965 brand / brandes** — stale debugging/workaround framing in `DEV_NOTES`-adjacent analysis files
- **2152 rest / ræste** — superseded chronology wording in `DEV_NOTES` and `compound_archaism_inventory.md`
- **2183 shoulder / sċuldrum** — clarify superseded-vs-current status in `DEV_NOTES` and shoulder dossiers

## Lane usage

- **Lane 1 and lane 2 were exhausted.**
- Lane 3 and lane 4 were filled normally.
- Refill rule used: the third and fourth slots were filled from the next highest-risk remaining category, yielding two additional `late_analogy` rows (`2152 rest / ræste`, `2183 shoulder / sċuldrum`).

## Systematic workflow issues noticed

- **The remaining queue is now dominated by paradigm-cell work.** Batch 09 again turned into one lane-4 row plus three late-analogy rows because the higher-risk non-regular lanes are exhausted.
- **Probe formalization is now lagging behind memo quality.** All four rows can already be explained, but none is fully clear of probe/infrastructure follow-up.
- **Some rows are now exposing stale workaround residue rather than unresolved philology.** `brand / brandes` is the clearest case: the memo suggests the row should probably be normalized back to a regular citation-form mapping rather than preserved as a memo-only special case.

Batch 09 is complete. The rollout continues to the next four-row round.
