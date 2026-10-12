---
row_id: 2276
concept: wax
counterpart: weaxan
proto: *wáxsaną
protoform: *wáxsaną
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2276-wax-weaxan.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2276-wax-weaxan.md
linked_dossier_or_analysis_files: []
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2276 wax / weaxan

## Current row state

- CONCEPT: `wax` [Germanic/data/germanic-aligned-final.tsv:1342-1342]
- COUNTERPART: `weaxan` [Germanic/data/germanic-aligned-final.tsv:1342-1342]
- PROTO: `*wáxsaną` [Germanic/data/germanic-aligned-final.tsv:1342-1342]
- PROTOFORM: `*wáxsaną` [Germanic/data/germanic-aligned-final.tsv:1342-1342]
- DERIVATION_CLASS: `regular` [Germanic/data/germanic-aligned-final.tsv:1342-1342]
- The live row already distinguishes the verb from the neighboring noun row, but only imperfectly. Row `2275` is the noun `weax` from `*wáxsą`, while row `2276` is the verb infinitive `weaxan` from `*wáxsaną`; the current note's shorthand `weax→weaxan` is therefore a disambiguation aid that risks re-blurring the very distinction it is trying to mark [Germanic/data/germanic-aligned-final.tsv:1340-1342].
- Row-specific support files exist and should stay linked: packet `Germanic/docs/lexeme_reports/packets/2276-wax-weaxan.md` and memo `Germanic/docs/lexeme_reports/research_memos/2276-wax-weaxan.md` [Germanic/docs/lexeme_reports/packets/2276-wax-weaxan.md:1-132; Germanic/docs/lexeme_reports/research_memos/2276-wax-weaxan.md:1-109]. No row-specific pilot file or clearly row-specific dossier/analysis file turned up during slice preparation.
- Current derivational support is not a mismatch story. The packet's compact trace already gives `PROTO: *wáxsaną`, `EXPECTED: weaxan`, `OUTPUTS: weaxan`, with explicit OE stages `*wæxsaną > *weaxsaną > weaxan` [Germanic/docs/lexeme_reports/packets/2276-wax-weaxan.md:17-42].
- The memo's most important row-policy conclusion is likewise documentary rather than phonological: keep `PROTO = PROTOFORM = *wáxsaną`, keep `COUNTERPART = weaxan`, and treat the current note wording as the main thing needing caution because bare `weax/wax` is ambiguous between noun and non-infinitival verbal material [Germanic/docs/lexeme_reports/research_memos/2276-wax-weaxan.md:54-80].

## Development-note summary

This row is best understood as a **regular attested OE verb row whose remaining problem is note discipline, not sound-change failure**. The live TSV already has `PROTO = PROTOFORM = *wáxsaną`, and the current packet trace reaches `weaxan` without any repair rule or hidden paradigm-cell substitution [Germanic/data/germanic-aligned-final.tsv:1342-1342; Germanic/docs/lexeme_reports/packets/2276-wax-weaxan.md:17-42]. The essential replacement note therefore has to preserve three distinct layers instead of collapsing them: `PROTO` is the dataset's comparative/project label, `PROTOFORM` is the same string because no separate OE-facing surrogate input is currently in play, and `COUNTERPART` is the attested Old English infinitive `weaxan` [Germanic/data/germanic-aligned-final.tsv:1342-1342]. Comparative dictionaries do not invalidate that setup, but they do show why the layers must stay separate: Kroonen cites the cognate set as `*wahs(j)an-`, Orel gives `*waxsanan`, and Ringe-Taylor discuss the prehistory as `PGmc *wahsijana ... > *weehsan > OE weaxan` [@Kroonen2013, s.v. *wahs(j)an-; @Orel2003, s.v. *waxsanan; @RingeTaylor2014; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:28723-28730; docs/references/orel_handbook_germanic_etymology.vision.txt:48470-48474; docs/references/ringe_taylor_linguistic_history_vol2.txt:10238-10240]. Those comparative headwords are source-faithful lexical labels, but they are not reasons to rewrite the live row's OE-directed input `*wáxsaną`.

