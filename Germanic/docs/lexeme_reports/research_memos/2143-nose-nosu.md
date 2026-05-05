# Research memo — 2143 nose / nosu

## Starting point

- **ID:** 2143
- **CONCEPT:** nose
- **COUNTERPART:** nosu
- **PROTO:** *nasō
- **PROTOFORM:** *núsō
- **DERIVATION_CLASS:** early_analogy
- **NOTE:** empty

The live row already encodes a three-way distinction: cognate-set `PROTO = *nasō`, project input `PROTOFORM = *núsō`, and OE target `nosu`. The row has no note, so the rationale currently lives in packeted `DEV_NOTES` material rather than in the TSV itself.

## Packet evidence assessment

**Authoritative/current in the packet:**

- The live TSV row is current: it keeps `*nasō` as the cognate-set proto, `*núsō` as the derivational input, and `nosu` as the OE target.
- The compact derivation trace is current and matches the live debug snapshot: `*núsō > *nósō > *nósu > nosu`.
- The `DEV_NOTES` section at `§15.3` is current project evidence that the earlier TSV `PROTOFORM *násō` was corrected to `*núsō` because Campbell explicitly cites OE `nosu < *nusō` [@Campbell1959].
- The later `DEV_NOTES` rule-order material at `§17.10.24` is current implementation evidence that `*núsō > nosu` depends on U-lowering preceding final `*ō`-raising.

**Useful background but not final authority:**

- The packet's Kroonen quotation is good etymological background for the Germanic ablaut pair `*nasō- ~ *nusō-` and for treating `*nus-` as a secondary zero-grade remodeling [@Kroonen2013].
- The Ringe-Taylor quotation on surviving OE u-stems is good philological background for `nosu` as an early OE feminine u-stem [@RingeTaylor2014].
- The lexical-table hits from `old_english_wiktionary.tsv` and `old_english_swadesh.tsv` are useful confirmation that the project's target form is attested in repo-local source tables, but they are supplementary rather than decisive.

**Stale or superseded material:**

- Older project history in which the row effectively behaved as `*nasō > nosu` is superseded. The packet already preserves the correction away from that state.
- Any project prose that still pairs `*nasō` directly with `nosu` is stale relative to the live TSV and current trace.

**Irrelevant or misleading material:**

- The packet has no row-specific dossier or analysis hit; that absence should not be read as evidence that no further repo research exists.
- Generic regression-cluster notes mentioning row 2143 are implementation diagnostics, not independent philological authority.

## Additional repo research

Checked beyond the packet:

- `Germanic/docs/DEV_NOTES.md` at `§15.3` and `§17.10.24`, to separate the settled TSV correction from later rule-order debugging.
- `Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md`, which confirms the live compact trace still outputs `nosu` from `*núsō`.
- `Germanic/docs/lexeme_reports/coverage_audit.md`, which confirms there is no pilot/full report yet for row 2143.
- `Germanic/docs/germanic_transducer_report.md`, which still contains stale historical prose listing `*nasō → nosu` and so should not be treated as current authority.
- `docs/references/campbell_old_english_grammar.txt`, especially §116 and §613, for `nosu < *nusō` and for the noun's u-stem status [@Campbell1959].
- `docs/references/ringe_taylor_linguistic_history_vol2.txt`, for `nosu` among the few surviving early OE u-stems [@RingeTaylor2014].
- `docs/references/orel_handbook_germanic_etymology.vision.txt`, which gives the broader cognate-set headword `*nasō` and OE `nasu`; this is useful for the etymological headword level, but not sufficient for the row's chosen OE target [@Orel2003].
- `docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt` and `docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt`, which confirm `nosu` as a dictionary form and also show related variation such as gen./dat. `nosa` and separate `nasu` material [@ClarkHall1960].

No row-specific dossier or analysis file was named in the packet or TSV note, and a repo search found no separate `nose/nosu` dossier beyond these materials.

## Reconstruction and early-stage forms

This row needs a strict three-part distinction.

- **Cognate-set proto / etymological headword:** `*nasō`, the full-grade form reflected elsewhere in the Germanic set and retained in TSV `PROTO` [@Kroonen2013; @Orel2003].
- **Project input form used for derivation:** `*núsō`, the zero-grade/remodeled variant chosen in TSV `PROTOFORM` because it is the stage that yields OE `nosu` and is explicitly supported by Campbell's `nosu < *nusō` [@Campbell1959].
- **OE target represented by the row:** `nosu`, the attested Old English form the row is meant to generate.

The current project solution is therefore not "change the cognate-set proto to `*núsō`" but "keep `*nasō` at the cognate-set level while feeding the remodeled zero-grade `*núsō` into the OE cascade." That is an early-stage stem/ablaut choice, not a late OE repair.

