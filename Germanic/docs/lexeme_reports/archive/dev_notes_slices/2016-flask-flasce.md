---
row_id: 2016
concept: flask
counterpart: flasce
proto: *flaskō
protoform: *fláskōn
derivation_class: early_analogy
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2016-flask-flasce.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2016-flask-flasce.md
linked_dossier_or_analysis_files: Germanic/docs/analysis/arestoration_r_l_research.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2016 flask / flasce

## Current row state

- CONCEPT: `flask`
- COUNTERPART: `flasce`
- PROTO: `*flaskō`
- PROTOFORM: `*fláskōn`
- DERIVATION_CLASS: `early_analogy`
- Live TSV note (quoted closely): `Proto corrected: weak fem. ōn-stem *flaskōn (Orel *flaskò(n) sb.f.; Kroonen *flaskǭ). TSV had *flaskō (strong ō-stem, no final vowel after heavy syllable). A-restoration trigger fix: *ǭ (nasalized, from *-ōn) now triggers A-restoration, preserving root *a before medial *sk.` [Germanic/data/germanic-aligned-final.tsv:333]
- Current row split: the live row already uses the corrected weak-feminine derivational input, but `PROTO` still preserves the older strong-ō interpretation, so the row is computationally fixed while its lexeme-headword metadata still carries superseded history [Germanic/data/germanic-aligned-final.tsv:333; Germanic/docs/lexeme_reports/research_memos/2016-flask-flasce.md:48-55, 72-90].
- `oe_known_problems.tsv`: no row-local entry for `2016`, `*fláskōn`, `*flaskō`, or `flasce`; that absence is bookkeeping only and should not be treated as philological evidence [Germanic/data/oe_known_problems.tsv:1-9; Germanic/docs/lexeme_reports/research_memos/2016-flask-flasce.md:19-20, 41-45, 91].
- `report_manifest.tsv`: no manifest entry for row 2016, so this slice needs to stand as the detailed replacement working note for the row's DEV_NOTES material [Germanic/docs/lexeme_reports/report_manifest.tsv:1-13].
- Packet / memo state: the packet already preserves the live compact derivation `*fláskōn -> flasce`, while the memo explicitly warns that the unrelated row-number hit at `DEV_NOTES:line-15558-15558` and the liquid-blocking wording at `DEV_NOTES:line-3830-3831` are not current row authority [Germanic/docs/lexeme_reports/packets/2016-flask-flasce.md:17-40, 48-57; Germanic/docs/lexeme_reports/research_memos/2016-flask-flasce.md:17-20].

## Development-note summary

Row 2016 has securely attachable, still-usable row-specific DEV_NOTES authority. The controlling note opens by stating the original project mismatch plainly: TSV had strong feminine `*flaskō`, the pipeline produced `flasc`, and the reason was ordinary heavy-syllable apocope, which removed final `*-ō` after the heavy `*-sk` cluster. The durable correction is declensional rather than cosmetic: DEV_NOTES then says, “OE flasce is weak feminine (ōn-stem). All major sources agree,” and records the project move from `*flaskō` to `*flaskōn` [DEV_NOTES:line-3799-3806]. For normal workflow, that is the key historical turn: `flasce` stopped being treated as a mysterious final-vowel problem once the row was re-read as a weak feminine.

DEV_NOTES also preserves the second-stage problem that matters for current technical explanation. Simply changing the stem class did not immediately fix the row. After `NWGmcNStemNLoss`, `*flaskōn` became `*flaskǭ`; Anglo-Frisian brightening then produced `*flæskǭ`; A-restoration failed because `*ǭ` was missing from `OEARestorationTriggerVowel`; and the bad intermediate result was `flæsċe`, wrong in both root vowel and consonant [DEV_NOTES:line-3808-3829]. The fix is worth carrying over literally because it is precise and still current: `define OEARestorationTriggerVowel [EnglishStarBackVowel | {*ô} | {*ǭ}];` [DEV_NOTES:line-3824-3828]. Once `*ǭ` is admitted as a trigger, DEV_NOTES reruns the derivation and gets `*flaskǭ > *flaske > flasce`; the note adds that `sc`, not `sċ`, is not a separate patch but the automatic consequence of avoiding front-vowel-triggered `sk` palatalization [DEV_NOTES:line-3833-3842].

The philological framing preserved elsewhere in DEV_NOTES should remain attached to this row, because it explains why the restored `a` is not merely a local FST convenience. Campbell is quoted directly: “*a* is commonly restored also before groups consisting of *f* or *s* followed by another consonant, e.g. ... *flasce* flask (after inflected *ascan, flascan*)” [DEV_NOTES:line-30400-30405]. A separate quoted passage gives the Ringe-Taylor-style formulation `PWGmc *flaska, *flaskon- > *flæske, *flæskon- > OE flasce, flascan` [DEV_NOTES:line-22590-22594]. Those two quotations are worth preserving together because they keep the row's explanatory hierarchy explicit: singular `flasce` is the target, but plural/oblique `flascan` belongs to the explanation for restored `a`, and the live `PROTOFORM = *fláskōn` is the project input that lets the corrected cascade model exactly that history [Germanic/docs/lexeme_reports/research_memos/2016-flask-flasce.md:41-60].

