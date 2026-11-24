# Hay article: final source-preparation memorandum

## Cooper (2003) and S 1196

Cooper knew of S 1196 and deliberately excluded it from his chronology of
highway terminology because he suspected the document was corrupt (2003:
61 nn. 151, 155). He notes the anomalous dating, the change from Latin to
Old English, the apparent *cyniges heiweg* / *cyninges strete*
correspondence, and the unusual *communis via*. These are documentary
difficulties independent of whether *heiweg* means ‘highway’. The argument
that it would make highway terminology substantially earlier depends on
that lexical identification and cannot independently establish it.

Cooper's footnote 151 gives a bounded fourteen-charter corpus. The relevant spellings, contexts, surviving
witnesses, manuscript dates, transaction dates, and Cooper's edition
references, as represented in the Sawyer Old Texts, are transcribed in
`COOPER_CHARTER_CORPUS.tsv`. The records include S 1338
*heahstræt*, S 1361 *hæhstræte*, and S 911 *hehstræte*. They are different
compounds and do not by themselves establish that ⟨hei-⟩ in S 1196 reflects
*hēah*. No single etymology is assumed for the compounds Cooper groups.
The texts also have *higi wegge* (S 508) and *heige weye* (S 727), but
the first is lexically unresolved and the latter is preserved in a late
fourteenth-century copy; neither independently establishes a ninth-century
Kentish reflex of *hēah*. No inspected item supplies a securely
contemporary ⟨i⟩ spelling whose derivation from *hēah* is independently
demonstrated. The table transcribes the electronic texts, not a
manuscript-wide collation. The article now distinguishes the lexical
identification of S 1196 from Cooper's independent concerns about the
document and corrects the account that he overlooked it.

## Ritt (2000) and accent interpretation

The scanned ILL copy is registered in the shared catalogue and project
manifest. The private source and searchable OCR are under
`docs/references/local/hay-article-literature-2026-11-24/`; only article
sheets 3–18 were OCRed, with the administrative delivery sheets excluded.
Pages 498–501 and 505–510, including the original p. 508 table and p. 509
sample, were checked against the images. The restricted source and OCR
remain Git-ignored.

Ritt challenges Jones's interpretation of Aldred's accentuation. His
alternative is that accents preferentially mark long vowels where length
is not predictable from spelling. The observed Matthew distribution is
426 accents: 318 in graphically closed syllables and 108 in graphically
open syllables. His p. 508 table accounts for 328/376 non-ambiguous
occurrences (87.3%), leaving 48 exceptions. This is Ritt's explanatory
analysis, not a direct observation that accents uniformly encode length.
On p. 509, the reported 100-item CVC sample is internally inconsistent:
79 short and 21 long items leave six items after 15 long items, but the
prose says eight. The stated 98% predictive accuracy is therefore not
reproduced. Ritt's account is relevant to the interpretation of Aldred,
not evidence of Farman's own practice.

## Farman (Ru1) calibration

The corrected accented census remains 197 types and 301 Old English
tokens: 196 non-target types/299 tokens plus *hóeg* (one type/two tokens).
The matched calibration includes unaccented tokens and separates token,
surface-type, raw-spelling, and lexical-type counts:

| Class | Accented tokens | Accented surface types | Lexical types with accent | Structure/context |
|---|---:|---:|---:|---|
| Short V + glide (*weg*, *dæg*) | 1/53 | 1/9 | 1/2 | Closed monosyllables 1/26; following vowel graph 0/27; ten exact spellings including *weig* at Mk 1:3, fol. 52v |
| Long V + glide (*stīg*) | 1/2 | 1/2 | 1/1 | Both tokens have a following vowel graph; only one lexical type |
| Short V + homorganic cluster | 5/133 | 5/23 | 4/5 | Closed monosyllables 3/52; following vowel graph 1/51; multisyllabic 1/30 |

