---
row_id: 2181
concept: shilling
counterpart: sċilling
proto: *skíllingaz
protoform: *skíllingaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2181-shilling-sċilling.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2181-shilling-sċilling.md
linked_dossier_or_analysis_files:
  - Germanic/docs/dossier-ing-lowering-2026.md
  - Germanic/docs/analysis/four_complex_tsv_items.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2181 shilling / sċilling

## Current row state

- The live OE row now reads `CONCEPT = shilling`, `COUNTERPART = sċilling`, `PROTO = *skíllingaz`, `PROTOFORM = *skíllingaz`, `DERIVATION_CLASS = regular`, with a note explicitly recording the 2026-04-27 correction from `*skéllinaz` to `*skíllingaz` and the two technical changes that made the row work: a new `pgrmWeakTailVowel` shape for `*-ingaz` and an `*_ng` exemption inside `OEMedUnstressedILowering` [Germanic/data/germanic-aligned-final.tsv:973-973].
- `PROTO` and `PROTOFORM` are identical in the live TSV, so the row is not currently using a surrogate oblique cell, a reconstructed OE-only preform, or an analogical repair input. The modelling input actually fed to the cascade is the same string that labels the comparative proto row: `*skíllingaz` [Germanic/data/germanic-aligned-final.tsv:973-973].
- That modelling input must be kept distinct from two other notational layers that survive in repo materials. Kroonen's lexicographic notation `*skellinga- ~ *skillinga-` is a dictionary stem label rather than the row's nominative singular FST input, while Kroonen's separate explanatory statement that the coin word continues `*skeld-linga-` is an etymological/internal-derivational analysis under the shield family, not the live row policy or an alternate `PROTOFORM` to feed directly into the current transducer [Germanic/data/germanic-aligned-final.tsv:973-973; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:22921-22924].
- The current published derivation trace is an exact match: `PROTO: *skíllingaz`, `EXPECTED: sċilling`, `OUTPUTS: sċilling`. Its OE-side stages are `PWGmc Final Bare A Loss: *skílling`, `OE Sk Palatalization: *ʃílling`, `OE Med Unstressed I Lowering1: *ʃílleng`, and `OE Med Unstressed I Lowering: *ʃílling`, then orthographic `sċilling` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4100-4120].
- Those two trace labels `OE Med Unstressed I Lowering1` and `OE Med Unstressed I Lowering` are not competing historical reconstructions of OE. They are computational substeps of the current composed fix: first a general unstressed `*ĭ > *e` lowering fires, then a restoration pass changes `*e` back to `*i` before `*ng`; the trace therefore exposes implementation order inside one rule block, not a claim that the row ever had a stable historical `*sċilleng` stage [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4111-4120; Germanic/docs/DEV_NOTES.md:38257-38303].
- `oe_known_problems.tsv` has no entry for row `2181`, for `shilling`, for `sċilling`, or for `*skíllingaz`; the row is no longer managed as an open exception bucket item [Germanic/data/oe_known_problems.tsv:1-8].
- `coverage_audit.md` still lists row `2181` among required OE rows with note-bearing regular derivations and no report yet, which is why this slice is needed as the row's replacement working note [Germanic/docs/lexeme_reports/coverage_audit.md:127-131].

## Development-note summary

The live row is now a regular exact-match derivation, but only after two separate problems were disentangled. The older row form `*skéllinaz` was not merely a notation variant of the current input. DEV_NOTES says plainly that it was “an editorial slip” with “single intervocalic *n, no *g*,” most likely a transcription error that dropped the derivational `-ing-`, and that there is “no philological tradition supporting `*skéllinaz` as a reconstruction” [Germanic/docs/DEV_NOTES.md:38093-38108]. That means the old and new forms represent different row policies: `*skéllinaz` was a bad modelling proto, whereas `*skíllingaz` is the current row-level nominative singular input.

DEV_NOTES then ties that row correction to the wider derivational class. The key philological claim is not peculiar to `shilling` alone: OE `sċilling` belongs to the productive PGmc masculine `*-ingaz` suffix class. DEV_NOTES summarizes the class with `*cyning`, `*æþeling`, `*wīcing`, `*Wōdening`, and `*sċilling`, and states that the suffixal `*-i-*` is the ordinary short vowel that triggers umlaut on the preceding stressed syllable where relevant, is not syncopated before `*ng`, and in OE “surfaces as orthographic `i`” [Germanic/docs/DEV_NOTES.md:38140-38159]. Campbell's handbook evidence preserved elsewhere in the repo aligns with that: his suffix survey lists `cyning king, scilling shilling` among forms where medial syncopation does not apply in the expected way for these suffix types [docs/references/campbell_old_english_grammar.txt:14614-14620].

