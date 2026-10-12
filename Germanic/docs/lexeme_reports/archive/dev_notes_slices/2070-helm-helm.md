---
row_id: 2070
concept: helm
counterpart: helm
proto: *xélmaz
protoform: *xélmaz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2070-helm-helm.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2070-helm-helm.md
linked_dossier_or_analysis_files:
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2070 helm / helm

## Current row state

- CONCEPT: `helm`
- COUNTERPART: `helm`
- PROTO: `*xélmaz`
- PROTOFORM: `*xélmaz`
- DERIVATION_CLASS: `regular`
- Live TSV note: `Kroonen *helma- m. 'helmet' → OE helm m.; helma is not nom.sg.` The row itself is still a straight `*xélmaz -> helm` row; the note is explanatory and warns against reading comparative `*helma-` as the OE target [Germanic/data/germanic-aligned-final.tsv:544-544].
- Packet state is clean and already matches the live row exactly: `PROTO: *xélmaz`, `EXPECTED: helm`, `OUTPUTS: helm`, with only final `-z` deletion, bare final `-a` loss, and OE orthographic `h*élm -> helm` shown in the compact trace [Germanic/docs/lexeme_reports/packets/2070-helm-helm.md:17-43].
- `oe_known_problems.tsv` has no entry for this row, and the packet also records `_None_` for matching `oe_known_problems.tsv` entries and `_No manifest entry._` for this row [Germanic/docs/lexeme_reports/packets/2070-helm-helm.md:11-13,45-47; Germanic/docs/lexeme_reports/research_memos/2070-helm-helm.md:27-30].
- Current memo assessment: row 2070 is a note-bearing **regular** row whose only real difficulty is representational. The memo explicitly separates Kroonen's comparative headword `*helma-`, the project's live derivational input `*xélmaz`, and the OE target `helm`, while also flagging OE `helma` as a different lexeme 'rudder/helm' rather than a competing paradigm cell of the helmet noun [Germanic/docs/lexeme_reports/research_memos/2070-helm-helm.md:17-23,32-37,44-68].
- Source-audit baseline from repo lexica is consistent with that memo. Kroonen distinguishes `*helma- m. 'helmet' ... OE helm m. 'id.'` from separate `*helman- m. 'rudder' ... OE helma m. 'id.'` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:12384-12395]. Clark Hall likewise separates `helm ... CP helmet` from `helma m. 'helm,' rudder` [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:21411-21416]. Bosworth-Toller gives `helm ... I. a covering for the head. (1) a helmet Helm galea` and separately uses `helma` in steering usage [docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:85393-85405,85353-85357].
- One repo-local lexical-table hit must stay quarantined as supplementary only: `old_english_wiktionary.tsv` maps English `helm` to OE `helma`, but the memo correctly treats that as ambiguous and likely aligned to the separate rudder lexeme rather than to the helmet row [Germanic/data/old_english_wiktionary.tsv:134-134; Germanic/docs/lexeme_reports/research_memos/2070-helm-helm.md:23-24,33-36].

## Development-note summary

No securely attachable **current row-specific DEV_NOTES authority** exists for row 2070. Both the packet and the memo record that `Germanic/docs/DEV_NOTES.md` has no relevant hit for this lexeme, so current authority has to come instead from the live TSV row, the packet's exact-match derivation, the memo's source audit, and the checked lexical references [Germanic/docs/lexeme_reports/packets/2070-helm-helm.md:49-51; Germanic/docs/lexeme_reports/research_memos/2070-helm-helm.md:36-38].

That absence of DEV_NOTES material does **not** mean the row is uncertain. The live project treatment is straightforward and should be stated without dilution: `PROTO = *xélmaz`, `PROTOFORM = *xélmaz`, and the OE target is `helm` [Germanic/data/germanic-aligned-final.tsv:544-544; Germanic/docs/lexeme_reports/packets/2070-helm-helm.md:20-23]. The memo is right that three levels must stay distinct: Kroonen's `*helma-` is the cognate-set comparative headword, the project's active derivational input is nominative-style `*xélmaz`, and the OE target is the attested noun `helm` [Germanic/docs/lexeme_reports/research_memos/2070-helm-helm.md:44-50]. For this row, `*helma-` is comparator/background evidence only; it is not the row's `PROTOFORM`, and it is not an instruction to retarget the OE form.

