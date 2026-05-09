---
row_id: 2211
concept: spur
counterpart: spora
proto: *spúrô
protoform: *spúrô
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file:
linked_research_memo_file:
linked_dossier_or_analysis_files:
  - Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2211 spur / spora

## Current row state

- The live OE row currently reads `2211 | spur | COUNTERPART spora | PROTO *spúrô | PROTOFORM *spúrô | DERIVATION_CLASS regular` [Germanic/data/germanic-aligned-final.tsv:1090-1090].
- The row is one of the cases where `PROTO` and `PROTOFORM` happen to coincide, but the distinction still matters: `PROTO` is the comparative etymological headword, `PROTOFORM` is the row's actual FST input, and `COUNTERPART` is the selected OE target `spora` [Germanic/data/germanic-aligned-final.tsv:1090-1090].
- No existing packet or research-memo stem for row `2211` was found under `Germanic/docs/lexeme_reports/`, so this slice uses the canonical row-based filename and functions as the replacement working note.
- No row-specific `oe_known_problems.tsv` entry is currently attached for `*spúrô`; the file's live contents list other problem rows only, not this one [Germanic/data/oe_known_problems.tsv:1-8].
- The current published derivation trace matches the row without any exception handling: `Proto Input: *spúrô` > `NWGmc U Lowering: *spórô` > `OE Unstressed Long Vowel Shortening: *spóra` > `Outcome: spora` [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4607-4625].
- Repo source material already shows that the OE lexeme circulated in more than one vocalic shape. Orel gives `*spurōn sb.m. ... OE spora id.` [@Orel2003, p. 544; docs/references/orel_handbook_germanic_etymology.vision.txt:40898-40899]; Bosworth-Toller has an entry under `spora` [@BosworthToller1898, s.v. "spora"; docs/references/bosworth_toller_anglo_saxon_dictionary.vision.txt:114770-114773]; Clark Hall's concise dictionary excerpt instead lists `spura m. spur` [@ClarkHall1960, s.v. "spura"; docs/references/clark_hall_concise_anglo_saxon_dictionary.vision.txt:37627-37627].

## Detailed development-note summary

The surviving DEV_NOTES support for row `2211` is thin, shared, and still usable. Nothing in the file suggests that `spora` is a current OE exception requiring a special `PROTOFORM`, an analogy-driven workaround, or a derivation-class change. The live trace instead shows a fully regular path from `*spúrô` to `spora`: root `*u` lowers before the following non-high vowel, and the final long vowel is then shortened in OE [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4607-4625]. That is why the live row remains `regular` and why the replacement working note should not import the mismatch-management language used elsewhere for `wulf`, `full`, `fugol`, or `bucc`.

What DEV_NOTES *does* preserve is evidence that OE had both an `o`-grade and a `u`-grade for this lexeme. The early Luick note lists `spura/spora` among the attested OE doublets, and the later Campbell quotation repeats the same point almost verbatim: “Even within OE itself, there is variation in some words, e.g. ... `spora` spur ... beside ... `spura`” [Germanic/docs/DEV_NOTES.md:122-128,25976-25985; @Luick1914, §78; @Campbell1959, §115]. For row `2211`, that means the current `COUNTERPART = spora` should be read as the dataset's selected member of an attested OE alternation, not as a claim that OE only had `spora` and never `spura`.

Brunner's wording in the source tradition preserved in the repo sharpens the same point and is worth carrying forward because it aligns closely with the DEV_NOTES reading: `spura (neben spora) Sporn`, with the lexeme also indexed as `spura, spora` [@SieversBrunner1965, §58; docs/references/brunner_1965_altenglische_grammatik.vision.txt:2572-2575,28093-28093]. Taken together with Orel's `OE spora` and Clark Hall's `spura`, the safest row-level conclusion is conservative. The lexeme is secure, the current row target `spora` is defensible, but the repo's philological support remains variant-rich rather than normalized. Later report prose should therefore preserve the doublet explicitly instead of silently treating `spora` as the only OE form.

