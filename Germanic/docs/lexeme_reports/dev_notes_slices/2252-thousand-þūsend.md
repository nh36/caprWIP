---
row_id: 2252
concept: thousand
counterpart: þūsend
proto: *θūs-undī
protoform: *θūs-èndi
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2252-thousand-þūsend.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2252-thousand-þūsend.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2252 thousand / þūsend

## Current row state

- `Germanic/data/germanic-aligned-final.tsv` line 1249 currently gives row `2252` as `COUNTERPART þūsend`, `PROTOFORM *θūs-èndi`, `DERIVATION_CLASS early_analogy`, with etymological `PROTO *θūs-undī` and the live note: `Kroonen *θūsundī- f. 'thousand' → OE þūsend; medial -e- is analogical (Vorbild: ærende < *arundiiu); preserved ū (not ȳ) proves -ī lost before i-umlaut (double umlaut would give *þȳsend); OS/OHG retain -u-` [Germanic/data/germanic-aligned-final.tsv:1249-1249].
- The row therefore already encodes the crucial three-way distinction that later prose must not blur: `PROTO *θūs-undī` is the comparative PGmc headword reflected by Kroonen's `*þūsundī-`; `PROTOFORM *θūs-èndi` is the project's OE-facing transponent; `COUNTERPART þūsend` is the OE citation form actually targeted by the row [Germanic/data/germanic-aligned-final.tsv:1249-1249; @Kroonen2013, p. 554].
- `oe_known_problems.tsv` has no row-local entry for this item, so the row is not currently being managed as an unresolved exception bucket separate from the live TSV note and DEV_NOTES history [Germanic/data/oe_known_problems.tsv:1-9].
- Existing lexeme-report infrastructure already uses the stem `2252-thousand-þūsend` in both packet and research memo files, so this slice reuses that stem rather than inventing a new filename [Germanic/docs/lexeme_reports/research_memo_index.tsv:114-114].

## Detailed development-note summary

The replacement working note for row `2252` has to preserve two different layers of truth at once. At the comparative level, the project is still following the standard PGmc etymon `*þūsundī-` / stem `*þūsund-`, with OE `þūsend` as the exceptional Old English continuation [@Kroonen2013, p. 554; @Fulk2018, §10.6]. At the row-model level, however, the live OE cascade no longer feeds that exact reconstruction into the FST. The row now uses `PROTOFORM *θūs-èndi`, i.e. a project transponent that already contains the resolved OE-side second-member vowel and short final high vowel needed for successful apocope, while leaving `PROTO *θūs-undī` in place as the etymological headword [Germanic/data/germanic-aligned-final.tsv:1249-1249; Germanic/docs/DEV_NOTES.md:27614-27620,27746-27749].

The key reason this row is `early_analogy` rather than `regular` is that neither fully regular chronology yields the attested OE form. If final `-ī` had remained present long enough to trigger ordinary i-umlaut, the word should have undergone **double umlaut** in the trisyllabic `V-u-i` configuration: the root vowel as well as the medial `u` should have umlauted, giving something like `*þȳsend`, not `þūsend` [@Campbell1959, §203; @Luick1914, §198]. The attested preserved root `ū` therefore argues strongly that the umlaut-triggering `-ī` was lost or neutralized before the OE umlaut period. But once that early loss is admitted, the regular expectation would be a form continuing medial `u`, broadly as in Old Saxon and Old High German `thūsund/dūsunt`, not OE `þūsend` [@Fulk2018, §10.6; @Kroonen2013, p. 554]. The row is thus non-regular in a very specific way: **early loss of the umlaut trigger is required, but early loss alone does not explain the medial `-e-`**.

That is why the row's internal chronology must be stated explicitly. The live project reading is: (1) inherited PGmc `*þūsundī-` / stem `*þūsund-`; (2) early inflectional restructuring toward an OE neuter noun, with loss of the old umlaut-triggering `-ī` before productive OE i-umlaut; (3) OE-side reshaping or reduction of the second syllable so that the citation form surfaces as `þūsend`; (4) project transponent `*θūs-èndi` chosen to model that already-resolved OE-side state [@Campbell1959, §689; @Fulk2018, §10.6; Germanic/docs/DEV_NOTES.md:18288-18324,27746-27749]. This chronology is exactly what makes the label `early_analogy` appropriate: the row presupposes an **early non-regular restructuring prior to the ordinary umlaut output that the base reconstruction would otherwise predict**.