The lexicographic evidence checked in the repo makes the lexical split explicit enough that a paradigm-cell explanation should be rejected. Kroonen does not merely list helmet material under `*helma-`; he also separately gives `*helman- m. 'rudder' ... OE helma m. 'id.'` [docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:12384-12395]. Clark Hall mirrors the same contrast by listing `helm ... helmet` and then `helma m. 'helm,' rudder` as distinct entries [docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:21411-21416]. Bosworth-Toller does the same, giving direct helmet evidence under `helm` (`Helm galea`) and steering/rudder material under `helma` [docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:85393-85405,85353-85357]. So the row's documentary problem is **lexeme disambiguation**, not uncertainty about nominative singular versus some other OE paradigm cell.

The safest row-specific statement is therefore narrow and explicit. Row 2070 is a regular OE derivation to attested `helm`; `*helma-` is useful comparative background because it explains why Kroonen's dictionary notation differs from the project input, but it should not overwrite `PROTO`/`PROTOFORM` `*xélmaz`; and OE `helma` must be carried only as a separate rudder lexeme, comparator, or false-positive background item, not as the OE target of this row [Germanic/docs/lexeme_reports/research_memos/2070-helm-helm.md:52-70].

## Relevant DEV_NOTES fragments

No securely attachable **current** row-specific DEV_NOTES fragment survives. The required review found no row-local DEV_NOTES discussion of row 2070, `*xélmaz`, `helm`, or the helmet-versus-rudder contrast; the packet therefore records `_None_` under `DEV_NOTES hits`, and the memo repeats `DEV_NOTES.md — no relevant hit for this lexeme` [Germanic/docs/lexeme_reports/packets/2070-helm-helm.md:49-51; Germanic/docs/lexeme_reports/research_memos/2070-helm-helm.md:36-38].

Because there is no row-attached DEV_NOTES fragment, later work should not infer hidden DEV_NOTES authority from the existence of the TSV note or from stray lexical-table matches. For this row, packet + memo + lexical source audit are the operative evidence bundle, and any historical `helma` material has to be labeled diagnostic/background explicitly rather than smuggled in as DEV_NOTES authority.

## Superseded or diagnostic material

- `Germanic/data/old_english_wiktionary.tsv` line `helm	helma	inh	template:inh	helm` is **misleading if uncontextualized** for row 2070. It is a real repo datum, but current checked lexica show `helma` as the separate rudder lexeme, not as the nominative singular of the helmet noun; use it only as comparator/background or source-audit evidence about gloss collision [Germanic/data/old_english_wiktionary.tsv:134-134; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:21411-21416; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:12393-12395].
- `Germanic/docs/germanic_transducer_report.md` preserves stale debugging history with the dataset-sweep entry ``*xelmăz → helma``. That line is worth preserving only as checked project chronology showing earlier conflation of the helmet row with the rudder lexeme; it is not current row authority and should never be cited as if it overruled the live TSV or packet trace [Germanic/docs/germanic_transducer_report.md:54-56; Germanic/docs/lexeme_reports/research_memos/2070-helm-helm.md:35-37,64-64].
- The absence of any `oe_known_problems.tsv` entry is itself a useful diagnostic fact. It confirms that row 2070 is not currently treated as a live FST exception bucket; the remaining issue is documentary separation of `helm` versus `helma`, not unresolved derivational failure [Germanic/docs/lexeme_reports/packets/2070-helm-helm.md:45-47; Germanic/docs/lexeme_reports/research_memos/2070-helm-helm.md:29-30,60-68].

## Open questions for later work

- If the TSV note is revised elsewhere later, make the comparator status fully explicit: Kroonen's `*helma-` is comparative headword notation for the helmet cognate set, while OE `helma` in repo lexica belongs to the separate rudder lexeme [Germanic/data/germanic-aligned-final.tsv:544-544; docs/references/kroonen_etymological_dictionary_pgmc.vision.txt:12384-12395].
- If broader source cleanup is undertaken, review whether the `old_english_wiktionary.tsv` mapping `helm -> helma` should be annotated or disambiguated so future packet generation does not re-import it as apparent direct support for the helmet row [Germanic/data/old_english_wiktionary.tsv:134-134; Germanic/docs/lexeme_reports/research_memos/2070-helm-helm.md:23-24,35-36].
- If a later family-level note discusses stale project history, keep the label explicit: `*xelmăz -> helma` is checked debugging chronology only, whereas the live row remains regular `*xélmaz -> helm` [Germanic/docs/germanic_transducer_report.md:54-56; Germanic/docs/lexeme_reports/packets/2070-helm-helm.md:20-23].