The accented *stígas* is on fol. 4v at Mt 3:3; Latin *semitas eius*
supports accusative plural. The unaccented *stige* on fol. 52v is an
alternative gloss beside *gongas* and is not securely classified for
case or number. Thus the sole long-vowel-plus-glide lexeme has no
closed-monosyllable token and cannot support a likelihood ratio.
Potential homorganic-cluster lengthening remains a separate class:
counting it as short gives 6/186 accented tokens, 6/32 surface types,
and 5/7 lexical types; counting it as lengthened gives 6/135 tokens,
6/25 surface types, and 5/6 lexical types. Eight uncertain
*gang*-family tokens and one *dægne* are listed separately and excluded.
The matched panel is a bounded descriptive sample, not a corpus-wide
rate; repeated tokens are not independent. The acutes suggest something
about Farman's late tenth-century practice, without establishing
ninth-century quantity or deciding between the historical derivations.

The data and regeneration script are `FARMAN_ACCENT_CALIBRATION.tsv` and
`calibrate_farman_accents.py`; exact source spellings, grammatical-form
notes, structures, folios, and extraction lines are retained. The script
includes the accented variants, the plural day forms, and only the
long-vowel noun *stīg*; verbal *stigað/stigende* homographs are recorded
separately. The Tamoto contexts checked for *stīg* are retained in the
generated rows.

## West Saxon ⟨ie⟩ and the attestations of ‘hay’

The only direct edition readings ⟨hieg⟩ found in this audit are Eadwine
Psalter PPs 71.16 and 146.8, Harsley 1889: 72, 241. The witness is Trinity
College Cambridge MS R.17.1, dated c. 1150. Its manuscript folios were
not independently collated, and the dialect of these glosses has not
been established. These readings are distinct from normalized *hīeġ*
and from reconstructed or illustrative forms. The inspected West Saxon
traditions attest *hig/hyg* (including Lambeth and CCCC 140); later
gospel copies have *heig/haig*. The concordance and DOE crosswalk now
record the Eadwine readings with their source, date qualification, and
verification limits.

Hogg (2006: 399–406) distinguishes Alfredian and Ælfrician West Saxon
clusters, notes the substantial linguistic differences between the
Vespasian Psalter and Rushworth¹ (402–404), and questions the
geographical significance of differences between Aldred and Owun
(405–406). At p. 400 he lists three possible sources of West Saxon ⟨ie⟩:
palatalization of earlier /eː/, i-umlaut of earlier diphthongs, and
hiatus resolution involving /i/ and /e/. Hogg–Fulk 2011 §§5.49, 5.53
condition the first on a preceding palatal consonant; §§5.82–84 discuss
the second; §§5.146–147 discuss the third, with examples including *sċe*
and *hie* but an explicitly uncertain analysis. Campbell 1959 §234
documents West Saxon /i+e/ contraction and disyllabic forms in other
dialects. These developments are real, but their existence does not
establish their applicability to ‘hay’. A possible ⟨ie⟩ spelling alone
cannot identify the relevant historical source or establish the
compound-independent stem history.

The article and `QUANTITY_EVIDENCE.md` now present that evidential
distinction explicitly. The source record does not yet justify treating
West Saxon vocalism as decisive evidence for an earlier diphthongal stem
or for paradigmatic levelling.

## Remaining questions and research files

The remaining requested publications are Dal (1934), including its
identified 1971 reprint, pp. 65–73; Wallenberg (1931), pp. 203–205; and
Brooks and Kelly (2013). These are not held, and the handoff identifies
the specific question each could address. Wallenberg 1934 is a different
book and not a substitute for the required 1931 work. No further general
acquisitions were pursued.

The central bibliography, source catalogue, project manifest, holdings,
and page map register Cooper, Hogg, and Ritt; Ritt's existing
ILL-pending record was updated to acquired/consulted rather than
duplicated. Cooper's JSTOR identifier is
recorded as a stable URL, not a verified DOI. Hogg (2006) is registered
under Hogg as chapter author; van Kemenade and Los are editors.

Use `CONCORDANCE.tsv`, `DOE_CROSSWALK_2026-11-23.tsv`,
`COOPER_CHARTER_CORPUS.tsv`, `QUANTITY_EVIDENCE.md`,
`LINDISFARNE_EVIDENCE.md`, `PARADIGM.md`, and this memorandum together.
The private reference PDFs and extracts are checkout-specific and
Git-ignored. Their paths and hashes must be checked in another worktree;
edition-only readings and electronic transcript negatives must not be
described as fresh manuscript collation.
