# SC058 / SC021 / SC022 / heaven-stage repair (2026)

Focused repair of the sound-change publication layer so the FST, sound-change
inventory, reader-facing chapter, lexical analyses, historical-stage metadata,
and generated book tell one historically defensible story. No corpus-score
optimisation; no SC renumbering.

## A. SC058 (build unblock)

SC058 `OENasalDissimilation` was a dead rule already removed from the FST,
inventory, staging map, and aliases, but its reader-facing chapter
`058-nasal-dissimilation.md` (heading `## SC058.`) survived and was still listed
in every reader-facing `chapter_files`. `check_reader_facing_section_order.py`
rejected it (`Unknown SC id SC058`), blocking authoritative section-19
regeneration.

Fix (mechanical): removed the `058-nasal-dissimilation.md` entry from all
reader-facing build scripts and deleted the orphaned chapter. SC057 and SC059
are now adjacent (a numbering gap at 058, no renumbering). Its mn-dissimilation
history is covered by the SC022 chapter and the SC022 dossier. Reader-facing
section 19 now regenerates from canonical sources.

## B. SC021 - RETAIN (unwitnessed)

SC021 `PNWGmcUnstressedORaising` (`{*o} -> {*u} || V C+ _ C* {*ų}`) is a genuine
Northwest Germanic change (Fulk 7.31: an-stem acc.sg. `*-onų > *-unų`). Its only
former corpus witness was heaven via the discarded `*xémonų` analysis. Empirical
status now: no selected input in the 380-row corpus carries `*ų`, so SC021 fires
on **0 rows** (full trace: 0 firings). It is retained as historically genuine but
**presently unwitnessed**; the FST rule is unchanged (inert, fires 0 times ->
cascade baseline unchanged). Reader-facing chapter and inventory updated;
`witness_count` is defined as the number of current selected derivations in which
the rule fires.

## C. SC022 - reconcile (witness = stem)

SC022 `PNWGmcMnDissimilation` is the literal adjacent `mn > βn`
(`{*m} -> {*β} || EnglishStarVocalic _ {*n}`), unchanged. Full trace: fires on
exactly **1 row, stem** (`*stámni > *stáβni`). heaven is **not** a direct
row-level witness (the selected `*xébun > heofon` path begins after the labial
was generalised); it remains deeper comparative/paradigmatic evidence (ON
himinn : hifni). The reader-facing SC022 chapter already stated this; the stale
aggregate and the inventory (`example_lexemes` heaven -> stem) are corrected. The
old cross-syllable `mV...n` proxy is absent from all current generated material.

## D. Heaven stage - Northern West Germanic (`nsgmc`)

Ringe & Taylor reconstruct `*hebun` as **northern West Germanic**, not
undifferentiated Proto-West Germanic. A new controlled domain code was added:

- `nsgmc` - **Northern West Germanic** (North Sea Germanic / Ingvaeonic): the
  innovating northern dialect area *within* West Germanic, ancestral to
  Anglo-Frisian and shared with Old Saxon (OE heofon, OS heban).

This is deliberately distinct from `pnwgmc` (Proto-Northwest Germanic, the common
ancestor of North + West Germanic - a different node) and narrower than `pwgmc`.
Ordered between `pwgmc` and `paf`. heaven's `*xébun` / `*hebun` / `*hebunas`
migrated `pwgmc -> nsgmc` (sidecar, model-entry markup, reader-facing section 21).
The deeper PGmc mn-obliques (`*xémenaz`, `*xémnas`, ...) stay `pgmc`.

The stage ontology is explicitly **not** a single linear chain: reconstruction
domains may branch/overlap, and the historical analysis determines the taxonomy.

## E. One-string-one-stage invariant (removed)

The earlier test asserted "no reconstructed form string may occur at more than
one stage". That is conceptually wrong - an unchanged spelling can persist across
stages, and distinct reconstructions may share a spelling. Replaced with a
per-occurrence invariant (each indexed occurrence has exactly one valid stage; no
identical occurrence carries conflicting stages), plus a lexeme-specific
regression that the single reconstruction `*hebun` is not re-split across stages.

## F. Sidecar moved upstream

`entry_stage_metadata.tsv` moved `docs/assembly/ -> Germanic/data/`: historical
judgments belong with the corpus data, upstream of assembly. Single canonical
copy; `build_class_manifests.py` reads the new path.

## G. Deferred: source (`h`) vs canonical (`x`) index normalisation

The printed index can still list both `*hebun` (Ringe & Taylor's spelling) and
`*xébun` (CAPR canonical) as separate headwords for the same nominative lexeme.
Preferred policy: keep source notation in running prose, but emit the canonical
`*xébun` headword in the index (via a `*hebun -> see *xébun` cross-reference or
`display=`-based canonical emission), while keeping the genuinely distinct
inflectional form `*hebunas` separate. The index has no alias / canonical-emission
mechanism today; building a general one is substantial and is **deferred to a
separate task**. This is *not* solved merely because both spellings now share the
`nsgmc` stage label - it remains open.

## Invariants preserved

germanic.txt rule bodies (SC021 retained/inert, SC022 unchanged), TSV rows
2068/2216, cascade baseline **380 / 373 / 7 / 0** (`outputs_sha256 a72bdeb8...`),
mismatch set (buck, fire, fowl, rust, tap, wolf, wool) - all unchanged. This pass
is sound-change presentation + historical-stage metadata only.