DEV_NOTES' strongest positive explanation for the medial `-e-` is the classic `ærende` comparison. Campbell's `þyslic` evidence is important negative control: “Only in this word is the mutation of the medial -u- recorded as y,” which shows that the `þūs-` element can mutate under a genuine front-vocalic trigger, but the simplex `þūsend` itself does not preserve that expected umlaut signature [@Campbell1959, §203]. Luick's double-umlaut discussion gives the actual regular comparator `ærende < *arundiiu`, and Luick later groups “thousand ... (ae. pūsend, ærende)” among forms “umgebildet” on that pattern [@Luick1914, §§198, 492]. Within the project this yields the working analogical story: OE speakers had inherited or observed `-und- > -end-` in `ærende`-type material and extended that visible `-end-` shape to `þūsend`, even though the historical trigger that made `ærende` regular was no longer available in `thousand` [Germanic/docs/DEV_NOTES.md:18107-18324].

That analogical account is still useful, but the slice must also preserve the later DEV_NOTES softening. The 2026 update adds Viredaz's caution that “OE e in this position could spell ə and reflect any PGmc short vowel,” so the OE spelling does not by itself prove a specific `ærende`-style proportional analogy [@GermanicSlavicBaltic2025, §2.1.4]. In other words, the secure part of the project decision is **negative** and chronological: a simple surviving-`-ī` umlaut derivation is excluded because that would predict root `ȳ`, not attested `ū`. The less secure part is **positive**: whether the second-syllable `e` should be explained specifically as analogical `-end-` reshaping, or more cautiously as OE schwa spelling over an already reduced unstressed vowel [Germanic/docs/DEV_NOTES.md:18326-18348]. The live TSV note still states the stronger analogical version, but the replacement slice should remember that DEV_NOTES itself later softened that certainty.

The project chronology inside DEV_NOTES also matters. The large row-specific note from 2026-04-12 belongs to the **mismatch era**, when the older input `*θūs-undī` still produced `þūsynde` and the team had to diagnose both the wrong medial vowel and the surviving final vowel [Germanic/docs/DEV_NOTES.md:17936-18097]. Later compound-programme notes then record the current solved state: row `2252` is listed as a match in the tiny OE hyphenated set, and the live analogue is written with grave-marked second-member notation `*θūs-èndi` [Germanic/docs/DEV_NOTES.md:27614-27620,27746-27749]. Replacement working prose therefore has to keep the two phases apart: the older note is still the main source for the philological problem, but the later notes control the current `PROTOFORM` and the row's present “match” status.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-17936-18097

- Source heading: `§14.7 OE þūsend 'thousand': Compound Analysis (2026-04-12)` through the first conclusion block
- Source line or section hint: `lines 17936-18097`
- Fragment type: `lexeme_specific`
- Status: `diagnostic_only`
- Issue tags: `mismatch_history`; `old_protoform`; `row_problem_statement`; `ad_hoc_transponent`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This is the indispensable mismatch-era fragment. DEV_NOTES records the old bad derivation `*θūs-undī -> þūsynde`, isolates the two concrete failures (“FST gives `y` ... but OE has `e`” and “final `-e` ... expected form has no final vowel”), and surveys the first round of source evidence from Fulk, Kroonen, and Campbell [Germanic/docs/DEV_NOTES.md:17940-18039]. Its first conclusion is now partly superseded: it floated `*θūsendi` as a working transponent and treated analogical `e` as the default answer [Germanic/docs/DEV_NOTES.md:18076-18097]. That remains useful project chronology, but not the live row state, because the row now uses `*θūs-èndi` and DEV_NOTES later softens the claim that the analogical account is the only viable explanation.

### DEV_NOTES:line-18107-18324

- Source heading: `Extended Research: The Origin of Medial -e-`
- Source line or section hint: `lines 18107-18324`
- Fragment type: `lexeme_specific`
- Status: `current_with_caution`
- Issue tags: `double_umlaut`; `ærende_vorbild`; `internal_chronology`; `early_analogy`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is still the core philological fragment for the row, provided its conclusion is read carefully. DEV_NOTES uses Luick's `ærende` material as the concrete Vorbild, cites Luick's grouping of `thousand` with `ærende`, and sets out the key chronological argument that a surviving final `-ī` would have caused **double umlaut**, hence unattested `*þȳsend` [Germanic/docs/DEV_NOTES.md:18107-18234,18236-18312]. The most durable part of the fragment is therefore not the categorical wording “The medial `e` must be analogical,” but the internal chronology it establishes: root `ū` excludes a regular surviving-`-ī` umlaut pathway, so any account of `þūsend` has to place loss of the old trigger before ordinary umlaut and then explain the medial `-e-` by something other than straight inheritance [Germanic/docs/DEV_NOTES.md:18242-18324].

