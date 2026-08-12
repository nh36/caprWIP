# Cleanup audit: removal of the redundant SC058 `OENasalDissimilation`

**Type:** backend technical consolidation (dead-code removal). **Not** a
historical redesign of SC022. **No lexical behavior change.**
**Branch:** `stem-row-2216-correction` · **HEAD at start:** `c710ba17`.
Cross-references: `dossier-sc022-mn-dissimilation-2026.md`,
`audits/2216-stefn-shadow-rule-probe.md`.

## 1. Why two rules existed

CAPR carried **two** nasal-dissimilation rules that both modelled the
`heaven`-type `mV…n` history:

- **SC022 `PNWGmcMnDissimilation`** (`germanic.txt:2151`, cascade pos 22,
  PNWGmc): `{*m} -> {*β} || V _ V C* N`. Output `*β` → surface `f`. Fires on
  `heaven` (`*xémunų → *xéβunų`).
- **SC058 `OENasalDissimilation`** (formerly `germanic.txt:2668`, cascade
  pos 55, OE): `{*m} -> {*f} || ShortV _ ShortV {*n} [ShortV | .#.]`. Output
  `*f` directly. Same worked example (`*hemunaz → *hefunaz → heofon`), same
  citations (K-S s.v. Himmel; Campbell §381).

They are redundant: the later SC058 duplicated a subset of the earlier SC022.

## 2. Proof that SC058 was dead (shadowed by SC022)

**A. Environment is a strict subset.** `EnglishStarShortVowel ⊂
EnglishStarVocalic` (SC058's short vowels are all in SC022's vowel class,
which additionally includes long vowels and diphthongs); `{*n} ⊂
EnglishStarNasal = {*m|*n}`; SC058's zero-consonant slot is covered by SC022's
`EnglishStarConsonant*`; and SC058 adds an extra `[ShortV|.#.]` right-context
restriction. So every `*m` matchable by SC058 is matchable by SC022.

**B. Reachability.** SC022 (pos 22) runs first and rewrites all such `*m → *β`.
No rule between SC022 and SC058 (a) restores `*β → *m` (the only `*β`-rule is
`{*β} -> {*b}` before `*b`), or (b) creates a new non-geminate `*m` in the
`ShortV _ ShortV n` context. The only `*m`-outputs anywhere are geminate `*mm`
(PWGmcJGemination, which runs *before* SC022 and is explicitly excluded by
SC058) and word-final `*m` (OEWeakTailNasalLoss, which runs *after* SC058 and
has no following `n`). So SC058's actionable input is empty when reached.

**C. Empirical (production cascade).** Using the actual sandbox stage bins,
`OENasalDissimilation` fires on **0 of 380** OE corpus rows (the stage before
SC058 equals the stage after SC058 for every row). An isolated build of the
rule confirms it is well-formed (non-vacuous by construction) but starved
in-cascade.

## 3. Zero-diff evidence

A shadow cascade with SC058 removed was compared against production over the
full 380-row OE corpus:

- **Changed lexical rows: 0.**
- Totals identical: prod = shadow = accepted 380, matched 372, mismatched 8,
  ambiguous 0. Mismatch set identical (buck, fire, fowl, rust, stem, tap,
  wolf, wool).
- `heaven` identical (`heofon`), via SC022's `*m→*β`.
- Synthetic forms built to satisfy SC058's environment
  (`xamunaz→hafon`, `xemunaz→heofon`, `stemun→steofon`) are identical prod vs
  shadow — SC022 consumes them first.

After editing the **actual** production source, the recompiled FST gives the
identical totals and mismatch set, and `heaven = heofon`. All 8 HARD-GATE
conditions pass.

## 4. What was removed

| File | Change |
| :-- | :-- |
| `Germanic/fsts/germanic.txt` | removed `OENasalDissimilation` comment + define; removed both `.o. OENasalDissimilation` composition refs |
| `Germanic/fsts/old_english_sandbox.txt` | removed the `SOENasalDissimilation` stage + its `save stack …oe_nasal_dissimilation.bin` (rechained `SOEBackMutation` to `SOEJClusterCoalescence`) |
| `Germanic/tools/oe_full_trace_report.py` | removed the `OENasalDissimilation` STAGES entry |
| `sound_change_inventory.tsv` | removed the SC058 row |
| `sound_change_historical_staging_map.tsv` | removed the SC058 row |
| `sound_change_aliases.tsv` | removed the two SC058 rows |
| `cascade_baseline/cascade_order_manifest.tsv` | regenerated from germanic.txt (83 → 82 positions) |

**SC022 `PNWGmcMnDissimilation` is byte-unchanged.** The K-S s.v. Himmel and
Campbell §381 citations from the removed comment are preserved in
`dossier-sc022-mn-dissimilation-2026.md` (§2, §20).

