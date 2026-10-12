---
row_id: 2104
concept: linden
counterpart: lind
proto: *líndō
protoform: *líndō
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2104-linden-lind.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2104-linden-lind.md
linked_dossier_or_analysis_files:
  - Germanic/docs/germanic_transducer_report.md
  - Germanic/docs/non_firing_rules_analysis.md
  - Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2104 linden / lind

## Current row state

- CONCEPT: `linden`
- COUNTERPART: `lind`
- PROTO: `*líndō`
- PROTOFORM: `*líndō`
- DERIVATION_CLASS: `regular`
- Live TSV note: `Kroonen *lindō- f. 'linden/lime tree' → OE lind f.; linden is not standard OE form` [Germanic/data/germanic-aligned-final.tsv:674].
- Packet state is internally regular and already matches the live row exactly: `PROTO: *líndō`, `EXPECTED: lind`, `OUTPUTS: lind`, with the compact trace `Proto Input: *líndō` > NWGmc final long-`ō` raising `*líndu` > OE high-vowel apocope `*línd` > surface `lind` [Germanic/docs/lexeme_reports/packets/2104-linden-lind.md:17-41].
- `oe_known_problems.tsv`: no row-specific entry is attached. The packet records `_None_`, and the memo independently says there is no row-specific problem entry for `*líndō`, `lind`, or `linden` [Germanic/docs/lexeme_reports/packets/2104-linden-lind.md:44-46; Germanic/docs/lexeme_reports/research_memos/2104-linden-lind.md:24-27].
- `report_manifest.tsv`: no manifest entry is present for this row [Germanic/docs/lexeme_reports/packets/2104-linden-lind.md:11-13].
- Current lexical-source baseline in repo references supports OE noun `lind`, not noun `linden`. Kroonen gives `*lindō- f. 'lime tree' ... OE lind f. 'id.'`; Clark Hall gives `lind I. f. lime-tree, linden` and separately `linden made of 'linden'-wood`; Bosworth-Toller keeps the headword under `lind`, e.g. `lind. Add: I. :-Lindan tilię ...` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:17999-18000; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:26285-26289; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:99594-99596].
- One repo-local lexical-table hit must stay quarantined as supplementary only: `old_english_wiktionary.tsv` has `linden	linden	inh	template:inh	linden`, but the memo explicitly treats that table as inadequate for choosing the OE target here because it does not distinguish noun `lind` from other uses of `linden` [Germanic/data/old_english_wiktionary.tsv:166; Germanic/docs/lexeme_reports/research_memos/2104-linden-lind.md:18-20, 29-32, 52-55].
- Current DEV_NOTES authority status: no securely attachable **current row-specific DEV_NOTES fragment** survives for row 2104. The packet records `_None_` for DEV_NOTES hits, and the memo separately states `Germanic/docs/DEV_NOTES.md — no relevant row-specific discussion found` [Germanic/docs/lexeme_reports/packets/2104-linden-lind.md:48-60; Germanic/docs/lexeme_reports/research_memos/2104-linden-lind.md:33-35].

## Development-note summary

No securely attachable **current row-specific DEV_NOTES authority** exists for row 2104. That absence should be stated directly, not papered over. The operative current evidence bundle is the live TSV row, the packet's compact regular derivation, the research memo's source audit, and the repo's dictionary references; `Germanic/docs/DEV_NOTES.md` does not currently carry a row-local problem note, repair note, or precedent fragment for `*líndō`, `lind`, or `linden` [Germanic/docs/lexeme_reports/packets/2104-linden-lind.md:44-60; Germanic/docs/lexeme_reports/research_memos/2104-linden-lind.md:24-35].

The live row itself is straightforward and should remain stated in that straightforward way. `PROTO` and `PROTOFORM` are both the project input `*líndō`, and the OE target is `lind`; the packet's derivation trace is regular and needs no paradigm-cell substitution, special analogical rescue, or exception label [Germanic/data/germanic-aligned-final.tsv:674; Germanic/docs/lexeme_reports/packets/2104-linden-lind.md:17-41]. The memo is explicit that the problem here is editorial headword control rather than phonological failure: stale material can make the row look like an OE final-`-n` problem, but the current generator and packet already give `lind`, not `linden` [Germanic/docs/lexeme_reports/research_memos/2104-linden-lind.md:15-20, 34-37, 58-63].

Three levels must stay distinct in any later reuse of this row. Kroonen's `*lindō-` is the comparative cognate-set headword written in stem notation; the project's live derivational input is `*líndō`; and the OE target is the attested noun `lind` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:17999-18000; Germanic/docs/lexeme_reports/research_memos/2104-linden-lind.md:40-49]. This row therefore does **not** involve a PROTO-versus-PROTOFORM split: unlike paradigm-cell rows, the live project input and row-level protoform are the same. The only form that must be explicitly rejected as current OE target is noun `linden`.

