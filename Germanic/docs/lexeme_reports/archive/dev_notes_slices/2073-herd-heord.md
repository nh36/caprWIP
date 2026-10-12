---
row_id: 2073
concept: herd
counterpart: heord
proto: "*xérdō"
protoform: "*xérdō"
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: null
linked_research_memo_file: null
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
  - Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt
  - Germanic/tmp/old_english_sandbox_results_current.json
  - Germanic/tmp/old_english_sandbox_results_with_stages.json
current_status: "Row corrected in the live TSV from stale hierd to heord; surviving DEV_NOTES block is row-specific and current, while sandbox/current-source leftovers still preserve the old conflation with hierde 'herdsman'."
needs_literature_agent: no
---

# DEV_NOTES material — 2073 herd / heord

## Current row state

- The live OE row now reads `ID 2073`, `CONCEPT herd`, `COUNTERPART heord`, `PROTO *xérdō`, `PROTOFORM *xérdō`, `DERIVATION_CLASS regular`, with an explicit row note: `TSV fix: was 'hierd' (herdsman) but *xerdō 'herd' (noun) > heord (R/T p.182); hierde 'herdsman' < *hirdijaz (R/T p.248)`. This row currently treats `PROTO` and `PROTOFORM` as identical; the repair was a counterpart/lexeme-identity correction, not a paradigm-cell substitution. [Germanic/data/germanic-aligned-final.tsv:555-555]
- Coverage machinery still treats the row as uncovered ordinary material rather than as a tracked exception: `coverage_audit.md` lists `| 2073 | herd | heord | regular | no | - | - | - | none |`, `report_manifest.tsv` has no entry for row `2073`, and `oe_known_problems.tsv` has no row-local problem ticket for `2073`, `heord`, or `*xérdō`. [Germanic/docs/lexeme_reports/coverage_audit.md:276-276; Germanic/docs/lexeme_reports/report_manifest.tsv:1-13; Germanic/data/oe_known_problems.tsv:1-8]
- A stale upstream breadcrumb still survives in `old_english_wiktionary.tsv`, which gives `herd\thierd\tinh\ttemplate:inh\therd`. That stale inherited-source entry matches the pre-fix confusion noted in DEV_NOTES and should be treated as diagnostic only, not as the current row target. [Germanic/data/old_english_wiktionary.tsv:136-136]
- The compact published OE derivation snapshot is now exact for the live row: `PROTO: *xérdō`, `EXPECTED: heord`, `OUTPUTS: heord`, with the visible OE-side chain `NWGmc Final Long O Raising: *xérdu` > `OE Breaking: *xéordu` > `OE Velar Fricative Palatalization: *çéordu` > `OE High Vowel Apocope: *çéord` > orthographic `h*éord` > surface `heord`. [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:2347-2367]
- An older full trace snapshot is still useful but must be labeled pre-fix/diagnostic: it still says `EXPECTED: hierd` while producing `OUTPUTS: heord`. The derivation itself is clean and confirms the row-specific DEV_NOTES claim that the phonology was right before the TSV was corrected: `*x*e*r*d*ō` > `BreakingLengthening: *x*eo*r*d*u` > `VelarFricPal: *ç*eo*r*d*u` > `HighVowelApocope: *ç*eo*r*d` > `Orthography: heord` > `Surface: heord`. [Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:19457-19510]
- Current sandbox artifacts are also stale and diagnostic. `old_english_sandbox_results_current.json` still stores `counterpart: "hierd"` and no outputs, and the staged sandbox trace again preserves the pre-fix comparator while failing at `ProtoRhoticFronting` and ending with fallback `Surface: herdō`. Those files illuminate current procedural drift, not current lexical policy. [Germanic/tmp/old_english_sandbox_results_current.json:1297-1301; Germanic/tmp/old_english_sandbox_results_with_stages.json:20197-20336]

## Development-note summary

A true row-specific DEV_NOTES block survives for this row, and it remains the controlling authority. Its central claim is not that `heord` needs a special phonological exception, but that the older target `hierd` was a **lexeme conflation**: the noun `herd` and the agent noun `herdsman/shepherd` were mixed together in source data. DEV_NOTES states flatly that “`Row 2073 has *xerdō → hierd but FST produces heord. This looks like an ie/eo confusion, but is actually a TSV data error: the COUNTERPART is wrong.`” [Germanic/docs/DEV_NOTES.md:14595-14598]

The row-specific block then stabilizes the distinction that this slice must preserve. For the noun row, `PROTO = PROTOFORM = *xérdō` and the correct OE target is `heord`; for the separate agent noun, the relevant etymon is `*hirdijaz`, whose OE outcome is `hierde`, not bare `hierd`. DEV_NOTES quotes Ringe–Taylor for both: “`PGmc *herdō 'herd' (Goth. hairda) > PNWGmc *herdu (ON hjorð, OHG herta) > OE heord`” and “`PGmc *hirdijaz 'herdsman' (Goth. hairdeis, ON hirðir, OS hirdi, OHG hirti) > *hiordi > WS *hierdi > hierde`”; it also preserves Campbell’s footnote that “`The diphthong of *hiorde* herdsman, is probably the mutation of that of *heordi- ... an analogical formation with the vowel of *heord*, herd.`” [Germanic/docs/DEV_NOTES.md:14609-14618]

