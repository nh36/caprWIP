---
row_id: 2208
concept: spindle
counterpart: spinl
proto: *spénnilō
protoform: *spénnilō
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2208 spindle / spinl

## Current row state

- Live TSV row 2208 now has `TOKENS = s p i n l`, `COUNTERPART = spinl`, `PROTOFORM = *spénnilō`, `PROTO = *spénnilō`, `DERIVATION_CLASS = regular`, and `CONCEPT = spindle` [Germanic/data/germanic-aligned-final.tsv:1078-1078].
- The live TSV note makes the controlling row decision explicit: the target was retargeted away from post-OE `spindle` to OE `spinl`, identified there as the syncopated variant of `spinel`, while the comparative proto was retained rather than replaced by the earlier DEV_NOTES experiment with single-`n` `*spenilō` [Germanic/data/germanic-aligned-final.tsv:1078-1078].
- Later reporting must still keep the three labels distinct even though the live row currently writes the same accented string in both proto columns: `PROTO` is the comparative headword represented in the row as `*spénnilō`; `PROTOFORM` is the OE-row input that the repaired derivation now tests; `COUNTERPART` is the OE target `spinl` [Germanic/data/germanic-aligned-final.tsv:1078-1078].

## Development-note summary

DEV_NOTES preserves a clear philological correction that remains fully current: the OE form is not `spindle`. The row-specific source audit quotes Clark Hall directly, "`spinel` f., gs. spinle 'spindle,' A, Cp.," and adds the cross-reference "`spinl, spinil = spinel`"; it also preserves the BT addendum `Spinil stilium...` and compound evidence such as `eár-spinl` and `wealc-spinl` [DEV_NOTES:line-40293-40306; @ClarkHall1960, s.v. "spinel"; @BosworthToller1898, s.v. "spinil"]. That is the durable reason the live row now targets `spinl`: `spinl` is an attested OE syncopated variant, whereas `spindle` is the later form with intrusive `-d-`.

The same DEV_NOTES audit also preserves the comparative etymology that the live TSV note still follows. Kluge--Seebold is quoted as deriving the word from "`wg. *spennilō` ... auch in ae. `spinel`, afr. `spindel`; ... `-d-` ist ein Gleitlaut [zwischen -n- und -l-]`," and Orel likewise gives "`*spennilō(n) ... OE spinel 'spindle'`" [DEV_NOTES:line-40313-40326; @KlugeSeebold2011, s.v. "Spindel"; @Orel2003, p. 364]. That comparative support is why the present row note says the proto was retained: the project corrected the OE target without abandoning the standard WGmc reconstruction.

Campbell's brief note on the same noun remains useful background and should be carried forward because DEV_NOTES already extracted the wording that matters: "`netel` nettle, `spinel` spindle; the medial syllable is not syncopated in the inflected forms..." [DEV_NOTES:line-782-785; @Campbell1959, §589]. This does not by itself force the row target to be `spinl`, but it does support the basic OE-side picture preserved elsewhere in DEV_NOTES: the unsyncopated citation form `spinel` exists, and syncopation belongs to a real OE alternation rather than to a fabricated modern back-formation.

The project chronology then splits into one superseded route and one current route. The superseded route was the first recommendation in §17.45: because the cascade already produced `spinl` from single-`n` `*spinilō`, DEV_NOTES originally proposed changing both `PROTOFORM` and `PROTO` to `*spenilō` and retargeting the row to `spinl` [DEV_NOTES:line-40344-40460]. That proposal is no longer the live row policy. The live TSV note and later DEV_NOTES material instead keep the comparative proto and treat the real problem as a phonological derivation gap between retained `*spénnilō` and the now-correct OE target `spinl` [Germanic/data/germanic-aligned-final.tsv:1078-1078; DEV_NOTES:line-42073-42188].

The current DEV_NOTES solution is therefore not "change the proto until the old cascade works," but "keep the comparative proto and repair the OE derivation." The interim diagnosis isolates the missing environment cleanly: after Step 1 retargeted the row to `spinl` and Step 2 extended preconsonantal `nn > n`, `*spinilō` still derived `spinl`, but retained-geminate `*spennilō` derived only `spinlu` because trisyllabic high-vowel apocope lacked a clause for a short vowel followed by a heavy-by-position first syllable (`ShortV + 2+C + ShortV + C+ + final high vowel`) [DEV_NOTES:line-40488-40610; @Campbell1959, §345; @RingeTaylor2014, §6.8.1]. The later §17.45.4 note records the durable form of that diagnosis and the repaired derivation path from retained geminate input: `*spénnilō → *spennilu → *spinnilu → *spinnil → *spinnl → *spinl` [DEV_NOTES:line-42073-42188].

For later report writing, the practical row-level conclusion is straightforward. The current row does **not** treat `spinl` as a reason to rewrite the comparative etymon to non-geminate `*spenilō`; that was an earlier convenience proposal. The current row instead pairs the comparative proto tradition `*spennilō / *spénnilō` with the attested OE syncopated target `spinl`, on the understanding that the intrusive `-d-` belongs to later High German / Old Frisian / Middle English / Modern English development, not to OE itself [DEV_NOTES:line-40307-40326; DEV_NOTES:line-42077-42188; @KlugeSeebold2011, s.v. "Spindel"; @Orel2003, p. 364].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-782-785

- Source heading: `Campbell quotation on nettle and spindle`
- Source line or section hint: `lines 782-785`
- Fragment type: `bibliography_or_source_audit_for_lexeme`
- Status: `background`
- Issue tags: `campbell`; `syncopation`; `spinel`; `oe_attestation`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs: `2139`