Not touched (intentionally): `germanic-aligned-final.tsv`, row 2068, row 2216,
`cascade_baseline_outputs.tsv`, `cascade_baseline_summary.json` (lexical
`outputs_sha256` unchanged — behavior identical), `cascade_order_manifest_frozen.tsv`
(historical snapshot; no test compares current-vs-frozen), reader-facing prose.

## 5. Test integrity

All host-runnable registry/cascade tests pass after the change:
`test_rule_registry`, `test_cascade_baseline`, `test_historical_partial_order`,
`test_cascade_interaction` (28 tests), plus `test_sc004_*` and
`test_english_apply_down_stats` (35 total). `cascade_order_manifest.py --check`
passes (manifest is an exact projection of the edited germanic.txt). The
executable **rule count legitimately drops by one** (structural metadata); the
**lexical baseline is unchanged** (scientific behavior).

## 6. Reader-facing propagation (Part 7 — audit only, not rewritten)

Both rules currently surface as **separate** reader-facing sound changes, so
the book effectively narrates the `heaven` `mV…n` dissimilation **twice**:

1. **SC022** → `reader_facing/022-mn-dissimilation.md`.
2. **SC058** → `reader_facing/058-nasal-dissimilation.md`, the
   `change_reports/full/058-oe-nasal-dissimilation-residual-note.md`, the
   `literature_dossiers/058-…dossier.md`, the chronology card
   `order_tests/chronology_cards/SC058-…md`, and the assembled
   `assembly/sound_change_volume_alpha_01.md`/`.tex` ("OE Nasal Dissimilation
   residual note", plus the inventory table row `058`).

- **Placed at different chronological positions:** yes — SC022 is PNWGmc
  (pos 22), SC058 was OE (pos 55).
- **Auto-generated vs hand-written:** the *registries/manifest/chronology graph*
  are generated from the FST metadata (now cleaned of SC058, so any fresh
  regeneration drops it); the *reader-facing prose chapters* and the *assembled
  book* are committed artifacts that will **not** auto-update.
- **Will deleting the backend rule auto-eliminate the duplicate reader-facing
  entry?** Partially — future regeneration of inventories/graphs excludes
  SC058, but the committed `058-*.md` chapters, the chronology graph
  (`order_tests/chronology_graph/first_break_*`), and the assembled
  `sound_change_volume_alpha_01.{md,tex}` still contain SC058 and require a
  later publication-cleanup pass.
- **Remaining human-facing reconciliation:** remove/merge the SC058 chapter and
  residual note into the SC022 treatment; regenerate the sound-change volume and
  chronology graph; decide SC-numbering (leave a gap at 058, as with other
  skipped SC numbers, or renumber — a later decision). **Deferred by design.**

## 7. Heaven's current data and the future probe (Part 8 — audit only)

Row **2068** (unchanged):
- PROTO `*xémenaz`; PROTOFORM `*xémonų`; COUNTERPART `heofon`;
  DERIVATION_CLASS `late_analogy`.
- NOTE: "PGmc mn-stem acc.sg. `*xemonų` (Kroonen p.220, Fulk §6.14). Derives via
  o-raising (`*o→*u` before `*ų`), mn-dissimilation (`*m→*β`), back umlaut
  (`*e→*eo`), trisyllabic apocope (`*ų→Ø`)."
- Current trace: `*xémonų → *xémunų → SC022 *xéβunų → … → heofon`.

The SC022 dossier established that `heaven` is historically an **mn-stem**
(nom. `*hemina-` vs oblique `*hemnaz`; ON `himinn`/dat. `hifni`), and that the
labial comes from the **oblique `-mn-` cluster**, not from the surface
intervocalic `mV…n`. The current PROTOFORM `*xémonų` is the vowel-retaining
form that the surface SC022 environment happens to catch.

**Future probe (do NOT implement now):** test whether an oblique/allomorphic
input carrying the `-mn-` cluster (e.g. an oblique-based `*hemn-` form such as
gen. `*hemnaz` / dat. `*hemni`) derives `heofon` through a historically
faithful adjacent-`mn` treatment of SC022 — i.e. replace the surface `mV…n`
approximation with the mn-stem cluster input. This is entangled with the
adjacent-`mn` question for row 2216 and with the SC022 environment redesign.

## 8. What remains for the later SC022/heaven redesign (explicitly deferred)

- Historically correct input representation for `heaven` (oblique mn-stem vs the
  current surface `mV…n` approximation).
- Whether to add **adjacent `mn`** to SC022 (shadow-tested clean for `stefn`).
- SC022 **environment** reformulation (segmental surface generalization vs
  cluster) and consolidation of the now-single rule.
- SC022 **name/stage** (`PNWGmc` vs Common-Germanic cluster change + NWGmc
  leveling; "dissimilation" vs allomorphy).
- **Row 2216** `*stámniz -> stefn` production decision (with the `*stab-`
  caveat).
- Reader-facing publication cleanup of the removed SC058 chapter/volume.

**This task consolidated duplicate backend machinery only. The historical
sound-change redesign is a separate, later task.**
