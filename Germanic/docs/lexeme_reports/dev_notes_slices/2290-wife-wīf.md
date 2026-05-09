---
row_id: 2290
concept: wife
counterpart: wīf
proto: *wḯbą
protoform: *wī́bą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2290 wife / wīf

## Current row state

- Live OE row `2290` currently reads `CONCEPT = wife`, `COUNTERPART = wīf`, `PROTO = *wḯbą`, `PROTOFORM = *wī́bą`, `DERIVATION_CLASS = regular`, and the source note is still only the duplicated Wiktionary inheritance chain: `Source: Wiktionary Old English Swadesh list (retrieved 2025-12-12) | Source: Wiktionary etymology (template:inh) | Source: Wiktionary etymology (template:inh)` [Germanic/data/germanic-aligned-final.tsv:1397-1397].
- The adjacent cognate-set rows show why the row now has two proto spellings. Dutch `wijf`, English `wife`, and German `Weib` still sit under plain comparative `*wībą`, while the OE row alone uses `PROTO = *wḯbą`; the shared concept-level field across the set remains `PROTOFORM = *wī́bą` [Germanic/data/germanic-aligned-final.tsv:1395-1398]. For this slice, that split is notation history, not evidence for a different lexeme.
- The current published derivation trace treats the row as a clean exact match: `# wife / PROTO: *wḯbą / EXPECTED: wīf / OUTPUTS: wīf`. The row's visible steps are `OE Heavy Syllable Nasal Apocope: *wḯb`, then `PGmc B Allophony: *wḯβ`, and finally surface `Outcome: wīf` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5884-5903].
- Row-local support infrastructure is still empty. `coverage_audit.md` lists `2290 | wife | wīf | regular | no | - | - | - | none`, and the required row-specific support-file check turned up no packet, research memo, pilot file, or clearly row-specific dossier/analysis file to link here [Germanic/docs/lexeme_reports/coverage_audit.md:414-414].
- Repo-local lexical support is straightforward even though the modern English concept label narrows one common OE glossing option. `old_english_wiktionary.tsv` pairs `wife -> wīf` directly [Germanic/data/old_english_wiktionary.tsv:347-347]. Clark Hall glosses `wif n. woman, female ... 'wife,' lady` [@ClarkHall1960; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:48366-48367]. Kroonen gives `*wiba- n. 'woman, wife' - ... OE wif n. 'id.', E wife, ... Du. wijf ... OHG wīb ... G Weib` and remarks `No clear etymology` [@Kroonen2013, p. 584; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29596-29599,42282-42282]. Orel likewise has `*wiban sb.n.: ... OE wif id. ... OHG wīb id. Of uncertain origin` [@Orel2003, p. 464; docs/references/orel_handbook_germanic_etymology.vision.txt:51154-51156,70282-70282].

## Development-note summary

No dedicated row-specific mismatch dossier for `wife / wīf` survives in `DEV_NOTES.md`. That needs to be stated plainly. The securely attachable DEV_NOTES material is the shared stressed-long-`ī` notation/migration note in `§17.46`, where row 2290 appears only because its root vowel belonged to the cohort moved from older combining-acute `*ī́` notation to single-codepoint `*ḯ` [Germanic/docs/DEV_NOTES.md:41893-42051]. This makes row 2290 another **thin but current** slice: the row itself is lexically well supported and derivationally regular, but the surviving development-note burden is mostly encoding history plus a superseded diagnostic trail about final-vowel behavior.

The distinction among `COUNTERPART`, `PROTO`, and `PROTOFORM` is therefore the main thing to preserve. `COUNTERPART = wīf` is the attested OE target and current exact-match output [Germanic/data/germanic-aligned-final.tsv:1397-1397; Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5884-5903]. `PROTO = *wḯbą` is the row's live OE-facing derivational input, using single-codepoint stressed `ḯ` because that is what the current cascade can consume safely [Germanic/docs/DEV_NOTES.md:41925-41939]. `PROTOFORM = *wī́bą` preserves the older/shared combining-acute notation still visible at the concept-set level [Germanic/data/germanic-aligned-final.tsv:1395-1398]. Those are not rival etymologies and not distinct chronological proto-stages for this row.