DEV_NOTES preserves a useful direct quotation from Campbell: "`netel` nettle, `spinel` spindle; the medial syllable is not syncopated in the inflected forms..." [@Campbell1959, §589]. For row 2208 this is background rather than the decisive attachment, but it is worth keeping because it records the unsyncopated OE form `spinel` in a standard grammar and implicitly places syncopation outside the inflected paradigm.

### DEV_NOTES:line-40293-40326

- Source heading: `source audit on actual OE form and retained comparative proto`
- Source line or section hint: `lines 40293-40326`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `attestation`; `source_audit`; `proto_reconstruction`; `glide_d`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the main current philological attachment for the row. It preserves Clark Hall's "`spinel` ...`spinl, spinil = spinel`" wording, the BT `Spinil` evidence, and Kluge--Seebold's explicit statement that the `-d-` is a glide consonant inserted between `-n-` and `-l-` [@ClarkHall1960, s.v. "spinel"; @BosworthToller1898, s.v. "spinil"; @KlugeSeebold2011, s.v. "Spindel"]. It also aligns Orel with the same reconstruction, so later reports can say both parts of the current row policy in one place: OE target `spinl/spinel`, comparative proto `*spennilō` [@Orel2003, p. 364].

### DEV_NOTES:line-40344-40460

- Source heading: `single-n probe and the first recommendation to rewrite the proto`
- Source line or section hint: `lines 40344-40460`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `superseded`
- Issue tags: `project_history`; `single_n_option`; `proto_vs_protoform`; `superseded_decision`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This fragment remains important project history because it explains an abandoned but initially attractive solution. DEV_NOTES showed that single-`n` `*spinilō` already produced `spinl` and therefore recommended a TSV-only rewrite to `*spenilō` plus `spinl`. That recommendation is now superseded by the live row's decision to keep the comparative proto and fix the phonology instead, but later writers will need this fragment to understand why older discussion may mention `*spenilō` as if it had become policy.

### DEV_NOTES:line-40488-40610

- Source heading: `residual spinlu problem after the row had already been retargeted`
- Source line or section hint: `lines 40488-40610`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `apocope`; `syllable_weight`; `degemination`; `implementation_diagnostics`
- Recommended next use: `use_to_explain_superseded_analysis`
- Shared with row IDs:

This is diagnostic rather than final authority, but it preserves the crucial reasoning that made the current row policy viable. After the target had already been corrected to `spinl`, DEV_NOTES showed why retained `*spennilō` still failed: the cascade lacked a trisyllabic apocope clause for heavy-by-position first syllables, so `*spennilō` stalled at `spinlu` even after `nn > n` before sonorants [@Campbell1959, §345; @RingeTaylor2014, §6.8.1]. That diagnosis is later absorbed into the final §17.45.4 note, but the interim fragment still matters because it explains what exactly had to be repaired.

### DEV_NOTES:line-42073-42188

- Source heading: `final row policy with retained proto and repaired spinl derivation`
- Source line or section hint: `lines 42073-42188`
- Fragment type: `lexeme_specific`
- Status: `current`
- Issue tags: `current_policy`; `derivation_trace`; `apocope_fix`; `retained_proto`
- Recommended next use: `cite_in_final_report`
- Shared with row IDs:

This is the best current working authority for the live row as it now stands. It explicitly recaps Step 1 as the retargeting from `spindle` to attested `spinl`, preserves Step 2's preconsonantal degemination, identifies the missing heavy-by-position apocope environment, and then writes out the expected retained-proto derivation `*spénnilō → *spennilu → *spinnilu → *spinnil → *spinnl → *spinl` [@Campbell1959, §345; @RingeTaylor2014, §6.8.1]. For later report work, this is the fragment that licenses keeping comparative `*spennilō/*spénnilō` while still treating `spinl` as the correct OE row target.

## Superseded or diagnostic material

Two older lines of DEV_NOTES reasoning should be preserved, but only as chronology. First, the original §17.45 recommendation preferred changing both `PROTOFORM` and `PROTO` to single-`n` `*spenilō` because that input already yielded `spinl` without further rule work [DEV_NOTES:line-40344-40460]. That solution is not the current row state and should not be cited as live metadata.

Second, the early Step 3 note is still worth preserving because it isolates the exact phonological gap that remained after `spindle → spinl` had already been fixed at the TSV level: retained-geminate input still surfaced as `spinlu` until trisyllabic apocope was broadened to cover heavy-by-position first syllables [DEV_NOTES:line-40488-40610]. Later work folded that diagnosis into the final §17.45.4 repair note, so the interim version is now diagnostic rather than authoritative [DEV_NOTES:line-42073-42188].

The very early placeholder "`The Case of spindle` ... `This needs separate investigation`" is no longer useful except as evidence that the problem had once been deferred without a row policy attached [DEV_NOTES:line-14535-14543]. Later writing should skip that placeholder and use the source-audit plus final-policy fragments instead.

## Open questions for later work

- Decide whether a later full report should foreground `spinel` or `spinl` in its opening lemma sentence. `spinl` is the current row target and is explicitly attested, but the report will likely need one sentence explaining its relation to dictionary citation `spinel` [DEV_NOTES:line-40297-40306; DEV_NOTES:line-42077-42080].
- Decide whether the final report should quote Kluge--Seebold's "`-d- ist ein Gleitlaut [zwischen -n- und -l-]`" directly in the main prose or reserve it for a note; it is the clearest compact explanation for why OE should not target `spindle` [DEV_NOTES:line-40315-40317; @KlugeSeebold2011, s.v. "Spindel"].
- If `index.tsv` is updated later, index the row at minimum to the current source-audit fragment `DEV_NOTES:line-40293-40326` and the current final-policy fragment `DEV_NOTES:line-42073-42188`; treat `DEV_NOTES:line-40344-40460` and `DEV_NOTES:line-40488-40610` as superseded/diagnostic rather than as standalone current authority.