### DEV_NOTES:line-18326-18348

- Source heading: `Update: New Source Material` (Viredaz 2025)
- Source line or section hint: `lines 18326-18348`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `current`
- Issue tags: `viredaz_update`; `schwa_spelling`; `softened_certainty`; `source_audit`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This short update is what prevents the slice from overstating the analogical argument. DEV_NOTES quotes Viredaz's statement that “OE e in this position could spell ə and reflect any PGmc short vowel,” explicitly reframing the earlier analysis as one possibility rather than a closed solution [Germanic/docs/DEV_NOTES.md:18331-18345]. For later report work, this fragment should accompany the `ærende` argument whenever the row note is described, because it marks the exact place where project certainty was reduced from “must be analogical” to “likely analogical, but not proved uniquely.”

### DEV_NOTES:line-27614-27620

- Source heading: `§16.6.4 Scope in our data (OE rows only)`
- Source line or section hint: `lines 27614-27620`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `compound_programme`; `verification_state`; `row_scope`; `current_match`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2148,2302`

This shared table is the clearest current checkpoint for live row status. It lists row `2252` among the three OE hyphenated analogue rows and marks `*θūs-endi` / `þūsend` simply as `match` [Germanic/docs/DEV_NOTES.md:27614-27620]. The notation here is slightly older than the final grave-marked version, but the fragment is still current as a state-control note: it shows that by the compound-programme stage the row was already treated as solved rather than as an open mismatch.

### DEV_NOTES:line-27746-27749

- Source heading: `§17.11.0 Motivation`
- Source line or section hint: `lines 27746-27749`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `protoform_migration`; `grave_notation`; `proto_vs_protoform`; `row_notation`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2148,2302`

This is the controlling fragment for the live row notation. DEV_NOTES states that the OE analogue set now uses grave-accent Nebenton notation and explicitly includes `*θūs-èndi` in that migrated set [Germanic/docs/DEV_NOTES.md:27746-27749]. For row `2252`, the fragment matters because it tells later writers exactly which form belongs to the current `PROTOFORM` field and why the older mismatch-era spellings (`*θūs-undī`, `*θūsendi`, `*θūs-endi`) must be treated as historical project states rather than as the live row input.

## Superseded or diagnostic material

- The strongest superseded item is the mismatch-era working recommendation to use `*θūsendi` as an ad hoc repair. DEV_NOTES proposed that form before the later grave-marked compound migration and before the Viredaz update, so it should now be cited only as project history, not as a live modelling decision [Germanic/docs/DEV_NOTES.md:18087-18097,27746-27749].
- DEV_NOTES' categorical claim that “The medial `e` must be analogical” is too strong as a stand-alone present-tense summary. The later Viredaz note keeps the row in `early_analogy`, but it does so under softer evidential conditions than the first April conclusion implied [Germanic/docs/DEV_NOTES.md:18301-18307,18331-18345].
- The row should not be normalized into a `regular` narrative by appealing only to early loss of `-ī`. Early trigger loss explains preserved root `ū`, but it does **not** by itself explain why OE alone has medial `e` while OS/OHG retain `u`; that residual mismatch is exactly why the row continues to need an OE-oriented transponent and an `early_analogy` label [Germanic/data/germanic-aligned-final.tsv:1249-1249; @Kroonen2013, p. 554; @Fulk2018, §10.6].
- No row-local `oe_known_problems.tsv` entry needs to be carried over into the working note. The outstanding issue for row `2252` is explanatory nuance and source-weighting, not a still-failing derivation in the live row state [Germanic/data/oe_known_problems.tsv:1-9; Germanic/docs/DEV_NOTES.md:27614-27620].

## Open questions for later work

- If the TSV note is ever revised, soften the positive claim about the medial `-e-`: the secure conclusion is that `*þȳsend` is excluded and that the row reflects early restructuring before umlaut, while the precise mechanism behind `-end-` should probably be phrased as likely `ærende`-type analogy, not as an exclusive proof.
- If a final lexeme report is drafted, decide whether to foreground Luick's analogical model or present Luick and Viredaz side by side as competing explanations beneath the same agreed chronology. The current slice supports either approach, but it should not silently suppress the Viredaz caution.
- If the broader OE compound/transponent programme is reviewed again, keep row `2252` tied to rows `2148` and `2302`, since DEV_NOTES repeatedly treats those three rows as the complete hyphenated/grave-marked OE analogue set [Germanic/docs/DEV_NOTES.md:27614-27620,27746-27749].
