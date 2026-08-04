# Reconciliation of early-stage classification conflicts (Phase 2)

This document reconciles, per audited rule, the CAPR research layers — the
staging map (`sound_change_historical_staging_map.tsv`), the inventory, the full
change reports, the literature and book dossiers, the chronology cards, and the
reader-facing prose. The staging map is treated as an index of prior decisions,
not as independently authoritative: where it disagrees with the sourced research
layers, the sourced layers govern.

Only rules with a real agreement/contradiction finding are discussed
individually; the 20 `no_change` rules were verified against their reader-facing
prose and agree across layers (Northwest-Germanic `NWGmc*` rules genuinely are
Northwest Germanic per Ringe & Taylor; pan-WGmc `PWGmc*` rules carry no northern
hedge).

## Cross-cutting findings

1. **FST name vs historical stage.** Four internal identifiers assert a stage
   the sourced research contradicts: `PGmcRhotacism` (SC003), `PGmcFinalZDeletion`
   (SC020), `NWGmcNasalSpirantLengthening`/`Loss` (SC026/SC027). In every case the
   *metadata* stage in the staging map already matches the research (wgmc,
   ingvaeonic); only the Foma identifier is a legacy error. Resolvable by rename.

2. **Staging `cascade_position` is the SC ordinal, not the executable position.**
   The staging map's `cascade_position` equals the SC number; the true executable
   order (`cascade_order_manifest.tsv`) differs (e.g. `PWGmcFinalBareALoss` is
   executable position 38, not 41; `NWGmcInStemNLoss` is 61, not 64; `PGmcRhotacism`
   is not in `EnglishProtoToOE` at all — it is composed earlier in
   `PGmcConsonantRules`). Downstream tooling must read the manifest, not the
   staging ordinal.

3. **Stage ≠ cascade position is legitimate for FST-dependency rules.** SC016,
   SC049, SC050 sit at cascade positions that diverge from their historical stage
   for documented computational reasons. These are not contradictions; they are
   technical dependencies that the prose/trace must explain rather than "fix".

## Per-rule reconciliation

### SC012 `PWGmcLThVoicing` — CONTRADICTION (staging over-claims)

- Staging map: `hist_stage=pwgmc`, `hist_scope=pan_wgmc`, `confidence=A`,
  `chronology_problem=none`, notes "no staging issue".
- Reader-facing (`012-lth-voicing.md`), full change report, and literature
  dossier: all three state the change is **northern West Germanic**, citing
  Ringe & Taylor pp.170–171, and the change report and reader prose **explicitly
  reject** an unqualified pan-PWGmc conclusion ("Neither a pan-PWGmc attribution
  nor an exact local placement follows from the evidence"). Campbell §414 gives a
  broad "West Germanic" formulation.
- **Resolution (from cited sources):** narrow scope `pan_wgmc → north_wgmc`,
  downgrade confidence `A → B`, and correct the internal name's pan-PWGmc
  implication. The chronology is boundary-only on both sides, so no positive
  local seam is claimed. This is a `metadata_or_prose_only` action; no move.

### SC003 `PGmcRhotacism` — name error only (layers otherwise agree)

- Staging map already records `hist_stage=wgmc` and flags the name as a legacy
  identifier. Reader-facing (`003-west-germanic-rhotacism.md`) and change report
  state the label is "historically misleading: a later West Germanic rhotacism,
  not a Proto-Germanic one" (Ringe & Taylor pp.52, 98, 102; Crist 2001 pp.104–106,
  2002 pp.1,4; Hogg p.37).
- **Resolution:** the sole error is the Foma identifier. Rename to a West
  Germanic label. Terminus ante quem before SC044 OEBreaking is lexically forced
  (A). The historical "after final-*z* deletion" relation (Crist) is implemented
  by scoping rhotacism to non-final contexts, not by ordering — record, do not
  "fix". Keep distinct from SC020.

### SC020 `PGmcFinalZDeletion` — name error + open scope

- Staging `hist_stage=wgmc`; reader-facing (`020-wgmc-final-z-deletion.md`) and
  dossier: pan-WGmc final-*z* loss, not Proto-Germanic (Hogg p.37; Crist 2002 p.1).
  Position is well-constrained lexically: SC019 NWGmcFinalLongORaising < SC020 <
  SC040 OEMedUnstressedULowering (both A).
- **Resolution:** rename to a West Germanic label. **Genuine open question:** exact
  scope (all-WGmc vs Ingvaeonic) and the precise relation to SC003 rhotacism
  (final vs medial *z; bleeding via context-scoping). Flag for joint SC003/SC020
  scope audit; do not force a scope value now.