Current row policy therefore has to be read in three layers. First, the derivational input `*fláskōn` is current and productive. Second, the live `PROTO = *flaskō` is surviving superseded metadata from the abandoned strong-ō reading, not the best current lexeme-level headword [Germanic/data/germanic-aligned-final.tsv:333; Germanic/docs/lexeme_reports/research_memos/2016-flask-flasce.md:48-55, 72-87]. Third, the row is not a live `oe_known_problems.tsv` exception, because the corrected cascade already returns `flasce` [Germanic/data/oe_known_problems.tsv:1-9; Germanic/docs/lexeme_reports/packets/2016-flask-flasce.md:42-44]. The one DEV_NOTES sentence that must be actively demoted is the side claim that `*r` and `*l` “independently block A-restoration”; the later dedicated analysis explicitly rejects that formulation and even lists `flasce` among positive A-restoration examples [DEV_NOTES:line-3830-3831; Germanic/docs/analysis/arestoration_r_l_research.md:22-22, 83-83, 696-696].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-3799-3806

- Source heading: `Case 3: *flaskō → *flaskōn (OE flasce 'flask, bottle')`
- Source line or section hint: `lines 3799-3806`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `protoform_vs_proto`; `stem_class_correction`; `heavy_syllable_apocope`; `row_policy`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This opening row note preserves the decisive correction that still governs the row. DEV_NOTES states the old mismatch in exact row-local terms: TSV had strong feminine `*flaskō`, the pipeline therefore gave `flasc`, and the reason was that heavy-syllable apocope removed final `*-ō` after the `*-sk` cluster. It then records the durable reanalysis: “OE flasce is weak feminine (ōn-stem). All major sources agree,” followed by the project correction from `*flaskō` to `*flaskōn` [DEV_NOTES:line-3799-3806]. For current workflow this fragment is the best short authority for why live `PROTOFORM = *fláskōn` is a real stem-class repair rather than an ad hoc row-specific patch.

### DEV_NOTES:line-3808-3829

- Source heading: `same flask note: weak-stem correction exposed missing *ǭ trigger`
- Source line or section hint: `lines 3808-3829`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `a_restoration`; `trigger_set_fix`; `n_stem_loss`; `debugged_derivation`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This fragment keeps the row from being oversimplified into “change the protoform and the problem disappears.” DEV_NOTES writes out the failed intermediate derivation after the stem-class correction: `*flaskōn -> *flaskǭ -> *flæskǭ`, then no A-restoration because `*ǭ` was missing from `OEARestorationTriggerVowel`, and therefore wrong `flæsċe` [DEV_NOTES:line-3810-3823]. The fix is explicit and should be preserved exactly: `define OEARestorationTriggerVowel [EnglishStarBackVowel | {*ô} | {*ǭ}];` [DEV_NOTES:line-3824-3828]. Later row writing should cite this fragment whenever it needs to explain why the weak feminine was necessary but not sufficient until the trigger set was repaired.

### DEV_NOTES:line-3833-3842

- Source heading: `same flask note: corrected derivation to flasce`
- Source line or section hint: `lines 3833-3842`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `a_restoration`; `surface_derivation`; `sk_palatalization`; `final_output`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the row's cleanest current derivation fragment. DEV_NOTES reruns the corrected sequence step by step: `*flaskōn -> *flaskǭ`, brightening to `*flæskǭ`, A-restoration back to `*flaskǭ`, no front-vowel-triggered `sk` palatalization, then unstressed-vowel shortening to `*flaske`, surface `flasce` [DEV_NOTES:line-3833-3838]. The note then adds the practical conclusion worth keeping: “Both the root vowel (a, not æ) and the consonant (sc, not sċ) are now correct,” and the consonant fix follows from the restored back-vocalic environment rather than from a special orthographic rule [DEV_NOTES:line-3840-3842].

### DEV_NOTES:line-22590-22594

- Source heading: `quoted comparative note on restored a in n-stems`
- Source line or section hint: `lines 22590-22594`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `literature_quote`; `plural_support`; `n_stem_context`; `a_restoration`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This quoted comparative passage is worth preserving because it names the singular and plural together: “Retracted a also normally appears in the root syllables of n-stems ... `PWGmc *flaska, *flaskon- > *flæske, *flæskon- > OE flasce, flascan`” [DEV_NOTES:line-22590-22594]. For row 2016 the lasting value of the fragment is that it keeps plural/oblique `flascan` inside the explanation rather than relegating it to an optional footnote. That is exactly the explanatory shape the live row and memo both need: weak-feminine history plus paradigm support, not a flattened one-form inheritance claim.

