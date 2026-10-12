---
row_id: 2282
concept: west
counterpart: westene
proto: *wéstanē
protoform: *wéstanē
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2282 west / westene

## Current row state

- The live OE row now reads `CONCEPT = west`, `COUNTERPART = westene`, `PROTO = *wéstanē`, `PROTOFORM = *wéstanē`, `DERIVATION_CLASS = regular` [Germanic/data/germanic-aligned-final.tsv:1367-1367].
- The row note already encodes the decisive editorial move: `DEV_NOTES §17.38: target switched from bare-stem 'west' to 'westene' (Clark Hall westan(e) 'from the west') so the proto/target pair is lautgesetzlich; Orel HGE p.459 *westanē → OE westan id.` [Germanic/data/germanic-aligned-final.tsv:1367-1367].
- No obvious row-specific packet, research memo, pilot file, or clearly row-specific dossier/analysis file was found during the required support-file check under `Germanic/docs/lexeme_reports/` and nearby documentation directories.
- The row is therefore now a **same-string PROTO / PROTOFORM** row whose main documentation burden is lexical disambiguation, not phonological rescue: the project must keep the `*westan` / `west` lexeme distinct from the `*westanē` / `westan(e)` lexeme even though both sit under the English concept label `west` [Germanic/docs/DEV_NOTES.md:38661-38677].

## Detailed development-note summary

This row is a clean example of a **target-switch note rather than a rule-change note**. The present derivation is not trying to explain why `*wéstanē` unexpectedly keeps an extra syllable. DEV_NOTES states the opposite: the cascade already produced `westene`, and the problem was that the TSV had paired that proto with the wrong Old English target [Germanic/docs/DEV_NOTES.md:38653-38657,38688-38697]. The replacement slice therefore has to preserve the exact lexical distinction the old row blurred.

The most important philological point is that the relevant handbooks treat two different Proto-Germanic items here. Orel separates `*westan sb.n.` from `*westanē adv.`. The first is glossed with OE `west` 'westwards'; the second with OE `westan` 'from the West', and is explicitly said to be derived from `*westan` [Germanic/docs/DEV_NOTES.md:38661-38667; @Orel2003; docs/references/orel_handbook_germanic_etymology.vision.txt:50544-50546,50560-50563]. Clark Hall shows the same split on the Old English side: `west adv. westwards, 'west,' in a westerly direction` versus `westan, westane adv. from the west` [Germanic/docs/DEV_NOTES.md:38669-38677; @ClarkHall1960; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:48102-48105]. Those quotations are the row's core evidence. They show that bare `west` and suffixed `westan(e)` are not free spelling variants of one OE cell; they are distinct lexical/adverbial formations with different proto partners.

That distinction is exactly why the `PROTO` / `PROTOFORM` / `COUNTERPART` separation has to be made explicit even though the first two columns coincide. In the live row, `PROTO = *wéstanē` is the comparative headword chosen for the cognate set; `PROTOFORM = *wéstanē` is also the actual row-level derivational input fed to the OE cascade; `COUNTERPART = westene` is the OE-facing output for that suffixed adverbial formation [Germanic/data/germanic-aligned-final.tsv:1367-1367]. What must **not** be said is that `*wéstanē` somehow directly underlies bare `west`. DEV_NOTES is explicit that bare `west` instead belongs with `*westan`, while `*westanē` belongs with `westan(e)` [Germanic/docs/DEV_NOTES.md:38674-38677,38688-38697].

The current row also needs a careful statement about spelling and normalization. DEV_NOTES preserves the FST probe as ``*wéstanē → westene  ✓ matches OE 'westan(e)' adverb``, adding that `westene` reflects `regular medial-syllable a→e reduction of attested westane` [Germanic/docs/DEV_NOTES.md:38682-38685]. Clark Hall's dictionary headword is `westan, westane`, not exact `westene` [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:48104-48104]. The safe wording is therefore that the row's `COUNTERPART = westene` is the project's regularized/output-side spelling for the attested `westan(e)` lexeme, not that Clark Hall directly attests the exact graph `westene` [Germanic/docs/DEV_NOTES.md:38704-38706; @ClarkHall1960].

