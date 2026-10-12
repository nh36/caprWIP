---
row_id: 2272
concept: wash
counterpart: wascan
proto: *wáskaną
protoform: *wáskaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2272-wash-wascan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2272-wash-wascan.md
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2272 wash / wascan

## Current row state

- CONCEPT: `wash`
- COUNTERPART: `wascan`
- PROTO: `*wáskaną`
- PROTOFORM: `*wáskaną`
- DERIVATION_CLASS: `regular`
- Live TSV note (quoted closely): `Proto encoding: -aną (full vowel) for A-restoration; R/T §6.3.1 | Medial sc before back vowel: not palatalized in early OE (Campbell §440); wascan [sk] is the conservative form.` [Germanic/data/germanic-aligned-final.tsv:2272]
- Row-specific support files already exist in packet and research-memo form, and both are consistent with the live row's present interpretation: regular A-restoration to `wascan`, plus conservative non-palatalized medial `sc` before a back-vowel tail [Germanic/docs/lexeme_reports/packets/2272-wash-wascan.md:1-379; Germanic/docs/lexeme_reports/research_memos/2272-wash-wascan.md:1-98]. No obvious row-specific pilot file or row-specific dossier file was found during slice preparation.

## Development-note summary

This row is presently a **regular** one, but the DEV_NOTES history is still worth preserving because two distinct issues once got entangled: (1) the engineering encoding needed for OE A-restoration in Class VI infinitives, and (2) whether the Old English target should be conservative `wascan` or a more normalized-looking `wasċan` / variant `wæscan`. The live row keeps those strands separate and should continue to do so [Germanic/data/germanic-aligned-final.tsv:2272].

The field distinction should be made explicit even though `PROTO` and `PROTOFORM` happen to coincide here. In the **live row**, `PROTO = *wáskaną` and `PROTOFORM = *wáskaną` are the same project-encoded form, i.e. the comparative/engineering input that the cascade actually uses for the OE derivation. `COUNTERPART = wascan` is the Old English target that the row is trying to reach. Those are not three interchangeable spellings of the same object. Comparative dictionaries often cite the Proto-Germanic verb more abstractly as `*waskan-` or `*waskanan`, and they are not fully uniform about the OE citation form either: Kroonen gives “`*waskan- ... OE wæscan`,” Orel gives “`*waskanan ... OE wascan`,” and Ringe-Taylor write “`*waskan ‘to wash’ > OE wascan`” [@Kroonen2013, s.v. *waskan-; @Orel2003, s.v. *waskanan; @RingeTaylor2014, vol. 2, p. 127; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:29170-29173; docs/references/orel_handbook_germanic_etymology.vision.txt:49670-49674; docs/references/ringe_taylor_linguistic_history_vol2.txt:7594-7596]. For this row, the project has already chosen the conservative OE lemma spelling `wascan`, and the slice should preserve that choice rather than flatten the literature's variation.

On the phonology, the A-restoration part is straightforward in current DEV_NOTES authority. Campbell's canonical statement explicitly lists `wascan` among the `sC`-cluster cases: “*a* is commonly restored also before groups consisting of *f* or *s* followed by another consonant, e.g. `*wascan` wash, `asce` ash, `flasce` flask ...” [@Campbell1959, §158; Germanic/docs/DEV_NOTES.md:30399-30403; docs/references/campbell_old_english_grammar.txt:4739-4743]. DEV_NOTES also has a direct row-table anchor for exactly this lexeme: row `2272` is classified as “`sC cluster, A-restoration fires (Campbell §158, *flasce*-class)`” [Germanic/docs/DEV_NOTES.md:30637-30637]. The later shared Class VI probe then explains why the live `PROTOFORM` keeps plain `-aną`: “the 10 Class VI strong verbs (`bákaną, grábaną, xláðaną, wádaną, wákaną, wáskaną, …`) rely on the plain `a` in the infinitival suffix to trigger OEARestoration,” and the trigger set “includes `{*a}` but not `{*ă}`” [Germanic/docs/DEV_NOTES.md:21745-21749]. That is the current explanation for the live row's `*wáskaną`, not the older experimental `*waskăną` [Germanic/docs/DEV_NOTES.md:21738-21749].

The medial `sc` issue is separate and should stay separate. The row note cites Campbell §440, and that citation is materially correct: Campbell says that internally `sc` was palatalized before front vowels, but “internally before back vowels ... [sk] remained,” and his examples in that environment include “`*wascan wash`” [@Campbell1959, §440; docs/references/campbell_old_english_grammar.txt:11468-11484]. Ringe and Taylor say the same thing in more general phonological terms: “Medially `*sk` was apparently palatalized unless a back vowel followed” [@RingeTaylor2014, vol. 2, p. 195; docs/references/ringe_taylor_linguistic_history_vol2.txt:11772-11775]. So the row's claim that `wascan [sk]` is the conservative form is not a stylistic normalization preference; it is the phonological point that keeps the row from drifting toward `wasċan` as though medial palatalization were automatic.

