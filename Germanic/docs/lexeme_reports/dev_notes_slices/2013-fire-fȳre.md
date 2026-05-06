---
row_id: 2013
concept: fire
counterpart: fȳre
proto: *fūri
protoform: *fūri
derivation_class: known_unmodelled
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2013-fire-fȳre.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2013-fire-fȳre.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2013 fire / fȳre

## Current row state

- CONCEPT: `fire`
- COUNTERPART: `fȳre`
- PROTO: `*fūri`
- PROTOFORM: `*fūri`
- DERIVATION_CLASS: `known_unmodelled`
- Live TSV note (quoted closely): inherited dat.sg. `*fūri` triggers i-umlaut and then loses final `*-i` by high-vowel apocope, so the regular outcome is `fȳr`; attested `fȳre` has dative `-e` restored analogically by proportion with regular a-stems such as `word : worde` [Germanic/data/germanic-aligned-final.tsv:322].
- `oe_known_problems.tsv` line 7 gives the same row-level policy in more explicit mismatch language: `*fūri` is an `exception / analogical_dat_e`, the FST's `fȳr` is the regular inherited result, and target `fȳre` is a later morphological restoration the FST is not expected to model [Germanic/data/oe_known_problems.tsv:7].
- `report_manifest.tsv` still lists row 2013 as `pilot/fire.md`, status `pilot`, so the slice needs to function as the detailed working note for a row that remains intentionally documented rather than fully regularized [Germanic/docs/lexeme_reports/report_manifest.tsv:9].
- Current philological caution: the live row collapses `PROTO` and `PROTOFORM` into the same oblique form, but the dedicated fire note in DEV_NOTES quotes Kroonen's heteroclitic lexeme `*fōr ~ *fun-` and treats `*fu(w)eri > *fūri` as the particular dative-locative cell that explains the umlaut. The oblique comparator is defensible as `PROTOFORM`; it is not the best lexeme-level headword description [DEV_NOTES:line-6180-6195; @Kroonen2013, p. 151].

## Development-note summary

The stable repo-level conclusion is that row 2013 is **not** a phonology bug and should not be described as if the FST were simply “missing final `-e`.” DEV_NOTES works through the inherited sequence explicitly: PGmc/PWGmc dative-locative `*fu(w)eri > *fūri` supplies the only `*-i` ending in the paradigm that can trigger the fronted OE vowel; i-umlaut gives `*fȳri`; high-vowel apocope after the heavy syllable then deletes that `*-i`, so the regular sound-law output is endingless `fȳr`, not `fȳre` [DEV_NOTES:line-6227-6246; @Kroonen2013, p. 151; @RingeTaylor2014, pp. 119, 379--380]. The current TSV note and the current known-problems ledger agree with exactly that analysis rather than treating the mismatch as unresolved noise [Germanic/data/germanic-aligned-final.tsv:322; Germanic/data/oe_known_problems.tsv:7].

The same DEV_NOTES discussion is also the row's best authority for why `*fūri` was chosen in the first place. It preserves Kroonen's formulation: "`*fōr ~ *fun- n. 'fire' ...`" with dative `*fu(w)eni`, and then quotes the key lexeme-specific conclusion that front-mutated Germanic reflexes such as OE `fȳr` and OHG `fuir/fiur` "are based on a dative form `*fu(w)eri`" [DEV_NOTES:line-6182-6187; @Kroonen2013, p. 151]. DEV_NOTES then spells out the paradigm consequence: nom.sg. `*fōr` has no umlaut trigger, gen.sg. `*funins` does not explain `ȳ`, and only the dative-locative cell does [DEV_NOTES:line-6189-6195]. That means the row is a genuine paradigm-cell case, but only for the inherited vowel history. It does **not** follow that the whole attested target `fȳre` is itself the direct sound-law reflex of `*fūri`.

Where the row becomes non-automatic is the final dative ending. DEV_NOTES' later addendum keeps the useful part of the March analysis while effectively abandoning its original recommendation. The durable point is the four-part analogy: `word : worde :: fȳr : X`, so `X = fȳre` [DEV_NOTES:line-6296-6314]. That is the repo's clearest explanation of why the attested form can be real Old English without being the phonologically primary output of the chosen comparator. DEV_NOTES is careful here to preserve an important limitation from Ringe-Taylor: "`whether OHG dat. or inst. fyur reflects an inherited dat. sg. *fuiri is doubtful, since endingless dat. sg. forms of other a-stems are also found.`" The slice should therefore not overclaim that an endingless OE dat.sg. `fȳr` is directly attested; the safer claim is that `fȳr` is the regular inherited outcome and also the ordinary citation/headword form in the light lexical sources checked in the packet and memo, while `fȳre` is the attested analogically remodeled dative [DEV_NOTES:line-6331-6349; Germanic/docs/lexeme_reports/research_memos/2013-fire-fȳre.md:64-70; @RingeTaylor2014, p. 119].