DEV_NOTES also records why the project chose this solution instead of retreating to the shorter lexeme. The decided plan says: `PROTOFORM stays *wéstanē` and `COUNTERPART west → westene`; this `keeps the proto/OE pair lautgesetzlich rather than retreating to the bare-stem *wéstan → west mapping` [Germanic/docs/DEV_NOTES.md:38701-38712]. That sentence should be preserved nearly as-is because it captures the row policy precisely. The project is not claiming that bare `west` is wrong Old English. It is claiming that **for this row**, once the proto side is fixed as `*wéstanē`, the lawful OE counterpart is the suffixed adverbial formation, not the unsuffixed directional adverb.

The brief cognate note in DEV_NOTES is likewise worth keeping, but cautiously. The note says Dutch `westen` and German `Westen` preserve the same suffixed formation, while English `west` continues the bare-stem variant [Germanic/docs/DEV_NOTES.md:38708-38712]. That is useful comparative orientation for later report work because it explains why the row's concept label `west` can hide two formations. But the row itself remains strictly an Old English adverbial-alignment issue: the TSV had mixed the suffixed proto with the unsuffixed OE comparator.

Two smaller DEV_NOTES traces should be preserved only as diagnostic context. First, an earlier chronology note briefly counted ``*wéstanē → west`` among forms `fixed` by a z-loss reorder [Germanic/docs/DEV_NOTES.md:24445-24449]. That statement is now clearly superseded for row-level policy: the later dedicated section shows that the real issue was not rule ordering but proto/target mismatch [Germanic/docs/DEV_NOTES.md:38649-38723]. Second, the later stress/quantity audit says `*westanē` / `*wéstanē` was `deliberately untouched` because the suffixal `*ē` is genuinely unstressed [Germanic/docs/DEV_NOTES.md:42728-42733]. That is useful background if the vowel quantity marking is revisited, but it is not the main lexeme note.

Overall, surviving DEV_NOTES support for row 2282 is strong enough to be lexeme-addressable. Unlike thinner slices that rely on shared precedent only, this row has a dedicated mini-dossier in `§17.38` with source audit, probe, diagnosis, explicit plan, and status line [Germanic/docs/DEV_NOTES.md:38649-38723]. The replacement working note should therefore preserve that dossier's exact lexical split and should not flatten it into a generic statement such as “OE west comes from PGmc `*westanē`.”

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-38649-38677

- Source heading: `§17.38 *wéstanē → westene (expected west): TSV proto/target mismatch`
- Fragment type: `row_specific_source_audit`
- Status: `current`
- Issue tags: `lexeme_split`; `proto_vs_target`; `west_vs_westan_e`; `quotation_preserved`
- Recommended next use: `primary_index_anchor`
- Shared with row IDs:

This is the row's main source audit and the best anchor for any future indexing. It records the mismatch, then quotes the two-way lexical split from Orel and Clark Hall: `*westan sb.n.` / OE `west` versus `*westanē adv.` / OE `westan` id., and `west adv.` versus `westan, westane adv.` [Germanic/docs/DEV_NOTES.md:38649-38677; @Orel2003; @ClarkHall1960]. For row 2282, that fragment does nearly all the essential work. It explains why the old target was wrong, why the new target is not an arbitrary extra syllable, and why the row must keep the part-of-speech/cell distinction explicit: unsuffixed directional `west` is not the same item as ablative/directional-adverbial `westan(e)`.

### DEV_NOTES:line-38679-38712

- Source heading: `§17.38` FST probe + diagnosis + decided plan
- Fragment type: `row_specific_resolution`
- Status: `current`
- Issue tags: `fst_probe`; `target_switch`; `lautgesetzlich_pair`; `protoform_policy`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment contains the actual project resolution. DEV_NOTES gives the probe ``*wéstan → west`` and ``*wéstanē → westene`` and then states that `The cascade is correct on both sides`; the problem is that the TSV had paired `*westanē` with `west`, i.e. different lexemes [Germanic/docs/DEV_NOTES.md:38681-38697]. The same block then says explicitly that for row 2282 `PROTOFORM stays *wéstanē` while `COUNTERPART west → westene`, because that is the form `actually derived by the cascade` and is equivalent to attested `westane` modulo regular reduction [Germanic/docs/DEV_NOTES.md:38701-38712]. If only one current fragment besides the source audit is cited later, it should be this one.