Philologically, the slice should preserve the fact that other OE-side spellings exist without letting them displace the row target. Clark Hall heads the verb as `wascan` and explicitly notes variant spellings “`(æ; acs, a(c)x)`”; Brunner likewise lists “`wascan, wæscan`” in the Class VI strong-verb discussion [@ClarkHall1960, s.v. wascan; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:47118-47119; docs/references/brunner_1965_altenglische_grammatik.vision.txt:15964-15965]. The supplementary repo tables also show lexical variation nearby: `old_english_wiktionary.tsv` gives `wash -> wasċan`, and `old_english_swadesh.tsv` lists `þwēan, wascan` for “to wash” [Germanic/data/old_english_wiktionary.tsv:330-330; Germanic/data/old_english_swadesh.tsv:133-133]. Those are useful background data, but they do not override the current row's narrower target. `COUNTERPART` here is the conservative lemma `wascan`; `wæscan`, `wasċan`, and even late family material like `wescep` belong in the documentation as variants or secondary family evidence, not as reasons to rewrite the row [docs/references/ringe_taylor_linguistic_history_vol2.txt:13481-13483].

The only major DEV_NOTES phase that is clearly superseded is the March 2026 workaround that rewrote strong Class VI infinitives with breve `-ăną`. That phase did record a targeted success — “`*waskăną` → `wascan` ✓ (was `wæscen`)” — but later notes replaced it with the current plain-`a` policy because the workaround overgenerated elsewhere [Germanic/docs/DEV_NOTES.md:9498-9512,21738-21749]. For row 2272, therefore, the current documentation should say plainly: the live row is regular; the live input is `*wáskaną`; A-restoration is the reason the root vowel returns to `a`; conservative medial `[sk]` is the reason the target is `wascan`; and the March `*waskăną` episode is project history, not live authority.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-30637-30637

- Source heading: `Words in the TSV with proto *-aCl-* or *-aCr-* before a back-vowel tail`
- Source line or section hint: `line 30637`
- Status: `current_primary_row_anchor`
- Issue tags: `row_specific`; `a_restoration`; `sC_cluster`; `regular_target`
- Recommended next use: `primary_index_anchor`

This is the strongest lexeme-addressable DEV_NOTES line for the row itself. It names the exact pair and classifies it tersely but correctly: “`| 2272 | *wáskaną | wascan | sC cluster, A-restoration fires (Campbell §158, *flasce*-class) |`” [Germanic/docs/DEV_NOTES.md:30637-30637]. The value of this line is that it is already row-shaped: it ties the project's encoded input `*wáskaną` directly to OE `wascan` and states the relevant environment without importing unrelated lexeme problems. If index anchoring is attempted later, this is the safest single line.

### DEV_NOTES:line-21738-21749

- Source heading: `A. Empirical probes (stems with root *á, Class VI strong verb infinitives)`
- Source line or section hint: `lines 21738-21749`
- Status: `current_shared_technical_policy`
- Issue tags: `protoform_encoding`; `class_vi_infinitives`; `a_restoration`; `plain_a_not_breve`
- Recommended next use: `secondary_index_anchor`
- Shared with row IDs: `1934, 2046, 2266, 2268, 2272`

This fragment is shared rather than row-exclusive, but it is still current authority for the live `PROTOFORM`. DEV_NOTES contrasts `*bákăną -> bæcan` with `*bákaną -> bacan`, then states explicitly that the Class VI infinitives, including `wáskaną`, “rely on the plain `a` in the infinitival suffix to trigger OEARestoration,” and that the trigger inventory includes `{*a}` but not `{*ă}` [Germanic/docs/DEV_NOTES.md:21742-21749]. For row 2272 this matters because it is the note that turns the older `*waskăną` success into superseded debugging history. Use it whenever the slice or a later report needs to justify why the live row keeps plain `-aną`.

### DEV_NOTES:line-30399-30403