DEV_NOTES states the notation point in wording worth preserving directly: “The diaeresis is purely notational. Semantically `*ḯ` = stressed long *ī” [Germanic/docs/DEV_NOTES.md:41938-41939]. That sentence controls how row 2290 should be read. The project did **not** discover a new lexical preform `*wḯbą` different in substance from comparative `*wī́bą`; it replaced an unstable input spelling with one the transducer could handle reliably. DEV_NOTES is equally explicit about the surface collapse: `OldEnglishRemoveStars` maps `{*ḯ} -> ī`, because OE orthography does not preserve the internal stress-tier distinction once rule-gating work is done [Germanic/docs/DEV_NOTES.md:41952-41957]. For row 2290, the trace shows exactly that collapse in practice.

What the row does contribute beyond notation is a tidy lexical/phonological check. The comparative dictionaries agree on the inherited noun family `*wiba- ~ *wiban` with OE `wif/wīf`, Dutch `wijf`, and German `Weib` [@Kroonen2013, p. 584; @Orel2003, p. 464]. The current trace then shows the specifically OE path the project is using: final nasal loss in a heavy syllable (`*wḯbą > *wḯb`) followed by a voiced fricative stage `*wḯβ`, with ordinary written `wīf` at surface [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5891-5903]. Campbell's general phonological summary fits that output pattern: “Internally between voiced sounds voiced spirants are represented,” while “Final `f` sometimes represents an old voiced spirant,” and later the system yields “alternation of voiced medial spirants with final voiceless ones” [@Campbell1959, §§57, 449; docs/references/campbell_old_english_grammar.txt:2361-2363,2381-2382,11668-11671]. For this slice, that is supportive phonology, not a DEV_NOTES controversy.

The only direct naming of row 2290 inside DEV_NOTES is the migration inventory, where Batch 5 lists `2286, 2290, 2296 | hwīnan, wīf, wīþiġ` [Germanic/docs/DEV_NOTES.md:42020-42026]. That fragment is thin, but still worth preserving because it anchors the row explicitly within the live stressed-`ḯ` migration history. Its silence about anything else is also informative: unlike rows that needed target replacement, analogical rescue, or exception framing, `wīf` appears only as a migrated stressed-long-`ī` row, not as a lexical problem case.

The safest present conclusion is conservative. Row 2290 is currently a regular exact-match row whose lexeme identity is not in serious doubt. The surviving DEV_NOTES value lies in documenting notation migration and in keeping older diagnostic material from being mistaken for live row status. What is missing is not evidence for `wīf`, but a richer row-dedicated DEV_NOTES narrative. On present evidence this slice should remain cautious and should not overstate the row as if DEV_NOTES preserved a substantive lexeme dispute.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-41893-41957

- Source heading: `§17.46 Stressed long-ī tier (*ḯ) — principled fix for the *swīn regression`
- Source line or section hint: `lines 41893-41957`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `stressed_long_i`; `notation_policy`; `proto_vs_protoform`; `surface_mapping`
- Recommended next use: `cite_if_explaining_notation_layers`
- Shared with row IDs: `2101`; `2103`; `2105`; `2106`; `2153`; `2182`; `2188`; `2197`; `2257`; `2285`; `2286`; `2290`; `2296`

This is the controlling current fragment for row 2290 even though it is a shared infrastructure note rather than a `wīf` dossier. It explains why stressed long `*ī` moved onto a dedicated symbol and preserves the key wording: “The diaeresis is purely notational. Semantically `*ḯ` = stressed long *ī” [Germanic/docs/DEV_NOTES.md:41938-41939]. For row 2290, that sentence is what prevents later writers from misreading `PROTO = *wḯbą` and `PROTOFORM = *wī́bą` as competing reconstructions.

The same fragment also supplies the surface-side rule that matters for this lexeme: `OldEnglishRemoveStars` maps `{*ḯ} -> ī`, because OE orthography does not distinguish stressed-root long `ī` from other long `ī` once the internal gating is done [Germanic/docs/DEV_NOTES.md:41952-41957]. That is exactly the bridge from the live input spelling `*wḯbą` to written `wīf`.

### DEV_NOTES:line-42006-42026