### DEV_NOTES:line-38714-38723

- Source heading: `§17.38` risk assessment and status
- Fragment type: `row_status_note`
- Status: `current`
- Issue tags: `single_row_edit`; `no_fst_change`; `status_line`
- Recommended next use: `cite_for_change_scope`
- Shared with row IDs:

This short tail section is useful because it states what the change was **not**. DEV_NOTES says the risk is `Tiny`, that the resolution is a `Single-row TSV edit`, and that `No FST change` is required because `*wéstanē → westene` already passed through the cascade before the row edit [Germanic/docs/DEV_NOTES.md:38714-38723]. That matters for later historical reconstruction of the row: the fix was an alignment correction, not a phonological-engine intervention.

### DEV_NOTES:line-24445-24449

- Source heading: earlier z-loss reorder audit
- Fragment type: `diagnostic_only`
- Status: `superseded`
- Issue tags: `older_problem_state`; `misleading_target`; `project_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs: `2282` and other reorder-test rows

This earlier note preserves an obsolete description of the row state: it lists ``*wéstanē → west`` among forms `fixed` by a reorder [Germanic/docs/DEV_NOTES.md:24445-24449]. That wording should not be used as current row policy. It is still worth preserving because it shows that before `§17.38` the project was still treating bare `west` as the row target and therefore misread a target-alignment problem as part of a larger rule-ordering story. The later dedicated note supersedes it completely [Germanic/docs/DEV_NOTES.md:38649-38723].

### DEV_NOTES:line-42728-42733

- Source heading: quantity-marking audit for `*ē`
- Fragment type: `background_only`
- Status: `current`
- Issue tags: `unstressed_long_e`; `proto_spelling`; `background_phonology`
- Recommended next use: `cite_only_if_quantity_is_discussed`
- Shared with row IDs: several suffix-`*ē` rows

This fragment is not a west-only note, but it is a useful safeguard if future work revisits proto spelling. DEV_NOTES says `*westanē` / `*wéstanē` was `deliberately untouched` because the suffixal `*ē` here is genuinely unstressed [Germanic/docs/DEV_NOTES.md:42728-42733]. That helps explain why the row keeps `*ē` rather than adopting the stressed `*ḗ` notation used elsewhere, but it should remain background support, not the main row anchor.

## Superseded or diagnostic material

- The old row state `*wéstanē` vs. expected `west` should be described as **superseded alignment**, not as a still-open derivational defect. `§17.38` resolves it directly by distinguishing the two lexemes and switching the target, while leaving the cascade untouched [Germanic/docs/DEV_NOTES.md:38688-38723].
- Any wording that treats `westene` as though it were merely a spelling variant of bare `west` is also superseded. The whole point of the note is that `west` and `westan(e)` are different lexical entries in both Orel and Clark Hall [Germanic/docs/DEV_NOTES.md:38661-38677; @Orel2003; @ClarkHall1960].
- Conversely, any wording that overstates the exact graph `westene` as a directly dictionary-cited OE lemma should be avoided. The handbook/dictionary support is for `westan, westane`; `westene` is the repo's regularized FST-side realization of that lexeme under medial-syllable reduction [Germanic/docs/DEV_NOTES.md:38682-38685,38704-38706; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:48104-48104].

## Open questions for later work

- If `index.tsv` is updated later, the strongest row-specific anchors are `DEV_NOTES:line-38649-38677` and `DEV_NOTES:line-38679-38712`; the short status block `DEV_NOTES:line-38714-38723` is a useful secondary anchor for change scope.
- Any future final report should keep the cell distinction explicit: bare directional adverb `west` < `*westan`; ablative/directional-adverbial `westan(e)` / repo-regularized `westene` < `*westanē` [Germanic/docs/DEV_NOTES.md:38663-38677; @Orel2003; @ClarkHall1960].
- If later source work wants to refine the spelling discussion, it should document the exact status of `westene` versus attested `westane` more explicitly; the current DEV_NOTES claim is plausible and probably right, but it is still a repo-side normalization statement rather than a direct dictionary lemma citation [Germanic/docs/DEV_NOTES.md:38682-38685].