Project chronology matters because DEV_NOTES itself contains both the superseded and the current policy. The March 2026 fire note first recommends changing the target to `fȳr`, but the live row, the current known-problems ledger, the packet, and the research memo all keep `fȳre` as the target and treat the mismatch as a documented analogical exception rather than a row that should be silently retargeted [DEV_NOTES:line-6274-6279; Germanic/data/oe_known_problems.tsv:7; Germanic/docs/lexeme_reports/research_memos/2013-fire-fȳre.md:27-30, 76-83]. Cross-row DEV_NOTES references that cite fire as a clean precedent for “using an oblique form that can be derived lautgesetzlich” must therefore be read with caution: the oblique form solves the umlaut source, but the final `-e` still belongs to later analogical restoration, so row 2013 remains properly `known_unmodelled` rather than fully regular [DEV_NOTES:line-3208-3208; DEV_NOTES:line-3457-3457].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-88-90

- Source heading: `Could we use paradigm forms? (Why we decided not to)`
- Source line or section hint: `lines 88-90`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `background`
- Issue tags: `paradigm_cell`; `methodology`; `project_history`; `protoform_vs_proto`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs: `1946; 1965; 2251`

This short shared fragment is worth preserving because it captures the early methodological assumption under which fire entered the project's paradigm-cell workflow at all. DEV_NOTES says that for "fire, brand, berry, thorn" the project had "successfully resolved mismatches by adopting a paradigm form in which the phonological development is lautgesetzlich." For row 2013 that is only partly true in current hindsight. The dative-locative cell really does solve the source of OE `ȳ`; what it does **not** solve by itself is the attested final `-e`. Later row-specific notes therefore narrow this early claim rather than fully discarding it.

### DEV_NOTES:line-1769-1774

- Source heading: `2026-01-10 tracing follow-up and data note`
- Source line or section hint: `lines 1769-1774`
- Fragment type: `lexeme_specific`
- Status: `superseded`
- Issue tags: `debug_history`; `protoform_change`; `project_history`; `old_rule_hypothesis`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This fragment preserves the earliest row-specific shift that still matters for chronology. The tracing note first treats the problem as if a phonological contraction such as `{uw} > {ȳr}` might be missing, but the immediately following data note records the more important move: "the 'fire' row now uses dat.sg. `*fūri` (> `fȳre`) to avoid modelling nominative levelling." That is no longer the whole story, because the later dedicated fire note shows that `*fūri` only gets regularly as far as `fȳr`. Still, the fragment should be kept because it records when the row stopped being framed as a nominative-leveling issue and started being framed as a paradigm-cell issue.

### DEV_NOTES:line-6169-6246

- Source heading: `OE fȳr/fȳre 'fire': paradigm and umlaut problem`
- Source line or section hint: `lines 6169-6246`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `heteroclitic_paradigm`; `paradigm_cell`; `i_umlaut`; `high_vowel_apocope`; `analogical_dative`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the core row-specific authority and should do most of the replacement-note work. DEV_NOTES opens by stating the exact mismatch: TSV proto `*fūri` with target `fȳre`, but FST output `fȳr`. It then preserves the key handbook quotation from Kroonen: "`*fōr ~ *fun- n. 'fire' ...`" with a dative form `*fu(w)eni`, followed by the conclusion that front-mutated reflexes such as OE `fȳr` and OHG `fuir/fiur` "are based on a dative form `*fu(w)eri`" [@Kroonen2013, p. 151]. DEV_NOTES turns that into a precise paradigm statement: nom.sg. `*fōr` does not supply umlaut; gen.sg. `*funins` does not either; only dat.sg. `*fu(w)eri > *fūri` carries the `*-i` that explains `ȳ` [DEV_NOTES:line-6189-6195]. The phonological sequence is then written out explicitly and remains current: `*fūri` → `*fȳri` by i-umlaut, then `*fȳri` → `fȳr` by high-vowel apocope after a heavy syllable [DEV_NOTES:line-6227-6246; @RingeTaylor2014, pp. 119, 379--380]. This fragment is the main reason later work should keep `PROTOFORM = *fūri` even if the lexeme-level `PROTO` is someday cleaned up.