### SC004 `PWGmcAiMonophthongization` — CONFLATION (analytical question)

- The FST composes three rewrites: `*ai→*ē /_#`, `*ai→*ā`, `*ái→*ā`. Reader-facing
  (`004-...md`): the word-final reduction is an early Northwest-Germanic vowel
  shift (Ringe & Taylor pp.40–41); the nonfinal `*ai>*ā` generalization is
  "stated more sharply than in the current handbook discussion" and its "broader
  chronology remains less certain."
- **Resolution:** `definitely_conflated`. The word-final `*ē` component is early
  NWGmc and well-supported; the nonfinal generalization is model-sharpened and
  less securely dated. Action `split_rule` (candidate). No rename until the split
  decision is made (renaming a conflated rule first would be premature). Lexically,
  SC004 precedes OEInterStressRaising (A: *sáiwalō > sāwol).

### SC026 / SC027 `NWGmcNasalSpirant*` — name error (metadata already correct)

- Staging already `hist_stage=ingvaeonic`, `hist_scope=north_sea_germanic`. The
  full change report states CAPR's `NWGmc` labels "should be read as an analytic
  split of one broader North Sea Germanic / Ingvaeonic development" (Campbell §121;
  Fulk §4.11; Luick §§299, 301.1; Sievers-Brunner §186.1; Ringe & Taylor
  pp.140–141).
- **Resolution:** rename both internal identifiers away from `NWGmc`. The two-rule
  model split is defended (the transducer needs the conditioning string visible for
  the vowel effect before nasal deletion) — keep the split, correct the names. The
  SC026 < SC027 corridor is lexically forced (A: fist/goose/youth). Earlier boundary
  runner-limited; no positive later boundary through order 86.

### SC064 `NWGmcInStemNLoss` — GENUINE GAP (registry-internal contradiction)

- Registry-internal conflict: `hist_stage=nwgmc` but `v1_chapter=4` (Anglo-Frisian→
  OE); `confidence=C`. The change report treats it as a narrow, witness-driven
  (*furht-* / `fright` → `fyrhte`; Kroonen p.201) late *n-loss operating in the OE
  post-apocope tail, whose late position after OE High Vowel Apocope is well
  supported cross-source (Ringe & Taylor vol.2 pp.71–72; Campbell §§472–473; Brunner
  §280; Fulk §7.34; Bammesberger §7.3.4).
- **Resolution:** none yet. The cascade *position* (after high-vowel apocope) is
  well-justified, but the *stage label* is genuinely unresolved: the `NWGmc` name
  conflicts with OE-adjacent operation and the chapter-4 assignment, while the
  phenomenon itself may be older. Action `defer_unresolved`; do not force a stage.

### SC016 / SC049 / SC050 — apparent position conflict, actually FST dependency

- SC016 `OEWsPalatalGlide` (OE West Saxon; Campbell §44) sits at executable
  position 13, before many Northwest-Germanic rules, because *júką > ġeoc* requires
  glide insertion before SC017 u-lowering. SC049 `PGmcBAllophony` (Hogg pp.101–102;
  Ringe & Taylor p.121) sits late (46) because [β] must surface only on singleton
  *b after SC010 j-gemination. SC050 `SieversLawSyncope` (Adamczyk 2001; Fulk §6.15)
  sits at 47 as a feeder into OE palatalization.
- **Resolution:** no contradiction. Stage and cascade position legitimately
  diverge by documented computational dependency; the correction is `prose/trace`
  clarity, not a move.

## Summary of resolution status

| Rule | Finding | Resolvable from cited sources? |
| --- | --- | --- |
| SC012 | staging over-claims pan-PWGmc | yes — narrow to north_wgmc, B |
| SC003 | FST name legacy (PGmc→WGmc) | yes — rename |
| SC020 | FST name legacy; scope open | name yes; scope/rhotacism relation = open |
| SC004 | conflation of two developments | analytical — split decision needed |
| SC026/027 | FST name legacy (NWGmc→NSG) | yes — rename; keep model split |
| SC064 | registry-internal stage/chapter conflict; C | no — genuine gap, defer |
| SC016/049/050 | stage ≠ position | not a conflict — document dependency |

No external research was required at this phase: every contradiction was
resolvable from, or explicitly identified as a gap by, the sources already cited
in the CAPR archive. External research should be reserved for the two genuine
open questions (SC020 exact scope / rhotacism relation; SC064 stage), if the
existing dossiers prove insufficient when those are taken up.
