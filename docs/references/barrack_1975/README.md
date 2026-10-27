# Barrack1975 local holding

Charles Michael Barrack, *A Diachronic Phonology from Proto-Germanic to
Old English Stressing West-Saxon Conditions*, Janua Linguarum,
Series Practica 144 (The Hague and Paris: Mouton, 1975).
Title and copyright were checked on PDF sheets 3 and 4. A supplied
filename's reprint date is not the work's composition/publication year.
The bibliographic owner is `docs/refs.bib`, key `Barrack1975`.

## Complete ingestion

The supplied PDF and complete native searchable text are retained locally
at the paths in `holdings.tsv`. All 136 sheets are extracted, including
frontmatter, rule lists and references; the text has 136 form feeds.
Neither the copyrighted PDF nor its complete transcript is committed.
A public clone therefore needs a separately lawfully supplied holding.
The manifest records content identities, not private download locations.

Restore the PDF to the manifest's canonical path and verify its SHA256
before extracting:

```sh
shasum -a 256 docs/references/barrack_1975_diachronic_phonology.pdf
mkdir -p docs/references/local/barrack-1975
pdftotext -layout docs/references/barrack_1975_diachronic_phonology.pdf \
  docs/references/local/barrack-1975/complete.txt
shasum -a 256 docs/references/local/barrack-1975/complete.txt
```

The exact retained extraction hashes are in `holdings.tsv`.
Poppler may emit invalid-font-weight warnings; useful text is nevertheless
present throughout. A different extractor version may produce a different
text hash; do not silently certify it as the recorded extraction.
Phonetic matrices, accents and some consonantal signs need the original
image. Searchable text is not a corrected diplomatic transcription.

## Consultation and page map

`page_map.tsv` records checked navigation anchors, not a claim that every
page image was read. The title, copyright and printed p.53 were visually
checked; notation on pp.11, 13 and 15 and the related rule discussions on
pp.82–84 were consulted in extracted text.

Printed p.53 compares lord histories with different assumptions about
compounding and accent loss. It discusses *hlāfweard*, *hlāferd*,
*hlāford*, *hlāfurd* and *hlāfard*, linking w-loss and alternative vowel
developments to its numbered rules. The distinction between alternative
derivations matters: this is not evidence that every variant followed
one continuous chain. Its rejection of a necessary retraction intermediary
also prevents treating Campbell's analysis as unanimous.

This bounded consultation prepares the deferred lord dossier. It does not
admit lord, reopen world, adjudicate soul, or authorize Barrack's complete
theory as the production chronology. Complete ingestion is not complete
reading or source-method certification.