The surviving DEV_NOTES material is thinly row-specific but still good enough to preserve the crucial phonological point. The late `*x`-loss audit explicitly lists row `2276 *wáxsaną → weaxan` under the `*xs` set and immediately states: “These do not require the loss rule. Per Campbell §416, *xs survives as `x` (= ks) when no further consonant follows” [Germanic/docs/DEV_NOTES.md:39265-39276]. That is the best current project-language anchor for the row, because it says in one place what future editors most need to remember: `weaxan` is **not** a preconsonantal `x`-loss item. Campbell and Brunner provide the historical explanation behind that project rule. Campbell's wording, preserved in DEV_NOTES, is that “When a consonant follows, xs > s in OE, e.g. wæstm fruit, -wæsma growth (both related to weaxan) ...” [Germanic/docs/DEV_NOTES.md:39033-39040; @Campbell1959, §417]. Brunner states the conditioning even more narrowly: “Wenn auf hs andere Konsonanten (auch j) folgen, ist h ausgefallen,” citing `wæstm Wuchs (zu weaxan)` but also noting retention elsewhere [Germanic/docs/DEV_NOTES.md:39058-39070; @SieversBrunner1965, §221]. For row `2276`, the practical conclusion is straightforward: the `xs/hs` cluster is lost in forms like `wæstm` where another consonant follows, but the citation-form infinitive `weaxan` itself remains in the preserved-`x` bucket.

That is why the noun/verb separation with row `2275` has to stay explicit. The late audit helpfully lists both `2275 *wáxsą → weax` and `2276 *wáxsaną → weaxan` on separate lines, which is stronger evidence than the current TSV note's compressed wording because it shows the project already treats noun and verb as distinct lexeme rows even when both are inherited `*xs` continuations [Germanic/docs/DEV_NOTES.md:39269-39271]. The older diagnostic material in `final_vowel_apocope_investigation.md` is noun-row history only: it preserves a former bad output `*waxsą → weahsa (exp. weax)` and should not be recycled as evidence for the verb row [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:298-298]. The packet's local lexical-table hit `wax -> weax` is similarly noun-oriented background, not authority for row `2276` [Germanic/docs/lexeme_reports/packets/2276-wax-weaxan.md:98-108].

The row's main documentation hazard is therefore lexical ambiguity on the Old English side, not uncertainty about the intended counterpart. Local reference works support `weaxan` directly as the verb lemma, with variant spellings such as `weahsan`, `wexan`, and `wæxan` [@ClarkHall1960, s.v. "weaxan"; @SieversBrunner1965; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:47395-47403; docs/references/brunner_1965_altenglische_grammatik.vision.txt:29152-29158]. Bright's verb note is particularly useful because it says succinctly that “`weaxan (weahsan) has adopted commonly the pret. of a reduplicating verb`,” which keeps the infinitive distinct from preterite material [@BrightCassidyRingler1971; docs/references/bright_anglo_saxon_reader.vision.txt:3100-3101]. Clark Hall makes the ambiguity problem explicit from the other direction by recording `wax = wēox pret, 3 sg. of weaxan` [@ClarkHall1960, s.v. "wax"; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:46951-46953]. In other words, bare `wax/weax` can denote the neighboring noun row, or it can denote a non-infinitival verbal form in dictionary practice. The slice should therefore preserve the memo's conservative conclusion almost verbatim: row `2276` targets the OE strong-verb infinitive `weaxan`, while noun `weax` belongs to row `2275` and preterite `wax/wēox` belongs to a different paradigm slot [Germanic/docs/lexeme_reports/research_memos/2276-wax-weaxan.md:54-80].

## Relevant DEV_NOTES fragments

No securely attachable **dedicated current row-specific** DEV_NOTES dossier survives for row `2276`. The usable material is instead shared phenomenon-level doctrine plus one late row inventory that names the lexeme directly. That thinness should be stated openly rather than papered over.

### DEV_NOTES:line-39260-39276

- Source heading: `6. Corpus rows that depend on the current loss rule`
- Source line or section hint: `lines 39260-39276`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `current`
- Issue tags: `xs_cluster`; `x_loss_guard`; `noun_verb_separation`; `regular_row`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2017,2031,2146,2194,2275,2276`

This is the strongest current DEV_NOTES anchor for the row because it is both explicit and narrow. DEV_NOTES lists row `2276` by exact pair — ``2276 `*wáxsaną` → `weaxan``` — inside the `*xs` bucket and then says of the whole set: “These do not require the loss rule. Per Campbell §416, *xs survives as `x` (= ks) when no further consonant follows” [Germanic/docs/DEV_NOTES.md:39265-39276]. For this slice, the value of the fragment is twofold. First, it directly blocks a future overcorrection in which `weaxan` would be treated like `wæstm` and forced through `x`-loss. Second, it preserves the noun/verb split that the live TSV note only gestures toward: row `2275` noun `weax` and row `2276` infinitive `weaxan` are listed as separate preserved-`*xs` rows, not as one row with a derived citation-form gloss [Germanic/docs/DEV_NOTES.md:39269-39271]. If any DEV_NOTES line is later considered for index use, this is the best candidate.

### DEV_NOTES:line-39033-39040

- Source heading: `Campbell §417`
- Source line or section hint: `lines 39033-39040`
- Fragment type: `shared_handbook_quote`
- Status: `current`
- Issue tags: `campbell_quote`; `xs_before_consonant`; `wæstm_vs_weaxan`; `quotation_preserved`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2276` and other `*xs + C` comparison rows

