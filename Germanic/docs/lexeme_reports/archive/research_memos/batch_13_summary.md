# Batch 13 summary

## Rows memoed

1. **2315 lick (iptv.2sg) / licca** — **Lane 3** (`late_analogy`)
2. **1979 corn / corn** — **Lane 4** (`regular`)
3. **2316 lick (3sg) / liccaþ** — **refill** from the next highest-risk available lane (`late_analogy`), because **lane 1 and lane 2 were exhausted**
4. **2317 show (iptv.2sg) / sċēawa** — **refill** from the next highest-risk available lane (`late_analogy`), because **lane 1 and lane 2 were exhausted**

## Ready for final report

- **Ready:** 1979 corn / corn
- **Not yet ready:** 2315 lick (iptv.2sg) / licca; 2316 lick (3sg) / liccaþ; 2317 show (iptv.2sg) / sċēawa

## Rows needing paradigm probes

- **Needs paradigm probe:** 2315 lick (iptv.2sg) / licca; 2316 lick (3sg) / liccaþ; 2317 show (iptv.2sg) / sċēawa
  - `licca` needs a built-in probe covering infinitive `liccian`, imperative `licca`, and 3sg `liccaþ`.
  - `liccaþ` needs the same lick-specific probe family; the manual contrast is already clear, but no reusable built-in probe exists yet.
  - `sċēawa` needs a built-in probe covering infinitive `sċēawian`, imperative `sċēawa`, and 3sg `sċēawaþ`, with optional 2sg present expansion.
- **No paradigm probe needed:** 1979 corn / corn

## Rows recommending TSV changes

- **1979 corn / corn** — TSV `NOTE`
- **2315 lick (iptv.2sg) / licca** — TSV `PROTO`, TSV `NOTE`
- **2316 lick (3sg) / liccaþ** — TSV `NOTE` (optional clarification)
- **2317 show (iptv.2sg) / sċēawa** — TSV `NOTE`

## Rows recommending DEV_NOTES or dossier cleanup

- **2315 lick (iptv.2sg) / licca** — mark old `liċca` / `lecca` regression history as superseded in `DEV_NOTES`
- **2316 lick (3sg) / liccaþ** — mark old `licceþ` expectations as superseded in `DEV_NOTES`
- **2317 show (iptv.2sg) / sċēawa** — clean older `scēawa` normalization history and wrong “Class II noun” label in `DEV_NOTES`
- **1979 corn / corn** — no cleanup required

## Lane usage

- **Lane 1 and lane 2 were exhausted.**
- Lane 3 and lane 4 were filled normally.
- Refill rule used: the third and fourth slots were filled from the next highest-risk remaining category, yielding two additional `late_analogy` rows (`2316 lick (3sg) / liccaþ`, `2317 show (iptv.2sg) / sċēawa`).

## Systematic workflow issues noticed

- **The remaining queue is still dominated by weak-verb paradigm-cell clusters.** Batch 13 continued the same pattern as batches 11-12.
- **Built-in probe coverage is the main blocker now.** The lick and show rows are largely understood, but they still need reusable saved probes rather than more interpretive research.
- **Some regular rows now need only note cleanup.** `corn` is a good example: the analysis is stable, and the remaining work is just clarifying that note-mentioned oblique forms are background rather than live FST input.

Batch 13 is complete. The rollout continues to the next four-row round.