The practical project decision is narrow. Keep `PROTO = *spúrô`, keep `PROTOFORM = *spúrô`, keep `COUNTERPART = spora`, and keep the row `regular`. The useful DEV_NOTES contribution is historical-lexical context about OE `spora/spura` variation, not a row-specific repair history. Because no packet, memo, or row-local DEV_NOTES dossier currently exists, this slice is adequate as a working note but still weaker than the slices built from fuller report infrastructure.

## Relevant DEV_NOTES fragments with line-based refs

### DEV_NOTES:line-122-128

- Source heading: `Luick's doublets evidence`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `background`
- Issue tags: `u_o_alternation`; `doublet_evidence`; `luick`; `variant_history`
- Recommended next use: `keep_as_general_background`
- Shared with row IDs:

This is the earliest attachable DEV_NOTES fragment for row `2211`. It says that Luick provides “important evidence that OE itself had active u/o alternation” and includes the direct doublet `*spura/spora* 'spur'` beside `*spurnan/spornan*` and `*cnucian/cnocian*` [Germanic/docs/DEV_NOTES.md:122-128]. For this row the fragment is not a repair note and not a reason to rewrite the metadata. Its value is lexical-historical: it preserves the claim that both `spura` and `spora` belonged to the OE record, exactly the caution later report work will need [@Luick1914, §78].

### DEV_NOTES:line-25976-25985

- Source heading: `late source audit quoting Campbell on OE variation`
- Fragment type: `phenomenon_context_for_lexeme`
- Status: `background`
- Issue tags: `campbell`; `u_o_alternation`; `doublet_evidence`; `source_quote`
- Recommended next use: `use_with_caution_in_final_report`
- Shared with row IDs:

This later shared fragment is the clearest explicit wording now preserved in DEV_NOTES for the row's variant status. After restating the regular u-lowering rule and listing the classic `u`-retention exceptions, the note quotes Campbell: “Even within OE itself, there is variation in some words, e.g. `cnocian` knock, `spora` spur, `spornan` spurn, beside `cnucian`, `spura`, `spurnan`” [Germanic/docs/DEV_NOTES.md:25976-25985]. For row `2211`, the important point is the contrast: `spora` is the lowered form actually selected by the live row, while `spura` survives in the same note as the competing OE doublet [@Campbell1959, §115].

## Superseded or diagnostic material

- No row-specific superseded repair proposal currently survives for `2211`. The row does not have the kind of later rollback history seen in the `wulf`/`bucc` exception cluster.
- The main diagnostic trap is the surrounding DEV_NOTES prose on accepted `u`-retention mismatches. That prose governs lexemes such as `wulf`, `fugol`, and `bucca`, where the live OE target keeps `u` against the regular rule [Germanic/docs/DEV_NOTES.md:134-142]. Row `2211` is different: the current target is the regular lowered `o`-grade `spora`, and the trace already derives it cleanly [Germanic/docs/debug_snapshots/oe_derivation_class_trace_report.with_lexeme_reports.publish.md:4607-4625].
- The philological evidence in the repo is also mixed enough that it should be handled as a caution, not normalized away. Orel and Bosworth-Toller support `spora`, while Clark Hall's concise entry gives `spura`; Brunner and Campbell explicitly preserve both forms [@Orel2003, p. 544; @BosworthToller1898, s.v. "spora"; @ClarkHall1960, s.v. "spura"; @SieversBrunner1965, §58; @Campbell1959, §115]. That is a reason to document the doublet, not a reason to change the live row on the basis of a single dictionary citation.

## Open questions for later work

- If a final lexeme report is prepared, decide whether the opening lemma should present the OE evidence as `spora` with variant `spura`, or as a doublet `spora/spura` from the start; the surviving repo evidence supports both spellings, but does not yet rank them in a row-local dossier [@Orel2003, p. 544; @BosworthToller1898, s.v. "spora"; @ClarkHall1960, s.v. "spura"].
- If stronger philological support is wanted later, gather direct manuscript or glossary attestations for both spellings rather than relying only on handbook summary statements and dictionary headwords.
- If `index.tsv` is revisited later, the only obvious attachments are the two shared background fragments `DEV_NOTES:line-122-128` and `DEV_NOTES:line-25976-25985`; the current evidence base does not yet supply a richer row-specific fragment set.