This fragment is not row-specific in the same way as the late audit, but it preserves the direct quotation that explains why the audit classifies `weaxan` as a preservation case. DEV_NOTES quotes Campbell: “When a consonant follows, xs > s in OE, e.g. wæstm fruit, -wæsma growth (both related to weaxan) ...” [Germanic/docs/DEV_NOTES.md:39033-39040; @Campbell1959, §417]. The useful point for row `2276` is the conditioning phrase **“when a consonant follows.”** That means `wæstm` is evidence about `*xs + C`, not about the infinitive `weaxan` itself. This distinction is easy to lose when later prose cites the `wæstm` comparandum too quickly. The slice should therefore keep the quotation as background explaining the structural contrast, not as a reason to recast `weaxan` as if it belonged to the loss environment.

### DEV_NOTES:line-39058-39070

- Source heading: `Brunner §221`
- Source line or section hint: `lines 39058-39070`
- Fragment type: `shared_handbook_quote`
- Status: `current`
- Issue tags: `brunner_quote`; `hs_plus_consonant`; `wæstm_vs_weaxan`; `conditioning`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs: `2276` and related `*xs` rows

This Brunner fragment is the most precise statement of conditioning preserved in DEV_NOTES and is worth keeping alongside Campbell because it says in so many words that loss happens when another consonant follows `hs`: “Wenn auf hs andere Konsonanten (auch j) folgen, ist h ausgefallen,” with examples including `wasma Kraft (ahd. wahsamo), wæstm Wuchs (zu weaxan)` [Germanic/docs/DEV_NOTES.md:39058-39070; @SieversBrunner1965, §221]. For row `2276`, that quotation does important cleanup work. It shows that references to `wæstm`, `wahsamo`, or related derivatives are supportive only insofar as they define the loss environment; they do **not** turn the infinitive `weaxan` into an exception or a hidden analogical form. This is especially valuable because the row's note already risks lexical conflation on the OE side. The Brunner quotation keeps the consonant-conditioning story exact enough that the row can stay a simple regular infinitive row.

## Superseded or diagnostic material

- The current TSV note's wording `weax→weaxan` is useful only as a shorthand reminder that the row is verbal, but it is not safe as a stand-alone description of the OE target. Bare `weax/wax` is ambiguous between noun row `2275` and non-infinitival verbal forms such as Clark Hall's `wax = wēox` [Germanic/data/germanic-aligned-final.tsv:1342-1342; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:46951-46953; Germanic/docs/lexeme_reports/research_memos/2276-wax-weaxan.md:56-79].
- The packet's lexical-table hit `wax | weax` should remain clearly subordinate. It is a useful warning about noun-level lookup noise, but it is not evidence that row `2276` should be described through bare `weax` rather than through the infinitive `weaxan` [Germanic/docs/lexeme_reports/packets/2276-wax-weaxan.md:98-108].
- The old apocope investigation entry `*waxsą → weahsa (exp. weax)` is diagnostic history for noun row `2275`, not a surviving authority for the verb row [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:298-298]. It is useful only as a reminder that noun and verb must not be merged just because both descend from `*wax-` material.
- No superseded alternate `PROTOFORM`, no paradigm-cell rescue, and no row-specific `oe_known_problems.tsv` exception note surfaced in the support files. The danger here is not hidden morphology; it is over-reading thin notes and cross-row background [Germanic/docs/lexeme_reports/research_memos/2276-wax-weaxan.md:42-50,81-109].

## Open questions for later work

- If this row is later promoted into a final report, the safest top-line sentence is probably the memo's: row `2276` is the attested OE strong-verb infinitive `weaxan`, with `PROTO = PROTOFORM = *wáxsaną`; noun `weax` is row `2275`, and bare `wax/wēox` belongs only to paradigm or dictionary background [Germanic/docs/lexeme_reports/research_memos/2276-wax-weaxan.md:74-80].
- If later indexing is attempted, keep expectations modest. The row has one genuinely useful lexeme-addressable DEV_NOTES anchor (`DEV_NOTES:line-39260-39276`) and two good shared conditioning anchors (`DEV_NOTES:line-39033-39040`, `DEV_NOTES:line-39058-39070`), but no surviving dedicated mini-dossier comparable to the strongest indexed slices.
- If later source expansion is wanted, keep comparative lemma evidence (`*wahs(j)an-`, `*waxsanan`, `*wahsijana`) visibly separate from the live TSV input `*wáxsaną`. That separation is the main thing preventing a clean regular row from becoming a notation dispute [@Kroonen2013, s.v. *wahs(j)an-; @Orel2003, s.v. *waxsanan; @RingeTaylor2014].
