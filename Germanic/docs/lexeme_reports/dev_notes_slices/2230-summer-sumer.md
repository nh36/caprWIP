---
row_id: 2230
concept: summer
counterpart: sumer
proto: *súmaraz
protoform: *súmaraz
derivation_class: regular
source_file: Germanic/docs/DEV_NOTES.md
linked_packet_file: Germanic/docs/lexeme_reports/packets/2230-summer-sumer.md
linked_research_memo_file: Germanic/docs/lexeme_reports/research_memos/2230-summer-sumer.md
linked_dossier_or_analysis_files:
  - Germanic/docs/analysis/unstressed_e_o_before_r.md
  - Germanic/docs/analysis/arestoration_r_l_research.md
current_status: current
needs_literature_agent: no
---

# DEV_NOTES material — 2230 summer / sumer

## Current row state

- `Germanic/data/germanic-aligned-final.tsv` line 1164 currently gives row `2230` as `CONCEPT summer`, `COUNTERPART sumer`, `PROTO *súmaraz`, `PROTOFORM *súmaraz`, `DERIVATION_CLASS regular`, with the live note: `proto corrected *sumerăz→*sumarăz ... Both sumer and sumor attested ... sumer is the regular reflex via a-fronting ... sumor has unexplained -o-` [Germanic/data/germanic-aligned-final.tsv:1164-1164].
- `PROTO` and `PROTOFORM` are identical in the live row, and this row gives no evidence for splitting them apart. The lexeme-level comparative headword and the row-level derivational input are both `*súmaraz`; the distinct element is the OE `COUNTERPART`, which the project now fixes as `sumer`, not `sumor` [Germanic/data/germanic-aligned-final.tsv:1164-1164].
- No entry for this row appears in `Germanic/data/oe_known_problems.tsv`, so the row is not being tracked as an unresolved OE exception list item [Germanic/data/oe_known_problems.tsv:1-9].
- A packet and research memo already exist under the stem `2230-summer-sumer`, so this slice reuses that filename stem rather than inventing a new row-local name [Germanic/docs/lexeme_reports/research_memo_index.tsv:104-104].

## Detailed development-note summary

The durable row policy is now straightforward even though DEV_NOTES barely preserves it. Row `2230` is a true lexeme-level `regular` row: `*súmaraz` is both the comparative `PROTO` and the row's `PROTOFORM`, and the OE target remains `sumer` because the current derivational path already yields that form without any paradigm-cell workaround [Germanic/data/germanic-aligned-final.tsv:1164-1164; Germanic/docs/lexeme_reports/packets/2230-summer-sumer.md:17-18,19-42]. The linked A-restoration research explicitly treats this row as unaffected by the `a`-restoration problem because “first vowel is `*u`, not `*a`,” so the row's open issue is not computational breakage but how to describe the competing OE spellings accurately [Germanic/docs/analysis/arestoration_r_l_research.md:719-719].

The philological contrast that needs to stay explicit is **regular/project-selected `sumer` versus common citation/headword `sumor`**, not “attested versus unattested.” Kroonen's entry preserves both forms directly: `OE sumer, sumor m. 'id.'` [@Kroonen2013, p. 220]. Bright likewise keeps both in one lemma, `sumor (sumer), m.`, and gives genitive `sumeres` [@BrightCassidyRingler1971]. Clark Hall is even more useful for the paradigm shape: `sumor m., gs. sumeres, ds. sumera, sumere` [@ClarkHall1960]. Those dictionary forms are why the row should not be glossed as though `sumor` were a mere project error. The safe claim is narrower and stronger: `sumor` is a real and often default citation form, while `sumer` is also attested and is supported by oblique forms with `-e-` in the second syllable.

The reason the row nevertheless keeps `COUNTERPART = sumer` is the sound-change argument already summarized in the live TSV note and in the linked unstressed-vowel analysis. That analysis treats corrected PGmc `*sumarăz` / `*sumaraz` as yielding `sumer` by the regular fronting-and-merger path: `*a -> *æ -> e`, while noting that the pipeline never generates medial `-o-` for this item [Germanic/docs/analysis/unstressed_e_o_before_r.md:39-41,143-154]. Ringe and Taylor's treatment of unstressed vowels supports that direction: `*hwabar > OE hweþer` and `*watar > OE wæter`, and later “the first of two unstressed back vowels shows a tendency to be written e” [@RingeTaylor2014, §§5.1.2, 6.9.6]. That makes `sumer` the better regularized row target. By contrast, the row note leaves `sumor` as an attested but not yet regularly derived competitor, with unexplained `-o-` [Germanic/data/germanic-aligned-final.tsv:1164-1164; @RingeTaylor2014, §3.1.5].

