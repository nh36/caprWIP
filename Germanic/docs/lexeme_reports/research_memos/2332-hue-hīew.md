# Research memo — 2332 hue / hīew

## Starting point

- **ID:** 2332
- **CONCEPT:** hue
- **COUNTERPART:** hīew
- **PROTO:** *xéwją
- **PROTOFORM:** *xéwją
- **DERIVATION_CLASS:** regular

This row was added to separate two changes that had been witnessed by the same
two words. West Germanic gemination of \*w before \*j (SC010's \*w branch) and
the later English resolution of the resulting \*awwj (SC029) were both carried
entirely by `hay` and `strew`. Because every witness of the gemination also
underwent the resolution, nothing in the corpus showed that the gemination is
the broader of the two changes, and a reader could not tell the two events
apart. The selection research is in
`Germanic/docs/sound_changes/audits/sc010-w-gemination-and-hay-depth-adjudication.md`.

## Packet evidence assessment

**Authoritative/current:** the live TSV row; the compact derivation trace
`*xéwją -> hīew`; Campbell §120.2 [@Campbell1959, p. 46], which states the law,
gives the divergent outcomes of the two vowel types, and prints the target form;
Kroonen s.v. \*heuja- [@Kroonen2013, p. 224] for the reconstruction and the
comparative set.

**Useful background:** Ringe and Taylor's Proto-West-Germanic geminates
\*[niwwa-], \*[siwwian], \*[gliwwias] and the paradigm contrast between
non-geminated nominatives and geminated oblique cells [@RingeTaylor2014, p. 53];
the dictionaries for the ordinary Old English spellings [@ClarkHall1960;
@BosworthToller1898].

**Stale or superseded:** any statement that the corpus contains no \*iwj lexeme,
and any statement that the \*w branch of the gemination is witnessed only by
words that also undergo the later resolution.

## Reconstruction and early-stage forms

1. **Cognate-set proto:** PGmc \*heuja- n. 'visible layer, appearance'
   [@Kroonen2013, p. 224]; Campbell writes the same stem type in \*i-notation,
   \*hiwja- beside \*niwja- [@Campbell1959, §120.2, p. 46].
2. **Project input form:** `*xéwją`. The prevocalic \*-u- of the diphthong is
   written \*w, as in `*knéwą` (knee) and `*kéwwaną` (chew); `*x` is the
   Proto-Germanic voiceless dorsal fricative; the acute marks primary stress.
   The raising of \*e to \*i before \*j is left to the cascade, so the input is
   entered with \*é. The alternative spelling `*xíwją` reaches the same output.
3. **OE target form:** `hīew`, Campbell's West Saxon form, printed beside
   *hīow* [@Campbell1959, §120.2, p. 46].

Two candidate lexemes were considered and set aside. Campbell's own headline
example of the \*iwj type is *nīowe*, *nīewe* 'new', but the corpus cannot
currently target a *ja*-stem adjective: the cascade does not model the
inflectional \*-e of that class, and the same gap shows in
\*grōnijaz and \*mildijaz, which yield *grēn* and *mild* rather than *grēne* and
*milde*. Adding 'new' would therefore have introduced a row failing for reasons
unrelated to the gemination. Campbell's *glīow*, *glīw* 'mirth' is a genuine
member of the type, but the project targets West Saxon and Campbell does not
print a West Saxon *glīew*. 'Hue' is the one member of Campbell's list whose
West Saxon form he prints and whose stem class the corpus already handles, in
`hay` \*xáwją, with which it forms a minimal pair.

## Old English philology

*Hīw*, *hēow*, *hīow* n. 'shape, form, appearance, colour, hue' is well attested
and is the ancestor of Modern English *hue* [@Kroonen2013, p. 224;
@ClarkHall1960; @BosworthToller1898]. The selected spelling *hīew* is the rarer
West Saxon variant that Campbell prints in his treatment of this development
[@Campbell1959, §120.2, p. 46]; the project targets West Saxon throughout, and
`hay`'s counterpart *hīeġ* is selected on the same principle.

## Project value

- Gives the \*w branch of West Germanic *j*-gemination a witness that does not
  also undergo the later resolution of \*awwj, so the two changes are no longer
  carried by one and the same pair of words.
- Supplies a negative control for that resolution and for the fronting of the
  diphthong it produces, both of which are restricted to the low-vowel type.
- Forms a minimal pair with `hay`: the two inputs differ in one segment, both
  geminate, and thereafter one loses its \*w and keeps its \*j while the other
  loses its \*j and keeps its \*w, exactly as Campbell states.
- Gives the West Saxon simplification of \*ww its first witness outside the
  words with an inherited Proto-Germanic geminate.

## Paradigm probe

Not required for the corpus, but relevant to the analysis. Ringe and Taylor
contrast paradigm cells whose ending contained \*j, and which therefore
geminated, with cells whose ending contained \*i and did not: OHG *hewi* beside
*houwi*, and within Old English itself *glīg* from the non-geminated nominative
beside *glīowes* in the geminated genitive [@RingeTaylor2014, p. 53]. That
contrast is strong comparative warrant for the gemination, but representing it
would require two selected protoforms for one lexical derivation, which the
project's conventions do not allow. It is recorded in the adjudication memo and
in the reader-facing chapter instead.

## Recommended final report

A short final report is sufficient: a regular derivation whose interest lies in
which rules do *not* fire, the minimal pair with `hay`, and the West Saxon
spelling choice.

## Data-change recommendations

- **TSV PROTO / PROTOFORM / COUNTERPART / DERIVATION_CLASS / NOTE:** no change
  recommended; the row was authored in this pass from the adjudicated sources.
- **`oe_known_problems.tsv`:** no change recommended.
- **Recorded for a later pass:** the cascade does not model the \*-e of
  *ja*-stem adjectives, which is why 'new' could not be used here.