The lexical audit is strong enough that later prose should be explicit about why `linden` is non-authoritative. Kroonen directly lists OE `lind` under the comparative set [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:17999-18000]. Clark Hall makes the crucial disambiguation locally: `lind I. f. lime-tree, linden` is the noun entry, while `linden` is separately glossed `made of 'linden'-wood`, i.e. an adjective rather than the noun targeted by row 2104 [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:26285-26289]. Bosworth-Toller also preserves the lexical tradition under `lind`, not under `linden` [docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:99594-99596]. The packet's `old_english_wiktionary.tsv` hit `linden -> linden` is therefore background/source-audit material only and should never be allowed to outweigh the checked dictionary evidence [Germanic/data/old_english_wiktionary.tsv:166; Germanic/docs/lexeme_reports/research_memos/2104-linden-lind.md:29-32, 52-55].

The stale repo history also needs explicit labeling because it shows how the row was previously misread. Earlier diagnostic sweeps in `Germanic/docs/germanic_transducer_report.md`, `Germanic/docs/non_firing_rules_analysis.md`, and `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md` still expected `linden` and treated missing final `-n` as the issue [Germanic/docs/germanic_transducer_report.md:26-32; Germanic/docs/non_firing_rules_analysis.md:373-378; Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:306-310]. The memo correctly classifies that material as stale project history rather than live lexical authority [Germanic/docs/lexeme_reports/research_memos/2104-linden-lind.md:17-20, 29-33]. For row 2104, those files are diagnostic evidence of earlier expectation drift, not justification for changing the current row.

## Relevant DEV_NOTES fragments

No securely attachable **current** row-specific DEV_NOTES fragment survives for row 2104. The packet records `_None_` under high-confidence and supporting/background DEV_NOTES hits, and the memo independently confirms that `Germanic/docs/DEV_NOTES.md` contains no relevant row-specific discussion for this lexeme [Germanic/docs/lexeme_reports/packets/2104-linden-lind.md:48-60; Germanic/docs/lexeme_reports/research_memos/2104-linden-lind.md:33-35]. Current row authority therefore comes from TSV + packet + memo + lexical source audit, not from any hidden DEV_NOTES passage.

## Superseded or diagnostic material

- `Germanic/data/old_english_wiktionary.tsv` line `linden	linden	inh	template:inh	linden` is **misleading if uncontextualized** for row 2104. It is a real repo datum, but it does not distinguish the OE noun target from an adjectival or otherwise non-row-relevant `linden` use, and it conflicts with the checked dictionary evidence favoring noun `lind` [Germanic/data/old_english_wiktionary.tsv:166; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:26285-26289; Germanic/docs/lexeme_reports/research_memos/2104-linden-lind.md:18-20, 29-32, 52-55].
- `Germanic/docs/germanic_transducer_report.md` preserves stale debugging chronology, not current row policy. Its dataset sweep still lists ``*lindō → linden`` among OE outputs, reflecting earlier project assumptions rather than the current regular row `*líndō -> lind` [Germanic/docs/germanic_transducer_report.md:26-32; Germanic/docs/lexeme_reports/research_memos/2104-linden-lind.md:17-20, 29-33].
- `Germanic/docs/non_firing_rules_analysis.md` is likewise diagnostic only here. The mismatch table says ``*lindō -> lindō (expected linden) # Final -n missing``, which preserves the same outdated expectation drift toward `linden` rather than current lexical authority for OE `lind` [Germanic/docs/non_firing_rules_analysis.md:373-378; Germanic/docs/lexeme_reports/research_memos/2104-linden-lind.md:17-20].
- `Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md` should also remain superseded for this row. Its `Proto *-ō cases` table still gives ``*lindō → lindō (exp. linden)``, which is useful only as project archaeology showing the former expectation that final apocope should yield `linden` [Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:306-310; Germanic/docs/lexeme_reports/research_memos/2104-linden-lind.md:17-20].
- The absence of any row-specific `oe_known_problems.tsv` entry, manifest row, or DEV_NOTES fragment is itself a current-state fact worth preserving. Row 2104 is not presently managed as an open OE exception; the remaining issue is source hygiene around noun `lind` versus misleading packet-era `linden` evidence [Germanic/docs/lexeme_reports/packets/2104-linden-lind.md:11-13, 44-60; Germanic/docs/lexeme_reports/research_memos/2104-linden-lind.md:24-35, 58-66].

## Open questions for later work

- If a final lexeme report is drafted later, quote the lexical distinction explicitly so `PROTO` `*líndō`, comparative headword `*lindō-`, and OE noun target `lind` cannot be collapsed into packet-era `linden` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:17999-18000; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:26285-26289].
- Review whether `Germanic/data/old_english_wiktionary.tsv` should eventually be annotated or corrected for this concept, since its current `linden -> linden` line is the most reusable false positive in the packet bundle [Germanic/data/old_english_wiktionary.tsv:166; Germanic/docs/lexeme_reports/research_memos/2104-linden-lind.md:52-55].
- If stale diagnostic files are ever cleaned up, mark their `expected linden` language explicitly superseded so later row work cannot mistake project archaeology for current lexical authority [Germanic/docs/germanic_transducer_report.md:26-32; Germanic/docs/non_firing_rules_analysis.md:373-378; Germanic/docs/germanic_notes/final_vowel_apocope_investigation.md:306-310].
