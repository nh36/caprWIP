---
row_id: 1934
concept: bake
counterpart: bacan
proto: *bákaną
protoform: *bákaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/1934-bake-bacan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/1934-bake-bacan.md
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/arestoration_r_l_research.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 1934 bake / bacan

## Current row state

- CONCEPT: `bake`
- COUNTERPART: `bacan`
- PROTO: `*bákaną`
- PROTOFORM: `*bákaną`
- DERIVATION_CLASS: `regular`
- Live TSV note (abridged): `Proto encoding: -aną (full vowel) for A-restoration; R/T §6.3.1.`

## Development-note summary

The live row is not a lexically uncertain item. The regular comparator, the row target, and the attested Old English citation form all coincide at `bacan`. The controlling current notes say that Class VI infinitives like `*bákaną` must keep a plain suffix vowel because that back vowel is what allows OE A-restoration to return brightened `*æ` to `a`; the April probe writes the contrast out directly: `*bákăną` gives wrong `bæcan`, while `*bákaną` gives correct `bacan`. That is why the current TSV keeps `PROTOFORM = *bákaną` rather than a breve-marked workaround [@RingeTaylor2014, §6.3.1].

The handbook baseline is likewise explicit and should stay explicit in any later report. Campbell's canonical A-restoration statement includes `bacan` among the standard examples: “The restoration of *a* is common before all single consonants and geminates, e.g. *faran* go, *calan* be cold, *bacan* bake, *gnagan* gnaw, *grafan* dig …” [@Campbell1959, §158]. Ringe and Taylor give the general conditioning in the same direction: stressed `*æ` followed by a single or geminate consonant and then a back vowel becomes `a` [@RingeTaylor2014, §6.3.1]. For this row, then, regular comparator `*bákaną > bacan` and attested outcome `bacan` are the same thing; `bacen` is not a rival lexical outcome but a modelling error.

DEV_NOTES preserves that modelling error in useful detail. The March diagnostics showed `*bakaną -> bacen` because `OEUnstressedAFronting` was fronting the infinitival `-an-` to `-en-`, even though the same note cites Ringe-Taylor's contrast between infinitive `*bakan > OE bacan` and participial `*funðanăz > funden` [@RingeTaylor2014, pp. 126, 233]. A later chronology fix kept that contrast but repaired the implementation: after heavy-syllable `*ą` apocope, infinitival `*bakaną` leaves the nasal in coda position, secondary nasalization blocks fronting, and the test output is again `bacan`, while participles still give `-en`. That later derivational note is current insofar as it explains why the present grammar can distinguish regular infinitive `bacan` from regular participial `bacen` without changing the lexeme target.

Two older project detours should remain visible so they are not rediscovered as if current. First, the 2025 evaluator snapshots treated `bacana` as part of the generic `-ana` weak-tail problem; that was broad OE pipeline debugging, not lexical doubt about `bacan`. Second, March 2026 temporarily “fixed” the row by adding `{*ă}` to the A-restoration trigger set and rewriting strong-verb infinitives to `-ăną`, which did make `bakăną -> bacan` but also regressed ordinary fronting words such as `craft`, `dag`, and `mast`. The later April note explicitly reverses that direction by insisting that Class VI infinitives like `*bákaną` rely on plain suffix `a`, not breve `ă`, for the current row policy.

The remaining current verification note is worth keeping because it guards against a nearby misunderstanding. When the trigger set was later tightened so fronted `{*æ}` no longer counted as a back-vowel trigger, DEV_NOTES still records `bacan` among the A-restoration-dependent forms that remained correct. That means the row does not depend on the discarded over-broad trigger hack; it depends on the regular plain-`a` infinitive encoding and the repaired chronology.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2422-2485

- Source heading: `PGmc→OE TODOs / OE evaluator snapshot / Ending diagnostics`
- Source line or section hint: `lines 2422-2485`
- Status: `diagnostic_only`
- Issue tags: `weak_tail_cleanup`; `old_mismatch_snapshot`; `project_history`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs: `1943, 1967, 1971, 1972`

This early OE-wide snapshot keeps the first row-local failure in view: the project was still emitting `*bakăną -> bacana` and treating it as part of a broader `-ana` cleanup problem. The note pairs the generic to-do “reshape or drop weak-tail `ă/ą` endings in verbs” with the concrete sample mismatch ``*bakăną -> bacana`` versus target `bacan`. That evidence is useful only as chronology. It shows that `bacan` was already the expected OE target, while the wrong form was an unfinished weak-tail implementation shared with other infinitives such as `beġinnan`, `brecan`, `bringan`, and `brūcan`.

### DEV_NOTES:line-9185-9211

- Source heading: `The Problem / Tracing the Rules / What R/T Says`
- Source line or section hint: `lines 9185-9211`
- Status: `superseded`
- Issue tags: `fronting_overapplication`; `infinitive_vs_participle`; `diagnostic_trace`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This note preserves the most important superseded bug report. It states the wrong output plainly — `*bakaną → bacen` — and then explains that the infinitival `-an-` was being fronted by `OEUnstressedAFronting` and then reduced to `-en`. The same passage also keeps the decisive comparator from Ringe-Taylor: infinitive `*bakan > OE bacan`, but participial `*funðanăz > funden` [@RingeTaylor2014, pp. 126, 233]. Later work solves the implementation problem, so this fragment is no longer current row policy, but it remains the clearest replacement-note statement of why `bacen` was wrong for this row while still right for participles.

### DEV_NOTES:line-9497-9542