The general OE weak-vowel backdrop also matters, because row 2181 is best understood as an explicit exemption from a broader merger, not as a free-standing quirk. DEV_NOTES preserves Hogg's formulation that “by about 700 all unstressed front vowels had become /e/,” immediately followed by the crucial exception: “[i] was preserved in derivational suffixes such as `-ig, -ing, -isc`, e.g. mihtig, cyning, Englisc” [Germanic/docs/DEV_NOTES.md:6636-6645]. Campbell is quoted in the same cluster with the general merger statement “æ, e, and i fell together in a sound written e in unaccented syllables,” and Ringe–Taylor likewise describe the merger in unstressed syllables while noting that inherited `i` next to palatals can survive [Germanic/docs/DEV_NOTES.md:6647-6657]. For row 2181, the point is that `sċilling` keeps suffixal `i` not because the merger never existed, but because `-ing-` belongs to the small derivational class that resists it.

Section §17.35 records that the first practical obstacle was input coverage, not sound change. Once the proto was corrected to `*skíllingaz`, the FST still returned `+?` at `proto_input`, because `pgrmWeakTailVowel` admitted `-inaz` but not `-ingaz`. DEV_NOTES shows the failure set explicitly: `*kúningaz`, `*wíkingaz`, `*skíllingaz`, and even synthetic `*kéttingaz` all failed identically [Germanic/docs/DEV_NOTES.md:38110-38138]. This part of the row history is stale as a live problem but still essential for understanding why `PROTOFORM` had to change in tandem with grammar coverage: the row could not become regular until the grammar could even parse the suffix that the philology required.

The second obstacle was rule overreach after the new tail was admitted. The dossier explains that `OEMedUnstressedILowering` was too coarse: it lowered marked unstressed `*ĭ` before any ordinary consonant, and because `*n` was included in the consonant class, the rule wrongly changed the suffix vowel of `*kuningaz / *wīkingaz / *skíllingaz` to `*e`, producing `cyneng / wiċeng / sċilleng` [Germanic/docs/dossier-ing-lowering-2026.md:61-113]. The dossier also states the philological result in especially blunt terms: searches in the standard handbooks yielded “no attested OE writings of `*-eng*` for the `*-ing-*` suffix,” and “*cyning* is *cyning* in all dialects from the earliest texts onward” [Germanic/docs/dossier-ing-lowering-2026.md:225-237]. That is row-relevant current evidence, not just implementation chatter: it shows the live repair was meant to restore ordinary OE suffix behavior, not to create a special one-off carve-out for `shilling`.

The closure note in DEV_NOTES is the authoritative current state. It says the fix was implemented compositionally: a general `{*ĭ} -> {*e}` lowering still applies, but a following pass restores `{*e} -> {*i}` before `*n *g`, with the comment “Restore *e → *i before the *ng cluster (Campbell §380, R/T vol.2 §6.9.6, Hogg 1992 p.120)” [Germanic/docs/DEV_NOTES.md:38257-38272]. DEV_NOTES is explicit that this is safe because, by that stage of the cascade, palatalizing contexts have already turned relevant `*g` into `*ġ`, so surviving `*e + ng` corresponds exactly to the derivational `*-ing-/*-ung-` environment rather than to a broad miscellaneous class [Germanic/docs/DEV_NOTES.md:38281-38289]. The verification table then lists `*skíllingaz → sċilling` as fixed and no-regression comparators such as `*brínganą → bringan` and `*strángiz → strenġ` as unchanged [Germanic/docs/DEV_NOTES.md:38292-38303].

The most important row-level distinction to keep explicit is therefore three-way. `PROTO = *skíllingaz` is the project's row-level modelling input; `PROTOFORM = *skíllingaz` is the same thing because no alternate cell is needed; and OE `sċilling` is the attested target citation form after loss of nominative `*-az`, OE `sk > sċ` palatalization before front vocalism, and preservation of suffixal `-ing-` [Germanic/data/germanic-aligned-final.tsv:973-973; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4100-4120]. Kroonen's `*skellinga- ~ *skillinga-` and `*skeld-linga-` remain useful philological background, but they belong to source discussion about the larger cognate set and internal derivation, not to a competing live TSV policy [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:22921-22924].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-6636-6657