- Source heading: `§158 (the consonant-environment statement — the relevant statement, ref. line 4727ff.)`
- Source line or section hint: `lines 30399-30403`
- Status: `current_shared_handbook_quote`
- Issue tags: `campbell_quote`; `sC_cluster`; `a_restoration`; `quotation_preserved`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2272` and other `sC/fC` A-restoration cases

This is the DEV_NOTES location where Campbell's crucial wording is already excerpted in reusable form. The quotation should be preserved rather than paraphrased away: “*a* is commonly restored also **before groups consisting of *f* or *s* followed by another consonant**, e.g. *waścan* wash, *asce* ash, *flasce* flask ...” [Germanic/docs/DEV_NOTES.md:30399-30403; @Campbell1959, §158]. For row 2272, the strength of the fragment is that it captures the exact conditioning statement behind the row note's first half. It is not by itself enough to settle the `sc`-palatalization question, but it is the best preserved DEV_NOTES quotation for the A-restoration side.

### DEV_NOTES:line-3138-3151

- Source heading: `Fix / Derivation / Impact`
- Source line or section hint: `lines 3138-3151`
- Status: `current_shared_verification`
- Issue tags: `trigger_set_correction`; `verification_history`; `post_fix_validation`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1934, 2046, 2088, 2266, 2272`

This later verification note matters because it shows that `wascan` remained correct after the trigger logic was narrowed. DEV_NOTES removes `{*æ}` from the trigger set, argues that only genuine back vowels should trigger A-restoration, and then reports: “All A-restoration-dependent forms verified: bacan, wadan, wascan, hlaþan, grafan, ġeall, hamer all correct” [Germanic/docs/DEV_NOTES.md:3140-3151]. That makes the row less fragile than the March workaround notes might suggest. `Wascan` is not surviving only because of an over-broad hack; it survives the later cleanup too.

### DEV_NOTES:line-9498-9512

- Source heading: `Changes made / Results (Empirical Validation, Dry Run 2026-03-13)`
- Source line or section hint: `lines 9498-9512`
- Status: `superseded`
- Issue tags: `breve_workaround`; `waskana_to_waskana_breve`; `project_history`; `diagnostic`
- Recommended next use: `retain_only_as_superseded_history`
- Shared with row IDs: `1934, 2046, 2266, 2268, 2272, 2292`

This fragment should stay in the slice, but only under a superseded label. It records the abandoned intervention in full: DEV_NOTES changed five strong-verb infinitives from plain `-aną` to `-ăną`, including “`*waskaną` → `*waskăną` (wascan),” and then listed the targeted result “`waskăną → wascan ✓ (was wæscen)`” [Germanic/docs/DEV_NOTES.md:9499-9512]. That history explains older project language around the row, but it is no longer live authority because later notes explicitly revert the class to plain-suffix `a` as the correct trigger for A-restoration [Germanic/docs/DEV_NOTES.md:21738-21749].

## Superseded or diagnostic material

- The March 2026 `*waskăną` stage is useful implementation archaeology, not current lexical policy. It should be cited only to explain why the project briefly thought breve `ă` was needed for this row [Germanic/docs/DEV_NOTES.md:9498-9512,21738-21749].
- Supplementary OE-side forms such as `wæscan` and `wasċan` should be kept visible but subordinated. Clark Hall and Brunner show that those variants are real, and the local Wiktionary table preserves a normalized `wasċan`, but the row note's phonological point is precisely that conservative `wascan` with medial `[sk]` remains the best target for this lemma row [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:47118-47119; docs/references/brunner_1965_altenglische_grammatik.vision.txt:15964-15965; Germanic/data/old_english_wiktionary.tsv:330-330:330-330].
- Family-level background such as `þwēan` beside `wascan` or the late `3sg wescep` should not be mistaken for row instability. They are useful if a later full lexeme report surveys the wider wash-family, but they do not undermine the present row's `COUNTERPART` [Germanic/data/old_english_swadesh.tsv:133-133; docs/references/ringe_taylor_linguistic_history_vol2.txt:13481-13483].

## Open questions for later work

- If this row is ever indexed, keep the two live strands explicit: A-restoration before `sC` and conservative non-palatalized medial `sc` before a back vowel. `DEV_NOTES:line-30637-30637` is strong for the first strand, while the second strand rests more on the row note plus the external handbook quotations than on a unique DEV_NOTES anchor [Germanic/data/germanic-aligned-final.tsv:2272; @Campbell1959, §440; @RingeTaylor2014, vol. 2, p. 195].
- A later full report could quote the comparative dictionaries together to show why OE spellings vary across the literature (`wascan` in Orel and R/T, `wæscan` in Kroonen) without treating that variation as a reason to change the row [@Orel2003, s.v. *waskanan; @Kroonen2013, s.v. *waskan-; @RingeTaylor2014, vol. 2, p. 127].
- If DEV_NOTES is ever cleaned up, the March 2026 `*waskăną` material should be labeled even more explicitly as superseded debugging history so it cannot be mistaken for the row's present canonical `PROTOFORM`.
