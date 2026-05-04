# Batch 11 summary

## Rows memoed

1. **2309 make (iptv.2sg) / maca** — **Lane 3** (`late_analogy`)
2. **1969 breeches / brēċ** — **Lane 4** (`regular`)
3. **2310 make (3sg) / macaþ** — **refill** from the next highest-risk available lane (`late_analogy`), because **lane 1 and lane 2 were exhausted**
4. **2311 bore (iptv.2sg) / bora** — **refill** from the next highest-risk available lane (`late_analogy`), because **lane 1 and lane 2 were exhausted**

## Ready for final report

- **Ready:** 1969 breeches / brēċ
- **Not yet ready:** 2309 make (iptv.2sg) / maca; 2310 make (3sg) / macaþ; 2311 bore (iptv.2sg) / bora

## Rows needing paradigm probes

- **Needs paradigm probe:** 2309 make (iptv.2sg) / maca; 2310 make (3sg) / macaþ; 2311 bore (iptv.2sg) / bora
  - `maca` needs a built-in probe covering infinitive `macian`, imperative 2sg `maca`, present 2sg, and present 3sg `macaþ`.
  - `macaþ` already has the decisive manual contrast, but still lacks a reusable built-in probe spec.
  - `bora` needs a built-in probe covering imperative 2sg, 2sg present, 3sg present, and infinitive comparators.
- **No paradigm probe needed:** 1969 breeches / brēċ

## Rows recommending TSV changes

- **1969 breeches / brēċ** — TSV `NOTE`
- **2309 make (iptv.2sg) / maca** — TSV `PROTO`, TSV `NOTE`
- **2311 bore (iptv.2sg) / bora** — TSV `NOTE`

## Rows recommending DEV_NOTES or dossier cleanup

- **2309 make (iptv.2sg) / maca** — mark old Option A/B/C exploration as superseded in `DEV_NOTES`
- **2310 make (3sg) / macaþ** — cross-link or mark old `maceþ` analysis as superseded in `DEV_NOTES`
- **2311 bore (iptv.2sg) / bora** — clean older class-II `-eþ` / `bura` diagnostic history in `DEV_NOTES`
- **1969 breeches / brēċ** — no cleanup required

## Lane usage

- **Lane 1 and lane 2 were exhausted.**
- Lane 3 and lane 4 were filled normally.
- Refill rule used: the third and fourth slots were filled from the next highest-risk remaining category, yielding two additional `late_analogy` rows (`2310 make (3sg) / macaþ`, `2311 bore (iptv.2sg) / bora`).

## Systematic workflow issues noticed

- **The remaining backlog is still dominated by specialized paradigm-cell rows.** Batch 11 again became three `late_analogy` rows plus one note-bearing regular row.
- **The class-II weak-verb micro-cluster now needs infrastructure more than interpretation.** `maca`, `macaþ`, and `bora` are largely understood, but they still need reusable built-in probe specs and clearer supersession markers in `DEV_NOTES`.
- **Regular note-bearing rows can now be closed quickly when the note is the only ambiguity.** `breeches` is a good example: the memo mostly tightens explanatory distinctions rather than changing analysis.

Batch 11 is complete. The rollout continues to the next four-row round.
