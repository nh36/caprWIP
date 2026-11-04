# Local source-holdings reconciliation

Base: `c1cfd0a5b2c3dbdefa18da32d05bb229e02543c0`.
Filesystem observations: 4 November 2026. This is preservation housekeeping,
not new source adjudication or certification of the four-cell publication.

Subsequent same-day update: the [Desktop intake](../desktop_2026-11-04/README.md)
adds Seiler2019 and Fulk1998 from the user's supplied PDFs. They are no longer
acquisition gaps. The original population/copy counts below describe the initial
audit; current `inventory.json` also includes the two explicitly supplied
Desktop files and their new holdings. The original snapshot remains in commit
`cf77a36b`. Bennett1968, Stiles1995 and Hock1973 remain requested.

## Result and scope

Twenty-three previously stranded original PDF/DjVu files are now byte-preserved
in the durable main project's ignored reference library and this research
worktree. Twenty separate searchable extracts were added; no scan was replaced,
no existing edition overwritten, and no new OCR operation was performed.
Three verified November restoration bundles retain 46 original/extract members,
including the already-held Colman pair and Lloyd legacy OCR.

`inventory.json` reconciles all 149 bibliography records, 1,059 distinct
project-relative-path/hash assets and 14,858 physical file copies across
available worktree libraries. It finds associated assets for 135 bibliography
records. The remaining 14 are not automatically missing acquisitions: they
include online-only references, earlier editions distinct from held editions,
and bibliographical references without a located source file.

The searched external candidate set contains 100 files: 99 have exact-byte
project copies; one is CAPR's own manuscript, not an external scholarly source.
No scholarly original in that searched set remains stranded. This is not a
claim that every scholarly file anywhere on the computer has been identified.
The scope includes Downloads/Germanic, New CAPR resources, New to OCR,
New new to OCR, Books2/German stuff, prior worktrees' source-readings caches,
the specifically identified top-level Seiler volume, and the available
August CAPR archive. Other cache/session candidates were distinguished from
originals: three edition originals were incorporated; OCR sample derivatives
and CAPR's own Barrack handoff reports were not counted as new sources.

## What the records establish

`audit.py` regenerates the observed inventory:

```sh
python3 docs/references/holdings_audit_2026-11-04/audit.py \
  --main /Users/nathanhill/Code/capr \
  --output docs/references/holdings_audit_2026-11-04
```

Each registered source retains its bibliographical identity/key, located
source/text paths and SHA256s, extraction coverage/method records where known,
external acquisition locations when recoverable, verified restoration-bundle
members and links to research/source-access records. Assets also retain all
observed same-disk copy locations. Exact-byte duplicates are not new editions
or independent scholarly votes. Unregistered newly acquired works retain
their identities in `intake-decisions.json` and `preservation.json`; no
citation keys were invented.

The bibliography's file field is not an exhaustive library inventory.
Ignored originals and existing companion texts were checked separately.
Filename pairing locates companions; it does not certify edition identity
or transcription completeness. In particular, the 2002 Kluge electronic
conversion is not the held 2011 print edition, and the old 2002 text is not
silently paired with the 2011 PDF. OCR-derived PDFs, page chunks, partial
excerpts, native extracts and complete selected chapters are distinguished.
Full-file extraction is not a claim that image-only sheets were transcribed
or that all glyphs were corrected.

Reading status is deliberately claim-specific. New acquisitions record exactly
whether opening identity was checked, a previously documented reading reused,
or merely a file retained. Existing dossier links preserve direct/indirect
reading evidence; citation occurrence alone is not certified as direct
inspection. Where reading or transcription completeness cannot be established,
the inventory says so rather than inventing a whole-book reading certificate.
This remaining uncertainty is distinct from an absent holding.

## Named findings

Colman2011's original PDF and complete local text exist at the recorded
project-local paths, are regular files rather than symlinks, and match the
accepted closeout:

| File | SHA256 |
|---|---|
| `docs/references/colman_2011_moneyers_buga_boia.pdf` | `0af5841706ba5a00007acc5fa027b0faf4263b1287199430cb212a21326f3c9d` |
| `docs/references/local/colman-2011/complete.txt` | `36b5aecf61225a39c09299e3695bf0c02b8389b7e8e195e277b4352e1f0e0e7c` |

Neither file depends on Downloads. Both also have verified restoration-bundle
members. Their original bibliography metadata is unchanged.

Lloyd and Springer's volume I scan was genuinely stranded; the searchable
335-sheet legacy OCR was already held. The original scan is now
`docs/references/ewa_band1_lloyd_springer.pdf`. Its title/copyright images
identify 1988, agreeing with `LloydSpringer1988`, not the old resource note's
1998. The separately preserved DjVu is not assumed to be an equivalent edition.
Title, contents/preface and the OCR's final *bezzisto* endpoint were checked;
this is not a global diplomatic correction of the OCR.

The nineteen initial original files include Lloyd PDF/DjVu, Ciszek-Kiliszewska,
Mateo Mendaza, the Hogg Cambridge History volume, deMello's Celtic dissertation,
Martín Arista, Pilch, McFadden, the Beiträge 15 container, McCully/Hogg, Beeler,
Krahe, Bammesberger's Laryngaltheorie, Kluge's 24th-edition conversion, Vine,
Polome1967 and alternate Versloot/Polome1994 PDFs.
Their exact identities, origins, qualifications and hashes are in
`intake-decisions.json` and `preservation.json`.

`research-supplement.json` records the three original editions recovered from
prior research caches: Skeat1874 Luke, Strunk1904 Juliana and a
Wright-Wuelcker1884 volume I variant. `seiler-supplement.json` records the
complete open-access edited volume containing Seiler2017 and its separately
extracted complete chapter, sheets 162-183. This is not Seiler2019.

At the initial audit Bennett1968, Stiles1995, Fulk1998, Hock1973 and Seiler2019
were not located in the then-searched roots. The subsequent Desktop intake
resolves Fulk1998 and Seiler2019; the other three remain unacquired.
The inventory names the remaining access dossiers. Bennett1950, other Stiles
papers, Fulk2018/2010, Hogg1979 and Seiler2017 are not substitutes.
The acquisition update does not retrospectively certify scientific arguments
or the original audit's direct-reading status.

## Preservation limits

The pre-existing ga-prefix restoration bundle has 58 verified matching members.
The three November bundles have 38, six and two respectively; their hashes and
member checks are recorded in the inventory/supplements. These are local
restoration copies, not independent off-machine backups. Another worktree on
the same disk is not disaster recovery.

There are still 122 distinct PDF assets without a verified member in these
restoration bundles; some have same-disk worktree copies. No independent
off-machine backup was verified for the library. Text-only and partial holdings
also remain explicitly visible, rather than being represented as original PDFs.
The August archive exists and contains four Git bundles, but that does not
establish preservation of ignored originals.

Only metadata, acquisition notes and the inventory generator are committed.
Copyrighted PDFs, restricted complete extracts, source-page images and private
restoration bundles remain ignored project-local holdings.
