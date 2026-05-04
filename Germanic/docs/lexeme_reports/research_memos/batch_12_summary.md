# Batch 12 summary

## Rows memoed

1. **2312 bore (3sg) / boraþ** — **Lane 3** (`late_analogy`)
2. **1975 calf / ċealf** — **Lane 4** (`regular`)
3. **2313 learn (iptv.2sg) / liorna** — **refill** from the next highest-risk available lane (`late_analogy`), because **lane 1 and lane 2 were exhausted**
4. **2314 learn (3sg) / liornaþ** — **refill** from the next highest-risk available lane (`late_analogy`), because **lane 1 and lane 2 were exhausted**

## Ready for final report

- **Ready:** 1975 calf / ċealf
- **Not yet ready:** 2312 bore (3sg) / boraþ; 2313 learn (iptv.2sg) / liorna; 2314 learn (3sg) / liornaþ

## Rows needing paradigm probes

- **Needs paradigm probe:** 2312 bore (3sg) / boraþ; 2313 learn (iptv.2sg) / liorna; 2314 learn (3sg) / liornaþ
  - `boraþ` needs a built-in probe covering 3sg, 2sg, imperative, infinitive `borian`, and optionally non-`j` infinitive comparators.
  - `liorna` needs a saved learn-specific probe covering at least infinitive `liornian`, imperative `liorna`, and 3sg `liornaþ`.
  - `liornaþ` needs the same learn-specific probe family; the manual 3sg contrast is already good, but no reusable built-in probe exists yet.
- **No paradigm probe needed:** 1975 calf / ċealf

## Rows recommending TSV changes

- **1975 calf / ċealf** — TSV `NOTE`
- **2312 bore (3sg) / boraþ** — TSV `NOTE`
- **2313 learn (iptv.2sg) / liorna** — TSV `NOTE`
- **2314 learn (3sg) / liornaþ** — TSV `NOTE`

## Rows recommending DEV_NOTES or dossier cleanup

- **2312 bore (3sg) / boraþ** — clean older `boreþ` / class-II `-eþ` history in `DEV_NOTES`
- **2313 learn (iptv.2sg) / liorna** — mark old `*lezn-` workaround as superseded in `DEV_NOTES`
- **2314 learn (3sg) / liornaþ** — mark old `*leznōθi` / `leorneþ` and stale analysis references as superseded in `DEV_NOTES` / related analysis files
- **1975 calf / ċealf** — no cleanup required

## Lane usage

- **Lane 1 and lane 2 were exhausted.**
- Lane 3 and lane 4 were filled normally.
- Refill rule used: the third and fourth slots were filled from the next highest-risk remaining category, yielding two additional `late_analogy` rows (`2313 learn (iptv.2sg) / liorna`, `2314 learn (3sg) / liornaþ`).

## Systematic workflow issues noticed

- **The remaining queue is now mostly small paradigm clusters.** Batch 12 was another three-row `late_analogy` micro-cluster plus one note-bearing regular row.
- **Saved probes are lagging behind memo confidence.** The learn and bore rows are analytically stable enough for memo purposes, but they still need reusable built-in probes before the presentation layer will be tidy.
- **Northumbrian-vs.-West-Saxon framing needs consistent prose discipline.** The learn rows especially need the final reports to separate live Northumbrian targets from older West-Saxon-oriented workaround history.

Batch 12 is complete. The rollout continues to the next four-row round.