Later DEV_NOTES material does not supersede that fix; it reinforces it. Shared rule-history notes keep `*xérdō > heord` as a successful heavy `-rd` short-diphthong case under high-vowel apocope, and a later smoothing discussion explicitly says that `eo` before `-rd` is retained rather than smoothed away, citing `heord` as the comparison form. So the surviving row picture is conservative and stable: the identity problem is solved; the phonology is regular; the remaining noise is stale source/debug residue. [Germanic/docs/DEV_NOTES.md:14593-14644,29430-29435,29459-29466,36186-36190]

## Relevant DEV_NOTES fragments

### Germanic/docs/DEV_NOTES.md:14593-14644

- Source heading: `OE heord 'herd' vs hierde 'herdsman' (2026-04-07)`
- Source line hint: `lines 14593-14644`
- Fragment type: `row_specific_lexeme_identity_and_data_correction`
- Status: `current`
- Issue tags: `counterpart_fix`; `lexeme_conflation`; `breaking`; `i_umlaut`; `agent_noun_vs_simplex`
- Recommended next use: `treat as the row-defining authority whenever explaining why this row targets heord and why PROTO/PROTOFORM remain *xérdō`
- Shared-with rows if relevant: `none; contrastively relevant to any future shepherd/herdsman row built on *hirdijaz`

This is the decisive surviving row-specific note. DEV_NOTES opens with the direct correction: “`Row 2073 has *xerdō → hierd but FST produces heord. This looks like an ie/eo confusion, but is actually a TSV data error: the COUNTERPART is wrong.`” [Germanic/docs/DEV_NOTES.md:14595-14598] It then separates two etyma in a compact table: `*herdō` = “`herd` (noun, ō-stem)” > `heord`, versus `*hirdijaz` = “`herdsman` (agent noun, ja-stem)” > `hierde` [Germanic/docs/DEV_NOTES.md:14602-14607]. The embedded primary-source quotations are still the best row-local evidence and should be kept intact: R/T are quoted for the noun pathway, “`PGmc *herdō 'herd' (Goth. hairda) > PNWGmc *herdu (ON hjorð, OHG herta) > OE heord`,” and for the agent noun, “`PGmc *hirdijaz 'herdsman' ... > *hiordi > WS *hierdi > hierde`” [Germanic/docs/DEV_NOTES.md:14609-14615]. Campbell’s footnote is also preserved as row-relevant contrast evidence: “`The diphthong of *hiorde* herdsman, is probably the mutation of that of *heordi- ... an analogical formation with the vowel of *heord*, herd.`” [Germanic/docs/DEV_NOTES.md:14616-14618]

DEV_NOTES then spells out the sound-change split rather than leaving it implicit. For `*herdō` “herd,” it gives “`*e → eo (breaking before *rd)`” and “`Result: heord`”; for `*hirdijaz` “herdsman,” it gives “`*i → io (breaking before *rd) → ie (i-umlaut from *-ij-)`” and “`Result: hierde (with weak ja-stem ending)`” [Germanic/docs/DEV_NOTES.md:14620-14628]. The conclusion remains fully current: “`The FST is correct: *xerdō → heord. The TSV COUNTERPART hierd is wrong—it should be heord.`” DEV_NOTES immediately adds the crucial guardrail, “`If we wanted the herdsman, it would be hierde`” [Germanic/docs/DEV_NOTES.md:14630-14641]. This is row-specific support, not shared background only.

### Germanic/docs/DEV_NOTES.md:29428-29475

- Source heading: `high-vowel apocope refactor / verification probes`
- Source line hint: `lines 29428-29475`
- Fragment type: `shared_background_with_explicit_row_probe`
- Status: `current`
- Issue tags: `high_vowel_apocope`; `short_diphthong_weight`; `heavy_rd_cluster`; `regression_check`
- Recommended next use: `cite when documenting why heord loses final -u regularly once breaking has created eo before the heavy -rd cluster`
- Shared-with rows if relevant: `2052 hall / heall; 2120 march / mearc; 2068 heaven / heofon; other short-diphthong apocope probes`

This fragment is not the identity fix, but it is current and row-relevant rule support. DEV_NOTES says the apocope clauses were split by weight, and the clause relevant here is: “`ShortDiphthong + C + C+ (2+ C) → heavy → apocopate (e.g. *xérdō → heord, *márkō → mearc, *xállō → heall).`” [Germanic/docs/DEV_NOTES.md:29430-29435] The verification table then repeats the row explicitly: “`| *xérdō | heord | heord | HEAVY (rd cluster) |`” [Germanic/docs/DEV_NOTES.md:29459-29466].