- Source heading: `§17.46 ... E. TSV migration (Phase 4)`
- Source line or section hint: `lines 42006-42026`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `tsv_migration`; `row_explicit`; `stressed_long_i`; `regular_row`
- Recommended next use: `cite_if_documenting_row_history`
- Shared with row IDs: `2286`; `2296`

This is the only securely attachable DEV_NOTES fragment that names row 2290 directly. Batch 5 lists `2286, 2290, 2296 | hwīnan, wīf, wīþiġ` [Germanic/docs/DEV_NOTES.md:42020-42026]. The fragment is thin, but it is still the row's best explicit DEV_NOTES anchor because it places `wīf` in the deliberate OE-row migration from older `*ī́` notation to stressed `*ḯ`.

The fragment should be read narrowly. It does not preserve a mismatch diagnosis, a target correction, or a philological dispute unique to `wīf`. Its value is that it names the row and locates it in a current verified implementation cohort.

### DEV_NOTES:line-42031-42051

- Source heading: `§17.46 ... F. Verification`
- Source line or section hint: `lines 42031-42051`
- Fragment type: `diagnostic_project_history_for_lexeme`
- Status: `current`
- Issue tags: `verification`; `shared_probe_block`; `regular_output`; `diagnostic_only`
- Recommended next use: `use_as_supporting_history_only`
- Shared with row IDs: migrated `*ḯ` rows

The verification block does not probe `wīf` by name, but it still matters as supporting history because it documents that the stressed-`ḯ` migration held the branch mismatch total steady through phase 4 batches 1-5 [Germanic/docs/DEV_NOTES.md:42031-42051]. For row 2290, the practical claim is modest: the row entered the new notation cohort without creating a fresh mismatch bucket.

This fragment should remain secondary. The actual row-local confirmation comes from the later published derivation trace `PROTO: *wḯbą / OUTPUTS: wīf`, not from an explicit `wīf` probe in this verification table [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5884-5903].

## Superseded or diagnostic material

- The older/shared spelling `*wī́bą` should remain visible here because it still survives in the row's `PROTOFORM` field and across the non-OE cognate-set rows [Germanic/data/germanic-aligned-final.tsv:1395-1398]. But DEV_NOTES makes clear that the shift to `*wḯbą` was an input-tokenization repair, not a new etymology [Germanic/docs/DEV_NOTES.md:41925-41939].
- The earlier apocope diagnostic `*wībą → wība (exp. wīf)` is useful project history but should now be treated as superseded diagnostic material, not as the live row state [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:299-299]. The published trace now shows that the live cascade reaches `wīf` via heavy-syllable nasal apocope plus the expected fricative stage, not stranded `wība` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:5891-5903].
- `germanic_nan_exceptions.csv` still contains `*wīban,wife,noun – retain -an`, which is relevant only as a fossil of an older noun-ending diagnostic queue, not as present row policy [Germanic/docs/germanic_nan_exceptions.csv:52-52]. Nothing in the current row state, coverage audit, or published OE trace suggests that row 2290 is still a live `-an`-retention problem.
- The comparative dictionaries' uncertainty about deeper etymology — Kroonen `No clear etymology`, Orel `Of uncertain origin` [@Kroonen2013, p. 584; @Orel2003, p. 464] — should not be inflated into a row-local TSV problem. The uncertainty concerns remote prehistory, not whether OE `wīf` belongs to the inherited Germanic noun family represented here.

## Open questions for later work

- If a fuller lexeme report is ever written, add a more explicit lexicographic note on the semantic range `woman, female; wife, lady` so the modern concept label `wife` is not mistaken for a narrower lexical match than the dictionaries support [@ClarkHall1960; @Kroonen2013, p. 584].
- If later reporting wants stronger row-local philology, add a direct Bosworth-Toller or DOE citation for `wīf`; the current slice is adequate, but its lexical support is still lighter than rows with packets or memos.
- If `dev_notes_slices/index.tsv` is revisited later, row 2290 still looks better kept as a no-index slice. The only strong row-explicit DEV_NOTES anchor is `DEV_NOTES:line-42006-42026`, and that anchor documents notation-migration history rather than a substantive lexeme-specific argument.
