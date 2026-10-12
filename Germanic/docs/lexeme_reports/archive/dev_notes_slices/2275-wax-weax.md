---
row_id: 2275
concept: wax
counterpart: weax
proto: *wáxsą
protoform: *wáxsą
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files: [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md]
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2275 wax / weax

## Current row state

- CONCEPT: `wax`
- COUNTERPART: `weax`
- PROTO: `*wáxsą`
- PROTOFORM: `*wáxsą`
- DERIVATION_CLASS: `regular`
- The live TSV row is sparse but stable: row 2275 keeps `COUNTERPART = weax`, `PROTO = PROTOFORM = *wáxsą`, has no explanatory row note, and carries only the duplicated inherited-source placeholder `Source: Wiktionary etymology (template:inh) | Source: Wiktionary etymology (template:inh)` [Germanic/data/germanic-aligned-final.tsv:1340-1340]. That duplicated source-note field is provenance of dataset intake, not the real authority for the row's current philological treatment.
- Current report infrastructure is thin. `coverage_audit.md` lists row 2275 as `regular`, with no packet, no memo, no pilot, and `none` under report triggers, which matches the file-system check: no row-specific support files were found under `packets/`, `research_memos/`, or `pilot/` for this noun row [Germanic/docs/lexeme_reports/coverage_audit.md:404-404]. Nearby row 2276 does have verb-specific `weaxan` support files, but those are for the separate infinitive row and should not be treated as noun-row authority.
- One older row-relevant analysis file does exist: `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md` preserves the diagnostic output `*waxsą → weahsa (exp. weax)` in a list of earlier false results [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:293-302]. That file is useful only as labeled project history, not as the current analysis.
- Dictionary and handbook support for the OE noun itself is straightforward. Clark Hall gives `weax (e) n. 'wax'` [@ClarkHall1960, s.v. "weax"; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:47392-47392]. Kroonen lists Proto-Germanic `*wahsa- n. 'wax' ... OE weax n. 'id.'` [@Kroonen2013; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:28710-28718]. Orel likewise gives `*waxsan sb.n.: ... OE weax id.` [@Orel2003, p. 439; docs/references/orel_handbook_germanic_etymology.vision.txt:48451-48458].

## Development-note summary

The surviving DEV_NOTES support for row 2275 is real but thin. There is no dedicated noun-row dossier comparable to the large row-specific notes written for harder cases. Instead, the live DEV_NOTES contribution is a short but important inventory entry inside the `*xC`-loss discussion: row 2275 is explicitly grouped under `*xs` cases that **do not** need any consonant-loss repair, because the cluster survives as OE `x` when no further consonant follows [Germanic/docs/DEV_NOTES.md:39265-39275]. This means the row should be documented as a regular preservation case, not as an unresolved apocope problem and not as a lexeme requiring special exception handling.

That short DEV_NOTES statement needs to be unpacked carefully, because the row can easily be blurred together with adjacent `weaxan` material. For this noun row, **PROTO** and **PROTOFORM** are both the project's active derivational input `*wáxsą`, the form actually used in the OE pipeline [Germanic/data/germanic-aligned-final.tsv:1340-1340]. **COUNTERPART** is the attested OE noun `weax`, i.e. the target noun form, not the verb and not a paradigm cell of the verb [@ClarkHall1960, s.v. "weax"; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:47392-47392]. Comparative dictionaries use different lemma conventions for the cognate set: Kroonen's headword is `*wahsa-`, while Orel's is `*waxsan` [@Kroonen2013; @Orel2003, p. 439]. Those are source-level proto lemmas, not the same thing as the dataset's row-local input string `*wáxsą`. Future work should therefore avoid collapsing three distinct layers into one label: comparative proto headword (`*wahsa-` / `*waxsan`), project input (`*wáxsą`), and OE output (`weax`).

The main sound-law point is also narrow but solid. Campbell's rule is explicit: `xs > ks` in OE, and he names `weaxan` among the examples showing that the cluster survives long enough to condition breaking and to surface orthographically as `x` [@Campbell1959, §416; docs/references/campbell_old_english_grammar.txt:11014-11017]. DEV_NOTES applies exactly that principle to row 2275, stating: `These do not require the loss rule. Per Campbell §416, *xs survives as x (= ks) when no further consonant follows` [Germanic/docs/DEV_NOTES.md:39273-39275]. For the noun `weax`, this is the whole current project claim. The row is regular because nothing after `*xs` triggers the later `xs > s` development.