### DEV_NOTES:line-30400-30405

- Source heading: `quoted Campbell statement on restored a before sC clusters`
- Source line or section hint: `lines 30400-30405`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `campbell_quote`; `a_restoration`; `s_cluster`; `plural_support`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This Campbell quotation should be carried over directly rather than paraphrased away. DEV_NOTES preserves the wording: “*a* is commonly restored also before groups consisting of *f* or *s* followed by another consonant, e.g. ... *flasce* flask (after inflected *ascan, flascan*)” [DEV_NOTES:line-30400-30405]. For row 2016 that sentence does two jobs at once: it places `flasce` inside a recognized `sC` restoration environment, and it preserves the inflected-form logic that helps explain why the singular surfaces with `a`.

### DEV_NOTES:line-3830-3831

- Source heading: `same flask note: old liquid-blocking gloss`
- Source line or section hint: `lines 3830-3831`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `a_restoration`; `liquid_blocking`; `old_rule_hypothesis`; `project_history`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

These two lines must remain visible, but only as superseded project wording. DEV_NOTES says the new trigger causes restoration before eligible consonant clusters “excluding `*r`, `*l` — which independently block A-restoration” [DEV_NOTES:line-3830-3831]. The later dedicated analysis rejects that formulation explicitly, stating that no source treats a single intervening `*r` or `*l` as a blocker and listing `flasce` among the positive restoration examples [Germanic/docs/analysis/arestoration_r_l_research.md:22-22, 83-83, 696-696]. Keep this fragment only so later writers can explain why older row prose may overstate liquid blocking.

### DEV_NOTES:line-20556-20560

- Source heading: `Regressions Identified (56 vs 43 mismatches)`
- Source line or section hint: `lines 20556-20560`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `debug_history`; `intermediate_output`; `ending_regression`; `project_chronology`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This regression ledger preserves a real but intermediate broken state: `*fláskōn -> flascæ` [DEV_NOTES:line-20556-20560]. It is useful for debugging chronology because it shows that the row passed through a stage where the stem-class correction had exposed the right lexeme but unstressed-vowel handling was still wrong. It is not current lexical authority and should never be cited as evidence against target `flasce`.

### DEV_NOTES:line-15556-15559

- Source heading: `Recommended Action` 
- Source line or section hint: `lines 15556-15559`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `false_positive`; `row_id_noise`; `search_hygiene`; `project_history`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This is not a flask note at all. It is an unrelated `cniht` action item whose text happens to say “Update TSV row 2016,” followed by a different proto correction entirely [DEV_NOTES:line-15556-15559]. The fragment is worth recording only because row-ID grep hits can otherwise mislead later packet work; it carries no lexical authority for `flasce`.

## Superseded or diagnostic material

This row does **not** suffer from a lack of attachable DEV_NOTES authority. The core `flaskō -> flaskōn` note at `DEV_NOTES:line-3799-3842` is real row-specific material and remains the main replacement working note for the row. What needs pruning is not absence of evidence but bad evidence hierarchy.

Three items should stay demoted. First, the live `PROTO = *flaskō` is still visible in TSV metadata, but it now belongs to superseded row history rather than current derivational policy [Germanic/data/germanic-aligned-final.tsv:333]. Second, the note's `*r/*l`-blocking gloss is outdated and should not be reused as current A-restoration theory [DEV_NOTES:line-3830-3831; Germanic/docs/analysis/arestoration_r_l_research.md:22-22]. Third, `*fláskōn -> flascæ` and the stray row-2016 hit at lines 15556-15559 are debugging/search artifacts only, not live lexical argument [DEV_NOTES:line-20556-20560; DEV_NOTES:line-15556-15559].

## Open questions for later work

- Decide whether the live TSV `PROTO` should eventually be updated from strong-ō `*flaskō` to a weak-feminine lexeme headword so the row's metadata no longer contradicts its current derivation.
- If a final lexeme report is written, keep the three-way distinction explicit: superseded cognate-headword metadata (`*flaskō` in the live row), current modelling input (`*fláskōn`), and attested OE target (`flasce`).
- If later prose mentions variant `flaxe`, keep it subordinate to the main `flasce / flascan` analysis rather than letting the late West-Saxon variant displace the row target [Germanic/docs/lexeme_reports/research_memos/2016-flask-flasce.md:42-43, 58-60, 82-90].
- When citing A-restoration discussion for this row, quote the corrected `sC`-cluster evidence and the `flasce, flascan` passages, not the obsolete liquid-blocking gloss.