- Source heading: `Changes made / Results / Analysis: Why the Fix Fails`
- Source line or section hint: `lines 9497-9542`
- Status: `superseded`
- Issue tags: `breve_workaround`; `regression_history`; `a_restoration_trigger_set`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs: `2046, 2266, 2268, 2272, 2292`

This fragment records the abandoned workaround in full. DEV_NOTES changed the trigger set so `{*ă}` counted as a back vowel and rewrote five strong-verb infinitives, including `*bakaną → *bakăną`; the targeted outputs then improved to `bakăną → bacan`, `grabăną → grafan`, `wadăną → wadan`, `wakăną → wacan`, `waskăną → wascan`, and `weljăną → willan`. But the same note immediately marks the fix as a failure because it caused A-restoration to over-apply in unrelated lexemes: `kraftăz → craft` for expected `cræft`, `dagăz → dag` for expected `dæġ`, and similar regressions [@Campbell1959, §158; @RingeTaylor2014, §6.3.1]. For row 1934 this passage should be used only to document the superseded project detour `-ăną`, not as support for the live protoform.

### DEV_NOTES:line-10841-10895

- Source heading: `Expected Derivations / Implementation Results (2026-03-15)`
- Source line or section hint: `lines 10841-10895`
- Status: `current`
- Issue tags: `chronology_fix`; `infinitive_vs_participle`; `verification_history`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `1950`

This derivational note keeps the now-current phonological contrast in a form later writers can reuse. It sets out the expected table `*bakaną → bacan` beside `*bakanăz → bacen`, explains that after `*ą` apocope the infinitival nasal is word-final/coda while the participial nasal is not, and then reports the implementation result `bakaną   → bacan    ✓` together with `funðanăz → funden   ✓`. The main value of the fragment is that it separates two things that older notes temporarily conflated: regular infinitive `bacan` and regular participial `-en` belong to the same repaired chronology, so the row does not need a special lexical exemption.

### DEV_NOTES:line-21738-21750

- Source heading: `A. Empirical probes (stems with root *á, Class VI strong verb infinitives)`
- Source line or section hint: `lines 21738-21750`
- Status: `current`
- Issue tags: `current_row_policy`; `protoform_encoding`; `class_vi_infinitives`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2046, 2088, 2266, 2268, 2272`

This is the governing current-policy fragment for the row. It preserves the decisive probe pair verbatim: ``*bákăną`` gives wrong `bæcan`, but ``*bákaną`` gives correct `bacan`. DEV_NOTES then states the row policy in plain prose: “The current TSV has `*bákaną` with plain `a` for exactly this reason” and adds that the Class VI infinitives rely on plain suffix `a` to trigger `OEARestoration`. Use this fragment whenever the final report needs to justify why the live row keeps plain `-aną` instead of the older breve-marked workaround [@RingeTaylor2014, §6.3.1].

### DEV_NOTES:line-3138-3151

- Source heading: `Fix / Derivation / Impact`
- Source line or section hint: `lines 3138-3151`
- Status: `current`
- Issue tags: `trigger_set_correction`; `verification_history`; `a_restoration`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2046, 2088, 2266, 2272`

This verification fragment matters because it shows `bacan` survived a later tightening of the trigger logic. DEV_NOTES removes `{*æ}` from `OEARestorationTriggerVowel`, argues that only genuine back vowels should trigger restoration, and then reports: “All A-restoration-dependent forms verified: bacan, wadan, wascan, hlaþan, grafan, ġeall, hamer all correct.” That is current evidence that row 1934 depends on the repaired regular trigger set rather than on the earlier over-broad `{*ă}` hack [@RingeTaylor2014, §6.3.1].

### DEV_NOTES:line-36529-36533

- Source heading: `The canonical conditioning of A-restoration (literature consensus)`
- Source line or section hint: `lines 36529-36533`
- Status: `current`
- Issue tags: `handbook_consensus`; `regular_comparator`; `literature_quote`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2003, 2046`

This literature table is the best compact source fragment for the row's philological baseline. It keeps Campbell's quotation in a reusable form — “The restoration of *a* is common before all single consonants and geminates, e.g. *faran* go, *calan* be cold, *bacan* bake, *gnagan* gnaw, *grafan* dig …” — and pairs it with Ringe-Taylor's general rule that stressed `*æ` before a single consonant, geminate, or `sC` cluster plus a back vowel becomes `a` [@Campbell1959, §158; @RingeTaylor2014, §6.3.1]. For this slice that quotation should be preserved rather than paraphrased away, because it states directly that `bacan` is a textbook A-restoration outcome.

## Superseded or diagnostic material

Three non-current phases should stay distinct. The oldest `bacana` stage is generic weak-tail cleanup history. The middle `bacen` stage is the real row-local modelling bug, because it wrongly fronted an infinitive that the handbook tradition expects to stay `-an`. The `-ăną` / `{*ă}` phase is a later workaround that temporarily forced the right answer for `bacan` but only by breaking the trigger system elsewhere. None of those phases creates genuine lexical uncertainty about the target `bacan`.

## Open questions for later work

- Decide whether the final lexeme report needs both the Campbell quotation and the Ringe-Taylor contrast `bacan` vs. participial `funden`, or whether one of them can carry the philological burden alone.
- If the final report summarizes project chronology, keep the order explicit: `bacana` weak-tail cleanup history, then `bacen` fronting bug, then discarded `-ăną` workaround, then restored plain-`a` row policy.
- If row 2268 (`wacan`) is later sliced, note that it shares the Class VI plain-`a` policy fragment even though its live TSV row has separate lexeme-selection complications.