### DEV_NOTES:line-6274-6279

- Source heading: `same fire note: target-retargeting recommendation`
- Source line or section hint: `lines 6274-6279`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `row_policy`; `retargeting`; `project_history`; `superseded_decision`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This fragment has to remain visible because packets and older summaries can still inherit it. DEV_NOTES explicitly recommended "Option A": change the row target from dative `fȳre` to nominative/accusative `fȳr`, on the grounds that `fȳr` is the regular phonological outcome and dictionary headword. That recommendation is now superseded by live repo state. The current TSV row, the known-problems ledger, and the fire memo all keep `fȳre` as the row target and classify the mismatch as understood but intentionally unmodelled. Later report prose should mention this recommendation only as abandoned project history.

### DEV_NOTES:line-6289-6353

- Source heading: `four-part analogical model for dative -e restoration`
- Source line or section hint: `lines 6289-6353`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `four_part_analogy`; `analogical_restoration`; `known_exception`; `fST_limit`; `dative_e`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This addendum preserves the current best explanation for why the target remains `fȳre` even though the inherited output is `fȳr`. DEV_NOTES states the proportion directly: `word : worde :: fȳr : X`, therefore `X = fȳre`. It glosses this as "classic four-part analogical leveling": the surface dative `-e` of regular a-stems is extended into the remodeled fire paradigm even though the inherited ending had already been deleted in `*fūri > fȳr`. The same fragment also keeps the necessary caution from Ringe-Taylor: "whether OHG dat. or inst. fyur reflects an inherited dat. sg. *fuiri is doubtful, since endingless dat. sg. forms of other a-stems are also found." For row 2013, the lasting use of the fragment is twofold: it justifies keeping `fȳre` as an attested analogical dative, and it explains why the FST is still correct to stop at `fȳr` [@RingeTaylor2014, pp. 119, 379--380].

### DEV_NOTES:line-1426-1428

- Source heading: `remaining documented exceptions ledger`
- Source line or section hint: `lines 1426-1428`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `current`
- Issue tags: `known_exception`; `ledger`; `mismatch_triage`; `current_policy`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This small ledger fragment is the cleanest DEV_NOTES confirmation of present row policy outside the long fire discussion. It says the remaining mismatches are documented exceptions and lists `*fūri → fȳr (expected fȳre) — exception: analogical_dat_e`. That wording matches the live `oe_known_problems.tsv` entry closely enough that the two should now be read together: row 2013 is not pending a phonological fix, but already triaged as a known analogical exception.

## Superseded or diagnostic material

The main superseded item is the explicit March recommendation to retarget the row to `fȳr` [DEV_NOTES:line-6274-6279]. That proposal should remain visible because it is historically intelligible and because later packet work still preserves it, but it is no longer controlling policy.

Two other DEV_NOTES cross-references also need to be handled as diagnostic rather than authoritative for row 2013. The ræst note says fire is a precedent where an oblique paradigm cell "`*fūri → fȳre`" explains the OE vowel [DEV_NOTES:line-3208-3208], and a later summary likewise says the fire row records an oblique cell "that can be derived lautgesetzlich" [DEV_NOTES:line-3457-3457]. Those statements are useful as evidence that fire became a methodological precedent inside the project, but they are too compressed to stand alone now. Read against the dedicated fire note, they are accurate only up to the inherited `fȳr` stage; they leave out the analogical restoration that keeps the row in `known_unmodelled`.

The breaking-table hit `| 2013 | *fūri | fȳre | irrelevant |` is diagnostic search noise only and should not be promoted into row argument [DEV_NOTES:line-30617-30617].

## Open questions for later work

- If the TSV metadata is ever cleaned up, decide whether `PROTO` should stop repeating the oblique comparator and instead reflect the heteroclitic lexeme-level headword behind the fire paradigm, while still keeping `PROTOFORM = *fūri`.
- If the final lexeme report cites OE headword `fȳr`, keep the functional distinction explicit: `fȳr` is the regular inherited output and citation form, whereas row target `fȳre` is the attested analogical dative.
- If later prose quotes the four-part analogy, retain the built-in caution that DEV_NOTES does **not** claim direct attestation of an endingless OE dat.sg. `fȳr`; the safe claim is regular inherited `fȳr`, later analogical `fȳre`.
- If cross-row methodology notes continue using fire as an oblique-cell precedent, add a short qualifier that fire is only partly parallel to fully regular paradigm-cell solutions such as `brandes`: its oblique input explains the vowel, but not the restored final `-e`.