The evidential status here is shared-background rule history with an explicit row probe. It does not argue that `heord` should replace `hierd`; fragment 1 already settled that. What it adds is a later confirmation that, once the row is correctly identified as `*xérdō 'herd'`, the FST’s ordinary weight-sensitive OE high-vowel apocope handles the output without a lexeme-specific patch. DEV_NOTES even logs `heord` among the regressions that “`self-resolved`” after the refactor [Germanic/docs/DEV_NOTES.md:29473-29475].

### Germanic/docs/DEV_NOTES.md:36186-36190

- Source heading: `meord / mēd smoothing discussion`
- Source line hint: `lines 36186-36190`
- Fragment type: `shared_background_only`
- Status: `current_background`
- Issue tags: `smoothing`; `rd_cluster`; `dialect_background`; `eo_retention`
- Recommended next use: `use only to prevent misclassification of heord as a smoothing casualty or as a form that should lose eo before -rd`
- Shared-with rows if relevant: `2124 meed / meorde; other -rd diphthong rows`

This later fragment is shared background only, but it still matters for row 2073. While discussing `meord`, DEV_NOTES says the diphthong before `-rd-` lies “`outside the smoothing rule`” and states plainly: “`Both dialects retain *eo* before -rd. (Cf. WS *heord* 'herd', Anglian *heord* / *hiord* — both keep the diphthong; smoothing affects *sēoc → sēc 'sick'* before /k/, not /-rd/.)`” [Germanic/docs/DEV_NOTES.md:36186-36190] That means the row should not be rewritten as though `eo` before `-rd` were an unstable or automatically smoothed sequence.

Its support is therefore shared-background-only, not row-specific. It is useful chiefly as a fence against later overcorrection: `heord` is not merely an arbitrary West Saxon spelling to be replaced by simple `e`, and Anglian `hiord` here is background dialect information, not a reason to abandon the live row target `heord`. [Germanic/docs/DEV_NOTES.md:36186-36190]

## Superseded or diagnostic material

- The stale `hierd` residue in `old_english_wiktionary.tsv`, the current sandbox JSON, and the older full-trace snapshot should all be read as **diagnostic leftovers of the pre-2026-04-07 conflation**, not as current row authority. DEV_NOTES’ project-status ledger records the event succinctly as “`heord fix: was 'hierd' (herdsman ≠ herd)`,” which is exactly what those stale artifacts preserve. [Germanic/docs/DEV_NOTES.md:10396-10398; Germanic/data/old_english_wiktionary.tsv:136-136; Germanic/tmp/old_english_sandbox_results_current.json:1297-1301; Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:19457-19460]
- General DEV_NOTES quotations about `hierde` belong to the contrast lexeme, not to row `2073` itself. Campbell’s quoted discussion of W-S `io > ie` gives `hierde shepherd` among umlauted broken forms, and a later morphology note uses `*hierde* < *xerdijaz` as a standard ja-stem comparison; both are useful only to confirm that the **agent noun** pathway is different and that bare `hierd` was never the right noun target. [Germanic/docs/DEV_NOTES.md:15269-15278,26260-26264]
- The older full trace is especially worth labeling carefully: its `EXPECTED: hierd` field is superseded, but its `OUTPUTS: heord` line is still diagnostically valuable because it shows the phonology had already been producing the noun outcome before the data fix landed. [Germanic/docs/debug_snapshots/oe_full_trace_report_2026-03-11.txt:19457-19510]
- No surviving material argues for changing `PROTOFORM` away from `*xérdō`. Unlike paradigm-cell repair rows such as `heofon` or `meorde`, this row’s correction is lexical identification only; any attempt to rewrite the row around `*hirdijaz` would be a category error unless the concept itself changed from “herd” to “herdsman/shepherd.” [Germanic/data/germanic-aligned-final.tsv:555-555; Germanic/docs/DEV_NOTES.md:14593-14644]

## Open questions for later work

- The lexeme decision is closed, but stale collateral remains. If maintenance work later regenerates source tables and sandbox diagnostics, row `2073` should be one of the cleanup checks so that `hierd` no longer survives in inherited-source and sandbox artifacts after the live TSV fix. [Germanic/data/old_english_wiktionary.tsv:136-136; Germanic/tmp/old_english_sandbox_results_current.json:1297-1301]
- If a later packet or memo is commissioned, it may be worth documenting whether the Anglian comparison form `hiord` deserves explicit variant handling anywhere. The surviving DEV_NOTES material mentions it only as shared dialect background, not as this row’s target. [Germanic/docs/DEV_NOTES.md:36186-36190]
- If future editorial work creates or revises a separate shepherd/herdsman row, that file should cite the present row’s contrast material directly and keep `*hirdijaz > hierde` segregated from `*xérdō > heord`; the conflation is precisely the mistake this row’s DEV_NOTES block was written to prevent. [Germanic/docs/DEV_NOTES.md:14602-14618,14630-14641]
