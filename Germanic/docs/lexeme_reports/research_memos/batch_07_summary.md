# Batch 07 summary

## Rows memoed

1. **2273 wasp / wæfs** — **Lane 2** (`attested_variant`)
2. **2058 have / hæfeþ** — **Lane 3** (`late_analogy`)
3. **1959 bottom / botm** — **Lane 4** (`early_analogy`)
4. **2068 heaven / heofon** — **refill** from the next highest-risk available lane (`late_analogy`), because **lane 1 was exhausted**

## Ready for final report

- **Ready:** 2273 wasp / wæfs; 1959 bottom / botm
- **Not yet ready:** 2058 have / hæfeþ; 2068 heaven / heofon

## Rows needing paradigm probes

- **Needs paradigm probe:** 2058 have / hæfeþ; 2068 heaven / heofon
  - Both rows still need built-in probe specs even though the core memo conclusions are already fairly stable.
- **No paradigm probe needed:** 2273 wasp / wæfs; 1959 bottom / botm

## Rows recommending TSV changes

- **2058 have / hæfeþ** — TSV `NOTE`
- **1959 bottom / botm** — TSV `NOTE`
- **2068 heaven / heofon** — TSV `NOTE`

## Rows recommending DEV_NOTES or dossier cleanup

- **2058 have / hæfeþ** — stale `DEV_NOTES` wording
- **1959 bottom / botm** — optional light `DEV_NOTES` cross-reference cleanup
- **2068 heaven / heofon** — `DEV_NOTES` cleanup
- **2273 wasp / wæfs** — no cleanup required

## Lane usage

- **Lane 1 was exhausted.**
- Lane 2, lane 3, and lane 4 were filled normally.
- Refill rule used: the fourth slot was filled from the next highest-risk remaining category, yielding a second `late_analogy` row (`2068 heaven / heofon`).

## Systematic workflow issues noticed

- **The rollout has now entered the stage where refill behavior matters.** Lane 1 exhaustion is real, and the lane-based scheduler is behaving as intended.
- **A growing share of remaining rows need probe infrastructure more than argument discovery.** `have` and `heaven` are good examples: the memo stage can already explain the solution, but the reusable probe layer still lags.
- **Attested-variant rows can now be relatively low-friction.** `wasp` required almost no data changes once the packet and repo-local philology were checked carefully.

Batch 07 is complete. The rollout continues to the next four-row round.