The live derivational sequence is the one shown in the packet and debug snapshot:

1. `*núsō` (project PGmc input)
2. `*nósō` (NWGmc U-lowering)
3. `*nósu` (NWGmc final long `*ō` raising)
4. `nosu` (OE surface)

By contrast, `*nasō` would yield `nasu`, not `nosu`; that full-grade route is relevant as background because it explains dictionary/headword variation, but it is not the row's intended derivation.

## Old English philology

`nosu` is an attested OE form, not a reconstruction. The philological issue is not whether the target exists, but which pre-OE stem shape best underlies it.

- Campbell uses `nosu < *nusō` as a phonological example and later treats `nosu` as one of the relic u-stems [@Campbell1959].
- Ringe & Taylor likewise list `nosu` among the few early OE feminine u-stems [@RingeTaylor2014].
- Clark Hall gives `nosu` with gen./dat. `nosa`, confirming ordinary dictionary treatment of the form as an OE noun [@ClarkHall1960].
- Bosworth-Toller separately preserves both `nosu` and `nasu` material, which means the repo should not collapse all OE nose forms into a single headword without comment [@BosworthToller1898].
- Orel's `*nasō ... OE nasu` is useful as broader etymological background, but for this row it is secondary to the more specific evidence tying `nosu` to `*nusō` [@Orel2003; @Campbell1959].

So the memo should treat `nosu` as the row's attested OE citation target, while acknowledging that `nasu` also exists in the lexicographical record and likely reflects the full-grade side of the same ablaut/remodeling history. No stronger dialect or manuscript claim is needed on current repo evidence.

## Project problem and solution

The project problem had two layers:

1. an older data problem, where the row paired `PROTOFORM *násō` with expected `nosu`, even though that input actually yields `nasu`; and
2. a later implementation-order problem, where one regression temporarily blocked the now-correct `*núsō > nosu` derivation until U-lowering and final-`*ō` raising were put back into the right order.

The current solution is coherent:

- keep `TSV PROTO = *nasō` for the cognate set;
- keep `TSV PROTOFORM = *núsō` for the derivational input actually represented by the row;
- keep `COUNTERPART = nosu` as the OE target; and
- treat the row as `early_analogy`, because the special move is an upstream ablaut/stem selection before the ordinary OE sound changes apply.

That solution is better than either of the alternatives the repo history implies:

- `*nasō > nosu`, which is simply inconsistent with the current cascade; or
- rewriting the whole row so that both `PROTO` and `PROTOFORM` become `*núsō`, which would hide the broader cognate-set etymology.

## Paradigm probe

A paradigm probe is **not required** for this row.

This is not a late paradigm-cell case like `ban`, `berry`, or `span`, and the row does not target a non-lemma oblique form. The issue is the early selection of the zero-grade/remodeled PGmc input `*núsō`, not uncertainty about which OE paradigm cell should be represented. The current evidence base is therefore sufficient without a dedicated `oe_paradigm_probe.py` run.

## Recommended final report

Recommend a short final report that foregrounds the three-way distinction `*nasō` (cognate-set proto) vs. `*núsō` (project input) vs. `nosu` (attested OE target), cites Campbell and Kroonen for the zero-grade/remodeled variant, and notes that older project prose pairing `*nasō` directly with `nosu` is superseded.

## Data-change recommendations

- **TSV `PROTO`:** **no change recommended.** `*nasō` is still useful as the cognate-set headword.
- **TSV `PROTOFORM`:** **no change recommended.** `*núsō` is the correct row-level input for `nosu`.
- **TSV `COUNTERPART`:** **no change recommended.** `nosu` is the right OE target for this row.
- **TSV `DERIVATION_CLASS`:** **no change recommended.** `early_analogy` is appropriate because the special choice happens before the OE sound changes, at the ablaut/stem-selection level.
- **TSV `NOTE`:** **change recommended.** Add a short note explaining that `PROTO` keeps the full-grade cognate-set form `*nasō`, while `PROTOFORM *núsō` is the zero-grade/remodeled variant required for OE `nosu`, citing at least Campbell and Kroonen.
- **`oe_known_problems.tsv`:** **no change recommended.** This row is not an open known-problem item under the current analysis.
- **`DEV_NOTES`:** **no required change recommended.** The key `nosu` correction and chronology discussion are already present and still useful.
- **Dossier text:** **no change recommended.** There is no row-specific dossier/analysis file to revise.
- **Other repo prose cleanup:** **change recommended.** `Germanic/docs/germanic_transducer_report.md` should be corrected or marked historical where it still lists `*nasō → nosu`, because that conflicts with the live TSV and current trace.