Campbell's `sumor` evidence matters, but only for the first syllable. He cites `sumor summer` among OE words showing retention of `u` before single `m` [@Campbell1959, §§117-118]. That supports the root vocalism of the lexeme and helps explain why the row is not an A-restoration case. It does **not** settle the medial `-e-` versus `-o-` question in the unstressed syllable. For this row, Campbell is therefore secondary support for `su-`, not an argument to replace `sumer` with `sumor`.

Because DEV_NOTES itself preserves only a stale diagnostic line for this lexeme, the slice has to function as the replacement working note. The non-negotiable distinctions for later report writing are therefore: comparative `PROTO *súmaraz`; row-level `PROTOFORM *súmaraz`; OE target `sumer`; attested rival/headword `sumor`; oblique support `sumeres/sumere`; and stale project history `*sumerăz`, which survives in DEV_NOTES only as an obsolete ProtoInput-failure string, not as current row analysis [Germanic/docs/DEV_NOTES.md:2425-2425; Germanic/docs/analysis/unstressed_e_o_before_r.md:143-154].

## Relevant DEV_NOTES fragments

### DEV_NOTES:line-2425-2425

- Source heading: `PGmc→OE TODOs (consolidated)`
- Source line or section hint: `line 2425`
- Fragment type: `superseded_or_diagnostic_for_lexeme`
- Status: `diagnostic_only`
- Issue tags: `stale_proto_string`; `proto_input_history`; `not_row_analysis`
- Recommended next use: `use_as_project_history_only`
- Shared with row IDs:

This is the only live DEV_NOTES hit that attaches directly to row `2230`, and it is useful mainly because it is **stale**. The line still lists `*sumerăz` among ProtoInput failures: `remaining ProtoInput failures are elsewhere (e.g. ... *sumerăz)` [Germanic/docs/DEV_NOTES.md:2425-2425]. That wording predates the row's later proto correction to `*súmaraz` / `*sumarăz` and carries none of the actual row policy about `sumer` versus `sumor`. Keep it only as project chronology showing that DEV_NOTES cleanup lagged behind the row fix; do not use it as evidence for the row's current proto, counterpart, or derivation class.

## Superseded or diagnostic material

- The main superseded item is the older project proto spelling `*sumerăz`. It still appears in DEV_NOTES line `2425` and in the older action-item wording of `analysis/unstressed_e_o_before_r.md`, but the live row has already replaced it with `*súmaraz` and treats the old spelling as historical project state rather than current reconstruction [Germanic/docs/DEV_NOTES.md:2425-2425; Germanic/docs/analysis/unstressed_e_o_before_r.md:143-145; Germanic/data/germanic-aligned-final.tsv:1164-1164].
- The linked unstressed-vowel analysis remains useful background, but parts of it are diagnostic history rather than live row state. Its recommendation header still says `*sumerăz/sumor -> fix proto AND target`; that is now only a record of what had to be changed, because the present TSV row already has corrected proto and corrected target [Germanic/docs/analysis/unstressed_e_o_before_r.md:143-154].
- Local lexical-table evidence for `sumor` should also be handled diagnostically. It confirms that `sumor` is a common dictionary/headword form, but it does not by itself outweigh the attested `sumer` and oblique `sumeres` material that underwrites the row's present `COUNTERPART` choice [Germanic/docs/lexeme_reports/packets/2230-summer-sumer.md:104-110; @Kroonen2013, p. 220; @ClarkHall1960].

## Open questions for later work

- If a final lexeme report is drafted, decide whether to quote the dictionary evidence directly (`sumor (sumer)`, `sumeres`, `sumere`) or compress it to one sentence. The oblique forms are probably the strongest concise support for keeping `sumer` as the row target.
- If `DEV_NOTES.md` is ever cleaned up, either delete row `2230` from the obsolete ProtoInput-failure list or update the stale `*sumerăz` spelling so future slicing does not mistake it for live row evidence.
- If later indexing is reconsidered, decide whether a purely diagnostic DEV_NOTES attachment is worth indexing at all. At present the row's real working note lives here and in the linked packet/memo, not in substantive DEV_NOTES prose.