- Source heading: `OE hierfest 'harvest' — Unstressed Front Vowel Merger`
- Source line or section hint: `lines 6636-6657`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `unstressed_front_vowel_merger`; `derivational_suffixes`; `ing_preservation`; `direct_quote`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2057`

This is the best preserved direct handbook quotation for the general rule/exemption pair that governs row 2181. Hogg's wording is explicit that unstressed front vowels merged to `/e/`, but that `[i] was preserved in derivational suffixes such as -ig, -ing, -isc`, with `cyning` as a model example [Germanic/docs/DEV_NOTES.md:6636-6645]. Campbell and Ringe–Taylor are then quoted immediately afterward for the broader unstressed-vowel merger [Germanic/docs/DEV_NOTES.md:6647-6657]. For `sċilling`, this fragment is current because it states the exact OE-side generalization that the closure later operationalizes: the row belongs to the small derivational suffix class that keeps `i`.

### DEV_NOTES:line-38093-38159

- Source heading: `§17.35 — *skéllinaz / sċilling (row 2181): missing PGmc *-ingaz derivational suffix`
- Source line or section hint: `lines 38093-38159`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `protoform_vs_proto`; `ing_suffix`; `row_policy`; `philology`; `source_audit`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the core row-specific philological fragment. It does three things that later reporting should not collapse together. First, it says the old row proto `*skéllinaz` was wrong and had no real source support [Germanic/docs/DEV_NOTES.md:38093-38108]. Second, it identifies the exact modelling gap in `pgrmWeakTailVowel`, showing that the grammar could not parse `*-ingaz` inputs at all before the fix [Germanic/docs/DEV_NOTES.md:38110-38138]. Third, it gives the row's class membership and current suffix analysis: `*sċilling` is treated as a normal PGmc `*-ingaz` derivative whose nominative singular loses final `*-az`, leaving bare OE `-ing` [Germanic/docs/DEV_NOTES.md:38140-38159]. This is the fragment that most clearly separates stale `*skéllinaz` row policy from current `*skíllingaz` row policy.

### DEV_NOTES:line-38257-38303

- Source heading: `§17.35.10 Closure (2026-04-27)`
- Source line or section hint: `lines 38257-38303`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `implementation_fix`; `verification`; `trace_interpretation`; `ing_preservation`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `963`

This is the authoritative implementation-and-verification fragment for the live row. It records the final composed `OEMedUnstressedILowering` rule, explains why restoration before `*ng` was chosen over right-context subtraction, and states why the environment is safe after palatalisation has already removed non-suffixal competitors [Germanic/docs/DEV_NOTES.md:38257-38289]. It also contains the empirical proof that the row is no longer a mismatch: `*skíllingaz → sċilling` is listed as fixed, while comparator probes such as `*brínganą → bringan` and `*strángiz → strenġ` show no collateral damage [Germanic/docs/DEV_NOTES.md:38292-38303]. The trace's visible `*ʃílleng → *ʃílling` sequence should be read through this fragment.

## Superseded or diagnostic material

The earliest substantial repo analysis for this row is now diagnostic history, not current row guidance. `analysis/four_complex_tsv_items.md` treated the problem as `*skellinăz → sċilling`, emphasized Kroonen's `*skeld-linga-` explanation, and concluded that the row was best handled as a “DOCUMENTED EXCEPTION” because the pipeline could neither parse the compound-like morphology nor derive the attested vowel [Germanic/docs/analysis/four_complex_tsv_items.md:90-128]. That analysis remains worth preserving because it captures the older state of the evidence review, but it is stale in two crucial ways: the live row no longer uses `*skellinăz/*skéllinaz`, and the grammar now does accept and correctly derive `*skíllingaz`.

Section §17.35 itself also preserves some diagnostic material inside a now-current heading. The heading still foregrounds the obsolete form `*skéllinaz`, and the opening mismatch note records the pre-fix bad output `sċillen` [Germanic/docs/DEV_NOTES.md:38085-38091]. Those lines are still useful project history, but later report prose should not cite them as if the row still lacked `-ing-` or still surfaced without final `g`.

The packet and memo both correctly treat the row as fixed, but they also preserve a caution that should survive into later write-ups: Kroonen's broader etymological discussion and the project's row-level input are not the same thing. The memo is right that `*skíllingaz` should be described as the project's modelling input, while `*skellinga- ~ *skillinga-` and `*skeld-linga-` remain source-side background about the cognate family rather than alternate live `PROTOFORM` candidates [Germanic/docs/lexeme_reports/research_memos/2181-shilling-sċilling.md:47-56].

## Open questions for later work

- If row 2181 is eventually indexed, index only the current evidence layers: the shared Hogg/Campbell/Ringe–Taylor quotation on unstressed `i`, the row-specific `*-ingaz` philology / proto correction, and the 2026-04-27 closure. The older `*skeld-linga-` exception analysis is useful background but should stay marked as diagnostic history unless a later source audit specifically needs it.
- If a later central report wants a one-sentence row description, keep the notation hierarchy explicit: Kroonen's `*skellinga- ~ *skillinga-` is lexicographic stem notation, `*skeld-linga-` is an etymological internal analysis, `*skíllingaz` is the live nominative singular modelling input, and `sċilling` is the attested OE target.
- If the shared `-ing-/-ung-` material is ever consolidated into a cross-row note, row 2181 should remain one of the clearest control cases because the trace still visibly exposes the general lowering plus `*_ng` restoration sequence [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4111-4120].