The contrast with the shared Campbell §417 quotation remains useful, but only as contrast. DEV_NOTES preserves Campbell's wording that `When a consonant follows, xs > s in OE, e.g. *wastm* fruit, *-wæsma* growth (both related to *weaxan*)` [Germanic/docs/DEV_NOTES.md:8151-8155; @Campbell1959, §417]. That passage helps prevent an over-broad reading of the noun row: it explains why derivatives such as `wæstm` can lose the `x`-cluster before a consonant while bare `weax` does not. In other words, the noun row is not an exception to the `*xs + consonant` rule; it simply does not instantiate that environment.

The stale project history in `final_vowel_apocope_investigation.md` should be preserved, but only with a warning label. That file once recorded `*waxsą → weahsa (exp. weax)` alongside many other false noun outputs [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:298-298]. For row 2275, that is diagnostic evidence of an earlier implementation phase in which the project was still overgenerating a final vowel plus `-hsa` sequence. It is not current authority, and the later DEV_NOTES inventory effectively supersedes it by classifying `*wáxsą → weax` with the ordinary `*xs` survivors [Germanic/docs/DEV_NOTES.md:39270-39275]. The safe conclusion is therefore conservative: the row's current regular status is well supported, but the supporting DEV_NOTES prose is brief and mostly limited to rule placement rather than a full lexeme dossier.

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-39270-39275

- Source heading: `#### 6. Corpus rows that depend on the current loss rule`
- Source line or section hint: `lines 39270-39275`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `xs_preservation`; `no_loss_rule`; `regular_row`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2276`

This is the only strong lexeme-local DEV_NOTES anchor currently attached to row 2275, and it should be quoted directly in any future report. DEV_NOTES names the row itself — `2275 *wáxsą → weax` — and then states the policy sentence that matters: `These do not require the loss rule. Per Campbell §416, *xs survives as x (= ks) when no further consonant follows` [Germanic/docs/DEV_NOTES.md:39270-39275]. That makes the fragment strong enough to justify the row's present `regular` status, but it is still a short inventory note rather than a richer philological dossier.

### DEV_NOTES:line-8151-8155

- Source heading: `Campbell §417 (p.173)`
- Source line or section hint: `lines 8151-8155`
- Fragment type: `copied_shared_lexeme_fragment`
- Status: `current`
- Issue tags: `xs_plus_consonant`; `contrastive_background`; `derivative_environment`
- Recommended next use: `cite_as_background_only`
- Shared with row IDs: `2276` and `wæstm`-related material

This fragment is not noun-row-specific, but it is the best shared background for explaining why row 2275 is ordinary. DEV_NOTES quotes Campbell: `When a consonant follows, xs > s in OE, e.g. *wastm* fruit, *-wæsma* growth (both related to *weaxan*)` [Germanic/docs/DEV_NOTES.md:8151-8155; @Campbell1959, §417]. Its value for `weax` is contrastive: it marks the conditioning environment that the noun row lacks. Future writing should therefore use it only to explain why `weax` keeps `x` while `*xs + consonant` derivatives may not.

## Superseded or diagnostic material

- `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md` is explicitly superseded for this row's current analysis. Its `*waxsą → weahsa (exp. weax)` entry documents an older false-output state, not the present project position [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:298-298].
- The duplicated TSV source-note field is also diagnostic rather than explanatory. It records inherited-source ingestion, but it does not explain why the row is regular or why `*xs` survives here [Germanic/data/germanic-aligned-final.tsv:1340-1340].
- No row-specific packet, memo, or pilot file was located. That absence should be stated plainly rather than padded with verb-row `weaxan` material from 2276, which belongs to a different lexeme entry even if the two rows share etymological background [Germanic/docs/lexeme_reports/coverage_audit.md:404-404].

## Open questions for later work

- If this row is ever promoted beyond a slice into an indexed report, decide whether the short but explicit inventory note at `DEV_NOTES:line-39270-39275` is enough on its own, or whether the noun should remain unindexed until a fuller noun-specific dossier exists.
- If a future report wants a compact philological paragraph, keep the label distinction explicit: comparative proto headwords `*wahsa-` / `*waxsan` are not the same object as the dataset's active input `*wáxsą`, and neither is identical to the OE noun `weax` [@Kroonen2013; @Orel2003, p. 439; Germanic/data/germanic-aligned-final.tsv:1340-1340].
- If the project later revisits old apocope-era diagnostics, row 2275 is a good test case for documenting that the earlier `weahsa`-type failure has already been superseded by the later `*xs`-preservation analysis, not left open as a live problem.
