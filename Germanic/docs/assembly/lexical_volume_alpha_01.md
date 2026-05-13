# Germanic Lexeme Reports: Lexical Derivation Volume

_Alpha 01 assembly scaffold. This document assembles the current lexeme-report corpus in manifest order without revising entry-level prose, citations, locators, or transducer logic._

## Introduction

The lexical catalogue is organized by derivation class rather than as a single
undifferentiated list. This makes the interpretive burden of each entry
explicit. Regular derivations establish the baseline relation between selected
input and Old English target under the current cascade. The variant, analogy,
reconstructed-comparator, and exception classes then show where that baseline is
not sufficient on its own.

This lexical catalogue is a word-centered volume. It shows how individual
selected inputs develop to individual Old English targets and how each entry is
classified. A later sound-change volume or report should remain separate and
rule-centered, covering chronology, interactions among rules, and broader
system-level exception handling.

## Data and sources

This alpha assembles the current model-entry corpus against the live manifest, compact derivation-trace report, and project bibliography. The lexical data layer is the current aligned Germanic dataset as represented by the model-entry metadata and the current compact trace source; comparative dictionaries, Old English dictionaries, and historical grammars remain in the entry prose exactly as already cited there.

Broad citations are carried forward honestly where the citation-layer audit already judged them mechanically acceptable for assembly. This alpha therefore tests book structure and technical integration rather than attempting a final source-polish pass.

## Transducer and derivation method

Each lexical entry retains the pilot structure: a generated derivation summary, a boxed derivation trace split into Earlier Germanic changes and Old English changes, and the current model-entry prose. The summary distinguishes citation reconstruction, selected input, transducer outcome, and selected target where those differ, and the boxed trace remains a compact PDF-oriented rendering of the current compact trace data.

## Derivation classes

The lexical catalogue is ordered by the seven live `DERIVATION_CLASS` values in the manifest. Counts in this alpha are taken directly from `manifest_all_by_class.tsv`:

- `regular`: **70**
- `attested_variant`: **4**
- `early_analogy`: **35**
- `late_analogy`: **28**
- `reconstructed_oe`: **3**
- `known_unmodelled`: **2**
- `unexplained_unmodelled`: **5**

\clearpage

## Part I. Regular derivations

Regular derivations are entries where the selected transducer input and the Old
English target stand in a straightforward relation under the current cascade.
These entries form the baseline against which the analogy and exception classes
are interpreted.

### adder — OE nǣdre

Derivation: _\*nḗdrōn_ $\rightarrow$ _nǣdre_ (regular).

#### Derivation trace

Proto input: _\*nḗdrōn_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc N Stem N Loss & \emph{*nḗdrǭ} \\
NWGmc Long E Lowering & \emph{*nǣdrǭ} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Unstressed Long Vowel Shortening & \emph{*nǣdræ} \\
OE Unstressed AE Merger & \emph{*nǣdre} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _nǣdre_

#### Reconstruction and comparative evidence

Kroonen distinguishes the masculine snake word _\*nadra-_ from a feminine
ablauting formation _\*nēdrōn-_, and gives Old English _nǣdre, næddre_ under the
latter [@Kroonen2013, 426]. Orel likewise points from the masculine entry to a
feminine _\*nēdrōn ~ \*nadrōn_ type [@Orel2003, 325].

The selected input therefore is not a reshaped convenience form. It is the
comparative reconstruction that specifically underlies the Old English noun.

#### Old English evidence

The Old English word is securely represented by _nǣdre_, with _næddre_ as a
secondary variant. Clark Hall cross-references _næddre_ to _nædre_, and Fulk
treats _næddre_ as the later geminated form beside the older base [@ClarkHall1960,
225; @Fulk2018, 149].

#### Development to Old English

From _\*nḗdrōn_, the stressed long mid vowel develops to Old English _ǣ_, and
the weak feminine ending remains as final _-e_, giving _nǣdre_. The doubled
consonant of _næddre_ is secondary and does not alter the inherited base form.

### bake — OE bacan

Derivation: _\*bákaną_ $\rightarrow$ _bacan_ (regular).

#### Derivation trace

Proto input: _\*bákaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*bækaną} \\
OE A Restoration & \emph{*bakaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*bakan} \\
OE Secondary Nasalization & \emph{*bakąn} \\
OE Weak Tail Reduction & \emph{*bakan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _bacan_

#### Reconstruction and comparative evidence

Orel reconstructs the verb as _\*bakanan_ and cites Old English _bacan_ beside Old High German _backan, bahhan_ [@Orel2003]. Campbell gives _bacan_ as one of the standard examples of Old English A-restoration before a single consonant, and Ringe and Taylor state the same development from _\*bakan_ to Old English _bacan_ [@Campbell1959, 61; @RingeTaylor2014].

#### Old English evidence

Bosworth-Toller and Clark Hall both record _bacan_ as the ordinary Old English verb 'to bake' [@BosworthToller1898, 72; @ClarkHall1960]. The target in this entry is therefore the attested infinitive headword itself, not a selected oblique or finite paradigm cell.

#### Development to Old English

From _\*bákaną_, Anglo-Frisian brightening first gives _\*bækaną_. A-restoration then returns the stem vowel to _a_ before single _k_ plus the back-vocalic infinitive suffix, and later apocope and weak-tail reduction yield _bacan_ [@Campbell1959, 61; @RingeTaylor2014]. The development is therefore straightforward: _\*bákaną > bacan_.

### beech — OE bōc

Derivation: _\*bōkō_ $\rightarrow$ _bōc_ (regular).

#### Derivation trace

Proto input: _\*bōkō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc Final Long O Raising & \emph{*bōku} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE High Vowel Apocope & \emph{*bōk} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _bōc_

#### Reconstruction and comparative evidence

Kroonen gives the beech noun as _\*bōk(j)ō-_ and cites Old English _boc, bēce_ among its reflexes [@Kroonen2013]. The selected input _\*bōkō_ is the nominative-singular shape of that family, which is the relevant comparison form here.

#### Old English evidence

Kroonen's Old English evidence already separates the paradigm material: _boc_ as the nominative form and _bēce_ as an oblique form [@Kroonen2013]. The relevant comparator is therefore _bōc_; _bēċe_ remains related paradigm evidence rather than the form chosen for this comparison.

#### Development to Old English

With nominative input _\*bōkō_, the development is compact. Northwest Germanic final long _ō_ raises to _u_, and later high-vowel apocope leaves _bōc_. The regular comparison is therefore _\*bōkō > bōc_.

### begin — OE beġinnan

Derivation: _\*bigínnaną_ $\rightarrow$ _beġinnan_ (regular).

#### Derivation trace

Proto input: _\*bigínnaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*bigínnan} \\
OE Secondary Nasalization & \emph{*bigínnąn} \\
OE Velar Palatalization & \emph{*biʤínnąn} \\
OE Prefix I Reduction & \emph{*bĕʤínnąn} \\
OE Weak Tail Reduction & \emph{*bĕʤínnan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _beġinnan_

#### Reconstruction and comparative evidence

The verb is modeled here as inherited _\*bigínnaną_. Ringe and Taylor state that intervocalic _\*g_ is palatalized between front vowels in Old English [@RingeTaylor2014], and Campbell lists _ginnan_ among familiar examples of palatal _g_ in this verb family [@Campbell1959, 174].

#### Old English evidence

Bosworth-Toller and Clark Hall lemmatize the verb as _be-ginnan_ / _beginnan_ [@BosworthToller1898, 84; @ClarkHall1960]. Those plain-_g_ dictionary spellings support the same verb that appears here in normalized form as _beġinnan_.

#### Development note

The prefix deserves separate notice. Ringe and Taylor explicitly cite _bi- > be-_ as an Old English unstressed-prefix development [@RingeTaylor2014].

#### Development to Old English

From _\*bigínnaną_, heavy-syllable nasal apocope yields _\*bigínnan_. Intervocalic _\*g_ between front vowels then palatalizes to _ġ_, and the unstressed prefix reduces _bi-_ to _be-_, giving _beġinnan_.

### bier — OE bǣr

Derivation: _\*bḗrō_ $\rightarrow$ _bǣr_ (regular).

#### Derivation trace

Proto input: _\*bḗrō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc Final Long O Raising & \emph{*bḗru} \\
NWGmc Long E Lowering & \emph{*bǣru} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE High Vowel Apocope & \emph{*bǣr} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _bǣr_

#### Reconstruction and comparative evidence

Kroonen reconstructs the noun as _\*bērō-_ f. 'bier' and cites Old English _bar, bær_ among the reflexes [@Kroonen2013, 717]. The selected input _\*bḗrō_ is the same lexeme in the accent notation used here.

#### Old English evidence

Clark Hall and Bosworth-Toller lemmatize the noun as _bær_, and Kroonen also records _bar_ beside it [@ClarkHall1960; @BosworthToller1898, 73; @Kroonen2013, 717]. The target _bǣr_ is therefore a normalized long-vowel spelling of the same noun.

#### Source note

Lexicographic spellings vary between _bær_ and _bar_. The normalized target _bǣr_ simply marks the same long vowel explicitly [@ClarkHall1960; @BosworthToller1898, 73; @Kroonen2013, 717].

#### Development to Old English

From _\*bḗrō_, Northwest Germanic final long _ō_ raises to _u_, long _ē_ lowers to _ǣ_, and high-vowel apocope yields _bǣr_. The resulting noun matches the normalized Old English target.

### birth — OE byrd

Derivation: _\*búrdiz_ $\rightarrow$ _byrd_ (regular).

#### Derivation trace

Proto input: _\*búrdiz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*búrdi} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE I Umlaut & \emph{*byrdi} \\
OE High Vowel Apocope & \emph{*byrd} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _byrd_

#### Reconstruction and comparative evidence

Kroonen cites the noun under stem-level _\*burdi-_ and gives Old English _(ge-)byrd_ among the reflexes [@Kroonen2013]. The selected input _\*búrdiz_ is the nominative-style form that stands behind that stem label.

#### Old English evidence

Clark Hall and Bosworth-Toller both attest simplex _byrd_ as an Old English noun meaning 'birth' [@ClarkHall1960; @BosworthToller1898, 125]. The prefixed form _gebyrd_ is also well established in the tradition: Kroonen lists _(ge-)byrd_, Bosworth-Toller has a separate _ge-byrd_ entry, and Campbell cites _gebyrd_ and _gebyrdu_ in his grammatical discussion [@Kroonen2013; @BosworthToller1898, 125; @Campbell1959].

#### Form note

The relevant comparator here is the simplex noun _byrd_. The prefixed forms remain related attested material within the same lexical family, and Hogg's discussion of deverbal feminines provides the broader derivational setting [@Hogg1992].

#### Development to Old English

From _\*búrdiz_, loss of final _z_ gives _\*búrdi_. I-umlaut fronts _u_ to _y_, and high-vowel apocope then yields _byrd_. The result is the ordinary simplex Old English noun.

### bone — OE bān

Derivation: _\*báiną_ $\rightarrow$ _bān_ (regular).

#### Derivation trace

Proto input: _\*báiną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Ai Monophthongization & \emph{*bāną} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*bān} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _bān_

#### Reconstruction and comparative evidence

Kroonen cites the noun as _\*baina-_, and Orel gives the same lexeme under _\*bainan_ [@Kroonen2013; @Orel2003]. Both are comparative headword conventions for the same neuter noun whose Old English reflex is _bān_.

#### Old English evidence

Clark Hall and Bosworth-Toller record _bān_ as the ordinary Old English noun [@ClarkHall1960; @BosworthToller1898]. Bright's glossary also distinguishes citation-form _bān_ from oblique _bāne_, which keeps the nominative-accusative singular separate from the rest of the paradigm [@BrightCassidyRingler1971].

#### Source note

The comparative headwords _\*baina-_ and _\*bainan_ provide lexeme background. The relevant comparison form here is the nominative-accusative singular _\*báiną_.

#### Development to Old English

West Germanic monophthongization turns stressed _\*ai_ into _ā_, giving _\*bāną_; heavy-syllable nasal apocope then yields _bān_. The resulting form matches the attested Old English citation noun.

### both — OE bū

Derivation: _\*bō_ $\rightarrow$ _bū_ (regular).

#### Derivation trace

Proto input: _\*bō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc Stressed Monosyllable O Raising & \emph{*bū} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\raggedright [no change]\par
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _bū_

#### Reconstruction and comparative evidence

Kroonen treats the Germanic numeral under _\*ba-_ and gives the inherited
paradigm _\*bai, \*bans, \*bōz/\*bōns, \*bō_, with Old English _bēġen_, _bā_, and
neuter _bū_ [@Kroonen2013, p. 47]. For the present entry, the relevant inherited
form is the unextended neuter dual _\*bō_.

The older explanation of _bēġen_ derives it from _\*bō-jen-_, and Orel still
gives _OE bezen (< \*bō-jenō)_ beside _ON báðir_, _OFris bēthe_, _OS be-thia_,
and _OHG bēde, beide_ [@Orel2003, p. 65]. Fulk reports that explanation
cautiously and notes Seebold's preference for a _\*bō-þ-_ analysis instead
[@Fulk2018, §10.1]. That debate matters for _bēġen_ and for the extended forms
behind Modern English _both_, German _beide_, and Dutch _beide_; it does not
displace the inherited neuter _\*bō > bū_ treated here.

#### Old English evidence

The Old English dual paradigm is well established. Brunner gives masculine
_bēġen_, feminine _bā_, and neuter _bū_ beside _bā_, with compounds such as
_bā twā_, _bū tū_, and _bām twām_ [@SieversBrunner1965, §324 Anm. 2].
Campbell and Fulk present the same basic pattern: masculine _bēġen_, feminine
_bā_, neuter _bā, bū_, genitive _bēġra, bēġ(e)a_, and dative _bǣm_
[@Campbell1959, §683; @Fulk2018, §10.1].

_bū_ is therefore an attested neuter dual form, not a reconstruction. It is the
cleanest target for this entry because _bēġen_ belongs to the historically more
contested _\*bō-jen-_ / analogical zone, while _bā_ remains a partner form
within the dual paradigm rather than the most straightforward monosyllabic
comparison.

#### Development to Old English

_\*bō_ is a stressed monosyllabic form. Campbell cites _cū_, _hū_, _tū_, and
_bū_ as examples of final accented _ō > ū_ in the West Germanic stage leading
to Old English [@Campbell1959, §122]. Brunner states the same development more
directly: _Auslautendes ō erscheint als û in bū ... cu ... hū, tū_
[@SieversBrunner1965, §69].

The development is therefore straightforward: _\*bō > bū_.

#### Form comparison

The comparison below is manual. It separates the inherited OE target from the
other forms that belong to the same broader lexical history.

| Form | Source / stage | Status | Relevance to this entry |
| :--- | :--- | :--- | :--- |
| _\*bō > bū_ | PGmc neuter dual > OE neuter dual | selected regular comparison | main line of the entry |
| _bēġen_ | OE masculine dual | attested, but historically contested and at least partly analogical in Kroonen | real OE evidence, not the selected target |
| _bā_ | OE feminine dual; also neuter variant | attested partner form | part of the OE paradigm, but not the chosen monosyllabic comparator |
| _báðir_, _beide_, _both_ | Norse, continental West Germanic, Modern English extended forms | related but different formation | useful background, not the direct continuation of OE _bū_ |

### bow — OE bīeġan

Derivation: _\*báugijaną_ $\rightarrow$ _bīeġan_ (regular).

#### Derivation trace

Proto input: _\*báugijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Au Fronting & \emph{*báeugijaną} \\
OE Diphthong Leveling & \emph{*bēagijaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*bēagijan} \\
OE Secondary Nasalization & \emph{*bēagijąn} \\
Sievers Law Syncope & \emph{*bēagjąn} \\
OE Velar Palatalization & \emph{*bēaʤjąn} \\
OE I Umlaut & \emph{*bīeʤjąn} \\
OE Weak Tail Reduction & \emph{*bīeʤjan} \\
OE J Loss After Heavy & \emph{*bīeʤan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _bīeġan_

#### Reconstruction and comparative evidence

Kroonen reconstructs the weak verb as _\*baugjan-_ 'to (make) bend' and cites Old English _biegan_ among its reflexes [@Kroonen2013]. Ringe and Taylor give the northwest Germanic and West Saxon development more fully as _PNWGmce \*baugijana > \*béagjan > WS OE biegan_ [@RingeTaylor2014]. The entry therefore concerns the weak causative member of the bend-family, alongside the related strong verb and noun.

#### Old English evidence

Clark Hall lemmatizes _biegan_, and Bosworth-Toller records _bigan_ with examples such as _Ic bēge mīne cneówa_ and _Se ord bīgde upp tō þām hiltum_ [@ClarkHall1960; @BosworthToller1898, 102]. The form _bīeġan_ used here is a normalized spelling of that attested Old English weak verb.

#### Development to Old English

From _\*báugijaną_, the stem reaches pre-Old-English _\*bēagjan_, after which palatalization of _\*gj_ and i-umlaut yield West Saxon _biegan_; Campbell lists _biegan_ among the regular _ie_ outcomes of _\*éa_ under i-umlaut [@RingeTaylor2014; @Campbell1959, 80]. The development is therefore straightforward: _\*báugijaną > bīeġan_.

### breeches — OE brēċ

Derivation: _\*brōkiz_ $\rightarrow$ _brēċ_ (regular).

#### Derivation trace

Proto input: _\*brōkiz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*brōki} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Velar Palatalization & \emph{*brōʧi} \\
OE I Umlaut & \emph{*brēʧi} \\
OE High Vowel Apocope & \emph{*brēʧ} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _brēċ_

#### Reconstruction and comparative evidence

Kroonen cites the noun under _\*brōk-_, with Old English _brōc_ and plural 'breeches' among its reflexes [@Kroonen2013]. Ringe and Taylor give the plural development directly as _PNWGmce \*brokiz > \*breeci > OE bréc_ [@RingeTaylor2014]. The deeper verbal base belongs to the noun's etymological background, while the selected input here is the plural noun form _\*brōkiz_.

#### Old English evidence

Bright notes _brōc_ with plural _brēc_, and Clark Hall gives _brēc fp. breeches_ while also listing _broc_ as a feminine noun probably represented chiefly in the plural [@BrightCassidyRingler1971; @ClarkHall1960, 64]. The spelling _brēċ_ used here makes the long vowel and palatal consonant explicit; the Old English evidence itself is the attested plural _brēc_.

#### Development to Old English

After loss of final _-z_, the stem ends in _-ki_, so the velar palatalizes and _ō_ undergoes i-umlaut to _ē_; final high-vowel apocope then yields _brēċ_ [@RingeTaylor2014]. The development is therefore regular: _\*brōkiz > brēċ_.

### calf — OE ċealf

Derivation: _\*kálbaz_ $\rightarrow$ _ċealf_ (regular).

#### Derivation trace

Proto input: _\*kálbaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*kálba} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Final Bare A Loss & \emph{*kálb} \\
Anglo Frisian Brightening & \emph{*kælb} \\
OE Breaking & \emph{*kealb} \\
PGmc B Allophony & \emph{*kealβ} \\
OE Velar Palatalization & \emph{*ʧealβ} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _ċealf_

#### Reconstruction and comparative evidence

Kroonen treats the noun under _\*kalbiz-_ and notes an older s-stem _\*kalbaz, pl. \*kalbizō_, while Orel cites _\*kalbaz_ as the citation form and Ringe and Taylor derive West Saxon _Cealf_ from _\*kalbaz, \*kalbiz-_ [@Kroonen2013; @Orel2003, 248; @RingeTaylor2014, 220]. The selected input here is the singular _\*kálbaz_, since the entry concerns the citation-form noun.

#### Old English evidence

Clark Hall gives _cealf I. (æ, e) nm. (nap. cealfru)_, and Bosworth-Toller likewise records _Caelf_ / _Cealf_ beside plural forms such as _calfur_ and _cealfru_ [@ClarkHall1960; @BosworthToller1898, 131]. Campbell and Fulk show the same singular-plus-_-r-_ plural pattern [@Campbell1959; @Fulk2018, 193]. The spelling _ċealf_ used here makes the palatalized initial explicit; the ordinary attested dictionary headword is _cealf_.

#### Development to Old English

After loss of final _-z_ and bare _-a_, Anglo-Frisian brightening gives _\*kælb_, and breaking before _l_ plus consonant yields _\*kealb_. Ringe and Taylor's account of the lexeme and their rule for initial _k_ in front-vocalic environments support the West Saxon palatalized onset represented here as _ċ-_, so _\*kálbaz_ develops regularly to _ċealf_ [@RingeTaylor2014, 220].

### corn — OE corn

Derivation: _\*kúrną_ $\rightarrow$ _corn_ (regular).

#### Derivation trace

Proto input: _\*kúrną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc U Lowering & \emph{*kórną} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*kórn} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _corn_

#### Reconstruction and comparative evidence

Kroonen cites the noun as _\*kurna-_, and Orel gives the citation form _\*kurnan_, both with Old English _corn_ among the reflexes [@Kroonen2013; @Orel2003, 264]. The singular form _\*kúrną_ is the nominative-accusative singular appropriate to the citation noun.

#### Old English evidence

Clark Hall gives _corn n. 'corn,' grain_, Bright's glossary lists _corn, n._ with genitive singular _cornes_, and Bosworth-Toller treats _corn_ as an ordinary noun headword [@ClarkHall1960; @BrightCassidyRingler1971, 347; @BosworthToller1898, 144]. The target is therefore an attested citation form, while forms such as _cornes_ simply provide paradigm background.

#### Development to Old English

With northwest Germanic lowering, _\*kúrną_ becomes _\*kórną_, and later loss of final nasal after a heavy syllable yields _\*kórn_, whence _corn_. The oblique form _\*kurnăn_ belongs to comparative background rather than to the derivational input of this entry.

### deed — OE dǣd

Derivation: _\*dḗdiz_ $\rightarrow$ _dǣd_ (regular).

#### Derivation trace

Proto input: _\*dḗdiz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*dḗdi} \\
NWGmc Long E Lowering & \emph{*dǣdi} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE High Vowel Apocope & \emph{*dǣd} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _dǣd_

#### Reconstruction and comparative evidence

Orel reconstructs the noun as _\*dēdiz_, and Ringe and Taylor derive the same inherited i-stem from Proto-Germanic _\*dédiz_ through northwest Germanic _\*dadiz_ [@Orel2003; @RingeTaylor2014]. The stress-marked form _\*dḗdiz_ represents that same inherited noun in a notation that keeps the stressed long vowel explicit.

#### Old English evidence

Campbell states that Primitive Germanic _ē_ appears as West Saxon _ǣ_ but in other Old English dialects mostly as _ē_, and Brunner gives the contrast explicitly as West Saxon _dǣd_ beside non-West-Saxon _dēd_ [@Campbell1959; @SieversBrunner1965]. Clark Hall likewise lists _dæd_ and cross-refers Anglian _dēd_ to it [@ClarkHall1960]. West Saxon _dǣd_ is therefore the relevant Old English form here, with Anglian _dēd_ as a dialectal doublet.

#### Development to Old English

From inherited _\*dēdiz_, loss of final _-z_ and the West Saxon lowering of stressed long _ē_ yield _dǣd_; Anglian _dēd_ preserves the non-West-Saxon outcome [@Campbell1959; @SieversBrunner1965]. The development treated here is therefore the regular West Saxon line.

### door — OE dor

Derivation: _\*dúrą_ $\rightarrow$ _dor_ (regular).

#### Derivation trace

Proto input: _\*dúrą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc U Lowering & \emph{*dórą} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*dór} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _dor_

#### Reconstruction and comparative evidence

Kroonen reconstructs a neuter _\*dura-_ 'gate, (single) door' and cites Old English _dor_ among its reflexes. In the same entry he separates Old English _duru_, Old Frisian _dore_, and Old High German _tura_ as reflexes of _\*durō-_ instead [@Kroonen2013].

#### Old English evidence

Clark Hall records _dor_ as a neuter noun and separately records feminine _duru_ with its own inflection [@ClarkHall1960]. Ringe and Taylor likewise treat _duru_ as an early Old English u-stem, originally a root noun shifted into that class [@RingeTaylor2014]. The selected target here is therefore the attested neuter _dor_, while _duru_ remains a parallel Old English reflex from another stem history.

#### Development to Old English

From _\*dúrą_, Northwest Germanic u-lowering gives _\*dórą_, and heavy-syllable nasal apocope then yields _dor_. The regular development treated in this entry is therefore _\*dúrą > dor_; the feminine _duru_ belongs to the separate line identified by Kroonen and Ringe-Taylor [@Kroonen2013; @RingeTaylor2014].

### fare — OE faran

Derivation: _\*fáraną_ $\rightarrow$ _faran_ (regular).

#### Derivation trace

Proto input: _\*fáraną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*færaną} \\
OE A Restoration & \emph{*faraną} \\
OE Heavy Syllable Nasal Apocope & \emph{*faran} \\
OE Secondary Nasalization & \emph{*farąn} \\
OE Weak Tail Reduction & \emph{*faran} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _faran_

#### Reconstruction and comparative evidence

Kroonen gives the inherited strong verb as _\*faran-_, and Orel gives the same lexeme as _\*faranan_, both with Old English _faran_ among the reflexes [@Kroonen2013; @Orel2003, 132]. Campbell also uses _faran_ as a standard example of Old English A-restoration [@Campbell1959, 61].

#### Old English evidence

Clark Hall lemmatizes the strong verb as _faran_ and separately records weak _færan_ 'to frighten'; _fære_, _færst_, and _færð_ belong to present-tense forms of _faran_ rather than to the infinitive itself [@ClarkHall1960]. Bosworth-Toller preserves the same distinction [@BosworthToller1898, 108]. The selected target is therefore the attested citation infinitive _faran_.

#### Development to Old English

From _\*fáraną_, Anglo-Frisian brightening first gives _\*færaną_, but A-restoration before single _r_ returns _\*faraną_; later apocope and weak-tail reduction yield _faran_ [@Campbell1959, 61]. Fulk's contrast with participial _faren- < \*faræn- < \*faran-_ shows why fronting elsewhere in the paradigm does not alter the infinitive headword [@Fulk2018].

### fell — OE fell

Derivation: _\*féllą_ $\rightarrow$ _fell_ (regular).

#### Derivation trace

Proto input: _\*féllą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*féll} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _fell_

#### Reconstruction and comparative evidence

Kroonen reconstructs the noun as _\*fella-_ 'membrane, skin, hide' and cites Old English _fell_ beside Dutch _vel_ and German _Fell_ [@Kroonen2013]. The selected input _\*féllą_ is the derivable singular form of that same inherited noun.

#### Old English evidence

Clark Hall records _fell_ as the noun 'fell, skin, hide', and Bright's glossary likewise gives _fell_ with inflected forms such as accusative singular _fel_ and dative plural _fellum_ [@ClarkHall1960; @BrightCassidyRingler1971]. The target is therefore the attested noun _fell_, not the verb _fellan_ or the preterite _feoll_.

#### Development to Old English

With _\*féllą_, no special earlier reshaping is needed: heavy-syllable nasal apocope yields _\*féll_, surfacing as _fell_. The regular development treated here is therefore _\*féllą > fell_.

### fern — OE fearn

Derivation: _\*fárnaz_ $\rightarrow$ _fearn_ (regular).

#### Derivation trace

Proto input: _\*fárnaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*fárna} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Final Bare A Loss & \emph{*fárn} \\
Anglo Frisian Brightening & \emph{*færn} \\
OE Breaking & \emph{*fearn} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _fearn_

#### Reconstruction and comparative evidence

Kroonen cites the noun as masculine _\*farna-_ and gives Old English _fearn, fern_, while Orel gives the same lexeme as neuter _\*farnan_ with Old English _fearn_ [@Kroonen2013; @Orel2003, 133]. Those are comparative headword conventions rather than competing Old English outcomes; the modeled input here is the nominative-style _\*fárnaz_.

#### Old English evidence

Clark Hall gives _fearn_ as an Old English noun, and Bosworth-Toller records _fearn_ with inflected forms such as _fearnes_, _fearna_, and _fearne_ [@ClarkHall1960; @BosworthToller1898, 219]. Kroonen's additional _fern_ remains useful comparative background, but the best-supported citation target in the local lexical sources is _fearn_ [@Kroonen2013].

#### Development to Old English

From _\*fárnaz_, loss of final _-z_ and final _-a_ gives _\*fárn_; Anglo-Frisian brightening then yields _\*færn_, and breaking before _r_ plus consonant gives _fearn_ [@Campbell1959; @RingeTaylor2014]. The development treated here is therefore the regular _rC_-breaking line.

### field — OE feld

Derivation: _\*félθuz_ $\rightarrow$ _feld_ (regular).

#### Derivation trace

Proto input: _\*félθuz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc L Th Voicing & \emph{*félduz} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*féldu} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE High Vowel Apocope & \emph{*féld} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _feld_

#### Reconstruction and comparative evidence

Ringe and Taylor treat Old English _feld_ as one of the cases where earlier _\*felþu- ~ \*feldu-_ may reflect either inherited _\*þ ~ \*d_ alternation or the regular West Germanic development _\*lþ > ld_ [@RingeTaylor2014, 170]. The broader proto label _\*félθuz_ can remain as comparative background, while that narrower historical ambiguity does not affect the regular classification.

#### Old English evidence

Clark Hall records _feld_ with oblique forms such as _felda_ and _felde_, and Campbell notes early place-name spellings in _-felth_ beside the later standard form [@ClarkHall1960, 114; @Campbell1959, 169]. The selected target is therefore the attested citation noun _feld_, with the older _-felth_ spellings as historical support rather than as rival targets.

#### Development to Old English

In the modeled pathway, medial _\*lþ_ becomes _ld_, final _-z_ is lost, and high-vowel apocope then yields _feld_. Whether the voiced dental ultimately reflects inherited alternation or the regular _\*lþ > ld_ development, both accounts converge on the same Old English form [@RingeTaylor2014, 170].

### fly — OE flēogan

Derivation: _\*fléuganą_ $\rightarrow$ _flēogan_ (regular).

#### Derivation trace

Proto input: _\*fléuganą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Diphthong Leveling & \emph{*flēoganą} \\
OE Heavy Syllable Nasal Apocope & \emph{*flēogan} \\
OE Secondary Nasalization & \emph{*flēogąn} \\
OE Weak Tail Reduction & \emph{*flēogan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _flēogan_

#### Reconstruction and comparative evidence

Ringe and Taylor derive the verb as _\*fleugana > OE fléogan_ and elsewhere contrast West Saxon _fléogan_ with Anglian _flégan_, alongside related forms _fléoge / flége_ [@RingeTaylor2014]. The selected input _\*fléuganą_ represents that inherited strong verb in the notation used here.

#### Old English evidence

Clark Hall and Bosworth-Toller record _flēogan_ as the ordinary Old English strong verb, and Bright gives the familiar paradigm _flēag, flugon, flogen_ with present _fleogeð_ [@ClarkHall1960; @BosworthToller1898; @BrightCassidyRingler1971]. The target in this entry is therefore the attested verbal infinitive itself.

#### Form note

Ringe and Taylor also list related _fléoge / flége_ and Anglian _flégan_, which belong to the same family but do not replace the infinitive _flēogan_ treated here [@RingeTaylor2014].

#### Development to Old English

From _\*fléuganą_, Old English diphthong leveling gives _\*flēoganą_; heavy-syllable nasal apocope and weak-tail reduction then yield _flēogan_ [@RingeTaylor2014]. The development is therefore regular: _\*fléuganą > flēogan_.

### forlorn — OE lēosan

Derivation: _\*léusaną_ $\rightarrow$ _lēosan_ (regular).

#### Derivation trace

Proto input: _\*léusaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Diphthong Leveling & \emph{*lēosaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*lēosan} \\
OE Secondary Nasalization & \emph{*lēosąn} \\
OE Weak Tail Reduction & \emph{*lēosan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _lēosan_

#### Reconstruction and comparative evidence

Kroonen reconstructs the verb under _\*leusan-_ and cites prefixed daughters such as Gothic _fra-liusan_ and Old English _for-lēosan_; Orel likewise gives Old English _for-leósan_ [@Kroonen2013; @Orel2003]. The inherited verbal base is therefore clear, though the daughter set often appears with the prefix.

#### Old English evidence

The direct Old English evidence behind English _forlorn_ lies in the prefixed verb _forlēosan_ and especially in the participle _forloren_, recorded by Ringe and Taylor and in the dictionaries [@RingeTaylor2014; @ClarkHall1960; @BosworthToller1898]. The simplex infinitive _lēosan_ represents the verbal base itself.

#### Form note

As a base-form comparison, the simplex infinitive is _lēosan_, while the English adjective continues the prefixed Old English family _forlēosan / forloren_ [@RingeTaylor2014].

#### Development to Old English

From _\*léusaną_, Old English diphthong leveling gives _\*lēosaną_, and later nasal apocope and weak-tail reduction yield _lēosan_ [@RingeTaylor2014]. The prefixed forms follow the same verbal base with added _for-_.

### gang — OE gang

Derivation: _\*gángaz_ $\rightarrow$ _gang_ (regular).

#### Derivation trace

Proto input: _\*gángaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*gánga} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Final Bare A Loss & \emph{*gáng} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _gang_

#### Reconstruction and comparative evidence

Orel reconstructs the noun as _\*gangaz_ and cites Old English _gang_ beside Old Norse _gangr_, Old Frisian _gang / gong_, Old Saxon _gang_, and Old High German _gang_ [@Orel2003]. The selected input _\*gángaz_ is the same lexeme in the accent notation used here.

#### Old English evidence

Clark Hall and Bosworth-Toller both record _gang_ as the noun 'going, journey, way', and Bright's glossary gives _gong (gang), m., path, course_ [@ClarkHall1960; @BosworthToller1898, 159; @BrightCassidyRingler1971, 392]. The target is therefore the attested noun headword itself.

#### Form note

This entry concerns the noun _gang_, not the separate verb _gangan_ [@ClarkHall1960; @BosworthToller1898, 159].

#### Development to Old English

From _\*gángaz_, loss of final _-z_ gives _\*gánga_, and later loss of final bare _-a_ yields _gang_. The development is therefore regular: _\*gángaz > gang_.

### give — OE ġiefan

Derivation: _\*gébaną_ $\rightarrow$ _ġiefan_ (regular).

#### Derivation trace

Proto input: _\*gébaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*géban} \\
OE Secondary Nasalization & \emph{*gébąn} \\
PGmc B Allophony & \emph{*géβąn} \\
OE Velar Palatalization & \emph{*ʤéβąn} \\
OE Ws Palatal Diphthongization & \emph{*ʤíeβąn} \\
OE Weak Tail Reduction & \emph{*ʤíeβan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _ġiefan_

#### Reconstruction and comparative evidence

Kroonen reconstructs the strong verb as _\*geban-_ and cites Old English _giefan_ among its reflexes [@Kroonen2013]. Ringe and Taylor contrast West Saxon _giefan_ with Mercian _for-geofan_ and Northumbrian _geafa_, showing that the inherited verb takes different later dialectal shapes [@RingeTaylor2014].

#### Old English evidence

Campbell gives _gefan (W-S giefan)_ among examples of initial palatalization, and Clark Hall records the verb under plain _giefan_ with forms such as _geaf_ and _giefen_ [@Campbell1959; @ClarkHall1960]. The spelling _ġiefan_ used here makes the palatal initial explicit.

#### Dialect note

West Saxon _ie_ here reflects palatal diphthongization after initial palatalization; non-West-Saxon forms such as _geafa_ or _for-geofan_ continue the same verb without the West Saxon vocalism [@RingeTaylor2014].

#### Development to Old English

From _\*gébaną_, initial _g_ palatalizes before _e_; West Saxon palatal diphthongization then yields _ie_, and later tail reduction gives _giefan_ [@Campbell1959; @RingeTaylor2014]. The result is therefore the regular West Saxon infinitive.

### gold — OE gold

Derivation: _\*gúlθą_ $\rightarrow$ _gold_ (regular).

#### Derivation trace

Proto input: _\*gúlθą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc L Th Voicing & \emph{*gúldą} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc U Lowering & \emph{*góldą} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*góld} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _gold_

#### Reconstruction and comparative evidence

Ringe and Taylor cite the noun as _\*gulþa- / \*gulda-_, and Kroonen gives the same pair [@RingeTaylor2014, 42; @Kroonen2013]. The selected input _\*gúlθą_ preserves the older consonantal form while leaving open whether the medial stop reflects inherited alternation or regular West Germanic development.

#### Old English evidence

Bosworth-Toller and Clark Hall both record _gold_ as the ordinary Old English neuter noun [@BosworthToller1898, 121; @ClarkHall1960, 152]. The target is therefore the attested citation form itself.

#### Development note

Ringe and Taylor note that the medial stop can be understood either as alternation _\*gulþa- / \*gulda-_ or as the ordinary West Germanic change _\*lþ > ld_; both routes lead to the same Old English consonantism [@RingeTaylor2014, 42].

#### Development to Old English

From _\*gúlθą_, the regular consonant development gives _\*gúldą_; Northwest Germanic / Old English lowering then yields _\*góldą_, and apocope gives _gold_ [@Campbell1959; @RingeTaylor2014, 42].

### grave — OE grafan

Derivation: _\*grábaną_ $\rightarrow$ _grafan_ (regular).

#### Derivation trace

Proto input: _\*grábaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*græbaną} \\
OE A Restoration & \emph{*grabaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*graban} \\
OE Secondary Nasalization & \emph{*grabąn} \\
PGmc B Allophony & \emph{*graβąn} \\
OE Weak Tail Reduction & \emph{*graβan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _grafan_

#### Reconstruction and comparative evidence

Campbell gives _grafan_ among the standard examples of Old English a-restoration before a single consonant and a following back vowel, and Ringe and Taylor describe the same development for Class VI infinitives [@Campbell1959, 61; @RingeTaylor2014].

#### Old English evidence

Clark Hall records _grafan_ as the verb 'to dig, grave' and separately records noun _græf_ 'grave, trench' [@ClarkHall1960]. The target here is the attested infinitive headword of the verb.

#### Development to Old English

From _\*grábaną_, Anglo-Frisian brightening first gives a fronted stem vowel. A-restoration then returns _a_ before single _b_ plus the back-vocalic infinitive ending, and later apocope and weak-tail reduction yield _grafan_ [@Campbell1959, 61; @RingeTaylor2014].

#### Form note

Noun _græf_ and verbal forms such as _græfð_ or past participial _græfen_ belong to other lexical or paradigm positions and do not replace the infinitive _grafan_ as the target here [@ClarkHall1960].

### guest — OE ġiest

Derivation: _\*gástiz_ $\rightarrow$ _ġiest_ (regular).

#### Derivation trace

Proto input: _\*gástiz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*gásti} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*gæsti} \\
OE Velar Palatalization & \emph{*ʤæsti} \\
OE I Umlaut & \emph{*ʤesti} \\
OE Ws Palatal Diphthongization & \emph{*ʤiesti} \\
OE High Vowel Apocope & \emph{*ʤiest} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _ġiest_

#### Reconstruction and comparative evidence

Campbell and Ringe-Taylor treat the noun as an ordinary i-stem whose West Saxon development shows palatal diphthongization, while non-West-Saxon evidence preserves forms of the _gest_ type [@Campbell1959; @RingeTaylor2014].

#### Old English evidence

Bosworth-Toller and Clark Hall record the word under forms such as _gist_, _gest_, _giest_, and _gyst_ [@BosworthToller1898; @ClarkHall1960]. The selected target _ġiest_ is the normalized West Saxon form within that attested family.

#### Development to Old English

From _\*gástiz_, Anglo-Frisian brightening gives a _gæst-_ stage, and i-mutation affects the front vowel before the lost high-vocalic ending. In West Saxon the initial palatal environment then produces _ie_, so the regular outcome is _ġiest_ [@Campbell1959; @RingeTaylor2014].

#### Dialect note

West Saxon _ġiest_ is the selected target here. Anglian _gest_ and related spellings remain real Old English comparators rather than corrections to that choice [@RingeTaylor2014; @BosworthToller1898].

### hair — OE hǣr

Derivation: _\*xḗrą_ $\rightarrow$ _hǣr_ (regular).

#### Derivation trace

Proto input: _\*xḗrą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc Long E Lowering & \emph{*xǣrą} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Velar Fricative Palatalization & \emph{*çǣrą} \\
OE Heavy Syllable Nasal Apocope & \emph{*çǣr} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _hǣr_

#### Reconstruction and comparative evidence

Kroonen cites the ordinary Proto-Germanic hair word as _\*hēra-_ [@Kroonen2013]. The selected input _\*xḗrą_ represents that same long-ē stem in the present derivation.

#### Old English evidence

Clark Hall and Bosworth-Toller record _hær_ / _hǣr_ as the ordinary Old English noun 'hair' [@ClarkHall1960, 158; @BosworthToller1898, 510]. The target is therefore the attested headword itself.

#### Development to Old English

From _\*xḗrą_, Northwest Germanic lowering gives a long front vowel, and later loss of the final nasal leaves the Old English form _hǣr_. The development treated here is straightforward and does not require any special paradigm choice.

#### Form note

Older references to _\*xazwăz_ belong to a different lexeme, and the separate _haddr / heordan / hād-_ material does not displace the ordinary simplex _hǣr_ treated here [@Kroonen2013; @ClarkHall1960, 158].

### harvest — OE hierfest

Derivation: _\*xárbistuz_ $\rightarrow$ _hierfest_ (regular).

#### Derivation trace

Proto input: _\*xárbistuz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*xárbistu} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*xærbistu} \\
OE Breaking & \emph{*xearbistu} \\
OE Velar Fricative Palatalization & \emph{*çearbistu} \\
PGmc B Allophony & \emph{*çearβistu} \\
OE I Umlaut & \emph{*çierβistu} \\
OE High Vowel Apocope & \emph{*çierβist} \\
OE Med Unstressed I Lowering1 & \emph{*çierβest} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _hierfest_

#### Reconstruction and comparative evidence

Bammesberger and Ringe-Taylor treat _\*harbist-_ as the inherited base and explain that the regular native West Saxon development would be of the _hierfest / hyrfest_ type [@Bammesberger1997; @RingeTaylor2014].

#### Old English evidence

Bosworth-Toller and Clark Hall record _hærfest_, with _herfest_ as a variant in the lexical tradition [@BosworthToller1898; @ClarkHall1960]. Those attested forms remain the main dictionary evidence for the noun.

#### Development to Old English

From _\*xárbistuz_, Anglo-Frisian brightening, breaking, and i-mutation produce a _hierbist-_ stage, and later lowering of unstressed medial _i_ to _e_ gives _hierfest_. That is the regular West Saxon development treated here [@RingeTaylor2014; @Campbell1959].

#### Source note

The selected target _hierfest_ represents the regular native West Saxon outcome discussed by Bammesberger and Ringe-Taylor. The attested Old English lexical tradition, however, is chiefly _hærfest / herfest_, commonly treated as non-West-Saxon or Anglian material in West Saxon transmission [@Bammesberger1997; @RingeTaylor2014].

### hedge — OE heġġ

Derivation: _\*xágjaz_ $\rightarrow$ _heġġ_ (regular).

#### Derivation trace

Proto input: _\*xágjaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc J Gemination & \emph{*xággjaz} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*xággja} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Final Bare A Loss & \emph{*xággj} \\
Anglo Frisian Brightening & \emph{*xæggj} \\
OE Velar Fricative Palatalization & \emph{*çæggj} \\
OE Velar Palatalization & \emph{*çæʤʤj} \\
OE I Umlaut & \emph{*çeʤʤj} \\
OE J Loss After Heavy & \emph{*çeʤʤ} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _heġġ_

#### Reconstruction and comparative evidence

The selected input models a palatal _\*-gj-\*_ noun whose Old English development includes gemination, palatalization, and i-mutation. The current derivation therefore reaches a palatal-geminate outcome of the _heġġ_ type [@Campbell1959].

#### Old English evidence

Bosworth-Toller and Clark Hall record the noun under standard spellings _hecg_ / _heċġ_ [@BosworthToller1898; @ClarkHall1960]. The lexical item itself is therefore well attested even though the selected form is normalized.

#### Development to Old English

From _\*xágjaz_, West Germanic j-gemination first yields a geminate stop, and later Old English palatalization and loss of final _j_ produce _heġġ_. The development is treated as regular rather than exceptional.

#### Form note

Standard dictionary spelling is _heċġ_ or _hecg_. Normalized _heġġ_ is the selected target here, while the ordinary lexicographic forms remain the main Old English citation evidence [@BosworthToller1898; @ClarkHall1960].

### helm — OE helm

Derivation: _\*xélmaz_ $\rightarrow$ _helm_ (regular).

#### Derivation trace

Proto input: _\*xélmaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*xélma} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Final Bare A Loss & \emph{*xélm} \\
OE Velar Fricative Palatalization & \emph{*çélm} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _helm_

#### Reconstruction and comparative evidence

Kroonen cites the helmet noun as _\*helma-_ and separately distinguishes a different lexeme _\*helman-_ 'rudder' [@Kroonen2013]. The selected input _\*xélmaz_ is the nominative-style form used for the helmet noun itself.

#### Old English evidence

Clark Hall and Bosworth-Toller record _helm_ as the ordinary Old English noun for 'helmet', while _helma_ belongs to a separate rudder lexeme [@ClarkHall1960; @BosworthToller1898, 542].

#### Development to Old English

From _\*xélmaz_, loss of final _z_ and later loss of the short final vowel yield _helm_. The development is therefore a straightforward citation-form match.

#### Form note

Comparative _\*helma-_ is headword notation for the helmet cognate set. It should not be confused with Old English _helma_, which is a different noun meaning 'helm, rudder' [@Kroonen2013; @ClarkHall1960].

### help — OE helpan

Derivation: _\*xélpaną_ $\rightarrow$ _helpan_ (regular).

#### Derivation trace

Proto input: _\*xélpaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Velar Fricative Palatalization & \emph{*çélpaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*çélpan} \\
OE Secondary Nasalization & \emph{*çélpąn} \\
OE Weak Tail Reduction & \emph{*çélpan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _helpan_

#### Reconstruction and comparative evidence

The entry treats the strong verb itself rather than the separate noun _help_. Bright's principal parts _helpan, healp, hulpon, holpen_ show the ordinary Old English strong-verb family continued by this input [@BrightCassidyRingler1971].

#### Old English evidence

Clark Hall and Bosworth-Toller record _helpan_ as the verbal headword 'to help' [@ClarkHall1960; @BosworthToller1898, 542]. The target is therefore the attested infinitive citation form.

#### Development to Old English

From _\*xélpaną_, no special repair is needed beyond the ordinary reduction of the infinitive ending. The derivation therefore reaches _helpan_ directly.

#### Form note

Noun _help_ belongs to a separate lexical line and should not replace verbal _helpan_ as the target here [@ClarkHall1960; @BosworthToller1898, 542].

### hind — OE hind

Derivation: _\*xéndjō_ $\rightarrow$ _hind_ (regular).

#### Derivation trace

Proto input: _\*xéndjō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc Final Long O Raising & \emph{*xéndju} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Velar Fricative Palatalization & \emph{*çéndju} \\
OE I Umlaut & \emph{*çindju} \\
OE High Vowel Apocope & \emph{*çindj} \\
OE J Loss After Heavy & \emph{*çind} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _hind_

#### Reconstruction and comparative evidence

Kroonen cites the animal name as _\*hindō-_ f. 'hind' [@Kroonen2013]. The selected input _\*xéndjō_ represents that same noun in the present derivation.

#### Old English evidence

Clark Hall and Bosworth-Toller record _hind_ as the noun 'hind, female deer' [@ClarkHall1960; @BosworthToller1898, 554]. The target is therefore the attested lexical item itself.

#### Development to Old English

From _\*xéndjō_, i-mutation produces the front-vocalic Old English stem, and later apocope plus loss of final _j_ yield _hind_. The outcome is therefore a regular citation-form derivation.

#### Form note

_hindan_ 'from behind, behind' is a different Old English lexeme and does not belong to the noun history of _hind_ [@ClarkHall1960; @BosworthToller1898, 554].

### hold — OE healdan

Derivation: _\*xáldaną_ $\rightarrow$ _healdan_ (regular).

#### Derivation trace

Proto input: _\*xáldaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*xældaną} \\
OE Breaking & \emph{*xealdaną} \\
OE Velar Fricative Palatalization & \emph{*çealdaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*çealdan} \\
OE Secondary Nasalization & \emph{*çealdąn} \\
OE Weak Tail Reduction & \emph{*çealdan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _healdan_

#### Reconstruction and comparative evidence

Campbell and Ringe-Taylor treat the verb as a regular _\*a + lC_ breaking case, with West Saxon _healdan_ opposed to Anglian and Mercian _haldan_ [@Campbell1959; @RingeTaylor2014].

#### Old English evidence

Bright gives the ordinary strong-verb citation form and principal parts _healdan, heold, heoldon, healden_ [@BrightCassidyRingler1971]. The target is therefore the attested infinitive headword itself.

#### Development to Old English

From _\*xáldaną_, Anglo-Frisian brightening first yields a fronted vowel, and West Saxon breaking then produces _ea_ before _ld_. Later reduction of the infinitive ending gives _healdan_ [@Campbell1959; @RingeTaylor2014].

#### Dialect note

West Saxon _healdan_ is the selected target here. Anglian and Mercian _haldan_ are genuine non-West-Saxon doublets rather than corrections to that choice [@Campbell1959; @RingeTaylor2014].

### horn — OE horn

Derivation: _\*xúrną_ $\rightarrow$ _horn_ (regular).

#### Derivation trace

Proto input: _\*xúrną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc U Lowering & \emph{*xórną} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*xórn} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _horn_

#### Reconstruction and comparative evidence

Kroonen and Orel cite lemma-style Proto-Germanic headwords of the _\*hurna- / \*xurnan_ type for this noun [@Kroonen2013; @Orel2003, 234]. The selected input _\*xúrną_ is the nominative-style form used in the derivation here.

#### Old English evidence

Clark Hall, Bosworth-Toller, and Bright all record _horn_ as the ordinary Old English noun [@ClarkHall1960; @BosworthToller1898, 108; @BrightCassidyRingler1971]. The target is therefore the attested citation form.

#### Development to Old English

From _\*xúrną_, Northwest Germanic u-lowering gives _\*xórną_, and later loss of the final nasal leaves _horn_. The development treated here is fully regular.

#### Form note

The note's oblique _\*xurnăn_ belongs to comparative stem background only. It does not replace the selected input _\*xúrną_ as the derivational form used here [@Kroonen2013; @Orel2003, 234].

### lead — OE lǣdan

Derivation: _\*láidijaną_ $\rightarrow$ _lǣdan_ (regular).

#### Derivation trace

Proto input: _\*láidijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Ai Monophthongization & \emph{*lādijaną} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*lādijan} \\
OE Secondary Nasalization & \emph{*lādijąn} \\
Sievers Law Syncope & \emph{*lādjąn} \\
OE I Umlaut & \emph{*lǣdjąn} \\
OE Weak Tail Reduction & \emph{*lǣdjan} \\
OE J Loss After Heavy & \emph{*lǣdan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _lǣdan_

#### Reconstruction and comparative evidence

Ringe and Taylor derive Old English _lǣdan_ from Proto-Germanic _\*laidijaną_, and Kroonen likewise cites a weak verb of the _\*laidjan-_ type for 'lead' [@RingeTaylor2014; @Kroonen2013, 363].

#### Old English evidence

Clark Hall and Bosworth-Toller both record _lædan_ / _lǣdan_ as the ordinary Old English verb 'to lead, guide, conduct' [@ClarkHall1960; @BosworthToller1898].

#### Development to Old English

From _\*láidijaną_, monophthongization of _\*ai_ first gives a _\*lād-_ stage. Later syncope, i-mutation, weak-tail reduction, and loss of _j_ after a heavy stem yield _lǣdan_, so the development represented here is fully regular [@RingeTaylor2014].

### learn — OE liornian

Derivation: _\*líznōjaną_ $\rightarrow$ _liornian_ (regular).

#### Derivation trace

Proto input: _\*líznōjaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Breaking & \emph{*líornōjaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*líornōjan} \\
OE Secondary Nasalization & \emph{*líornōjąn} \\
OE I Umlaut & \emph{*líornējąn} \\
OE Unstressed Long Vowel Shortening & \emph{*líornejąn} \\
OE Weak Tail Reduction & \emph{*líornejan} \\
OE Intervocalic J Vocalization & \emph{*líorneian} \\
OE Unstressed EI Contraction & \emph{*líornian} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _liornian_

#### Reconstruction and comparative evidence

Ringe and Taylor place the verb in a class-II weak family of the _\*liznō-_
type [@RingeTaylor2014], and Kroonen keeps the same comparative base for the
Germanic lexeme [@Kroonen2013]. The selected input therefore requires no change
of stem class or paradigm cell.

The non-obvious issue is dialectal. Campbell records Northumbrian _liornian_
beside _leornian_, and he states that the _eo_ of _leornian_ is secondary,
while Northumbrian preserves forms with _io_, where original _eo_ and _io_
remain distinct [@Campbell1959, §123 n. 2].

#### Old English evidence

The form modeled here is _liornian_, the Northumbrian member of the Old
English family. Dictionary practice more often privileges _leornian_ as the
ordinary headword [@ClarkHall1960; @BrightCassidyRingler1971], but Campbell's
dialect evidence shows that _liornian_ is a genuine Old English form
[@Campbell1959, §123 n. 2].

This entry therefore remains compact. The point is to state clearly that the
selected target belongs to the Northumbrian side of the OE evidence rather than
to the leveled _leornian_ headword tradition.

#### Development to Old English

From _\*líznōjaną_, the expected Old English developments include rhotacism of
_z_, followed by breaking before _r_ plus consonant, and the ordinary reduction
of the weak verbal ending. The result is _liornian_, preserving the _io_
spelling that Campbell associates with Northumbrian where original _eo_ and
_io_ remain distinct [@Campbell1959, §123 n. 2].

_Leornian_ reflects the later _eo_ development that Campbell treats as
secondary [@Campbell1959, §123 n. 2; §296]. The selected Northumbrian target is
therefore the regular comparison form for the _i_-grade member of the family.

#### Form comparison

The comparison below is manual. It distinguishes the regular Northumbrian form
modeled here from the better-known West Saxon headword.

| Form | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _\*líznōjaną -> liornian_ | computed regular output; attested Northumbrian comparison form | selected comparison |
| _leornian_ | attested later _eo_ form and dictionary headword | useful control, but not the target of this entry |

### lid — OE hlid

Derivation: _\*xlídą_ $\rightarrow$ _hlid_ (regular).

#### Derivation trace

Proto input: _\*xlídą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*xlíd} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _hlid_

#### Reconstruction and comparative evidence

Orel cites a neuter lexeme of the _\*xliđ-_ type with Old English _hlid_, and Lloyd includes OE _hlid_ beside ON _hliþó_ and OHG _(h)lit_ among forms that retain _i_ [@Orel2003; @Lloyd1966].

#### Old English evidence

Clark Hall and Bosworth-Toller record _hlid_ as the noun 'lid, cover, door, gate' [@ClarkHall1960; @BosworthToller1898, 563].

#### Development to Old English

The selected input already represents the later Germanic _hliđ-_ stage used for the derivation here. From _\*xlídą_, heavy-syllable apocope yields _hlid_, and the form belongs to the retained-_i_ set noted by Lloyd rather than to the lowered _e_ type [@Lloyd1966].

#### Form note

An earlier etymological stage _\*liþuz_ belongs to comparative background only. The form represented here is the later _\*xlídą > hlid_ line that matches the attested Old English noun [@Orel2003; @Lloyd1966].

### light — OE līehtan

Derivation: _\*léuxtijaną_ $\rightarrow$ _līehtan_ (regular).

#### Derivation trace

Proto input: _\*léuxtijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Diphthong Leveling & \emph{*lēoxtijaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*lēoxtijan} \\
OE Secondary Nasalization & \emph{*lēoxtijąn} \\
Sievers Law Syncope & \emph{*lēoxtjąn} \\
OE I Umlaut & \emph{*līextjąn} \\
OE Weak Tail Reduction & \emph{*līextjan} \\
OE J Loss After Heavy & \emph{*līextan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _līehtan_

#### Reconstruction and comparative evidence

Fulk gives Proto-Germanic _\*liuxtijanan_ with Old English _līehtan_ 'illuminate', and Ringe and Taylor likewise derive West Saxon _liehtan_ from the same weak-verb formation [@Fulk2018; @RingeTaylor2014].

#### Old English evidence

Clark Hall and Bosworth-Toller preserve the verb family under spellings such as _liehtan_, _lihtan_, and _līhtan_, distinct from the related noun _lēoht_ and adjective _leoht/liht_ [@ClarkHall1960; @BosworthToller1898].

#### Development to Old English

From _\*léuxtijaną_, the regular verbal line preserves _\*xt_, passes through a West Saxon _liehtan_ stage, and is represented here by normalized _līehtan_. The word treated in this entry is therefore the verb 'to light, illuminate', not the related noun from _\*leuxtą_ [@Fulk2018; @RingeTaylor2014].

#### Dialect note

Ringe and Taylor and Campbell distinguish West Saxon _liehtan_ from Anglian _lihtan_, while later West Saxon also shows _lyhtan_ [@RingeTaylor2014; @Campbell1959].

### linden — OE lind

Derivation: _\*líndō_ $\rightarrow$ _lind_ (regular).

#### Derivation trace

Proto input: _\*líndō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc Final Long O Raising & \emph{*líndu} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE High Vowel Apocope & \emph{*línd} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _lind_

#### Reconstruction and comparative evidence

Kroonen cites _\*lindō-_ 'lime tree' and gives Old English _lind_ as the relevant reflex [@Kroonen2013].

#### Old English evidence

Clark Hall and Bosworth-Toller both record _lind_ as the noun 'lime-tree, linden' [@ClarkHall1960; @BosworthToller1898, 630].

#### Development to Old English

From _\*líndō_, Northwest Germanic final _\*ō_ raising first gives a _\*líndu_ stage, and later high-vowel apocope yields _lind_. The development is therefore straightforward and regular.

#### Form note

The Old English noun represented here is _lind_. Clark Hall also has a separate adjectival _linden_ 'made of linden-wood', but that is not the noun counterpart for this entry [@ClarkHall1960].

### milk — OE meoloc

Derivation: _\*mélukz_ $\rightarrow$ _meoloc_ (regular).

#### Derivation trace

Proto input: _\*mélukz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*méluk} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Med Unstressed U Lowering & \emph{*mélok} \\
OE Back Mutation & \emph{*méolok} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _meoloc_

#### Reconstruction and comparative evidence

Kroonen and Orel reconstruct the noun as _\*meluk- / \*melukz_, and the nominative-style input used here is _\*mélukz_ [@Kroonen2013; @Orel2003, 306].

#### Old English evidence

Old English preserves a mixed dossier for this noun. Ringe and Taylor describe West Saxon _meolc < meoluc < \*meluk_, Campbell likewise discusses _meoluc_ and _meoloc_, and Anglian shows _milc_ [@RingeTaylor2014; @Campbell1959].

#### Development to Old English

The unsyncopated line from _\*mélukz_ loses final _\*z_, lowers unstressed _u_ to _o_, and with back mutation yields _meoloc_. That fuller unsyncopated outcome is the form represented here [@RingeTaylor2014].

#### Form comparison

Syncopated _meolc_ and Anglian _milc_ belong to the competing leveled tradition associated with oblique forms, whereas _meoloc / meoluc_ preserves the fuller nominal shape [@Campbell1959; @RingeTaylor2014].

### mother — OE mōder

Derivation: _\*mōdēr_ $\rightarrow$ _mōder_ (regular).

#### Derivation trace

Proto input: _\*mōdēr_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc Long E Lowering & \emph{*mōdǣr} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Unstressed Long Vowel Shortening & \emph{*mōdær} \\
OE Unstressed AE Merger & \emph{*mōder} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _mōder_

#### Reconstruction and comparative evidence

Kroonen and Orel cite the Proto-Germanic r-stem kinship noun as _\*mōder- / \*mōdēr_ [@Kroonen2013; @Orel2003].

#### Old English evidence

The transmitted Old English headword tradition is _mōdor / modor_, with oblique _mēder_ in the paradigm. Clark Hall, Campbell, and Ringe and Taylor all preserve that contrast [@ClarkHall1960; @Campbell1959; @RingeTaylor2014].

#### Development to Old English

From _\*mōdēr_, the regular suffixal development yields _mōder_. That regular nominative reflex is the form represented here, while the more familiar citation form _mōdor_ reflects later levelling within the r-stem paradigm [@Campbell1959; @RingeTaylor2014].

#### Form comparison

The note therefore concerns inherited vocalism rather than a different lexeme: _mōder_ is the regularized nominative represented here, but dictionaries usually print _mōdor / modor_, and the oblique evidence survives in _mēder_ [@ClarkHall1960; @RingeTaylor2014].

### net — OE nett

Derivation: _\*nátją_ $\rightarrow$ _nett_ (regular).

#### Derivation trace

Proto input: _\*nátją_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc J Gemination & \emph{*náttją} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*nættją} \\
OE Heavy Syllable Nasal Apocope & \emph{*nættj} \\
OE I Umlaut & \emph{*nettj} \\
OE J Loss After Heavy & \emph{*nett} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _nett_

#### Reconstruction and comparative evidence

Orel gives _\*natjan_ with Old English _nett_, and Fulk's account of West Germanic gemination before _j_ explains the geminate outcome after a short vowel [@Orel2003; @Fulk2018].

#### Old English evidence

Clark Hall and Bosworth-Toller record _nett_ as the noun, and Campbell notes that final geminates are often graphically simplified in Old English spelling [@ClarkHall1960; @BosworthToller1898, 29; @Campbell1959].

#### Development to Old English

From _\*nátją_, West Germanic j-gemination first gives _\*náttją_. Later brightening, loss of the weak ending, and loss of final _j_ after a heavy stem yield _nett_, so the development represented here is regular [@Fulk2018].

#### Form note

Spellings in _net_ can therefore be graphic simplifications, but the lexical target supported by the dictionary evidence is _nett_ [@Campbell1959; @Orel2003].

### nightmare — OE mare

Derivation: _\*márōn_ $\rightarrow$ _mare_ (regular).

#### Derivation trace

Proto input: _\*márōn_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc N Stem N Loss & \emph{*márǭ} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*mærǭ} \\
OE A Restoration & \emph{*marǭ} \\
OE Unstressed Long Vowel Shortening & \emph{*maræ} \\
OE Unstressed AE Merger & \emph{*mare} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _mare_

#### Reconstruction and comparative evidence

Ringe and Taylor treat the lexeme as Proto-Germanic / Proto-Northwest-Germanic _\*marōn-_, with Old English _mare, maran_, and variant _mere_; Orel preserves the same comparative lemma though with a different Old English headword tradition [@RingeTaylor2014; @Orel2003].

#### Old English evidence

Clark Hall records _mare_ 'nightmare, monster' and also preserves related variant forms _mera / mere_ [@ClarkHall1960, 213].

#### Development to Old English

The selected simplex input _\*márōn_ regularly gives _mare_ after brightening, A-restoration before the n-stem ending, and later reduction of the final vowel. The word represented here is the attested simplex noun, not an attested compound [@RingeTaylor2014].

#### Form note

The concept corresponds to an unattested compound _\*nihtmare_, but the Old English lexical evidence is for simplex _mare_, with oblique _maran_ and variant _mere / mera_ [@RingeTaylor2014; @ClarkHall1960, 213].

### coat — OE rocc

Derivation: _\*rúkkaz_ $\rightarrow$ _rocc_ (regular).

#### Derivation trace

Proto input: _\*rúkkaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc U Lowering & \emph{*rókkaz} \\
PGmc Final Z Deletion & \emph{*rókka} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Final Bare A Loss & \emph{*rókk} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _rocc_

#### Reconstruction and comparative evidence

Orel cites a masculine _\*rukkaz_ for the garment word, while Kroonen gives _\*hrukka-_. Both treat this as the garment lexeme and not as the separate stone word [@Orel2003; @Kroonen2013, 290].

#### Old English evidence

Clark Hall and Bosworth-Toller record _rocc_ as an over-garment or tunic and preserve compounds such as _bisceoprocc_ and _breóstrocc_ [@ClarkHall1960; @BosworthToller1898].

#### Development to Old English

With _\*rúkkaz_ as the selected input, Northwest Germanic u-lowering and later loss of final _-a_ yield _rocc_ as a regular outcome.

#### Source note

This entry concerns the garment noun only. The stone word seen in _stānrocc_ belongs to a different lexical history [@ClarkHall1960; @BosworthToller1898].

### sheep — OE sċēap

Derivation: _\*skḗpą_ $\rightarrow$ _sċēap_ (regular).

#### Derivation trace

Proto input: _\*skḗpą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc Long E Lowering & \emph{*skǣpą} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*skǣp} \\
OE Sk Palatalization & \emph{*ʃǣp} \\
OE Ws Palatal Diphthongization & \emph{*ʃēap} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _sċēap_

#### Reconstruction and comparative evidence

Ringe and Taylor cite a later West Germanic _\*skap > WS scéap_, while Orel preserves a Proto-Germanic noun of the _\*skēp-_ type for the same lexeme [@RingeTaylor2014; @Orel2003].

#### Old English evidence

Clark Hall records _scēap_ with spelling variation, and Campbell likewise lists West Saxon _scéap_ among the palatal-diphthongized forms [@ClarkHall1960; @Campbell1959].

#### Development to Old English

From _\*skḗpą_, Northwest Germanic lowering gives _\*skǣpą_; after apocope and palatalization the West Saxon branch diphthongizes to _sċēap_. The development represented here is therefore fully regular.

#### Dialect note

Ringe and Taylor contrast West Saxon _scéap_ with Mercian and Kentish _scép_, and Campbell also notes Northumbrian _scip_. The form represented here is the West Saxon headword [@RingeTaylor2014; @Campbell1959].

### shilling — OE sċilling

Derivation: _\*skíllingaz_ $\rightarrow$ _sċilling_ (regular).

#### Derivation trace

Proto input: _\*skíllingaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*skíllinga} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Final Bare A Loss & \emph{*skílling} \\
OE Sk Palatalization & \emph{*ʃílling} \\
OE Med Unstressed I Lowering1 & \emph{*ʃílleng} \\
OE Med Unstressed I Lowering & \emph{*ʃílling} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _sċilling_

#### Reconstruction and comparative evidence

Kroonen treats the cognate set under _\*skellinga- ~ \*skillinga-_ and connects it with _\*skeld-linga-_, while Orel likewise gives the coin word with OE _scilling_ among the reflexes [@Kroonen2013; @Orel2003]. The selected input _\*skíllingaz_ is the nominative-style form used here to represent that inherited _\*-ing-_ derivative.

#### Old English evidence

Clark Hall records _scilling_, and Campbell cites _scilling_ among nouns whose derivational _-ing_ keeps _i_ in unstressed syllables [@ClarkHall1960; @Campbell1959]. The target represented here is the ordinary OE citation form, normalized as _sċilling_.

#### Development to Old English

From _\*skíllingaz_, loss of final _-az_ yields _\*skílling_. Old English palatalization of initial _sk_ before front vocalism then gives _sċilling_. The note matters because derivational _-ing-_ keeps _i_, so the regular outcome is _sċilling_, not _\*sċilleng_ [@Campbell1959; @Hogg1992].

#### Form note

Kroonen's _\*skellinga- ~ \*skillinga-_ and his internal analysis _\*skeld-linga-_ belong to the etymological background of the cognate set. The selected input _\*skíllingaz_ is the specific form used for the derivation represented here [@Kroonen2013].

### show — OE sċēawian

Derivation: _\*skáwōjaną_ $\rightarrow$ _sċēawian_ (regular).

#### Derivation trace

Proto input: _\*skáwōjaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Aw Long Diphthong & \emph{*skḗawōjaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*skḗawōjan} \\
OE Secondary Nasalization & \emph{*skḗawōjąn} \\
OE Sk Palatalization & \emph{*ʃḗawōjąn} \\
OE I Umlaut & \emph{*ʃḗawējąn} \\
OE Unstressed Long Vowel Shortening & \emph{*ʃḗawejąn} \\
OE Weak Tail Reduction & \emph{*ʃḗawejan} \\
OE Intervocalic J Vocalization & \emph{*ʃḗaweian} \\
OE Unstressed EI Contraction & \emph{*ʃḗawian} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _sċēawian_

#### Reconstruction and comparative evidence

Orel and Kroonen cite a Class II verb of the type _\*skawōjan-_, with OE _scēawian_ among the reflexes [@Orel2003; @Kroonen2013, 482]. Brunner likewise records the Old English family as _scēawian, scāwian_, which places this entry in the ordinary show-verb set rather than in a special finite-cell workaround [@SieversBrunner1965].

#### Old English evidence

Bright lists _scēawian (W. II.)_ and also the related form _scēawa_ [@BrightCassidyRingler1971]. The source tradition therefore uses _scēawian_, while the target represented here is the normalized project spelling _sċēawian_.

#### Development to Old English

From _\*skáwōjaną_, Old English _aw_ before a following vowel yields _ēaw_, and the Class II suffix keeps _\*ō_ between _\*w_ and _\*j_. The development therefore runs regularly to _sċēawian_, without the direct _\*aw+j_ problem seen in other verb types [@Campbell1959; @Orel2003].

#### Form note

The difference between _scēawian_ and _sċēawian_ is orthographic normalization of initial _<sc>_, not a difference of lexeme or paradigm cell [@Campbell1959; @Hogg1992].

### sleep — OE slǣpan

Derivation: _\*slḗpaną_ $\rightarrow$ _slǣpan_ (regular).

#### Derivation trace

Proto input: _\*slḗpaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc Long E Lowering & \emph{*slǣpaną} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*slǣpan} \\
OE Secondary Nasalization & \emph{*slǣpąn} \\
OE Weak Tail Reduction & \emph{*slǣpan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _slǣpan_

#### Reconstruction and comparative evidence

Kroonen preserves the comparative verb as _\*slēpan-_, and Fulk cites the same family under root _\*slēb-_ [@Kroonen2013; @Fulk2018, 120]. The selected input _\*slḗpaną_ is the infinitive-style form used here for that inherited sleep-verb.

#### Old English evidence

Clark Hall gives _slæpan_ with preterite _slēp, slēap_, and Bright likewise lists _slæpan (slāpan), slēp slēpon slēpen_ [@ClarkHall1960; @BrightCassidyRingler1971, 435]. The target represented here is therefore the normalized infinitive _slǣpan_, not the preterite forms and not the separate noun _slǣp_.

#### Development to Old English

From _\*slḗpaną_, Northwest Germanic lowering gives _\*slǣpaną_. The later OE tail developments then yield _slǣpan_ regularly. Brunner and Bülbring show that the OE tradition also has variant spellings such as West Saxon _slāpan/slæpan_ and Anglian or Kentish _slēpan_, but those do not displace the infinitive chosen here [@SieversBrunner1965; @Bulbring1902].

#### Form note

The note concerns lemma type rather than a special derivational problem: this row represents the verb _slǣpan_, whereas _slǣp_ belongs to noun or lookup background and _slēp/slēap_ are preterite forms [@ClarkHall1960; @BrightCassidyRingler1971, 435].

### smear — OE smierwan

Derivation: _\*smérwijaną_ $\rightarrow$ _smierwan_ (regular).

#### Derivation trace

Proto input: _\*smérwijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Breaking & \emph{*sméorwijaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*sméorwijan} \\
OE Secondary Nasalization & \emph{*sméorwijąn} \\
Sievers Law Syncope & \emph{*sméorwjąn} \\
OE I Umlaut & \emph{*smíerwjąn} \\
OE Weak Tail Reduction & \emph{*smíerwjan} \\
OE J Loss After Heavy & \emph{*smíerwan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _smierwan_

#### Reconstruction and comparative evidence

Kroonen gives the comparative headword as _\*smerwjan-_ [@Kroonen2013]. Ringe and Taylor instead cite a later-stage _\*smirwijana_, from which they derive West Saxon _smierwan_, Mercian _smirwan_, and Northumbrian _smiriga_ [@RingeTaylor2014]. The selected input _\*smérwijaną_ therefore represents the Kroonen-aligned PGmc layer, while the later-stage dialect split belongs to a different chronological level.

#### Old English evidence

The target represented here is the West Saxon citation form _smierwan_. Campbell's Anglian discussion explains the contrasting _smirwan_, and Clark Hall, Brunner, and Bright show that the same lexical family later also includes forms such as _smirian_, _smyrian_, and preterite _smyrode_ [@Campbell1959; @ClarkHall1960; @SieversBrunner1965; @BrightCassidyRingler1971].

#### Development to Old English

From _\*smérwijaną_, breaking before _r + consonant_ yields _eo_, and later i-umlaut produces _ie_. The result is West Saxon _smierwan_. Anglian _smirwan_ reflects the well-known failure of breaking in this environment, not a different lexeme [@Campbell1959; @RingeTaylor2014].

#### Dialect note

The entry therefore represents the West Saxon member of a broader OE family: _smierwan_ in West Saxon, _smirwan_ in Anglian or Mercian, and related later class-II forms such as _smirian_ or _smyrian_ in the same lexical field [@RingeTaylor2014; @ClarkHall1960].

### span — OE spannan

Derivation: _\*spánnaną_ $\rightarrow$ _spannan_ (regular).

#### Derivation trace

Proto input: _\*spánnaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*spánnan} \\
OE Secondary Nasalization & \emph{*spánnąn} \\
OE Weak Tail Reduction & \emph{*spánnan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _spannan_

#### Reconstruction and comparative evidence

Kroonen cites the inherited verb as _\*spannan-_, with OE _spannan_ among the reflexes [@Kroonen2013]. The selected input _\*spánnaną_ is the infinitive-style form used here for that same verbal lexeme.

#### Old English evidence

Clark Hall keeps noun _spann_ and verb _spannan_ separate, and Brunner likewise records _sponnan, spannan stv._ [@ClarkHall1960; @SieversBrunner1965]. This entry treats the strong-verb infinitive, not the separate noun.

#### Development to Old English

From _\*spánnaną_, the final nasal ending is lost and the regular OE weak-tail steps surface _spannan_. No paradigm-cell substitution is needed: the current derivation already lands on the infinitive directly.

#### Form note

The note matters because English _span_ can also reach noun _spann_ in local lookup material. The entry represented here is the verb _spannan_, with the noun treated elsewhere [@ClarkHall1960].

### spar — OE spearra

Derivation: _\*spárrô_ $\rightarrow$ _spearra_ (regular).

#### Derivation trace

Proto input: _\*spárrô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*spærrô} \\
OE Breaking & \emph{*spearrô} \\
OE Unstressed Long Vowel Shortening & \emph{*spearra} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _spearra_

#### Reconstruction and comparative evidence

Kroonen and Orel place this noun in the beam or rafter set _\*spar(r)an-_, with cognates such as Old Saxon and Old High German _sparro_ [@Kroonen2013; @Orel2003]. The selected input _\*spárrô_ is the OE-facing nominal form used here for that same lexeme.

#### Old English evidence

The noun represented here is _spearra_. The important lexical point is negative: English gloss overlap also reaches the unrelated verb _sperran_ 'to bar', but that verb does not belong to this row.

#### Development to Old English

From _\*spárrô_, Anglo-Frisian brightening gives _\*spærrô_, and OE breaking before geminate _rr_ yields _\*spearrô_, later _spearra_. The development is therefore regular for a breaking-conditioned noun of this type [@Luick1914].

#### Form note

This entry concerns the noun _spearra_ only. It should be kept separate from verb _sperran_, even though the Modern English glosses overlap [@Kroonen2013; @Orel2003].

### still — OE stillan

Derivation: _\*stéllijaną_ $\rightarrow$ _stillan_ (regular).

#### Derivation trace

Proto input: _\*stéllijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*stéllijan} \\
OE Secondary Nasalization & \emph{*stéllijąn} \\
Sievers Law Syncope & \emph{*stélljąn} \\
OE I Umlaut & \emph{*stilljąn} \\
OE Weak Tail Reduction & \emph{*stilljan} \\
OE J Loss After Heavy & \emph{*stillan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _stillan_

#### Reconstruction and comparative evidence

The wider West Germanic family includes adjective _still_ and verb _stillen_ [@KlugeSeebold2011]. The selected input _\*stéllijaną_ represents the verbal j-formation used for the OE row.

#### Old English evidence

Clark Hall gives _stillan_ as the verb and separately _stille_ as the adjective [@ClarkHall1960]. Bosworth-Toller likewise preserves a substantial prefixed verbal family under _ge-stillan_ and related forms [@BosworthToller1898, 724]. The selected target is the verb _stillan_, not the adjective.

#### Development to Old English

As a heavy-stem Class I weak verb, _\*stéllijaną_ undergoes the expected syncope and i-umlaut, and later loss of _j_ after a heavy stem yields _stillan_. The development represented here is regular.

#### Form note

The note concerns lexical framing rather than sound law: _stillan_ is the verb represented here, while _stille_ belongs to the related adjectival branch of the family [@ClarkHall1960; @KlugeSeebold2011].

### summer — OE sumer

Derivation: _\*súmaraz_ $\rightarrow$ _sumer_ (regular).

#### Derivation trace

Proto input: _\*súmaraz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*súmara} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Final Bare A Loss & \emph{*súmar} \\
Anglo Frisian Brightening & \emph{*súmær} \\
OE Unstressed AE Merger & \emph{*súmer} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _sumer_

#### Reconstruction and comparative evidence

Kroonen gives the lexeme as _\*sumara-_, and Ringe and Taylor likewise use _\*sumaraz_, while Orel preserves an alternate _\*sumeraz_ [@Kroonen2013; @RingeTaylor2014; @Orel2003, 425]. The selected input _\*súmaraz_ follows the _\*a_ vocalism that underlies the regular development represented here.

#### Old English evidence

Clark Hall gives _sumor m., gs. sumeres, ds. sumera, sumere_, and Bright likewise lists _sumor (sumer)_ with genitive _sumeres_ [@ClarkHall1960; @BrightCassidyRingler1971, 440]. The tradition therefore preserves both _sumor_ and _sumer_, with the oblique forms strongly supporting second-syllable _e_.

#### Development to Old English

From _\*súmaraz_, loss of final _-az_ is followed by fronting and merger in the unstressed second syllable, yielding _sumer_. The selected form is the regularized _e_-form, while the common citation form _sumor_ remains part of the attested OE tradition [@RingeTaylor2014].

#### Form note

The entry does not deny _sumor_. It represents _sumer_ as the regular outcome chosen here, while _sumor_ remains a common headword spelling and _sumeres/sumere_ show that the _e_-vocalism was also real in Old English [@ClarkHall1960; @BrightCassidyRingler1971, 440].

### sunder — OE sundrian

Derivation: _\*súndrōjaną_ $\rightarrow$ _sundrian_ (regular).

#### Derivation trace

Proto input: _\*súndrōjaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*súndrōjan} \\
OE Secondary Nasalization & \emph{*súndrōjąn} \\
OE I Umlaut & \emph{*súndrējąn} \\
OE Unstressed Long Vowel Shortening & \emph{*súndrejąn} \\
OE Weak Tail Reduction & \emph{*súndrejan} \\
OE Intervocalic J Vocalization & \emph{*súndreian} \\
OE Unstressed EI Contraction & \emph{*súndrian} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _sundrian_

#### Reconstruction and comparative evidence

Orel distinguishes three related formations: adverbial _\*sunþraz > sundor_, Class I verbal _\*sunþrjanan > syndrian_, and Class II verbal _\*sunþrōjanan > sundrian_ [@Orel2003]. Kluge-Seebold aligns the cognate set with German _sondern_ and OE _gesundrian_, so this entry belongs with the Class II verb, not the adverb [@KlugeSeebold2011].

#### Old English evidence

Clark Hall and Bosworth-Toller keep _sundrian_ and _syndrian_ separate from adverbial _sundor_, and both preserve the prefixed verbal family _ā-sundrian_ [@ClarkHall1960, 296; @BosworthToller1898]. The target represented here is therefore the weak verb _sundrian_.

#### Development to Old English

From _\*súndrōjaną_, the Class II weak-verb suffix yields regular OE _-ian_, producing _sundrian_. Because this is the _\*-ōjan-_ verb and not the Class I _\*-jan-_ formation, the form represented here does not belong to the umlauted _syndrian_ branch.

#### Form note

The earlier confusion was lexical, not phonological: _sundor_ is the separate adverb, and _syndrian_ is a related but different verb. The verb treated here is the Class II verb _sundrian_ [@Orel2003; @ClarkHall1960, 296].

### swallow — OE swealwe

Derivation: _\*swálwōn_ $\rightarrow$ _swealwe_ (regular).

#### Derivation trace

Proto input: _\*swálwōn_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc N Stem N Loss & \emph{*swálwǭ} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*swælwǭ} \\
OE Breaking & \emph{*swealwǭ} \\
OE Unstressed Long Vowel Shortening & \emph{*swealwæ} \\
OE Unstressed AE Merger & \emph{*swealwe} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _swealwe_

#### Reconstruction and comparative evidence

Kroonen gives the bird name as _\*swalwōn-_, and Ringe and Taylor cite the later West Germanic stage _\*swalwa_, from which West Saxon _swealwe_ and Mercian _swalwe_ develop [@Kroonen2013, 535; @RingeTaylor2014, 200]. The selected etymological comparison belongs to the swallow-bird family, not to the verb _swelgan_.

#### Old English evidence

Clark Hall records _swealwe (a, o)_ as the noun headword [@ClarkHall1960]. Campbell and Brunner also preserve later or oblique-family forms such as _swaluwe_, _swalewan_, and _swealuwe_, but those belong to wider variation around the noun rather than to the citation form represented here [@Campbell1959; @SieversBrunner1965].

#### Development to Old English

From _\*swálwōn_, brightening yields _\*swælw-_, and breaking before _lw_ gives _\*swealw-_. The later noun ending develops regularly to _swealwe_. The relevant point is that the bird name has no inherited _\*g_: that consonant belongs to the separate verb _swelgan_ [@RingeTaylor2014, 200; @Kroonen2013, 535].

#### Form note

The final prose keeps the citation form _swealwe_ separate from two different kinds of background material: the unrelated verb _swelgan_, and later or oblique spellings such as _swaluwe_ or _swalewan_ [@ClarkHall1960; @Campbell1959].

### swine — OE swīn

Derivation: citation reconstruction _\*swī́ną_; selected input _\*swḯną_ $\rightarrow$ _swīn_ (regular).

#### Derivation trace

Proto input: _\*swḯną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*swḯn} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _swīn_

#### Reconstruction and comparative evidence

Kroonen cites the noun as _\*swina-_ 'pig' [@Kroonen2013]. The selected comparative form here is the bare neuter citation cell _\*swī́ną_, which matches the singular noun aimed at in Old English rather than an oblique stem form.

#### Old English evidence

Clark Hall records _swin (y)_ as the ordinary noun headword [@ClarkHall1960]. The target here is that singular citation form _swīn_, not a plural glossed in Modern English as *swine*.

#### Development to Old English

From selected input _\*swḯną_, loss of the final nasal vowel yields _swīn_. The outcome is therefore the regular monosyllabic noun with preserved long root _ī_.

#### Source note

The selected input writes stressed long _ī_ as _\*ḯ_, so comparative _\*swī́ną_ and derivational _\*swḯną_ represent the same lexical form.

### think — OE þenċan

Derivation: _\*θánkijaną_ $\rightarrow$ _þenċan_ (regular).

#### Derivation trace

Proto input: _\*θánkijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*θánkijan} \\
OE Secondary Nasalization & \emph{*θánkijąn} \\
Sievers Law Syncope & \emph{*θánkjąn} \\
OE Velar Palatalization & \emph{*θánʧjąn} \\
OE I Umlaut & \emph{*θenʧjąn} \\
OE Weak Tail Reduction & \emph{*θenʧjan} \\
OE J Loss After Heavy & \emph{*θenʧan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _þenċan_

#### Reconstruction and comparative evidence

Kroonen gives the verb as _\*þankjan-_ 'to think', and Ringe and Taylor cite fully inflected _\*þankijaną_ beside OE _þenċan_ [@Kroonen2013; @RingeTaylor2014]. The noun _\*þankaz_ belongs only to the wider derivational background.

#### Old English evidence

Bosworth-Toller preserves the verb under _þencan/geþencan_, and the citation form here is the ordinary infinitive _þenċan_ [@BosworthToller1898].

#### Development to Old English

From _\*θánkijaną_, palatalization before _\*j_ and i-umlaut produce _þenċan_. The infinitive is therefore a straightforward weak-verb outcome.

#### Lexical note

Campbell's assibilation discussion uses the same verb _þencan_; the class-III relic _hycgan_ is a different lexeme [@Campbell1959; @Hogg1992].

### thorn — OE þorn

Derivation: _\*θúrnaz_ $\rightarrow$ _þorn_ (regular).

#### Derivation trace

Proto input: _\*θúrnaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc U Lowering & \emph{*θórnaz} \\
PGmc Final Z Deletion & \emph{*θórna} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Final Bare A Loss & \emph{*θórn} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _þorn_

#### Reconstruction and comparative evidence

Kroonen gives _\*þurna-_ 'thorn, briar', while Orel preserves the masculine pair _\*þurnuz ~ \*þurnaz_ [@Kroonen2013; @Orel2003]. The selected input _\*θúrnaz_ belongs to that same comparative family.

#### Old English evidence

Bright lists _þorn, m._, and Clark Hall likewise treats _þorn_ as the ordinary noun headword [@BrightCassidyRingler1971; @ClarkHall1960].

#### Development to Old English

The inherited stem shows regular lowering of _u_ to _o_ before _r_, and final loss yields _þorn_. The noun is therefore a regular Old English continuation of the Proto-Germanic thorn-family.

#### Source note

The comparative sources preserve more than one stem formation, but the Old English target itself is simply the citation form _þorn_.

### tide — OE tīd

Derivation: citation reconstruction _\*tī́diz_; selected input _\*tḯdiz_ $\rightarrow$ _tīd_ (regular).

#### Derivation trace

Proto input: _\*tḯdiz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*tḯdi} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE High Vowel Apocope & \emph{*tḯd} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _tīd_

#### Reconstruction and comparative evidence

Kroonen gives _\*tīdi-_ 'time', and Orel's _\*tīđiz_ points to the same feminine noun [@Kroonen2013; @Orel2003]. The related verb _tīdan_ is separate.

#### Old English evidence

Bright records _tīd_ with singular _tīde_ and plural _tīda_, and Clark Hall treats _tīd_ as the ordinary noun 'time, period, season' [@BrightCassidyRingler1971; @ClarkHall1960, 309].

#### Development to Old English

From _\*tḯdiz_, final _z_ is lost and the high final vowel drops, leaving _tīd_. The development is straightforward for a feminine i-stem.

#### Lexical note

The note matters only because English *tide* can pull in the separate weak verb _tīdan_; the noun targeted here is _tīd_.

### token — OE tācn

Derivation: _\*táikną_ $\rightarrow$ _tācn_ (regular).

#### Derivation trace

Proto input: _\*táikną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Ai Monophthongization & \emph{*tākną} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*tākn} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _tācn_

#### Reconstruction and comparative evidence

Kroonen cites _\*taikna-_ and Orel _\*taiknan_ for the noun 'sign, token' [@Kroonen2013; @Orel2003, 438]. The selected input _\*táikną_ is the simple citation-form noun used for the derivation.

#### Old English evidence

Campbell and Sievers-Brunner preserve both unbroken _tācn_ and broken _tācen_, with oblique _tācnes_ remaining unbroken [@Campbell1959; @SieversBrunner1965].

#### Development to Old English

Monophthongization of _ai_ yields _ā_, and loss of the final nasal vowel leaves _tācn_. The unbroken form is therefore a regular Old English outcome.

#### Form note

_tācn_ is the attested unbroken citation form selected here. Later West Saxon prose often prefers _tācen_, but that does not displace the older unbroken form [@Campbell1959; @SieversBrunner1965].

### town — OE tūn

Derivation: _\*tūną_ $\rightarrow$ _tūn_ (regular).

#### Derivation trace

Proto input: _\*tūną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*tūn} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _tūn_

#### Reconstruction and comparative evidence

Kroonen cites _\*tūna-_ 'fenced area', while Orel gives _\*tūnan ~ \*tūnaz_ [@Kroonen2013; @Orel2003, 452]. The selected input _\*tūną_ is the simple citation-form noun used in the derivation.

#### Old English evidence

Clark Hall records _tūn_ as the ordinary headword 'enclosure, yard, village, town' [@ClarkHall1960].

#### Development to Old English

The inherited long _ū_ is preserved, and loss of the final nasal vowel yields _tūn_ regularly [@SieversBrunner1965].

#### Source note

The comparative headwords vary, but the Old English target here is the direct citation form _tūn_, not an oblique _\*tūnăn_.

### wade — OE wadan

Derivation: _\*wádaną_ $\rightarrow$ _wadan_ (regular).

#### Derivation trace

Proto input: _\*wádaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*wædaną} \\
OE A Restoration & \emph{*wadaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*wadan} \\
OE Secondary Nasalization & \emph{*wadąn} \\
OE Weak Tail Reduction & \emph{*wadan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _wadan_

#### Reconstruction and comparative evidence

Campbell and Ringe and Taylor describe A-restoration before a following back vowel, and Luick explicitly includes _wadan_ among the standard open-syllable examples [@Campbell1959; @RingeTaylor2014; @Luick1914, 239].

#### Old English evidence

Clark Hall gives _wadan_ as the verb 'to go, move, stride, advance', and Bright lists the same infinitive in the strong-verb paradigm [@ClarkHall1960; @BrightCassidyRingler1971].

#### Development to Old English

From _\*wádaną_, Anglo-Frisian brightening first gives _\*wædaną_. A-restoration before the back-vocalic infinitive ending then returns _a_, and later reduction yields _wadan_ [@Campbell1959; @RingeTaylor2014].

#### Development note

The note matters because this infinitive belongs to the A-restoration class. The citation form is therefore _wadan_, not a fronted _wæden_-type output.

### warp — OE weorpan

Derivation: _\*wérpaną_ $\rightarrow$ _weorpan_ (regular).

#### Derivation trace

Proto input: _\*wérpaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Breaking & \emph{*wéorpaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*wéorpan} \\
OE Secondary Nasalization & \emph{*wéorpąn} \\
OE Weak Tail Reduction & \emph{*wéorpan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _weorpan_

#### Reconstruction and comparative evidence

Ringe and Taylor distinguish preterite _\*warp_ from infinitive _\*werpana_, and the selected input here is the verbal form _\*wérpaną_ [@RingeTaylor2014].

#### Old English evidence

Clark Hall records _weorpan_ as the strong verb headword and separately lists _wearp_ as both noun and preterite. Bright gives the paradigm _weorpan, wearp, wurpon, worpen_ [@ClarkHall1960; @BrightCassidyRingler1971].

#### Development to Old English

Breaking before _r + C_ yields _weor-_, and the infinitive develops regularly to _weorpan_ [@Campbell1959; @Hogg1992].

#### Lexical note

The note matters because English *warp* also points to related _wearp_ material. Here the target is specifically the infinitive _weorpan_.

### wash — OE wascan

Derivation: _\*wáskaną_ $\rightarrow$ _wascan_ (regular).

#### Derivation trace

Proto input: _\*wáskaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*wæskaną} \\
OE A Restoration & \emph{*waskaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*waskan} \\
OE Secondary Nasalization & \emph{*waskąn} \\
OE Weak Tail Reduction & \emph{*waskan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _wascan_

#### Reconstruction and comparative evidence

Kroonen cites _\*waskan-_, Orel _\*waskanan_, and Ringe and Taylor likewise derive Old English _wascan_ from the same verb family [@Kroonen2013; @Orel2003, 489; @RingeTaylor2014, 142].

#### Old English evidence

Clark Hall heads the verb as _wascan_, while Sievers-Brunner also notes the variant _wæscan_ [@ClarkHall1960; @SieversBrunner1965].

#### Development to Old English

From _\*wáskaną_, brightening gives _\*wæskaną_. A-restoration before the _sC_ cluster restores _a_, and medial _sc_ remains unpalatalized before the following back vowel, yielding _wascan_ [@Campbell1959; @RingeTaylor2014, 142].

#### Form note

The conservative citation form _wascan_ is selected here. Spellings such as _wæscan_ or _wasċan_ belong to variant or normalized background rather than to the target of this entry.

### wax — OE weaxan

Derivation: _\*wáxsaną_ $\rightarrow$ _weaxan_ (regular).

#### Derivation trace

Proto input: _\*wáxsaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*wæxsaną} \\
OE Breaking & \emph{*weaxsaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*weaxsan} \\
OE Secondary Nasalization & \emph{*weaxsąn} \\
OE Weak Tail Reduction & \emph{*weaxsan} \\
OE Xs Merge & \emph{*weaXSan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _weaxan_

#### Reconstruction and comparative evidence

Kroonen cites the verb as _\*wahs(j)an-_, Orel as _\*waxsanan_, and Ringe and Taylor discuss the prehistory of Old English _weaxan_ within the same verbal family [@Kroonen2013; @Orel2003, 478; @RingeTaylor2014].

#### Old English evidence

Clark Hall gives _weaxan_ as the verb headword and separately records bare _wax_ as a preterite form; Bright likewise treats _weaxan_ as the infinitive [@ClarkHall1960; @BrightCassidyRingler1971].

#### Development to Old English

From _\*wáxsaną_, brightening and breaking yield _weax-_, and the infinitive develops regularly to _weaxan_. The cluster is preserved here, since _xs > s_ belongs to forms where another consonant follows, such as _wæstm_, not to the infinitive itself [@Campbell1959; @SieversBrunner1965].

#### Lexical note

The target here is the infinitive _weaxan_. Noun _weax_ and preterite _wax/wēox_ belong to different lexical or paradigm slots.

### way — OE weġ

Derivation: _\*wégaz_ $\rightarrow$ _weġ_ (regular).

#### Derivation trace

Proto input: _\*wégaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*wéga} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Final Bare A Loss & \emph{*wég} \\
OE Velar Palatalization & \emph{*wéʤ} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _weġ_

#### Reconstruction and comparative evidence

Kroonen cites the noun as _\*wega-_ 'way, road', while the selected derivational form here is nominative-singular _\*wégaz_ [@Kroonen2013]. Campbell, Hogg, and Ringe and Taylor use the same word as the standard contrast between singular palatal _weġ_ and inflected _wegas/wegum_ [@Campbell1959; @Hogg1992; @RingeTaylor2014, 341].

#### Old English evidence

The Old English singular is the ordinary noun _weg_, here normalized as _weġ_ to show the palatal final. The contrasting plural and oblique forms _wegas, wegum_ keep a velar stop before the following back vowel [@Campbell1959; @RingeTaylor2014, 341].

#### Development to Old English

From _\*wégaz_, final _\*z_ is lost and the weak tail apocopates, leaving word-final _\*g_ after a front vowel. In that environment Old English palatalization yields _weġ_, whereas _wegas_ remains velar because the following _a_ blocks the same outcome [@Campbell1959; @Hogg1992; @RingeTaylor2014, 341].

#### Form note

Normalized _weġ_ and dictionary _weg_ represent the same noun. _wē_ is not supported in the checked Old English evidence for 'way'.

### weapon — OE wǣpn

Derivation: _\*wḗpną_ $\rightarrow$ _wǣpn_ (regular).

#### Derivation trace

Proto input: _\*wḗpną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc Long E Lowering & \emph{*wǣpną} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*wǣpn} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _wǣpn_

#### Reconstruction and comparative evidence

Kroonen reconstructs a double-stem noun _\*wēbna- ~ \*wēpna-_ and cites OE _wæpn_ among its reflexes [@Kroonen2013, 617]. The selected input _\*wḗpną_ represents the unbroken citation-form noun rather than the later broken simplex.

#### Old English evidence

Campbell's cluster-noun discussion preserves unbroken _wépn_ beside broken
_wépen_-type forms [@Campbell1959, 150; @Campbell1959, 226–227]. Bright
contrasts broken nominative _wǣpen/wapen_ with unbroken oblique _wǣpnes_,
while Clark Hall lemmatizes the noun under _wapen_ and also preserves unbroken
forms in compounds and related spellings
[@BrightCassidyRingler1971, 29; @ClarkHall1960, 355].

#### Development to Old English

Northwest Germanic lowering gives _wǣpn_, and loss of the final nasal vowel leaves the unbroken cluster word-finally. The selected target is the attested unbroken form _wǣpn_.

#### Form note

The ordinary late West Saxon simplex headword is _wǣpen_, but Campbell's
noun-class discussion also preserves unbroken _wépn_ beside broken
_wépen_-type forms [@Campbell1959, 150; @Campbell1959, 226–227]. _wǣpnes_
remains the regular unbroken oblique comparator
[@BrightCassidyRingler1971, 29; @ClarkHall1960, 355].

### will — OE willa

Derivation: _\*wéljô_ $\rightarrow$ _willa_ (regular).

#### Derivation trace

Proto input: _\*wéljô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc J Gemination & \emph{*wélljô} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE I Umlaut & \emph{*willjô} \\
OE Unstressed Long Vowel Shortening & \emph{*willja} \\
OE J Loss After Heavy & \emph{*willa} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _willa_

#### Reconstruction and comparative evidence

Kroonen separates noun _\*weljan- 2_ 'will, wish' from verb _\*weljan- 1_ 'to want', while Orel and Kluge represent the noun as _\*weljōn/\*weljOn_ [@Kroonen2013; @Orel2003; @KlugeSeebold2011]. The selected derivational form _\*wéljô_ is the noun-side input used for this row.

#### Old English evidence

Clark Hall lemmatizes noun _willa m._ separately from verb _willan_ [@ClarkHall1960, 368]. The selected target is the noun citation form, not the related verb.

#### Development to Old English

From _\*wéljô_, j-gemination yields a heavy stem, i-umlaut gives _will-_, and later shortening plus j-loss produce _willa_. The noun is therefore a regular weak masculine outcome.

#### Lexical note

The target here is the noun _willa_ 'will, wish'. Related verb _willan_ belongs to a separate lexeme and should not be substituted for the noun row [@Kroonen2013; @ClarkHall1960, 368].

### wind — OE windan

Derivation: _\*wíndaną_ $\rightarrow$ _windan_ (regular).

#### Derivation trace

Proto input: _\*wíndaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*wíndan} \\
OE Secondary Nasalization & \emph{*wíndąn} \\
OE Weak Tail Reduction & \emph{*wíndan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _windan_

#### Reconstruction and comparative evidence

Kroonen distinguishes noun _\*winda-_ from verb _\*windan-_, and the present row belongs to the verb [@Kroonen2013]. Later handbook discussion keeps the dental original from PIE _\*wendh-_, not a Verner alternant [@Fulk2018; @RingeTaylor2014].

#### Old English evidence

Clark Hall and Bosworth-Toller record _windan_ as the verb headword [@ClarkHall1960; @BosworthToller1898, 101]. The selected target is the ordinary infinitive of the strong verb.

#### Development to Old English

The selected input _\*wíndaną_ yields the regular infinitive _windan_ by ordinary heavy-syllable apocope and weak-tail reduction. The form is therefore a straightforward strong-verb outcome.

#### Lexical note

The note matters because English *wind* also names the noun. This row targets the class-III verb, not the noun [@Kroonen2013; @ClarkHall1960].

### wold — OE weald

Derivation: _\*wálθuz_ $\rightarrow$ _weald_ (regular).

#### Derivation trace

Proto input: _\*wálθuz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc L Th Voicing & \emph{*wálduz} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*wáldu} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*wældu} \\
OE Breaking & \emph{*wealdu} \\
OE High Vowel Apocope & \emph{*weald} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _weald_

#### Reconstruction and comparative evidence

Kroonen reconstructs the noun as _\*walþu-_ and gives OE _weald_ beside other West Germanic _wald_ forms [@Kroonen2013]. The selected input _\*wálθuz_ is the nominative singular used for the derivation.

#### Old English evidence

Clark Hall makes _weald_ the main noun headword and cross-refers _wald_ and _wold_ to it [@ClarkHall1960]. The Anglian-looking _wald_ therefore remains variant background rather than the main target.

#### Development to Old English

_\*lþ_ voices to _ld_, Anglo-Frisian brightening yields _wæld-_, and breaking before the cluster gives _weald-_; apocope then yields _weald_. The noun is therefore a regular breaking outcome.

#### Dialect note

The note matters because _wald_ survives as an Anglian-type variant in the same family. The selected target is normalized _weald_, not the variant form [@ClarkHall1960; @RingeTaylor2014].

### yarn — OE ġearn

Derivation: _\*gárną_ $\rightarrow$ _ġearn_ (regular).

#### Derivation trace

Proto input: _\*gárną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*gærną} \\
OE Breaking & \emph{*gearną} \\
OE Heavy Syllable Nasal Apocope & \emph{*gearn} \\
OE Velar Palatalization & \emph{*ʤearn} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _ġearn_

#### Reconstruction and comparative evidence

Kroonen cites the noun as _\*garna-_, and Ringe and Taylor give the early chain _\*garna > \*geern > \*gearn > OE gearn_ [@Kroonen2013; @RingeTaylor2014, 220]. The selected input _\*gárną_ is the nominal citation form used here, while oblique _\*garnăn_ belongs only to comparative background.

#### Old English evidence

Clark Hall records _gearn (e) n._ 'yarn, spun wool', and Bosworth-Toller glosses _gearn_ as _filatum_ [@ClarkHall1960; @BosworthToller1898].

#### Development to Old English

From _\*gárną_, brightening and breaking before _rn_ yield _gearn_; palatalization of initial _g_ before the resulting front-vocalic sequence gives normalized _ġearn_. The derivation is regular.

#### Form note

Dictionary _gearn_ and normalized _ġearn_ refer to the same noun. The comparative stem _\*garna-_ and oblique _\*garnăn_ do not replace the selected input _\*gárną_.

\clearpage

## Part II. Attested variants and selected comparison forms

These entries treat the selected Old English target as one member of an attested
or historically documented variant set. The target is therefore anchored in the
record, but the lexical comparison must account for variation rather than for a
single unproblematic citation form.

### cud — OE cwedu

Derivation: citation reconstruction _\*kwíθuz_; selected input _\*kwéðuz_ $\rightarrow$ _cwedu_ (attested variant).

#### Derivation trace

Proto input: _\*kwéðuz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Dental Hardening & \emph{*kwéduz} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*kwédu} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\raggedright [no change]\par
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _cwedu_

#### Reconstruction and comparative evidence

Kroonen reconstructs the resin word as _\*kwedu-2_ and gives Old English
variants _cwidu_, _cweodu_, and _c(w)udu_ [@Kroonen2013, 355]. Orel likewise
lists _cwidu_ under the cognate set [@Orel2003, 266]. The selected input
_\*kwéðuz_
therefore represents the older e-grade, voiced-dental form behind the chosen
variant _cwedu_.

#### Old English evidence

The Old English word survives in a wider variant set than one dictionary
headword suggests. Ringe and Taylor discuss _cwidu > cwudu > cudu_ and also
note late West Saxon _cweodu_; Clark Hall gives _cwudu_, _cweodu_, and _cudu_
[@RingeTaylor2014, 338; @ClarkHall1960, 84]. Attested _cwedu_ is treated here
as the
conservative variant within that set.

#### Development to Old English

From _\*kwéðuz_, the West Germanic voiced dental hardens in the expected way and
the regular Old English development yields _cwedu_. The other Old English
spellings belong to the same lexical family, but reflect later leveling,
back-umlaut, or further reduction rather than a need to replace the selected
input.

#### Variant comparison

| Variant type | Old English form | Comment |
| :--- | :--- | :--- |
| conservative target | _cwedu_ | selected attested variant represented here |
| leveled i-grade form | _cwidu_ | common lexical variant in the same family |
| back-umlauted forms | _cweodu_, _cwudu_ | later developments within the same OE tradition |
| reduced form | _cudu_ | further reduced member of the same variant set |

### ten — OE tēon

Derivation: _\*téxun_ $\rightarrow$ _tēon_ (attested variant).

#### Derivation trace

Proto input: _\*téxun_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Med Unstressed U Lowering & \emph{*téxon} \\
OE Breaking & \emph{*téoxon} \\
OE H Loss & \emph{*téoon} \\
OE Contraction & \emph{*tḗon} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _tēon_

#### Reconstruction and comparative evidence

Fulk states that Old English _tien_ shows umlaut from the inflected forms,
whereas the uninflected form without umlaut is reflected in
_hund-tēon-tig_ [@Fulk2018, §10.2]. Brunner gives the same contrast more
broadly: _tēon_ develops from _\*tëhun_, while West Saxon _tien, tȳn_ belong to
a different, umlauted branch of the numeral history [@SieversBrunner1965,
§§129.2, 129 Anm. 6, 234].

The selected comparison form _tēon_ therefore represents the bare cardinal's
un-umlauted line, not the later umlauted simplex tradition.

#### Old English evidence

The attested simplex forms are varied. Campbell gives _tien_, north-western
West Saxon _tēn_, and late Northumbrian _tēo, tēa_
[@Campbell1959, §682]. Brunner likewise lists West Saxon _tien, tȳn_ beside
_tēn, tēo, tēa_ in other dialects [@SieversBrunner1965, §325].

Exact simplex _tēon_ is weaker as a directly cited headword than those
spellings. The un-umlauted stem is, however, explicit in _tēoða_ and
_-tēontig_ [@SieversBrunner1965, §129.2; @Fulk2018, §10.2]. The comparison
form _tēon_ is therefore a **normalized spelling** of that un-umlauted base.

#### Development to Old English

From _\*téxun_, lowering of medial unstressed _u_ gives _\*téxon_,
breaking gives _\*téoxon_, loss of intervocalic _h/x_ yields _\*téoon_,
and contraction produces _\*tḗon_, written _tēon_. This is the regular
bare-cardinal path.

The umlauted forms _tien / tīen_ belong to a different branch, created when
the numeral was levelled from inflected forms with a front-vocalic trigger
[@Fulk2018, §10.2; @SieversBrunner1965, §129 Anm. 6].

#### Variant comparison

The comparison below is manual. It distinguishes the normalized un-umlauted base
from the attested simplex variants.

| Form or branch | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _tēon_ | normalized un-umlauted comparison form; trace-supported | selected target |
| _tien / tīen_ | attested West Saxon umlauted simplex forms | genuine OE variants, but not the bare-cardinal line modeled here |
| _tēn / tēo / tēa_ | attested un-umlauted simplex variants in other dialects | support the same branch as the selected comparison form |

### three — OE þrīe

Derivation: _\*θréjez_ $\rightarrow$ _þrīe_ (attested variant).

#### Derivation trace

Proto input: _\*θréjez_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*θréje} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE I Umlaut & \emph{*θrije} \\
OE Intervocalic J Vocalization & \emph{*θriie} \\
OE Contraction & \emph{*θrīe} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _þrīe_

#### Reconstruction and comparative evidence

Kroonen cites the numeral under a broader stem-style reconstruction rather than
under one Old English-ready paradigm cell [@Kroonen2013]. The input
_\*θréjez_ is therefore best understood as the inherited masculine
nominative-accusative singular.

That distinction matters because the Old English numeral does not have one
uniform citation form across the paradigm. The masculine singular line must be
kept apart from feminine-neuter _þrēo_ and from later reduced spellings of
the masculine form.

#### Old English evidence

Campbell gives masculine nominative-accusative _þrīe_, feminine and neuter
nominative-accusative _þrēo_, genitive _þrēora_, and dative
_þrim_, adding that late West Saxon has _þry, þri_ for _þrīe_
[@Campbell1959, §683]. Fulk presents the same masculine _þrīe_ beside the
wider numeral paradigm [@Fulk2018, §10.1].

The target is therefore an attested Old English paradigm cell. _þrī_
belongs to later reduction or headword-style citation, whereas _þrīe_ is
the conservative masculine nominative-accusative form.

#### Development to Old English

From _\*θréjez_, loss of final _-z_ leaves a form of the _\*θréje_
type. The following _j_ fronts the stem vowel, then vocalizes between
vowels, and contraction yields _þrīe_. The compact trace records the same
sequence as _\*θrije > \*θriie > þrīe_.

#### Variant comparison

The comparison below is manual. It separates the selected masculine cell from
the later reduced form and from the rest of the numeral paradigm.

| Form | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _þrīe_ | attested masculine nom./acc.; trace output | selected target |
| _þrī / þry_ | later reduced masculine variant | genuine OE variant, but not the conservative comparison form |
| _þrēo_ | attested feminine-neuter nom./acc. | same numeral, different paradigm cell |
| _þrēora_, _þrim_ | attested genitive and dative forms | confirm the wider paradigm, not the selected cell |

### wasp — OE wæfs

Derivation: _\*wábsaz_ $\rightarrow$ _wæfs_ (attested variant).

#### Derivation trace

Proto input: _\*wábsaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*wábsa} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Final Bare A Loss & \emph{*wábs} \\
Anglo Frisian Brightening & \emph{*wæbs} \\
PGmc B Allophony & \emph{*wæβs} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _wæfs_

#### Reconstruction and comparative evidence

The Proto-Germanic form _\*wábsaz_ reaches Old English without any special
change of stem or paradigm cell. The question in this entry is instead which
attested Old English member of the variant set should serve as the comparison
form.

Fulk presents the Old English forms together as _wæfs_ with variants _wæsp_ and
_wæps_ [@Fulk2018, §6.5]. Bülbring and Brunner then make the chronology more
explicit by deriving later _wæps_ and late West Saxon _wasp_ from earlier
_waefs / wæfs_ through restricted metatheses [@Bulbring1902, §484 Anm. 3;
@SieversBrunner1965, §§193, 204].

#### Old English evidence

The earliest directly cited Old English form is _wæfs_, written _waefs_ in
the Épinal-Corpus material discussed by Bülbring and Brunner
[@Bulbring1902, §484 Anm. 3; @SieversBrunner1965, §193]. Later Old English also
shows _wæps_ and _wæsp / wasp_, and dictionary practice often favors
_wæps_ or later spellings as headwords [@ClarkHall1960].

This entry therefore distinguishes chronological priority from headword habit.
_wæfs_ is not a convenient reconstruction: it is an attested Old English form
and also the one that matches the regular development most closely.

#### Development to Old English

From _\*wábsaz_, the regular Old English path passes through loss of final _z_,
Anglo-Frisian fronting, and the allophonic development of _b_ to a fricative
before _s_, yielding _wæfs_.

The later forms _wæps_ and _wæsp / wasp_ belong to subsequent, lexically
restricted metatheses. They are genuine Old English forms, but they are later
within the variant history.

#### Variant comparison

The comparison below is manual. It separates the earliest attested and regular
form from the later metathesized doublets.

| Form | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _wæfs_ | earliest attested OE form; regular trace output | selected target |
| _wæps_ | later attested metathesized variant | genuine OE doublet, but secondary |
| _wæsp / wasp_ | later West Saxon metathesized variant | genuine OE doublet, but not the selected form |

\clearpage

## Part III. Early analogy and pre-Old-English input selection

These entries involve a distinction between the lexeme-level citation
reconstruction and the form selected as input to the Old English derivation.
The issue is upstream of Old English: the selected input represents the
pre-Old-English form that gives the attested target under the current cascade.

### bottom — OE botm

Derivation: citation reconstruction _\*búdmaz_; selected input _\*búttmaz_ $\rightarrow$ _botm_ (early analogy).

#### Derivation trace

Proto input: _\*búttmaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc U Lowering & \emph{*bóttmaz} \\
PGmc Final Z Deletion & \emph{*bóttma} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Final Bare A Loss & \emph{*bóttm} \\
OE Preconsonantal Degemination & \emph{*bótm} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _botm_

#### Reconstruction and comparative evidence

Kroonen reconstructs the word as a stem complex _\*budmō, gen. \*buttaz_,
summarized as _\*budman- ~ \*buttman-_, and gives Old English _botm_ as the reflex
[@Kroonen2013, 120]. The comparative label _\*búdmaz_ names the lexeme-level stem
complex, while the selected input _\*búttmaz_ represents the pre-Old-English
form with oblique _\*butt-_ generalized into the nominative formation.

Orel likewise preserves both sides of the comparison under _\*budmaz \*butmaz_
[@Orel2003, 100]. The selected input is thus a historical stem choice, not an
arbitrary respelling.

#### Old English evidence

The Old English noun itself is secure. Clark Hall gives _botm_
[@ClarkHall1960, 63]. Bosworth-Toller cross-references _bodan_ to _botm_,
showing the wider reflex family without weakening the attested lemma
[@BosworthToller1898, 112].

#### Development to Old English

Once the oblique _\*butt-_ stem has been generalized, the selected input
_\*búttmaz_ develops regularly to _botm_. The analogical step is therefore early:
it belongs to pre-Old-English stem formation rather than to a later choice
among Old English paradigm cells.

### brand — OE brandes

Derivation: citation reconstruction _\*brándaz_; selected input _\*brándas_ $\rightarrow$ _brandes_ (early analogy).

#### Derivation trace

Proto input: _\*brándas_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*brándæs} \\
OE Unstressed AE Merger & \emph{*brándes} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _brandes_

#### Reconstruction and comparative evidence

The inherited noun is the masculine a-stem _\*brándaz_, continued by Old English
_brand_ and its continental cognates [@Orel2003; @Kroonen2013]. The selected
input _\*brándas_ is not a different lexeme but the genitive singular of that
same a-stem noun.

What matters here is therefore not a stem-class disagreement but the difference
between the citation form and a specific inherited inflectional cell. The
selected input preserves the same root and declension as the headword while
making the oblique ending explicit.

#### Old English evidence

Old English dictionaries lemmatize the noun as _brand_ [@ClarkHall1960;
@BosworthToller1898, 116]. Bosworth-Toller also records inflectional forms such as
_brandas_, _branda_, and _brandum_ under the same entry [@BosworthToller1898, 116].

The specific comparison form in this entry, _brandes_, is the expected
genitive singular of that a-stem noun. It is therefore an inferred Old English
paradigm form rather than the ordinary dictionary headword.

#### Development to Old English

From _\*brándas_, the regular Old English development passes through the usual
unstressed-vowel weakening of the inflectional ending, yielding _brandes_.
Nothing in the stem itself requires a special repair. The root consonants and
the stressed vowel are the same as in the citation lemma _brand_.

The analytical weight of the entry lies in the ending. By choosing the oblique
singular rather than the nominative citation form, the entry presents the same
lexeme in a different inherited cell.

#### Form comparison

The comparison below is manual. It separates the citation lemma from the
selected oblique singular.

| Form / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | *brándaz | expected OE lemma _brand_ | brand | regular headword-level outcome |
| selected genitive singular | *brándas | compact-trace output: _brandes_ | brandes | exact match for the chosen oblique cell |

The noun itself is straightforwardly inherited. The main point of the entry is
that _brandes_ belongs to the same regular a-stem paradigm as _brand_, even
though the citation lemma remains the nominative singular.

### breast — OE brēost

Derivation: citation reconstruction _\*brústz_; selected input _\*bréustą_ $\rightarrow$ _brēost_ (early analogy).

#### Derivation trace

Proto input: _\*bréustą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Diphthong Leveling & \emph{*brēostą} \\
OE Heavy Syllable Nasal Apocope & \emph{*brēost} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _brēost_

#### Reconstruction and comparative evidence

The word family shows two related but distinct Proto-Germanic formations. The
root noun _\*brust-_ lies behind forms such as Gothic _brusts_, whereas Old
English _brēost_ belongs to a thematic formation _\*breusta-_, alongside Old
Norse _brjóst_ and Old Saxon _briost_ [@Kroonen2013; @Orel2003, 95;
@RingeTaylor2014, 43].

The selected input _\*bréustą_ therefore differs from the citation label
_\*brústz_ because Old English reflects the thematic branch rather than the root
noun. The morphological choice comes before the Old English sound changes
themselves.

#### Old English evidence

Old English dictionaries record the noun as _brēost_ / _breóst_
[@BosworthToller1898; @ClarkHall1960, 65]. The form is an established Old English
lexeme, not a reconstructed target assembled from comparative evidence alone.

What requires explanation is not the Old English attestation but the relation
between that attested noun and the broader Germanic word family. The relevant
comparison form is therefore the thematic Old English noun _brēost_.

#### Development to Old English

From _\*bréustą_, the regular Old English development gives _brēost_, with the
expected _eu > ēo_ vowel history [@Campbell1959]. No special repair is needed
once the correct thematic formation is chosen.

The earlier mismatch arose only if the word was forced into the root-noun line.
The Old English noun itself continues the thematic branch cleanly and directly.

#### Formation comparison

The comparison below is manual. It separates the broader root-noun family label
from the thematic formation actually continued in Old English.

| Formation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| broader root-noun family | *brústz | root-noun type outcomes outside OE | non-OE comparanda | useful family label, but not the direct source of _brēost_ |
| selected thematic formation | *bréustą | compact-trace output: _brēost_ | brēost | exact match between formation and attested OE noun |

The relevant point is the formation split. _brēost_ is the regular Old English
outcome of the thematic _\*breusta-_ branch, not of the root noun _\*brust-_.

### craft — OE cræft

Derivation: citation reconstruction _\*kráftiz_; selected input _\*kráftaz_ $\rightarrow$ _cræft_ (early analogy).

#### Derivation trace

Proto input: _\*kráftaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*kráfta} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Final Bare A Loss & \emph{*kráft} \\
Anglo Frisian Brightening & \emph{*kræft} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _cræft_

#### Reconstruction and comparative evidence

Comparative sources disagree about the older stem class. Kroonen gives a u-stem
_\*kraftu-_, while Orel prints _\*kraftiz ~ \*kraftuz_ [@Kroonen2013, 340; @Orel2003,
259].
The comparative label _\*kráftiz_ remains in view as a lexeme-level shorthand,
while _\*kráftaz_ is the pre-Old-English form used for the Old English
derivation.

#### Old English evidence

The Old English noun itself is secure. Clark Hall and Bosworth-Toller both give
_cræft_ as the headword [@ClarkHall1960, 19; @BosworthToller1898, 145].

#### Development to Old English

The comparison is between possible pre-Old-English inputs. The i-stem
comparator _\*kráftiz_ gives _creft_, while the u-stem comparator _\*kráftuz_
gives _craft_. The a-stem-shaped input _\*kráftaz_ yields _cræft_ and is
therefore the form used for the Old English derivation. This does not require
treating the comparative dictionaries as identical; it shows the narrower point
that the Old English derivation needs a pre-Old-English form without the
i-umlaut trigger of _\*-iz_ and without the back-vowel outcome associated with
the u-stem comparator.

#### Form comparison

| Candidate input | OE output | Result |
| :--- | :--- | :--- |
| *kráftiz | _creft_ | non-match; i-stem comparator |
| *kráftuz | _craft_ | non-match; u-stem comparator |
| *kráftaz | _cræft_ | exact match; selected pre-OE input |

### dill — OE dile

Derivation: citation reconstruction _\*déljaz_; selected input _\*déliz_ $\rightarrow$ _dile_ (early analogy).

#### Derivation trace

Proto input: _\*déliz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*déli} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE I Umlaut & \emph{*dili} \\
OE Med Unstressed I Lowering1 & \emph{*dile} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _dile_

#### Reconstruction and comparative evidence

Kroonen treats the word as preserving evidence for both an i-stem and a ja-stem
formation, with Old English _dile_ on one side and continental forms such as Old
Saxon _dilli_ and Old High German _tilli_ on the other [@Kroonen2013]. The
selected input _\*déliz_ therefore represents the i-stem side of the paradigm,
whereas the citation label _\*déljaz_ is a broader comparative headword.

That stem-class distinction matters for the Old English consonant shape. A
ja-stem with _\*-lj-_ would be expected to produce gemination, but the Old
English noun shows a single _l_. Fulk's discussion of ja-stems transferred to
the i-stems provides the relevant morphological background for the OE side
[@Fulk2018].

#### Old English evidence

Old English dictionaries record the plant name as _dile_, alongside the variant
_dili_ [@BosworthToller1898, 164; @ClarkHall1960]. The form discussed here is
therefore an attested Old English noun with single _l_.

The Old English evidence is the relevant point. Whatever broader comparative
headword is chosen for the family, the inherited form reflected in OE is the
i-stem type _dile_, not a geminated _dill_ outcome.

#### Development to Old English

From _\*déliz_, regular loss of final _z_ and the later lowering of unstressed
_i_ yield _dile_. The stem itself remains ungeminated throughout that path.

The important contrast is negative rather than phonological. If the word were
forced through a ja-stem _\*-lj-_ pathway, the expected result would show _ll_.
The attested Old English noun instead matches the i-stem development.

#### Formation comparison

The comparison below is manual. It separates the broader comparative headword
from the stem class actually reflected in Old English.

| Formation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| comparative ja-stem label | *déljaz | ja-stem type outcome with gemination | dill-type comparison | useful comparative label, but not the OE form |
| selected i-stem formation | *déliz | compact-trace output: _dile_ | dile | exact match between formation and attested OE noun |

The single _l_ is the decisive diagnostic. It identifies _dile_ with the i-stem
formation rather than with the continental ja-stem branch.

### fast — OE festan

Derivation: citation reconstruction _\*fastēną_; selected input _\*fástijaną_ $\rightarrow$ _festan_ (early analogy).

#### Derivation trace

Proto input: _\*fástijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*fæstijaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*fæstijan} \\
OE Secondary Nasalization & \emph{*fæstijąn} \\
Sievers Law Syncope & \emph{*fæstjąn} \\
OE I Umlaut & \emph{*festjąn} \\
OE Weak Tail Reduction & \emph{*festjan} \\
OE J Loss After Heavy & \emph{*festan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _festan_

#### Reconstruction and comparative evidence

Kroonen places the verb under a comparative headword _\*fastēną_, the wider
Germanic family behind meanings such as 'make firm' and, in Old English, 'fast'
[@Kroonen2013]. Ringe and Taylor, however, distinguish the Old English verb
more closely: they treat OE 'to fast' as originally a class-I weak verb that
later acquired the stative meaning through lexical association with that wider
family [@RingeTaylor2014].

The selected input _\*fástijaną_ therefore represents the inherited class-I
formation reflected in Old English, whereas the citation label _\*fastēną_
belongs to the broader comparative presentation of the lexeme.

#### Old English evidence

Old English dictionaries record forms such as _festan_, alongside related
_fæstan_ / _fǣstan_ spellings and meanings [@BosworthToller1898, 213;
@ClarkHall1960]. The form selected here is _festan_, which fits the regular
class-I phonological development.

The _æ_-forms remain relevant, but they do not control the entry. As Ringe and
Taylor argue, their vowel belongs to later analogical leveling under the
adjective _fæst_, whereas _festan_ reflects the regular inherited class-I verb
[@RingeTaylor2014].

#### Development to Old English

From _\*fástijaną_, Anglo-Frisian brightening and subsequent i-umlaut produce the
fronted vowel seen in _festan_. The later weak-tail reductions and loss of _j_
after a heavy syllable complete the regular Old English outcome.

What makes the entry non-regular is not the phonology of _festan_ itself, but
the choice of formation. Old English continues the class-I verb, even though
the comparative headword is often given under the parallel _\*fastēn-_ family.

#### Class comparison

The comparison below is manual. It distinguishes the comparative class-III
headword from the class-I formation actually reflected in Old English.

| Formation / class | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| comparative class-III headword | *fastēną | class-III type outcome, not _festan_ | wider family context | useful family label, but not the direct source of the target |
| selected class-I weak verb | *fástijaną | compact-trace output: _festan_ | festan | exact match between formation and attested OE verb |
| later analogical reshaping | adjective-driven _fæst_ influence | _fæstan_ / _fǣstan_ type spellings | fæstan-type evidence | genuine later OE reshaping, but secondary to the selected target |

The relevant point is the class split. _festan_ is the regular Old English
outcome of the class-I formation, while the better-known _æ_-forms belong to a
later analogical layer.

### flask — OE flasce

Derivation: citation reconstruction _\*flaskō_; selected input _\*fláskōn_ $\rightarrow$ _flasce_ (early analogy).

#### Derivation trace

Proto input: _\*fláskōn_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc N Stem N Loss & \emph{*fláskǭ} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*flæskǭ} \\
OE A Restoration & \emph{*flaskǭ} \\
OE Unstressed Long Vowel Shortening & \emph{*flaskæ} \\
OE Unstressed AE Merger & \emph{*flaske} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _flasce_

#### Reconstruction and comparative evidence

The wider Germanic family is often cited under a form such as _\*flaskō_, but
the evidence relevant for Old English points instead to a weak feminine
formation _\*fláskōn_ / _\*flaskǭ_ [@Orel2003; @Kroonen2013]. That distinction is
crucial for the suffixal history of the noun.

The selected input therefore differs from the citation label in stem class. Old
English _flasce_ belongs with the weak feminine line, and the plural or oblique
forms _flascan_ support that analysis [@RingeTaylor2014].

#### Old English evidence

Old English dictionaries record the noun as _flasce_, with inflectional support
from forms such as _flascan_; a later West Saxon _flaxe_ is also noted as a
secondary variant [@BosworthToller1898, 235; @ClarkHall1960, 121].

The relevant comparison form is therefore the weak feminine noun _flasce_.
The plural and oblique evidence matters because it helps explain why the vowel
and ending are preserved as they are in the singular.

#### Development to Old English

From _\*fláskōn_, the weak feminine passes through the expected loss of _n_ and
the later Old English development of the unstressed ending, reaching _flasce_.
Once the weak feminine formation is chosen, the noun follows a regular path to
its Old English shape [@Campbell1959].

The decisive issue is morphological rather than phonological. A simple strong
feminine citation form does not capture the OE weak noun as cleanly as the
selected _\*fláskōn_ does.

#### Formation comparison

The comparison below is manual. It separates the broader comparative headword
from the weak feminine formation actually reflected in Old English.

| Formation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| broader comparative headword | *flaskō | broader family label | wider family context | useful lexeme label, but not the cleanest OE-facing derivation |
| selected weak feminine formation | *fláskōn | compact-trace output: _flasce_ | flasce | exact match between formation and attested OE noun |

The weak feminine suffix is the relevant point. It aligns the inherited form
with attested _flasce_ and its supporting paradigm forms.

### follow — OE fylġan

Derivation: citation reconstruction _\*fulgēną_; selected input _\*fúlgijaną_ $\rightarrow$ _fylġan_ (early analogy).

#### Derivation trace

Proto input: _\*fúlgijaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*fúlgijan} \\
OE Secondary Nasalization & \emph{*fúlgijąn} \\
Sievers Law Syncope & \emph{*fúlgjąn} \\
OE Velar Palatalization & \emph{*fúlʤjąn} \\
OE I Umlaut & \emph{*fylʤjąn} \\
OE Weak Tail Reduction & \emph{*fylʤjan} \\
OE J Loss After Heavy & \emph{*fylʤan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _fylġan_

#### Reconstruction and comparative evidence

Kroonen keeps the verb under _\*fulgen-_ and gives Old English _fylgan, folgian_,
adding that Old Norse _fylgja_ and Old English _fylg(e)an_ continue a formation
_\*fulgjan-_ [@Kroonen2013]. The comparative headword and the class-I formation
are therefore related but not identical.

Ringe and Taylor make the split explicit as _PNWGmc \*fulgija- ~ \*fulgai- > OE fylgan ~ folgian_ and describe it as a dual formation that probably reflects an
older alternation between j-present and e-stative [@RingeTaylor2014, pp. 293-294].
This is a stem-class choice, not a spelling choice. The selected input
_\*fúlgijaną_ belongs to the class-I _\*fulgija- / \*fulgjan-_ branch; the citation
form _\*fulgēną_ belongs to the parallel class-II history behind _folgian_.

#### Old English evidence

The Old English evidence preserves both formations. Clark Hall gives _folgian_
and cross-refers to _fylgan_, while also listing _fylgan_ with variant spellings
_fylgian_ and _fyligan_ [@ClarkHall1960]. Bosworth-Toller likewise has separate
entries for _folgian_ and _fylgean_ [@BosworthToller1898].

Bright treats _fylg(e)an_ as a survival of the older conjugation and contrasts
it with forms that have conformed to the Second Conjugation, _folgian, folgode_
[@BrightCassidyRingler1971]. The relevant comparison form in this entry is
therefore the class-I verb _fylgan / fylgean_, here normalized as _fylġan_.
The spelling with _<ġ>_ represents the palatalized velar before a front-vocalic
environment.

#### Development to Old English

_\*fúlgijaną_ is a class-I weak-verb formation. In the class-I branch the _\*j_
blocks NWGmc lowering of _u_ to _o_, since Ringe and Taylor formulate that
lowering for environments in which no _\*j_ intervened [@RingeTaylor2014, p. 96].
The same front-vocalic environment then triggers i-umlaut, so _u_ becomes _y_
[@RingeTaylor2014, §6.6.2].

The subsequent Old English developments are palatalization of the velar,
weak-tail reduction, and loss of _j_ after a heavy syllable, yielding
_fylġan_. This is the regular outcome of the class-I formation. The class-II
form _folgian_ belongs to the parallel _\*-ē- / \*-ai-_ branch and is not the
form modeled here.

#### Class comparison

A class comparison identifies which inherited formation corresponds to the
established Old English form under discussion. The comparison below is manual;
no full automatic class probe is presented here.

| Formation / class | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation class-II formation | *fulgēną | probe output: _folgon_ | folgian | mismatch: the regular output is not the remodeled infinitive _folgian_ |
| parallel class-II branch | PNWGmc *fulgai- | Ringe-Taylor: OE _folgian_ | folgian | documents the separate class-II branch, but not the target of this entry |
| selected class-I formation | *fúlgijaną | compact-trace output: _fylġan_ | fylġan / fylgan | exact match between input, output, and class |

The relevant point is the class split. _fylġan_ is the regular Old English
outcome of the class-I _\*fulgija- / \*fulgjan-_ formation, whereas _folgian_
belongs to the parallel class-II branch.

### gall — OE ġealla

Derivation: citation reconstruction _\*gállą_; selected input _\*gállô_ $\rightarrow$ _ġealla_ (early analogy).

#### Derivation trace

Proto input: _\*gállô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*gællô} \\
OE Breaking & \emph{*geallô} \\
OE Velar Palatalization & \emph{*ʤeallô} \\
OE Unstressed Long Vowel Shortening & \emph{*ʤealla} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _ġealla_

#### Reconstruction and comparative evidence

The wider cognate family can be presented under a form such as _\*gállą_, but
the Old English noun itself belongs with a weak noun _\*gallōn-_, cited here as
_\*gállô_ [@Kroonen2013]. The selected input therefore differs from the broader
comparative headword in stem class.

That stem-class distinction matters directly for the Old English shape. The weak
masculine pathway preserves the ending needed for _ġealla_, whereas a simple
strong-noun headword does not align as closely with the attested OE noun.

#### Old English evidence

Old English dictionaries record the noun as _gealla_, and Bright also gives the
dative _geallan_, confirming a weak-noun paradigm [@BosworthToller1898, 297;
@ClarkHall1960, 145; @BrightCassidyRingler1971, 372]. The form used here, _ġealla_, is
a normalized spelling with macrons omitted and palatal _<ġ>_ made explicit.

Campbell also notes dialectal variation, contrasting West Saxon or Kentish
_gealla_ with Anglian _galla_ [@Campbell1959]. The target of this entry is the
West Saxon type _ġealla_.

#### Development to Old English

From _\*gállô_, the weak noun develops through the expected Old English history
of the suffix and the regular breaking environment before _ll_, yielding
_ġealla_ [@Campbell1959]. Once the weak masculine input is chosen, the noun
follows a regular path to its attested Old English form.

The decisive issue is therefore morphological. Old English reflects the weak
noun, while the broader family label belongs to a different way of presenting
the cognate set.

#### Stem comparison

The comparison below is manual. It separates the broader comparative headword
from the weak noun formation actually reflected in Old English.

| Formation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| broader family label | *gállą | broader cognate-set headword | wider family context | useful lexeme label, but not the direct source of _ġealla_ |
| selected weak noun | *gállô | compact-trace output: _ġealla_ | ġealla | exact match between formation and attested OE noun |
| dialectal Anglian continuation | weak noun branch | Anglian _galla_ type | galla | genuine OE variant, but not the selected West Saxon target |

The weak-noun stem class is the relevant point. It gives a direct route to
attested _ġealla_, while the broader comparative label serves only as a family
heading.

### knight — OE cniht

Derivation: citation reconstruction _\*kníxtaz_; selected input _\*knéxtaz_ $\rightarrow$ _cniht_ (early analogy).

#### Derivation trace

Proto input: _\*knéxtaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*knéxta} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Final Bare A Loss & \emph{*knéxt} \\
OE Breaking & \emph{*knéoxt} \\
OE Ws Palatal Umlaut & \emph{*knixt} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _cniht_

#### Reconstruction and comparative evidence

The comparative sources align on an _e_-grade reconstruction for this noun:
Ringe and Taylor cite _\*kneht_, Orel gives _\*knextaz_, and Kluge-Seebold
likewise points to _\*knehta-_ [@RingeTaylor2014; @Orel2003, 256;
@KlugeSeebold2011]. The selected input _\*knéxtaz_ follows that comparative
evidence.

A competing citation reconstruction _\*kníxtaz_ remains possible as a label for
the word family, but it is not the reconstruction followed here. The Old
English development discussed below is based on _\*knéxtaz_.

#### Old English evidence

Old English dictionaries record the noun as _cniht_ [@ClarkHall1960;
@BosworthToller1898, 71]. Campbell's discussion of related forms such as plural
_cneohtas_ helps show the same vowel environment from another point in the
paradigm [@Campbell1959].

The target is therefore an ordinary attested Old English noun. No reconstructed
OE comparator is needed here.

#### Development to Old English

From _\*knéxtaz_, the relevant Old English changes include breaking before the
velar cluster and then the later reduction that yields _cniht_
[@Campbell1959; @SieversBrunner1965]. With that corrected input, the derivation
is straightforward.

#### Stem comparison

The comparison below is manual. It separates the handbook-supported _e_-grade
input from a competing citation reconstruction.

| Formation / label | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| competing citation reconstruction | *kníxtaz | not the reconstruction followed here | broader citation tradition | useful as a competing label, but not the source-based choice used for the OE derivation |
| handbook-supported reconstruction | *knéxtaz | compact-trace output: _cniht_ | cniht | exact match between comparative reconstruction and attested OE noun |
| related plural evidence | same stem family | plural _cneohtas_ type background | cneohtas | supports the vowel environment, but not the selected target cell |

### lade — OE hladan

Derivation: citation reconstruction _\*laθōjaną_; selected input _\*xláðaną_ $\rightarrow$ _hladan_ (early analogy).

#### Derivation trace

Proto input: _\*xláðaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Dental Hardening & \emph{*xládaną} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*xlædaną} \\
OE A Restoration & \emph{*xladaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*xladan} \\
OE Secondary Nasalization & \emph{*xladąn} \\
OE Weak Tail Reduction & \emph{*xladan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _hladan_

#### Reconstruction and comparative evidence

The wider Germanic family can be cited under a weak-verb label such as
_\*laθōjaną_, but the Old English verb _hladan_ belongs to a strong-verb line
with voiced consonantism in the selected input _\*xláðaną_
[@RingeTaylor2014; @Kroonen2013]. The two forms are related as members of one
word family, but they do not play the same role in the OE derivation.

The selected input therefore marks an early stem choice. The entry follows the
strong Verner-grade form that reaches Old English _hladan_ directly.

#### Old English evidence

Old English dictionaries record the verb as _hladan_ and preserve the expected
strong-verb paradigm material around it [@BosworthToller1898, 559; @ClarkHall1960].
The target is an attested infinitive rather than a reconstructed paradigm cell.

For this entry the relevant comparison form is the infinitive _hladan_ itself.
The question is how that attested strong verb relates to the broader comparative
family.

#### Development to Old English

From _\*xláðaną_, the verb passes through the expected early voiced stop stage,
Anglo-Frisian brightening, and the later A-restoration that returns the root
vowel to _a_ before the full infinitival ending [@Campbell1959;
@RingeTaylor2014]. The resulting Old English infinitive is _hladan_.

#### Class comparison

The comparison below is manual. It separates the wider weak-verb family label
from the strong verb actually reflected in Old English.

| Formation / class | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| comparative weak-verb label | *laθōjaną | wider family background | broader family context | useful family label, but not the direct source of _hladan_ |
| selected strong Verner-grade input | *xláðaną | compact-trace output: _hladan_ | hladan | exact match between formation and attested OE infinitive |

### lap — OE lappa

Derivation: citation reconstruction _\*lábbaz_; selected input _\*láppô_ $\rightarrow$ _lappa_ (early analogy).

#### Derivation trace

Proto input: _\*láppô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*læppô} \\
OE A Restoration & \emph{*lappô} \\
OE Unstressed Long Vowel Shortening & \emph{*lappa} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _lappa_

#### Reconstruction and comparative evidence

The comparative sources point to a weak noun with _pp_: Orel gives _\*lappōn_,
Kroonen places the word in a weak _\*lappan-_ family, and Kluge-Seebold cites
West Germanic _lappa_ forms alongside Old English _læppa_
[@Orel2003; @Kroonen2013; @KlugeSeebold2011]. The selected input _\*láppô_
follows that evidence.

A competing comparative label _\*lábbaz_ has also circulated for the word
family, but the cited handbooks do not make it the direct source of the Old
English weak noun. The form relevant to the OE development is the weak
masculine input _\*láppô_.

#### Old English evidence

Campbell cites _lappa_ as a case of restored _a_, while Sievers-Brunner records
_lappa_, variant _læppa_, and plural or oblique _leappan_
[@Campbell1959; @SieversBrunner1965]. The dictionary tradition also preserves
_læppa_ [@ClarkHall1960; @BosworthToller1898, 613].

The target of this entry is the restored singular _lappa_. The variant _læppa_
and the oblique or plural _leappan_ remain part of the Old English record and
help frame the noun's vowel history.

#### Development to Old English

From _\*láppô_, Anglo-Frisian brightening first yields _æ_, and later
A-restoration returns the root vowel to _a_ before the back-vocalic ending,
after which shortening of the final vowel gives _lappa_
[@Campbell1959; @SieversBrunner1965]. With the weak masculine input chosen, the
OE development is regular.

#### Stem comparison

The comparison below is manual. It separates the weak masculine formation from
a competing voiced comparative label.

| Formation / label | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| competing voiced comparative label | *lábbaz | not the form followed for the OE weak-noun derivation | broader comparative background | useful as a competing label, but not the source-based choice used here |
| selected weak masculine noun | *láppô | compact-trace output: _lappa_ | lappa | exact match between formation and attested OE noun |
| attested OE variant line | same noun family | _læppa_, _leappan_ | læppa / leappan | useful control forms within the same OE tradition |

### laugh — OE hliehhan

Derivation: citation reconstruction _\*lákaną_; selected input _\*xláxjaną_ $\rightarrow$ _hliehhan_ (early analogy).

#### Derivation trace

Proto input: _\*xláxjaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc J Gemination & \emph{*xláxxjaną} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*xlæxxjaną} \\
OE Breaking & \emph{*xleaxxjaną} \\
OE Velar Fricative Palatalization & \emph{*xleaxçjaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*xleaxçjan} \\
OE Secondary Nasalization & \emph{*xleaxçjąn} \\
OE I Umlaut & \emph{*xliexçjąn} \\
OE Weak Tail Reduction & \emph{*xliexçjan} \\
OE J Loss After Heavy & \emph{*xliexçan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _hliehhan_

#### Reconstruction and comparative evidence

The wider Germanic family includes a non-j branch represented here by the
citation label _\*lákaną_, but Kroonen and Ringe-Taylor both distinguish a
j-present formation behind Old English _hliehhan_ [@Kroonen2013;
@RingeTaylor2014]. The selected input _\*xláxjaną_ reflects that j-present line.

This branch choice matters because it brings with it the geminate fricative and
the vowel development characteristic of the Old English verb. The comparative
family label and the OE-facing input are therefore related but not identical.

#### Old English evidence

Old English dictionaries and readers record the verb as _hliehhan_, while also
preserving variants such as _hlæhhan_ and _hlehhan_
[@BosworthToller1898; @ClarkHall1960; @BrightCassidyRingler1971]. The target of
this entry is the West Saxon _hliehhan_.

The variant set matters as background, but the argument of the entry rests on
the attested lemma _hliehhan_ itself.

#### Development to Old English

From _\*xláxjaną_, regular j-gemination yields the doubled fricative, and the
subsequent Old English vowel developments lead to _hliehhan_
[@Fulk2018; @Campbell1959]. Ringe and Taylor discuss the broken vowel of the
Old English form as part of this same history, with possible support from the
related noun _hleahtor_ [@RingeTaylor2014].

#### Branch comparison

The comparison below is manual. It separates the wider non-j family label from
the j-present branch actually reflected in Old English.

| Formation / branch | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| wider non-j family | *lákaną | comparative background outside the selected OE line | wider family context | useful family label, but not the direct source of _hliehhan_ |
| selected j-present branch | *xláxjaną | compact-trace output: _hliehhan_ | hliehhan | exact match between branch and attested OE lemma |
| attested OE variants | same OE verb line | _hlæhhan_, _hlehhan_ | hlæhhan / hlehhan | genuine variant evidence, but secondary to the selected form |

### loam — OE lām

Derivation: citation reconstruction _\*laimōn_; selected input _\*láimą_ $\rightarrow$ _lām_ (early analogy).

#### Derivation trace

Proto input: _\*láimą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Ai Monophthongization & \emph{*lāmą} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*lām} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _lām_

#### Reconstruction and comparative evidence

The inherited comparative noun is given as _\*laimōn_ or _\*laiman-_, and both
Orel and Kroonen identify Old English _lām_ as a neuter reflex of that family
[@Orel2003; @Kroonen2013, 363]. The selected input _\*láimą_ differs from the
comparative headword because it represents the stem class that matches the Old
English noun most directly.

This is therefore a class shift within the history of the English branch rather
than a dispute about the OE target itself.

#### Old English evidence

Old English dictionaries record the noun as _lām_, a neuter word for 'loam,
clay, mud' [@BosworthToller1898; @ClarkHall1960, 196]. The target is an attested
citation form rather than a reconstructed comparator.

The relevant question is not whether _lām_ is Old English, but which inherited
formation best accounts for that attested neuter noun.

#### Development to Old English

From _\*láimą_, regular monophthongization of _ai_ and the later loss of the
final nasal syllable yield _lām_. With that OE-facing input, the phonological
development is straightforward.

#### Class comparison

The comparison below is manual. It separates the inherited comparative n-stem
label from the OE-facing stem class used to derive the attested noun.

| Formation / class | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| inherited comparative noun | *laimōn | comparative family background | wider family context | useful headword, but not the direct OE-facing input |
| selected OE-facing stem class | *láimą | compact-trace output: _lām_ | lām | exact match between input and attested OE noun |

### lung — OE lungen

Derivation: citation reconstruction _\*lungō_; selected input _\*lúnganjō_ $\rightarrow$ _lungen_ (early analogy).

#### Derivation trace

Proto input: _\*lúnganjō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc J Gemination & \emph{*lúngannjō} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc Final Long O Raising & \emph{*lúngannju} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE I Umlaut & \emph{*lúngennju} \\
OE High Vowel Apocope & \emph{*lúngennj} \\
OE J Loss After Heavy & \emph{*lúngenn} \\
OE Final Geminate Simplification & \emph{*lúngen} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _lungen_

#### Reconstruction and comparative evidence

Kroonen treats the basic noun as _\*lungōn-_ and also cites an OE-facing
derivative _\*lungunjō-_, continued by Old English _lungen_ and close West
Germanic cognates [@Kroonen2013]. The selected input _\*lúnganjō_ models that
derived feminine formation rather than the base noun. The notation differs
slightly from Kroonen's _\*lungunjō-_, but both point to the same derived
feminine line.

The difference between the citation label and the selected input is therefore
derivational. Old English _lungen_ is not a direct reflex of the bare base noun
_\*lungō_; it belongs to an expanded feminine formation.

#### Old English evidence

Old English dictionaries record the noun as _lungen_, with inflected forms such
as _lungenne_ and _lungena_ [@BosworthToller1898, 634]. Clark Hall also preserves a
small family of compounds such as _lungenādl_, _lungensealf_, and _lungenwyrt_
[@ClarkHall1960].

The target is an attested Old English lexeme with its own paradigm, not a
rescued inflectional cell.

#### Development to Old English

From the selected derived input, the expected derivational consonant and vowel
adjustments lead to _lungen_. Once the expanded feminine formation is chosen,
the Old English outcome is regular.

#### Formation comparison

The comparison below is manual. It separates the base noun from the derived
feminine formation reflected in Old English.

| Formation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| base noun | *lungō | base-noun outcome without the OE derivative suffix | broader family context | useful headword, but not the direct source of _lungen_ |
| derived OE-facing formation | *lúnganjō | compact-trace output: _lungen_ | lungen | exact match between selected formation and attested OE noun |
| Kroonen's cited derivative | _\*lungunjō-_ | comparative support for the same OE-facing formation | lungen and cognate set | supports the derived feminine formation, with notation differing from the normalized input form used here |

### navel — OE nafola

Derivation: citation reconstruction _\*nablô_; selected input _\*nábulô_ $\rightarrow$ _nafola_ (early analogy).

#### Derivation trace

Proto input: _\*nábulô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Med Unstressed U Lowering & \emph{*nábolô} \\
Anglo Frisian Brightening & \emph{*næbolô} \\
OE A Restoration & \emph{*nabolô} \\
PGmc B Allophony & \emph{*naβolô} \\
OE Unstressed Long Vowel Shortening & \emph{*naβola} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _nafola_

#### Reconstruction and comparative evidence

Kroonen lemmatizes the word with a syncopated comparative headword _\*nablô_,
while Ringe and Taylor give the derivational pathway _\*nabulō > \*næbula > nafola_ [@Kroonen2013; @RingeTaylor2014]. The difference is one of stage and
notation rather than of lexeme identity: the selected input _\*nábulô_ is the
pre-syncope form needed for the Old English development.

The literature also differs on the older history of the medial _u_, whether it
is inherited or secondary [@Streitberg1896; @Ringe2006; @Mayrhofer1992;
@SieversBrunner1965]. For the Old English comparison, however, both lines place
a medial vowel in the pre-OE form.

#### Old English evidence

The Old English record includes _nafola_, _nafela_, and Corpus _nabula_
[@RingeTaylor2014; @Campbell1959]. The target of this entry is the nominative
singular _nafola_, the form that matches the selected derivational pathway
most directly.

_nafela_ is the better-known later West Saxon spelling, while _nabula_ preserves
a less reduced medial vowel. These forms belong to the same lexical history, but
this entry is centered on _nafola_.

#### Development to Old English

From _\*nábulô_, the trace gives _\*nábolô_ by lowering of unstressed _u_, then
_\*næbolô_ by Anglo-Frisian brightening, followed by A-restoration to _\*nabolô_
[@RingeTaylor2014]. Intervocalic _b_ then surfaces as _f_, and final weak-tail
shortening gives _nafola_.

The medial vowel is still present when A-restoration applies. That is why the
selected pre-syncope input differs from the syncopated comparative headword.

#### Stage comparison

The comparison below is manual. It separates the comparative citation form from
the pre-syncope input and from the later OE spellings.

| Formation / stage | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| syncopated comparative headword | *nablô | reduced _næfla_-type outcome rather than _nafola_ | not the selected target | useful citation form, but too reduced for the pathway modeled here |
| selected pre-syncope input | *nábulô | compact-trace output: _nafola_ | nafola | exact match between selected input and target |
| later OE reduction stages | same lexical history | attested _nafela_; Corpus _nabula_ | nafela / nabula | related OE spellings, but not the chosen comparator |

### neck — OE hnecca

Derivation: citation reconstruction _\*xnákkaz_; selected input _\*xnékkô_ $\rightarrow$ _hnecca_ (early analogy).

#### Derivation trace

Proto input: _\*xnékkô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Unstressed Long Vowel Shortening & \emph{*xnékka} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _hnecca_

#### Reconstruction and comparative evidence

The noun belongs to an ablauting n-stem family. Kroonen reconstructs a paradigm
with nominative _\*hnekkō_, genitive _\*hnukkaz_, and accusative plural
_\*hnakkuns_, and he places Old English _hnecca_ among the e-grade descendants
[@Kroonen2011]. Kluge-Seebold likewise identifies _ae. hnecca_ as an ablaut
partner of the a-grade _Nacken_ family [@KlugeSeebold2011].

A competing comparative label _\*xnákkaz_ remains useful for the wider family, and
Orel also gives an a-grade headword line [@Orel2003]. The selected input
_\*xnékkô_, however, is the form that matches the Old English branch.

#### Old English evidence

Old English dictionaries record the weak masculine noun _hnecca_
[@ClarkHall1960; @BosworthToller1898, 567]. The target is therefore an attested
citation form, not an oblique cell or a reconstructed lemma.

The phonological question is upstream of the Old English evidence. The attested
noun already shows that the branch continued an e-grade form rather than the
a-grade seen in much of the continental material.

#### Development to Old English

From _\*xnékkô_, the derivation is straightforward. The trace shortens the final
long vowel to _\*xnékka_, and Old English orthography gives _hnecca_.

The derivation depends on the earlier selection of the e-grade weak-noun form
continued by Old English.

#### Stem comparison

The comparison below is manual. It separates the wider a-grade family from the
selected e-grade Old English branch.

| Formation / label | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| competing comparative label | *xnákkaz | broader a-grade family rather than the selected OE source | continental _Nacken_ line | useful family label, but not the input followed for the Old English derivation |
| weak noun with a-grade | *xnakkô | expected _hnacca_ type outcome | hnacca | fixes the class, but not the vowel grade |
| selected e-grade nominative | *xnékkô | compact-trace output: _hnecca_ | hnecca | exact match between selected input and attested OE noun |
| oblique paradigm background | _\*hnukkaz_, _\*hnakkuns_ | ON/OHG/German a-grade continuation | hnakki / Nacken | shows the wider ablaut family, but not the chosen OE branch |

### needle — OE nǣdl

Derivation: citation reconstruction _\*nḗθlō_; selected input _\*nḗðlō_ $\rightarrow$ _nǣdl_ (early analogy).

#### Derivation trace

Proto input: _\*nḗðlō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Dental Hardening & \emph{*nḗdlō} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc Final Long O Raising & \emph{*nḗdlu} \\
NWGmc Long E Lowering & \emph{*nǣdlu} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE High Vowel Apocope & \emph{*nǣdl} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _nǣdl_

#### Reconstruction and comparative evidence

Ringe and Taylor treat the word as a voiced/voiceless alternant, and Ringe also
cites the pair _\*nēþlō- ~ \*nēdlō-_ [@RingeTaylor2014; @Ringe2006]. The selected
input _\*nḗðlō_ is the voiced Verner-grade form used for the Old English
comparison, while the citation form _\*nḗθlō_ remains the broader lexeme label.

Kroonen and Orel preserve different comparative headwords for the family
[@Kroonen2013; @Orel2003]. The development discussed here follows the
Ringe-Taylor alternant framework.

#### Old English evidence

Old English has the attested citation form _nǣdl_ [@ClarkHall1960]. Campbell
lists _nédl_ among the expected unbroken forms after _t_ and _d_, and Hogg also
includes _nidi_ / _nǣdl_ in the same broader cluster history
[@Campbell1959; @Hogg1992].

The target is therefore an attested citation form. No oblique-cell substitution
is involved in this entry.

#### Development to Old English

From _\*nḗðlō_, the trace gives _\*nḗdlō_ by dental hardening, then _\*nḗdlu_,
_\*nǣdlu_, and finally _\*nǣdl_, hence _nǣdl_ [@RingeTaylor2014; @Campbell1959].

The essential choice lies in the PGmc alternant selected for the derivation.
Once the voiced form is chosen, the rest of the pathway is regular.

#### Alternant comparison

The comparison below is manual. It separates the broader citation headword from
the voiced alternant used for Old English.

| Formation / stage | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| comparative voiceless headword | *nḗθlō | broader word-family label rather than the OE-facing alternant | _\*nēþlō_ line | useful citation form, but not the selected input for the Old English derivation |
| selected voiced Verner alternant | *nḗðlō | compact-trace output: _nǣdl_ | nǣdl | exact match between selected input and attested OE noun |
| later hardening stage | *nḗdlō | intermediate pre-OE stage in the same derivation | nǣdl | genuine stage in the pathway, but not the selected PGmc input |

### nose — OE nosu

Derivation: citation reconstruction _\*nasō_; selected input _\*núsō_ $\rightarrow$ _nosu_ (early analogy).

#### Derivation trace

Proto input: _\*núsō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc U Lowering & \emph{*nósō} \\
NWGmc Final Long O Raising & \emph{*nósu} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\raggedright [no change]\par
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _nosu_

#### Reconstruction and comparative evidence

Kroonen reconstructs a Germanic ablaut pair _\*nasō- ~ \*nusō-_ and adds that the
root _\*nus-_ is likely to have arisen as a secondary zero grade after a
remodeling of the older paradigm [@Kroonen2013]. Campbell is more specific for
Old English, citing _nosu < \*nusō_ [@Campbell1959].

The citation reconstruction _\*nasō_ is therefore best treated as the full-grade
comparative headword, while the selected input _\*núsō_ represents the remodeled
zero-grade line continued by the Old English form discussed here. Orel's _\*nasō ... OE nasu_ preserves the competing full-grade notation and shows that the two
lines should not be collapsed without comment [@Orel2003].

#### Old English evidence

_Nosu_ is an attested Old English noun. Ringe and Taylor list it among the few
surviving early Old English feminine u-stems [@RingeTaylor2014]. Clark Hall
likewise gives _nosu f._, with genitive-dative singular _nosa_, and cross-refers
_nasu_ to _nosu_ [@ClarkHall1960].

The selected OE target is therefore an attested _nosu_, not a reconstructed
placeholder. At the same time, the lexicographical record keeps _nasu_ visible as
a parallel notation belonging to the full-grade side of the tradition.

#### Development to Old English

From _\*núsō_, the regular path is the one documented by the current trace:
_\*núsō > \*nósō > \*nósu > nosu_. The early special step lies in the choice of the
zero-grade input, not in any late Old English repair.

With that input chosen, the OE development is straightforward. The full-grade
line behind _\*nasō_ instead points toward _nasu_, not to the form treated here.

#### Stem comparison

The comparison below is manual. It separates the full-grade comparative line
from the remodeled zero-grade input that yields the Old English form.

| Formation / label | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| full-grade comparative line | *nasō | expected full-grade continuation _nasu_ | nasu | useful comparative background, but not the selected OE-facing input |
| remodeled zero-grade line | *núsō | compact-trace output: _nosu_ | nosu | exact match between selected input and attested OE noun |

### sap — OE sæp

Derivation: citation reconstruction _\*sapōn_; selected input _\*sápą_ $\rightarrow$ _sæp_ (early analogy).

#### Derivation trace

Proto input: _\*sápą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*sæpą} \\
OE Heavy Syllable Nasal Apocope & \emph{*sæp} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _sæp_

#### Reconstruction and comparative evidence

The comparative sources do not give one uniform inherited stem. Kroonen derives
the word family from material pointing to dialectal dissolution of a primary
n-stem _\*safō, gen. \*sappaz_ [@Kroonen2013]. Orel preserves the comparative
notation _\*sapōn ~ \*sapan_ [@Orel2003], while Kluge-Seebold instead gives West
Germanic _\*sapi-_ and still cites Old English _sæp n._ [@KlugeSeebold2011].

The selected input _\*sápą_ therefore does not replace those comparative labels.
It identifies the OE-facing stem shape that yields the attested noun treated
here.

#### Old English evidence

Clark Hall records _sæp (e) n._ [@ClarkHall1960], and Kluge-Seebold likewise
cites _ae. sæp n._ [@KlugeSeebold2011]. The target is therefore an attested
neuter Old English noun. Orel's plain _sap_ notation belongs to comparative
normalization, not to the spelling adopted here for the Old English form
[@Orel2003].

#### Development to Old English

From _\*sápą_, Anglo-Frisian brightening yields _sæ_, and heavy-syllable nasal
apocope then produces _sæp_. That is the regular path documented by the current
trace.

The competing comparative lines do not give the same result. The inherited
n-stem notation _\*sapōn_ yields _sape_, while an i-stem continuation from the
_\*sapi-_ line leads to _sep / sepe_ rather than to _sæp_. The special step in
this entry is therefore the early stem choice, not a late OE paradigm-cell
selection.

#### Stem comparison

The comparison below is manual. It separates the competing comparative stem lines
from the selected OE-facing input.

| Formation / label | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| comparative n-stem line | *sapōn | local comparator output: _sape_ | sape | useful comparative background, but not the source of attested _sæp_ |
| inferred i-stem comparator from _\*sapi-_ | *sapiz | local comparator output: _sepe_ | sepe | confirms that an i-triggering stem does not reach the target |
| selected a-stem input | *sápą | compact-trace output: _sæp_ | sæp | exact match between selected input and attested OE noun |

### sea — OE sǣ

Derivation: citation reconstruction _\*sái_; selected input _\*sáiwiz_ $\rightarrow$ _sǣ_ (early analogy).

#### Derivation trace

Proto input: _\*sáiwiz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Ai Monophthongization & \emph{*sāwiz} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*sāwi} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE W Loss Before I & \emph{*sāi} \\
OE I Umlaut & \emph{*sǣi} \\
OE High Vowel Apocope & \emph{*sǣ} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _sǣ_

#### Reconstruction and comparative evidence

Kroonen gives the noun in stem notation as _\*saiwi-_, an i-stem whose English
reflex is cited as OE _sæ_ [@Kroonen2013]. Ringe and Taylor write the fuller
form _\*saiwiz_ and derive it through _\*sawi > \*sei > OE sǣ_
[@RingeTaylor2014, §6.7.1]. The comparative headword is therefore shorter than
the form required for the English history: _\*sái_ names the lexeme, but
_\*sáiwiz_ preserves the medial _\*w_ and the final high vowel that control the
later development.

#### Old English evidence

The Old English noun is the ordinary word for ‘sea’. Kroonen cites it as _sæ_;
the normalized form here is _sǣ_ [@Kroonen2013]. Campbell likewise treats
_sea_ as continuing the same _\*saiui- > \*sǣi_ history, with loss of _u/w_
before _i_ [@Campbell1959, §406].

#### Development to Old English

Once the fuller i-stem input is chosen, the development is regular. After
Proto-West-Germanic monophthongization _\*sáiwiz > \*sāwiz_ and final _\*-z_ loss
_\*sāwiz > \*sāwi_, the non-initial _\*w_ disappears before unstressed _\*i_, and
the following high vowel fronts the root vowel before final apocope. The
documented chain is _\*sáiwiz > \*sāwiz > \*sāwi > \*sāi > \*sǣi > sǣ_
[@RingeTaylor2014, §6.7.1; @Campbell1959, §406].

#### Stem and stage comparison

The comparison below is manual. It separates the abbreviated comparative
headword from the fuller i-stem input that yields the Old English form.

| Formation / label | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| abbreviated comparative headword | *sái | too short to preserve the _\*w ... \*i_ environment needed for the documented chronology | sǣ | useful comparative label, but not the selected OE-facing input |
| selected i-stem input | *sáiwiz | documented trace output: _sǣ_ | sǣ | exact match between selected input and Old English target |

### sieve — OE sife

Derivation: citation reconstruction _\*síbaz_; selected input _\*síbi_ $\rightarrow$ _sife_ (early analogy).

#### Derivation trace

Proto input: _\*síbi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc B Allophony & \emph{*síβi} \\
OE Med Unstressed I Lowering1 & \emph{*síβe} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _sife_

#### Reconstruction and comparative evidence

Kluge-Seebold gives _wg. \*sibi- n. ... ae. sife_, and Campbell groups _sife_
with short neuter i-stems such as _spere_ [@KlugeSeebold2011;
@Campbell1959, §609]. The older morphological background is the s-stem
_\*sib-iz_, but the selected input is the normalized i-stem form _\*síbi_.

Kroonen's relevant nearby entry is not ‘sieve’ but _\*sebjō-_ ‘kinship’, the
source of Old English _sibb_ [@Kroonen2013]. Orel's _\*sibaz ... OE sife_
preserves a broader handbook notation, but that a-stem shape does not fit the
Old English form treated here [@Orel2003].

#### Old English evidence

Clark Hall gives _sibi (GL) ... = sife_ and also _sife n. ‘sieve’_
[@ClarkHall1960]. Campbell likewise cites Corpus Glossary _sibi_ and treats
_sife_ as a short neuter i-stem [@Campbell1959, §§444, 609]. The normalized
Old English target is therefore _sife_, while _sibi_ is an attested earlier
spelling rather than a separate lexeme.

#### Development to Old English

From _\*síbi_, the documented trace gives _\*síβi > \*síβe > sife_. Medial _b_
is realized as a spirant and later written _f_, while the final unstressed _i_
lowers to _e_. The older s-stem background _\*sib-iz_ explains the morphology,
but the selected input _\*síbi_ is the immediate pre-Old-English form.

#### Stem comparison

The comparison below is manual. It distinguishes the accepted i-stem line from
its rejected competitors.

| Formation / label | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| ja-stem kinship line | Kroonen _\*sebjō-_ / comparator _\*sibja_ | OE _sibb_ | sibb | separate lexeme, not the target treated here |
| a-stem handbook line | *síbaz | expected _sif_ | sif | wrong ending for the attested noun |
| selected i-stem line from older _\*sib-iz_ | *síbi | documented trace output: _sife_ | sife; early spelling _sibi_ | exact match between selected input and Old English evidence |

### spare — OE sparian

Derivation: citation reconstruction _\*sparēną_; selected input _\*spárōjaną_ $\rightarrow$ _sparian_ (early analogy).

#### Derivation trace

Proto input: _\*spárōjaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*spærōjaną} \\
OE A Restoration & \emph{*sparōjaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*sparōjan} \\
OE Secondary Nasalization & \emph{*sparōjąn} \\
OE I Umlaut & \emph{*sparējąn} \\
OE Unstressed Long Vowel Shortening & \emph{*sparejąn} \\
OE Weak Tail Reduction & \emph{*sparejan} \\
OE Intervocalic J Vocalization & \emph{*spareian} \\
OE Unstressed EI Contraction & \emph{*sparian} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _sparian_

#### Reconstruction and comparative evidence

Kroonen and Orel keep the inherited verb under class-III _\*sparēn- / \*sparēnan_ [@Kroonen2013; @Orel2003]. Ringe and Taylor, however, reconstruct
_\*sparai- ~ \*sparja-_ for the English branch and derive the citation verb from a
class-II line [@RingeTaylor2014, pp. 162, 191]. The selected input
_\*spárōjaną_ therefore represents the refashioned class-II formation behind Old
English _sparian_, while the citation reconstruction _\*sparēną_ remains the
inherited comparative headword.

#### Old English evidence

Campbell says that _sparian_ does not show the ordinary class-III
characteristics, but the Ritual forms, normalized here as _spæria_, _spær_, and
_spærede_, together with Vespasian Psalter _spearad_, point to primitive Old
English forms both with and without back vowels [@Campbell1959, §764]. Brunner likewise records
Northumbrian _spæria_, _spærede_ beside common Old English _sparian_ and
Vespasian Psalter _spearad_ [@SieversBrunner1965, §364 Anm. 11]. The citation
form treated here is _sparian_; the Anglian forms are relics of the older
formation, not alternative headwords of equal status.

#### Development to Old English

Once the class-II formation _\*spárōjaną_ is chosen, the remaining development is
regular. The documented trace shows brightening, restoration of _a_ before the
back vocalism of the suffix, later i-mutation within the weak ending, weak-tail
reduction, and contraction to _sparian_. By contrast, Brunner's rule against
further apocope of final _-e_ explains why Ritual _spær_ cannot be the regular
continuation of inherited _\*spárē_ [@SieversBrunner1965, §150].

#### Formation comparison

The comparison below is manual. It contrasts the inherited class-III formation
with the refashioned class-II one that yields the citation verb.

| Formation / comparison | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| inherited class-III infinitive | *spárēną | manual comparison / probe output: _sparen_ | sparian | wrong class and wrong ending for the citation verb |
| inherited class-III imperative singular | *spárē | manual comparison / probe output: _spære_ | Ritual _spær_ | loss of final _-e_ is not regular, so the relic form cannot control the entry |
| inherited class-III finite present | *spárēθi | manual comparison / probe output: _spæreþ_ | _spearad_ | attested form is mixed, not a direct continuation of the inherited cell |
| selected class-II formation | *spárōjaną | documented trace output: _sparian_ | sparian | exact match between selected input and Old English citation form |

### staff — OE stæf

Derivation: citation reconstruction _\*stábiz_; selected input _\*stábaz_ $\rightarrow$ _stæf_ (early analogy).

#### Derivation trace

Proto input: _\*stábaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*stába} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Final Bare A Loss & \emph{*stáb} \\
Anglo Frisian Brightening & \emph{*stæb} \\
PGmc B Allophony & \emph{*stæβ} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _stæf_

#### Reconstruction and comparative evidence

The comparative dictionaries do not give one uniform stem class. Kroonen
reconstructs an a-stem _\*staba-_ [@Kroonen2013], Orel writes _\*stabiz ~ \*stabaz_ [@Orel2003], and Kluge-Seebold explicitly marks _g. \*stabi-/a-_
[@KlugeSeebold2011]. That disagreement matters because a direct i-stem input in
_\*-iz_ would predict i-mutation in Old English, whereas the attested noun keeps
_æ_.

#### Old English evidence

The Old English noun itself is the ordinary citation form _stæf_. Luick lists
_stæf_ among closed monosyllables with _æ_ [@Luick1914, p. 176], and Ringe and
Taylor pair singular _stæf_ with plural _stafas_ [@RingeTaylor2014]. The
normalized form here is therefore _stæf_; later English _staff_ with _a_
belongs to a later stage of the word's history.

#### Development to Old English

With the selected a-stem input, the development is regular. Final _\*-z_
disappears, bare final _-a_ is lost, Anglo-Frisian brightening gives _æ_ in the
closed monosyllable, and medial _b_ surfaces as a fricative written _f_. The
documented chain is _\*stábaz > \*stába > \*stáb > \*stæb > stæf_. A direct
continuation of _\*stábiz_, by contrast, would produce i-mutated _stefe_ rather
than the attested singular.

#### Formation comparison

The comparison below is manual. It separates the rejected i-stem line from the
selected a-stem input.

| Formation / label | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| comparative i-stem line | *stábiz | expected _stefe_ after i-mutation | stæf | wrong vowel for the attested singular |
| mixed comparative notation | Orel _\*stabiz ~ \*stabaz_; Kluge _\*stabi-/a-_ | source-level stem-class uncertainty | stæf | useful comparative background, but not a single OE-facing input |
| selected a-stem input | *stábaz | documented trace output: _stæf_ | stæf | exact match between selected input and Old English target |

### stem — OE stefn

Derivation: citation reconstruction _\*stámnaz_; selected input _\*stébnō_ $\rightarrow$ _stefn_ (early analogy).

#### Derivation trace

Proto input: _\*stébnō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc Final Long O Raising & \emph{*stébnu} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc B Allophony & \emph{*stéβnu} \\
OE High Vowel Apocope & \emph{*stéβn} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _stefn_

#### Reconstruction and comparative evidence

The source tradition behind _stefn_ is not the same as the comparative label
_\*stámnaz_. Ringe and Taylor cite _\*stebnō_ for the noun continued by
Gothic _stibna_ and Old English _stebn > stefn > stemn_ [@RingeTaylor2014, p.
330]. Orel likewise gives _\*stebnō ~ \*stemnō_, whereas Kroonen prefers
_\*stimnō-_, and Fulk describes the etymology of _stefn, stemn_ as insecure
[@Orel2003, p. 374; @Kroonen2013, p. 480; @Fulk2018, §6.11 n. 6].

These forms belong to the Old English noun _stefn_ 'voice, sound'. The
selected input _\*stébnō_ is therefore best treated as the OE-facing
transponent supported by that source tradition. It does not settle the deeper
comparative reconstruction implied by the citation label _\*stámnaz_.

#### Old English evidence

Clark Hall records _stefn_ as the noun 'voice, sound' and cross-refers
_stemn_ to the same word [@ClarkHall1960]. Ringe and Taylor give the OE
chronology directly as _stebn > stefn > stemn_ [@RingeTaylor2014, p. 330].

Bülbring and Luick treat _stemn_ as a later West Saxon development from
older _stefn_, produced by _fn > mn_ only after the earlier period of nasal
influence on _e_ [@Bulbring1902, §§62 Anm. 3, 445; @Luick1914, §75 Anm. 1].
The relevant comparison form is therefore the conservative _stefn_, not the
later West Saxon doublet _stemn_.

#### Development to Old English

From _\*stébnō_, raising of final long _ō_ gives a _\*stébnu_ stage.
Regular fricativization of _b_ before _n_ then yields _\*stéβnu_, and loss
of the final high vowel leaves _\*stéβn_, written _stefn_ in Old English.
The later form _stemn_ belongs to a separate West Saxon assimilation after
this stage [@RingeTaylor2014, p. 330; @Bulbring1902, §445].

#### Source comparison

The comparison below is manual. It keeps apart the broader comparative label,
the OE-facing transponent, and the later West Saxon variant history.

| Form or label | Status | OE relation | Result |
| :--- | :--- | :--- | :--- |
| _\*stámnaz_ | comparative citation label for the broader stem/trunk family | does not itself control the _stefn_ derivation discussed here | broader lexical label only |
| _\*stébnō_ | voice-noun transponent | trace output: _stefn_ | selected OE-facing input |
| _stemn_ | later attested West Saxon doublet | secondary form from _stefn_ by _fn > mn_ | real OE variant, but not the selected comparator |

### swan — OE swanes

Derivation: citation reconstruction _\*swánaz_; selected input _\*swánas_ $\rightarrow$ _swanes_ (early analogy).

#### Derivation trace

Proto input: _\*swánas_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*swánæs} \\
OE Unstressed AE Merger & \emph{*swánes} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _swanes_

#### Reconstruction and comparative evidence

The Germanic noun is ordinarily cited as the masculine a-stem _\*swanaz_
[@Orel2003, p. 367]. The selected input _\*swánas_ is not a competing
lexeme reconstruction. It is the **genitive singular** of the same paradigm.

The question here is therefore one of paradigm cell rather than stem history.
The citation form remains _\*swanaz > swan_; the selected comparison form is the
genitive singular _\*swánas > swanes_.

#### Old English evidence

Old English dictionaries give the ordinary headword as _swan_
[@ClarkHall1960]. Bright's glossary, however, also records the exact inflected
form _swanes_, glossing _swan, m., swan: gs. swanes_ and citing the phrase
_swanes feðre_ [@BrightCassidyRingler1971].

The target is therefore an **attested Old English genitive singular**, not a
reconstruction. It is also not the ordinary citation lemma. The entry must keep
those two facts distinct.

#### Development to Old English

From _\*swánas_, Anglo-Frisian brightening gives _\*swánæs_, and
subsequent merger of unstressed _æ_ with _e_ yields _swanes_. The
comparison is straightforward once the genitive singular is chosen as the
relevant cell.

#### Paradigm-cell comparison

The comparison below is manual. It separates the ordinary citation form from the
selected inflected cell.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | *swánaz | OE headword _swan_ | swan | ordinary lexeme line |
| selected genitive singular | *swánas | trace output: _swanes_ | swanes | selected attested cell |

### thousand — OE þūsend

Derivation: citation reconstruction _\*θūs-undī_; selected input _\*θūs-èndi_ $\rightarrow$ _þūsend_ (early analogy).

#### Derivation trace

Proto input: _\*θūsèndi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Early I Apocope & \emph{*θūsènd} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Strip Secondary Stress & \emph{*θūsend} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _þūsend_

#### Reconstruction and comparative evidence

Kroonen reconstructs the Germanic numeral as _\*þūsundī-_ and cites Old
English _þūsend_ among its continuations [@Kroonen2013, p. 554]. The
selected input _\*θūs-èndi_ is not the same claim. It is an OE-oriented
transponent with the second-member vowel already resolved to _e_ and the final
high vowel already shortened for apocope.

The important question is therefore chronological. Why does Old English show
_þūsend_, while related languages such as Old Saxon and Old High German keep
_u_ in the second syllable? [@Kroonen2013, p. 554].

#### Old English evidence

Old English _þūsend_ is an ordinary citation form, not a selected oblique or
paradigm cell. Campbell treats it as a neuter noun with normal case forms
[@Campbell1959, §689]. The problem lies in the internal history of the word, not
in its lexical status.

#### Development to Old English

If the old final _-ī_ had remained long enough to trigger ordinary double
umlaut, Campbell's rule would point toward a form of _\*þȳsend_ type rather
than attested _þūsend_ [@Campbell1959, §203]. Preserved root _ū_
therefore argues that the umlaut-triggering vowel was lost or neutralized before
the ordinary OE umlaut outcome could develop.

That early loss, however, does not by itself explain the medial _e_. Luick
compares the word with _ærende_ and later groups _thousand_ with forms
reshaped on that pattern [@Luick1914, §§198, 492]. Viredaz is more cautious,
arguing that Old English _e_ in this weak position may simply write schwa and so
need not prove a unique _ærende_-type analogy [@GermanicSlavicBaltic2025,
§2.1.4].

The selected transponent _\*θūs-èndi_ captures the OE-side state from which
the documented trace reaches _þūsend_.

#### Stage comparison

The comparison below is manual. It separates the secure chronology from the more
interpretive account of the second-syllable vowel.

| Stage / interpretation | Candidate form | OE relation | Result |
| :--- | :--- | :--- | :--- |
| surviving _-ī_ with ordinary double umlaut | _\*þūsundī-_ treated as still umlaut-active in OE | would point toward _\*þȳsend_ | excluded by preserved _ū_ |
| early loss of the trigger without further reshaping | _\*þūsund-_ type | explains _ū_, but not why OE alone has medial _e_ | incomplete account |
| selected OE-oriented transponent | _\*θūs-èndi_ | trace output: _þūsend_ | selected modeling input |

### timber — OE timber

Derivation: citation reconstruction _\*tímrą_; selected input _\*tímbrą_ $\rightarrow$ _timber_ (early analogy).

#### Derivation trace

Proto input: _\*tímbrą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*tímbr} \\
OE Epenthetic Vowel & \emph{*tímber} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _timber_

#### Reconstruction and comparative evidence

Kroonen reconstructs the noun as _\*timbra-_ and cites Old English
_timber_ among its continuations [@Kroonen2013]. Ringe and Taylor instead
state the history from _PGmc \*timra_ through West Germanic _\*timbr_ to
Old English _timber_ [@RingeTaylor2014].

The difference is therefore not over the Old English noun itself. It concerns
whether medial _b_ belongs in the comparative citation form or appears in an
early pre-Old-English stage of the cluster.

#### Old English evidence

Clark Hall lemmatizes the noun as _timber_ and also records _timbor_ as
a variant spelling [@ClarkHall1960]. The Old English form is thus an ordinary
citation noun, not a selected oblique cell or a reconstructed convenience form.

#### Development to Old English

With the consonantal frame _timbr-_ in place, the rest of the development is
straightforward. Loss of final _-ą_ leaves _\*tímbr_, and epenthetic
_e_ in the final cluster yields _timber_. Ringe and Taylor's
_\*timra > \*timbr > OE timber_ and the handbook treatment of this epenthetic
vowel point to the same Old English result [@RingeTaylor2014; @Campbell1959,
§§463-464].

#### Formation comparison

The comparison below is manual. It separates the comparative headword from the
OE-facing consonantal input.

| Formation or notation | Candidate form | OE relation | Result |
| :--- | :--- | :--- | :--- |
| Kroonen's comparative citation | _\*timbra-_ | already matches the consonantal frame of OE _timber_ | closest comparative support for the selected input |
| Ringe-Taylor citation line | _\*timra > \*timbr_ | reaches the same OE noun through early cluster expansion | compatible comparative background |
| modeled input | _\*tímbrą_ | trace output: _timber_ | selected OE-facing input |

### wake — OE wacan

Derivation: citation reconstruction _\*wakēną_; selected input _\*wákaną_ $\rightarrow$ _wacan_ (early analogy).

#### Derivation trace

Proto input: _\*wákaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*wækaną} \\
OE A Restoration & \emph{*wakaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*wakan} \\
OE Secondary Nasalization & \emph{*wakąn} \\
OE Weak Tail Reduction & \emph{*wakan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _wacan_

#### Reconstruction and comparative evidence

Kroonen gives the strong verb as _\*wakan-_ with Old English
_wacan_ [@Kroonen2013]. Ringe and Taylor separately derive Old English
_wacian_ from weak _\*wakai- ~ \*wakja-_ [@RingeTaylor2014, §3.3.2].

The difference is therefore lexical and class-based, not graphic. Strong
_wacan_ 'wake up, arise' and weak _wacian_ 'be awake, watch' belong to
related but distinct histories.

#### Old English evidence

Clark Hall keeps _wacan_ and _wacian_ as separate headwords
[@ClarkHall1960]. Bosworth-Toller adds an important caution under
_wacan_: the simplex infinitive itself does not occur, its place seeming to
be taken by _wæcnan_ [@BosworthToller1898, 226].

The target _wacan_ is therefore best understood as a normalized strong
headword for the verb family, not as a directly quoted simplex infinitive. It
still remains the correct Old English comparison form for the strong branch.

#### Development to Old English

With strong _\*wákaną_, Anglo-Frisian brightening first gives a form of the
_\*wækaną_ type. A-restoration then returns _a_, and the ordinary tail
reductions yield _wacan_. The weak verb _wacian_ belongs to a different
prehistory and is not the expected outcome of this input.

#### Class comparison

The comparison below is manual. It separates the strong and weak verb lines.

| Formation / class | Candidate input | OE outcome or comparison | Result |
| :--- | :--- | :--- | :--- |
| weak class-III / class-II branch | _\*wakēną_, _\*wakai- ~ \*wakja-_ | OE _wacian_ and related weak forms | related lexeme, but not the target of this entry |
| strong class-VI branch | _\*wákaną_ | trace output: _wacan_ | selected OE-facing input |
| strong normalized headword | _wacan_ | dictionary comparison form beside attested strong-family forms | correct Old English comparator, though not a directly quoted simplex infinitive |

### water — OE wæter

Derivation: citation reconstruction _\*wátną_; selected input _\*wátōr_ $\rightarrow$ _wæter_ (early analogy).

#### Derivation trace

Proto input: _\*wátōr_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Final Or Lowering & \emph{*wátar} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*wætær} \\
OE Unstressed AE Merger & \emph{*wæter} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _wæter_

#### Reconstruction and comparative evidence

Kroonen reconstructs a heteroclitic noun _\*watar-~\*watan-_ and states that
the Proto-Germanic material points to _\*watōr, \*watenaz_
[@Kroonen2013, p. 616]. Ringe and Taylor likewise start from singular
_\*wator_ before the Old English branch [@RingeTaylor2014, §3.1.4].

The generalized comparative label is therefore broader than the singular
form that actually corresponds to Old English _wæter_. The relevant
comparator is the inherited nominative-accusative singular _\*wátōr_.

#### Old English evidence

Bright gives the noun as _wæter_ with the regular paradigm
_wæteres, wætere, wæter(u), wætera, wæterum_
[@BrightCassidyRingler1971]. Ringe and Taylor add the dialectal contrast
between West Saxon _weeter_ and Mercian _weter_
[@RingeTaylor2014, §6.5.2].

The target is therefore an attested Old English citation form within a normal
paradigm. The complication lies on the comparative side of the lexeme, not in
Old English attestation.

#### Development to Old English

From _\*wátōr_, pre-final _\*ō_ becomes _a_ before final _r_,
yielding _\*watar_ [@RingeTaylor2014, §3.1.4]. Anglo-Frisian brightening then
gives _\*wætær_, and merger of unstressed _æ/e_ yields _wæter_.

#### Stage comparison

The comparison below is manual. It separates the generalized lexeme label from
the singular input that matches the Old English citation form.

| Stage or notation | Candidate form | OE relation | Result |
| :--- | :--- | :--- | :--- |
| generalized comparative label | _\*wátną_ | broader lexeme shorthand, not the singular that corresponds directly to _wæter_ | useful background only |
| heteroclitic stem notation | _\*watar-~\*watan-_ | source-faithful comparative reconstruction | explains why a singular comparator is needed |
| inherited singular input | _\*wátōr_ | trace output: _wæter_ | selected OE-facing input |

### whale — OE hwæl

Derivation: citation reconstruction _\*wálaz_; selected input _\*xwálaz_ $\rightarrow$ _hwæl_ (early analogy).

#### Derivation trace

Proto input: _\*xwálaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*xwála} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Final Bare A Loss & \emph{*xwál} \\
Anglo Frisian Brightening & \emph{*xwæl} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _hwæl_

#### Reconstruction and comparative evidence

The comparative sources are not uniform. Orel gives _\*xwalaz_ and notes some
mixed _\*xwaliz_ evidence [@Orel2003]. Kroonen instead cites
_\*hwali-_ [@Kroonen2013].

Both notations agree on inherited initial _hw-/xw-_, but they differ in
stem label. The a-stem-like input followed here is closer to Orel's notation
than to Kroonen's citation form.

#### Old English evidence

Clark Hall lemmatizes the noun as _hwal_, and Bosworth-Toller preserves the
plural _hwalas_ [@ClarkHall1960; @BosworthToller1898, 326]. The comparison form
is normalized here as _hwæl_ for the singular citation form with Anglo-
Frisian fronting.

The plural _hwalas_ remains important control evidence. It shows the same
lexeme with _a_ in an open syllable, beside singular _hwæl_ in the
closed monosyllable.

#### Development to Old English

From _\*xwálaz_, final _-z_ disappears and bare final _-a_ is lost.
Anglo-Frisian fronting then yields _æ_ in the closed monosyllable, and Old
English orthography writes _hwæl_.

#### Formation comparison

The comparison below is manual. It separates the competing comparative
notations from the normalized Old English singular.

| Comparative line | Candidate form | OE relation | Result |
| :--- | :--- | :--- | :--- |
| Orel's citation | _\*xwalaz_ | same stem notation as the modeled singular line | closest comparative support for the selected input |
| Kroonen's citation | _\*hwali-_ | same initial cluster, different stem label | important comparative rival, but not the notation followed here |
| modeled input | _\*xwálaz_ | trace output: _hwæl_ | selected OE-facing input |
| plural control | _hwalas_ | attested open-syllable plural beside singular _hwæl_ | confirms that the lexeme also preserves an _a_-vocalism branch |

### whine — OE hwīnan

Derivation: citation reconstruction _\*wainōjaną_; selected input _\*xwḯnaną_ $\rightarrow$ _hwīnan_ (early analogy).

#### Derivation trace

Proto input: _\*xwḯnaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Heavy Syllable Nasal Apocope & \emph{*xwḯnan} \\
OE Secondary Nasalization & \emph{*xwḯnąn} \\
OE Weak Tail Reduction & \emph{*xwḯnan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _hwīnan_

#### Reconstruction and comparative evidence

The citation reconstruction preserved in the header belongs to the lament-family
verb seen in German _weinen_ and Old English _wānian_. Kroonen instead separates
Old English _hwīnan_ under _\*hwinan-_, and Orel likewise distinguishes strong
_\*xwinanan_ from weak _\*wainōjanan_ [@Kroonen2013; @Orel2003]. Ringe and
Taylor make the same split at the Northwest Germanic level, linking Old Norse
_hvina_ and Old English _hwinan_ to the same strong verb [@RingeTaylor2014].

The difference affects both phonology and morphology. The lament family has
initial _w-_, diphthongal _ai_, and weak-II morphology, whereas the verb behind
Old English _hwīnan_ has initial _hw-/xw-_, long _ī_, and strong-verb
inflection [@Kroonen2013; @Orel2003]. The selected input _\*xwḯnaną_ therefore
represents a competing comparative identification rather than a hidden cell of
_\*wainōjaną_.

#### Old English evidence

Clark Hall records _hwinan_ with the gloss 'to hiss, whizz, whistle'
[@ClarkHall1960]. Seebold keeps the verb among the strong verbs and notes that
only a present-tense attestation is directly preserved, while Sievers-Brunner
likewise lists _hwinan stv._ [@Seebold1970; @SieversBrunner1965].

The Old English form is normalized here as _hwīnan_. That normalization adds the
usual vowel length marking to the dictionary spelling _hwinan_; it does not turn
an unattested verb into a reconstructed one.

#### Development to Old English

Once the strong-verb input _\*xwḯnaną_ is selected, the path to Old English is
straightforward. The compact trace shows heavy-syllable nasal apocope,
secondary nasalization, and weak-tail reduction, after which the form surfaces
as _hwīnan_.

No special paradigm maneuver is needed for this verb. The comparison is between
two different Germanic verb families: the Old English form belongs with the
strong verb _\*hwīnan-_, not with the weak lament verb.

#### Verb-family comparison

The comparison below is manual. It separates the competing comparative labels
that stand behind the inherited Old English forms.

| Verb family / interpretation | Candidate input | Old English outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lament-family weak verb | _\*wainōjaną_ | comparative continuation in OE _wānian_ | wānian | competing citation reconstruction, but not the source of _hwīnan_ |
| selected strong verb | _\*xwḯnaną_ | compact-trace output: _hwīnan_ | hwīnan | exact match between selected input and OE verb |
| comparative North Germanic cognate | Northwest Germanic strong verb behind ON _hvina_ / OE _hwinan_ | ON _hvina_ / OE _hwinan_ | hwīnan | supports the strong-verb identification |

### withy — OE wīþiġ

Derivation: citation reconstruction _\*wáiθiz_; selected input _\*wḯθagą_ $\rightarrow$ _wīþiġ_ (early analogy).

#### Derivation trace

Proto input: _\*wḯθagą_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*wḯθægą} \\
OE Heavy Syllable Nasal Apocope & \emph{*wḯθæg} \\
OE Velar Palatalization & \emph{*wḯθæʤ} \\
OE Unstressed AE Merger & \emph{*wḯθeʤ} \\
OE Late Unstressed Ag Suffix & \emph{*wḯθiʤ} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _wīþiġ_

#### Reconstruction and comparative evidence

The comparative evidence groups the word with Germanic forms of the
_\*wīþja/ō-_ or _\*wiþ-_ type [@KlugeSeebold2011; @Orel2003]. That material is
useful for the cognate set, but it does not by itself explain the Old English
suffix of _wīþiġ_.

For Old English, the relevant point is the suffix history. Campbell's account
of OE _-ig_, including forms such as _hunig_, supports an analysis in which the
_-iġ_ of _wīþiġ_ continues a derivational _\*-ag-_ sequence rather than a heavy
ja-stem _\*-ij-_ [@Campbell1959, §§275, 376]. The earlier ja-stem pathway
remains useful as a comparative possibility, but the Campbell-Adamczyk line on
heavy ja-stems points instead toward _-e_ or zero type outcomes
[@Campbell1959; @Adamczyk2001]. The selected input _\*wḯθagą_ is thus a
formation choice rather than a mere respelling of the comparative headword.

#### Old English evidence

Clark Hall records the noun as _wiðig_, with related inflected forms of the
same lexical base [@ClarkHall1960]. The form used here, _wīþiġ_, is a
normalized Old English spelling with macrons and palatal _<ġ>_.

The relevant comparison form is therefore not a reconstructed dictionary
convenience but an established Old English noun. What requires explanation is
why the selected Proto-Germanic input is _\*wḯθagą_ rather than a comparative
_\*wīþja-_-type headword.

#### Development to Old English

From _\*wḯθagą_, Anglo-Frisian brightening gives a fronted vowel in the suffixal
syllable, and, on the Campbell analysis adopted here, the later Old English
development of _\*-ag-_ yields _-iġ_ [@Campbell1959, §§275, 376].
Palatalization supplies the final _ġ_, and the full development reaches
_wīþiġ_.

This derivation is regular for the selected formation. The central claim of the
entry is therefore morphological: Old English _wīþiġ_ belongs with an
_\*-ag-_ derivative, whereas the comparative _\*wīþja-_ label belongs to a
different way of presenting the cognate family.

#### Formation comparison

The comparison below is manual. It distinguishes the comparative headword from
the Old English-facing formation that actually yields the attested noun.

| Formation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| comparative family label | *wáiθiz | broader cognate-set headword | OE family context | useful lexeme label, but not the direct source of _wīþiġ_ |
| heavy ja-stem analysis | _\*wīþja-_ type | Campbell/Adamczyk-style heavy ja-stem _-e_ / zero outcome | _wīþiġ_ | does not account cleanly for the OE suffix |
| selected _\*-ag-_ derivative | *wḯθagą | compact-trace output: _wīþiġ_ | wīþiġ | exact match between formation and target |

### world — OE weorold

Derivation: citation reconstruction _\*wíra-àldiz_; selected input _\*wír-àldu_ $\rightarrow$ _weorold_ (early analogy).

#### Derivation trace

Proto input: _\*wíràldu_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc I Lowering & \emph{*wéràldu} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Inter Stress Raising & \emph{*wéruldu} \\
OE Med Unstressed U Lowering & \emph{*wéroldu} \\
OE Back Mutation & \emph{*wéoroldu} \\
OE High Vowel Apocope & \emph{*wéorold} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _weorold_

#### Reconstruction and comparative evidence

The word is the old compound 'age of men'. Comparative sources preserve two
slightly different views of its first element. Orel and the _\*wira-_ tradition
keep the older _i_-vocalism, while Ringe and Taylor discuss the lowered form
_\*weraldiz_ and its pre-Old-English chain _\*weraldu > \*weruld_
[@Orel2003; @RingeTaylor2014, 341]. Kluge-Seebold preserves both tendencies by
giving compound _\*wira-aldō_ beside simplex _\*wera-_ [@KlugeSeebold2011].

The selected input _\*wír-àldu_ therefore differs from the citation label in two
ways. It keeps the older _\*wir-_ vowel of the comparative headword, but it also
presupposes the early shift of the compound into the ō-stems that Ringe and
Taylor note for this lexeme [@RingeTaylor2014, 341]. The early analogical step lies
in that stem-class reassignment; the later phonological developments can then run
regularly.

#### Old English evidence

Old English does not preserve a single isolated form. Ringe and Taylor give West
Saxon _weorold ~ worold_, Mercian _weoruld_, Northumbrian _woruld_, and Kentish
_wiarald_ [@RingeTaylor2014, 341]. Sievers-Brunner and Bright present the same wider
set, including the syncopated _world_ and later rounded _wurold_
[@SieversBrunner1965; @BrightCassidyRingler1971, 465].

The selected target here is the West Saxon form _weorold_. It is an attested Old
English form within that broader variant cluster, not the only form the lexeme
ever shows.

#### Development to Old English

From the selected input _\*wír-àldu_, Northwest Germanic _i_-lowering gives
_\*wér-àldu_. Inter-stress raising then changes the medial _a_ to _u_, producing
_\*wér-uldu_. In the Old English branch that unstressed _u_ lowers to _o_, and
back mutation yields _\*wéor-oldu_; final high-vowel apocope then gives
_weorold_.

This sequence matches the comparative background in Ringe and Taylor's
_\*weraldiz > \*weraldu > \*weruld_ chain while preserving the _\*wir-_ notation of
the selected comparative label [@RingeTaylor2014, 341]. The modeled Old English form
therefore stands at the meeting point of an early stem-class reshaping and later
regular sound change.

#### Stage comparison

The comparison below is manual. It separates the comparative headword from the
OE-facing stage chosen for the derivation.

| Stage / interpretation | Candidate form | Old English outcome or comparison | Relevance to this entry |
| :--- | :--- | :--- | :--- |
| comparative compound with older first-element vowel | _\*wíra-àldiz_ | citation reconstruction / lexeme label | preserves the older _\*wir-_ tradition of the compound |
| literature-stage lowered compound after early stem-class shift | _\*weraldiz > \*weraldu > \*weruld_ | Ringe-Taylor background chain to OE _weorold ~ worold_ | explains the older comparative literature cited for the word |
| selected OE-facing input | _\*wír-àldu_ | compact-trace output: _weorold_ | exact match for the selected West Saxon target |
| broader OE variant cluster | — | _worold_, _weoruld_, _woruld_, _wiarald_, _world_ | real attested comparanda that remain outside the selected target line |

### youth — OE ġeoguþ

Derivation: citation reconstruction _\*júgunθiz_; selected input _\*júgunθ_ $\rightarrow$ _ġeoguþ_ (early analogy).

#### Derivation trace

Proto input: _\*júgunθ_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Ws Palatal Glide & \emph{*jéugunθ} \\
NWGmc Nasal Spirant Lengthening & \emph{*jéugūnθ} \\
NWGmc Nasal Spirant Loss & \emph{*jéugūθ} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Diphthong Leveling & \emph{*jéogūθ} \\
OE Unstressed Long Vowel Shortening & \emph{*jéoguθ} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _ġeoguþ_

#### Reconstruction and comparative evidence

The wider etymological tradition reconstructs an earlier form of the word as
_\*ju(w)unþi-_ [@Kroonen2013; @Fulk2018]. The selected comparative label
_\*júgunθiz_ already stands at a later Germanic stage with _g_, and the chosen
input _\*júgunθ_ is later again: it represents the form after final _-i_ has been
lost.

That staging matters because Ringe and Taylor explicitly give the sequence
_\*jugunþi > \*juguþ > OE geoguþ ~ iuguþ_ [@RingeTaylor2014]. Campbell makes the
same point with the parallel _duguþ < \*dugunþ-_, adding _geoguþ_ to the same
history [@Campbell1959]. The selected input therefore differs from the broader
comparative headword because the Old English development must begin after early
loss of final _-i_.

#### Old English evidence

The Old English noun is attested with varying spellings. Campbell records forms
of the _iuguþ / gioguð / geoguð_ type, and Ringe and Taylor likewise cite
_geoguþ ~ iuguþ_ [@Campbell1959; @RingeTaylor2014]. The form is normalized here
as _ġeoguþ_: the initial palatal is written with _ġ_, and the attested spelling
variation is treated as orthographic rather than lexical.

Nothing in the source stack suggests that a different paradigm cell should be
chosen. The relevant Old English comparison form is the noun _ġeoguþ_ itself.

#### Development to Old English

The decisive early step is the loss of final _-i_ before the Old English umlaut
stage. If that high vowel remained, the word would develop an over-umlauted
_y_-type vowel instead of the attested form [@RingeTaylor2014].

From the selected input _\*júgunθ_, the later development is regular: palatal
fronting yields _\*jéugunθ_; nasal-spirant lengthening and loss give
_\*jéogūθ_; unstressed long-vowel shortening then produces _\*jéoguθ_, which
surfaces as _ġeoguþ_. Medial _u_ remains preserved because the handbooks treat
this environment as one of stem-_u_ harmony after stressed _u_, citing forms
such as _munuc_, _duguþ_, and _iuguþ_ [@Campbell1959; @SieversBrunner1965;
@Luick1914, 397].

#### Stage comparison

The comparison below is manual. It separates the broader comparative headword
from the later stages relevant to the Old English noun.

| Stage / interpretation | Candidate form | Old English outcome or comparison | Relevance to this entry |
| :--- | :--- | :--- | :--- |
| earlier etymological headword | _\*ju(w)unþi-_ | comparative family background | older comparative reconstruction of the lexeme |
| later g-bearing comparative label | _\*júgunθiz_ | citation reconstruction / lexeme label | preserves the later Germanic stage behind the selected entry |
| selected OE-facing input | _\*júgunθ_ | compact-trace output: _ġeoguþ_ | exact match for the chosen Old English form |
| full _-i_ stage retained too long | _\*jugunþi_ | expected over-umlauted _y_-type result | negative control showing why early _-i_ loss must precede the OE umlaut stage |

\clearpage

## Part IV. Late analogy and paradigm-cell selection

These entries involve a later paradigm-cell or analogical comparison. The
citation reconstruction remains relevant to the lexeme, but the selected target
is best explained through a particular inflectional or analogical form rather
than through the citation form alone.

### ban — OE bannes

Derivation: citation reconstruction _\*bánną_; selected input _\*bánnas_ $\rightarrow$ _bannes_ (late analogy).

#### Derivation trace

Proto input: _\*bánnas_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*bánnæs} \\
OE Unstressed AE Merger & \emph{*bánnes} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _bannes_

#### Reconstruction and comparative evidence

Orel cites a bann-noun under _\*bannan_, while Seebold distinguishes bann-stems
of both masculine and neuter type and gives Old English _gebann_ as the noun
reflex [@Orel2003; @Seebold1970]. The citation reconstruction _\*bánną_
therefore names the lexeme, but the selected input _\*bánnas_ is a specific
genitive singular cell.

That distinction matters because the analysis depends on medial, not final,
gemination.

#### Old English evidence

Old English lexicographic evidence securely supports the noun itself. Clark Hall
gives _+bann_, and Bosworth-Toller records _ge-bann_ with oblique usage such as
_gebanne_ [@ClarkHall1960; @BosworthToller1898, 303]. The exact unprefixed genitive
_bannes_ is less directly cited in the reviewed material, so it is best treated
here as the selected regular genitive comparison form rather than as a
dictionary headword.

#### Development to Old English

From _\*bánnas_, the geminate remains medial before the case ending and the
unstressed vowel develops regularly to give _bannes_. By contrast, citation
_\*bánną_ loses its final vowel and simplifies the word-final geminate, so the
regular nominative outcome is _ban_ [@Campbell1959].

#### Paradigm comparison

The comparison below is manual. It shows why the genitive singular is the
conservative cell used for the entry.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | *bánną | compact-trace output: _ban_ | ban | regular nominative outcome, but not the selected target |
| selected genitive singular | *bánnas | compact-trace output: _bannes_ | bannes | exact match for the chosen conservative cell |

### berry — OE berġes

Derivation: citation reconstruction _\*bázją_; selected input _\*bázjas_ $\rightarrow$ _berġes_ (late analogy).

#### Derivation trace

Proto input: _\*bázjas_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*bærjæs} \\
OE I Umlaut & \emph{*berjæs} \\
OE Unstressed AE Merger & \emph{*berjes} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _berġes_

#### Reconstruction and comparative evidence

Kroonen reconstructs the berry noun as _\*basja- ~ \*bazja-_ [@Kroonen2013]. The
selected input _\*bázjas_ is therefore not a rival lexeme headword, but a
specific genitive singular cell drawn from that paradigm.

The relevant point is that _\*rj_ did not geminate in Proto-West Germanic.
Ringe and Taylor's _here, herges_ comparison shows the same _rj_ environment in
an Old English paradigm without any hidden gemination repair [@RingeTaylor2014].

#### Old English evidence

Campbell cites feminine _berige_ 'berry' and notes that _-j-_ is retained after
_r_ in this type [@Campbell1959, 250]. The reviewed evidence therefore supports the
citation form more directly than the exact genitive _berġes_, which is best read
here as the selected regular genitive comparison form rather than as a
dictionary headword.

#### Development to Old English

Citation _\*bázją_ gives _bere_, not the selected target. The genitive singular
_\*bázjas_, however, gives _berġes_, with medial _-rġ-_ preserved in the same
way that Ringe and Taylor cite _herges_ beside _here_ [@RingeTaylor2014]. This
points to paradigm choice rather than to an extra phonological rule.

#### Paradigm comparison

The comparison below is manual. It shows the contrast between the citation form
and the selected genitive singular cell.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | *bázją | compact-trace output: _bere_ | berige / berġe | useful citation-form background, but not the selected target |
| selected genitive singular | *bázjas | compact-trace output: _berġes_ | berġes | exact match for the chosen conservative cell |

### bow — OE bēag

Derivation: citation reconstruction _\*béuganą_; selected input _\*báug_ $\rightarrow$ _bēag_ (late analogy).

#### Derivation trace

Proto input: _\*báug_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Au Fronting & \emph{*báeug} \\
OE Diphthong Leveling & \emph{*bēag} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _bēag_

#### Reconstruction and comparative evidence

The inherited verb belongs to the class-II strong-verb family _\*béuganą_
[@RingeTaylor2014, 55]. Within that paradigm, however, the infinitive and the
singular preterite continue different ablaut grades. The selected input _\*báug_
is the singular preterite cell, whereas the citation form _\*béuganą_ is the
infinitive.

Campbell's account of Old English class-II strong verbs treats the singular
preterite _au > ēa_ development as regular in this environment
[@Campbell1959, 53].
That is the phonological path relevant for _bēag_, whereas the analogical _ū_
of the present stem belongs to the separate history behind _būgan_
[@RingeTaylor2014, 55].

#### Old English evidence

Bosworth-Toller and Clark Hall both record _bēag_ as a preterite form of
_būgan_ [@BosworthToller1898, 122; @ClarkHall1960, 45]. The form discussed here is
therefore an attested Old English verbal form, not a reconstructed substitute
for the infinitive.

The ordinary dictionary headword remains _būgan_, but the relevant comparison
form for this entry is the singular preterite _bēag_. That is the paradigm
cell in which the inherited _\*au_ grade is preserved most directly.

#### Development to Old English

From _\*báug_, Anglo-Frisian fronting and the later leveling of the diphthong
produce _bēag_ [@Campbell1959, 53]. No special analogical repair is needed for that
cell. The form is the regular Old English outcome of the singular-preterite
grade.

The analogical element in the wider lexeme belongs instead to the present stem
seen in _būgan_. The selected input differs from the citation form because the
regular inherited pathway survives more transparently in the preterite than in
the infinitive.

#### Paradigm comparison

The comparison below is manual. It distinguishes the regular singular
preterite from the more familiar infinitival citation form.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation infinitive | *béuganą | inherited present-stem history behind _būgan_ | būgan | establishes the lexeme, but not the selected target |
| singular preterite | *báug | compact-trace output: _bēag_ | bēag | exact match between input, output, and attested cell |
| past participial branch | participial _\*bugan-_ type | later participial outcomes | bogen-type evidence | relevant to the paradigm, but not the clearest match for this entry |

The singular preterite is the relevant comparison form. It gives a direct
lautgesetzlich path to attested _bēag_, while the citation form _būgan_
belongs to a paradigm whose present stem has already undergone later leveling.

### cow — OE cȳ

Derivation: citation reconstruction _\*kōz_; selected input _\*kūi_ $\rightarrow$ _cȳ_ (late analogy).

#### Derivation trace

Proto input: _\*kūi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE I Umlaut & \emph{*kȳi} \\
OE High Vowel Apocope & \emph{*kȳ} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _cȳ_

#### Reconstruction and comparative evidence

Kroonen reconstructs a root noun with the inherited alternation
_\*kō- ~ \*ku-_, explicitly _nom. \*kōz, obl. \*kū-_ [@Kroonen2013, p. 299].
The citation form therefore belongs to the nominative singular, whereas the
selected input _\*kūi_ belongs to the oblique stem.

Ringe and Taylor also posit a later PNWGmc nominative _\*kūaz > \*kūz_ behind Old
English _cū_ [@RingeTaylor2014, §3.1.3]. That nominative history matters for
the headword, but the form _cȳ_ depends on the oblique _\*kū-_ stem and a
following _\*i_.

#### Old English evidence

Clark Hall lemmatizes the noun under _cū_ and records gen.sg. _cū(e), cȳ, cūs_,
dat.sg. _cȳ_, nom.-acc.pl. _cȳ_, and dat.pl. _cūm_ [@ClarkHall1960]. Ringe and
Taylor likewise state that the root-noun _cū_ exhibits dat.sg., nom.-acc.pl.
_cȳ < \*cūi_, dat.pl. _cūm < \*cūm_, and apparently gen.sg. _cā < \*cūiz_
[@RingeTaylor2014, §6.6.1].

The dictionary headword is therefore _cū_, but _cȳ_ is an established Old
English paradigm form rather than a convenient reconstruction. It serves as
datative singular and also as nominative-accusative plural. The genitive
singular is less stable, with _cā_, _cȳ_, _cū(e)_, and _cūs_ all appearing in
the local source record.

#### Development to Old English

_\*kūi_ is the dative singular of the oblique _\*kū-_ stem. The following _\*i_
triggers i-umlaut, so _ū_ becomes _ȳ_, and loss of the final high vowel leaves
_cȳ_. The development is _\*kūi > \*kȳi > \*kȳ > cȳ_.

This is the regular oblique-cell path recognized by Ringe and Taylor's paradigm
statement [@RingeTaylor2014, §6.6.1]. It also explains why _cȳ_ is the cleanest
comparison form for the present entry, even though the ordinary headword is
_cū_.

#### Paradigm comparison

A paradigm comparison identifies the Proto-Germanic inflectional cell that
corresponds to an established Old English paradigm form. The comparison below
is manual; no full automatic paradigm-generation run is presented here.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | *kōz | OE headword _cū_ belongs to the nominative history of the lexeme | cū | useful background, but not the chosen comparison for _cȳ_ |
| later generalized nominative | PNWGmc *kūaz > *kūz | inferred nominative _cū_ | cū | explains the leveled headword, not the oblique target |
| dative singular oblique | *kūi | compact-trace output: _cȳ_ | cȳ | exact match between input, output, and paradigm cell |
| genitive singular oblique | *kūiz | Ringe-Taylor: apparently _cā_; Hall: _cū(e), cȳ, cūs_ | gen.sg. variable | too unstable to control the entry |

The dative singular is the relevant comparison form. It gives a regular path to
attested _cȳ_, while the broader Old English paradigm shows how far the oblique
_\*kū-_ grade spread beyond that one cell.

### find — OE fundene

Derivation: citation reconstruction _\*fínθaną_; selected input _\*fúnðanǭ_ $\rightarrow$ _fundene_ (late analogy).

#### Derivation trace

Proto input: _\*fúnðanǭ_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Dental Hardening & \emph{*fúndanǭ} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Unstressed Fronting Early & \emph{*fúndænǭ} \\
OE Unstressed Long Vowel Shortening & \emph{*fúndænæ} \\
OE Unstressed AE Merger & \emph{*fúndene} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _fundene_

#### Reconstruction and comparative evidence

The inherited verb is the strong verb _\*fínθaną_, continued by Old English
_findan_ [@RingeTaylor2014]. The selected input _\*fúnðanǭ_, however, belongs to
the past-participial paradigm rather than to the infinitive. It represents an
oblique singular form of the participle.

That distinction matters because the familiar dictionary form _funden_ is not
the cleanest inherited comparison. Campbell, Luick, and Brunner treat the
better-known nominative participial forms as analogically leveled from inflected
cases of the paradigm [@Campbell1959; @Luick1914; @SieversBrunner1965]. The
selected input therefore targets the cell in which the regular development is
most transparent.

#### Old English evidence

Bosworth-Toller records _fundene_ under _findan_ as an Old English
participial form [@BosworthToller1898]. Clark Hall likewise preserves the
participial stem in forms such as _funden_ and _tō-fundennes_
[@ClarkHall1960].

The ordinary dictionary headword for the participle is _funden_, but the
relevant comparison form for this entry is the attested oblique _fundene_.
It is an Old English form in its own right, not a merely convenient probe.

#### Development to Old English

From _\*fúnðanǭ_, the participial oblique develops through regular loss and
weakening of the final ending, yielding _fundene_. In that cell both the
consonantism and the medial vowel history remain regular.

The broader participial paradigm then matters for interpretation. The more
familiar nominative _funden_ represents a later analogical leveling, whereas the
selected oblique form preserves the inherited pathway more directly.

#### Paradigm comparison

The comparison below is manual. It distinguishes the attested oblique
participle from the more familiar but analogically leveled participial forms.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation infinitive | *fínθaną | inherited verb _findan_ | findan | establishes the lexeme, but not the selected target |
| nominative participial line | *fúnðanaz | later leveled _funden_ type | funden | important paradigm background, but not the cleanest regular cell |
| selected oblique participle | *fúnðanǭ | compact-trace output: _fundene_ | fundene | exact match between input, output, and attested cell |

The oblique participle is the relevant comparison form. It preserves the inherited
development most directly, while the nominative participial headword belongs to
a later analogical leveling within the paradigm.

### fright — OE fyrhte

Derivation: citation reconstruction _\*furxtīn_; selected input _\*fúrxtīnaz_ $\rightarrow$ _fyrhte_ (late analogy).

#### Derivation trace

Proto input: _\*fúrxtīnaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*fúrxtīna} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Final Bare A Loss & \emph{*fúrxtīn} \\
OE I Umlaut & \emph{*fyrxtīn} \\
NWGmc In Stem N Loss & \emph{*fyrxtī} \\
OE Unstressed Long Vowel Shortening & \emph{*fyrxti} \\
OE Med Unstressed I Lowering1 & \emph{*fyrxte} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _fyrhte_

#### Reconstruction and comparative evidence

The noun belongs to the inherited in-stem abstract _\*furxtīn_, the same family
as Gothic _faurhtei_ [@Orel2003]. The selected input _\*fúrxtīnaz_ is not a
different lexeme but an oblique singular cell within that in-stem paradigm.

Ringe and Taylor treat the later nominative forms with _-u_ or _-o_ as
analogically remodeled, whereas the oblique in-stem forms continue the older
history more directly [@RingeTaylor2014]. The selected input therefore differs
from the citation form because the oblique cell preserves the inherited pathway
more clearly than the better-known lemma forms do.

#### Old English evidence

Bosworth-Toller records _fyrhte_ with multiple textual attestations, and it
also records nominative forms such as _fyrhtu_ and _fyrhto_
[@BosworthToller1898]. The noun must be kept distinct from the adjective
_forht_, a distinction also reflected in Clark Hall [@ClarkHall1960].

The relevant comparison form is therefore the attested oblique _fyrhte_.
The nominative lemma forms remain part of the Old English evidence, but they are
not the cleanest inherited comparison for this entry.

#### Development to Old English

From _\*fúrxtīnaz_, the oblique in-stem develops through the loss and weakening
of the final ending and the regular OE history summarized by Campbell as
_-e < -i < -in_ in this class of abstracts [@Campbell1959]. That yields
_fyrhte_.

The later nominative forms with _-u_ or _-o_ belong to a subsequent analogical
reshaping of the paradigm. The selected target is earlier in that sense: it is
the attested OE cell in which the inherited in-stem development remains most
transparent.

#### Paradigm comparison

The comparison below is manual. It separates the attested oblique form from the
later remodeled nominative line.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation in-stem headword | *furxtīn | broader noun-class label | wider family context | useful lexeme label, but not the selected cell |
| remodeled nominative line | nominative in-stem forms | _fyrhtu_ / _fyrhto_ type lemma forms | fyrhtu / fyrhto | genuine OE evidence, but later remodeled |
| selected oblique singular | *fúrxtīnaz | compact-trace output: _fyrhte_ | fyrhte | exact match between input, output, and attested cell |

The oblique in-stem form is the relevant comparison form. It yields attested
_fyrhte_ directly, while the more familiar nominative forms belong to a later
analogical layer.

### hammer — OE hameres

Derivation: citation reconstruction _\*xámaraz_; selected input _\*xámaras_ $\rightarrow$ _hameres_ (late analogy).

#### Derivation trace

Proto input: _\*xámaras_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*xámæræs} \\
OE Unstressed AE Merger & \emph{*xámeres} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _hameres_

#### Reconstruction and comparative evidence

The inherited noun is the masculine a-stem _\*xámaraz_, reflected in Old English
citation forms such as _hamor_ and _hamer_ [@Kroonen2013; @Orel2003, 197;
@ClarkHall1960, 160]. The selected input _\*xámaras_ is the genitive singular of that
same noun rather than a different lexeme.

The genitive matters because the citation tradition is already mixed in its
unstressed vowel, while the oblique singular gives a cleaner comparison form.
This is a cell choice within one paradigm, not a change of stem class.

#### Old English evidence

Bosworth-Toller directly records _hameres_ in an Old English genitival
phrase [@BosworthToller1898]. The same dictionary tradition and Clark Hall also
preserve the simplex headword as _hamor_ or _hamer_
[@BosworthToller1898; @ClarkHall1960, 160].

Sievers-Brunner gives a paradigm line _hamor — hamores_, which shows that the
oblique tradition itself was not entirely uniform [@SieversBrunner1965]. The
relevant comparison form here is the attested genitive singular _hameres_.

#### Development to Old English

From _\*xámaras_, Anglo-Frisian brightening and the subsequent merger of
unstressed _æ_ with _e_ yield _hameres_. The derivation of that oblique form is
straightforward once the genitive singular cell is selected.

The noun as a whole retains a mixed citation tradition in _hamor_ and _hamer_,
and the selected oblique cell avoids making that variation carry the argument of
the entry.

#### Paradigm comparison

The comparison below is manual. It separates the attested genitive singular
from the less stable citation tradition.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | *xámaraz | regular citation form _hamer_ / _hamor_ | hamor / hamer | good lexical background, but not the selected target |
| selected genitive singular | *xámaras | compact-trace output: _hameres_ | hameres | exact match between input, output, and attested cell |
| later oblique tradition | oblique a-stem forms | _hamores_ type evidence | hamores | attested background variant, but not the chosen comparison form |

### have — OE hæfeþ

Derivation: citation reconstruction _\*xabēną_; selected input _\*xábēθi_ $\rightarrow$ _hæfeþ_ (late analogy).

#### Derivation trace

Proto input: _\*xábēθi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Early I Apocope & \emph{*xábēθ} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc Long E Lowering & \emph{*xábǣθ} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*xæbǣθ} \\
OE Velar Fricative Palatalization & \emph{*çæbǣθ} \\
PGmc B Allophony & \emph{*çæβǣθ} \\
OE Unstressed Long Vowel Shortening & \emph{*çæβæθ} \\
OE Unstressed AE Merger & \emph{*çæβeθ} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _hæfeþ_

#### Reconstruction and comparative evidence

The verb belongs to the inherited class-III weak paradigm usually cited under
_\*xabēną_ and Old English _habban_ [@Kroonen2013; @RingeTaylor2014]. Within that
paradigm, however, the infinitive and the singular present indicative do not
continue the same stem. Ringe and Taylor distinguish a _-ja-_ stem in the
infinitive from a non-geminating _-ai- / -ē-_ stem in the 2sg and 3sg present
forms [@RingeTaylor2014].

The selected input _\*xábēθi_ is therefore the 3sg present cell rather than a
rephrasing of the infinitive. Fulk's discussion of _habban_ treats the ordinary
citation form as analogically leveled, which is why the finite cell is the
cleaner comparator here [@Fulk2018].

#### Old English evidence

The ordinary Old English headword is _habban_, while the present paradigm also
shows forms of the _hæf-_ type [@BosworthToller1898; @ClarkHall1960, 157]. Campbell
notes occasional unsyncopated forms that support the normalized target
_hæfeþ_ [@Campbell1959].

The target form is therefore a normalized finite cell rather than the ordinary
dictionary lemma. It represents the inherited non-geminating present stem more
directly than _habban_ does.

#### Development to Old English

From _\*xábēθi_, early apocope of final _-i_, subsequent vowel changes, and the
regular fricative outcome of _b_ in this environment yield _hæfeþ_
[@RingeTaylor2014; @Campbell1959]. The derivation of the finite form itself is
regular.

The wider lexeme is less straightforward only because the infinitive _habban_
shows later leveling. That difference in paradigm history is what makes the 3sg
present cell the more useful comparison form.

#### Paradigm comparison

The comparison below is manual. It separates the analogically leveled citation
form from the regular 3sg present line.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation infinitive | _-ja-_ stem of _\*xabēną_ | citation form _habban_ | habban | important headword, but shaped by later leveling |
| selected 3sg present | *xábēθi | compact-trace output: _hæfeþ_ | hæfeþ | exact match between input, output, and selected finite cell |
| syncopated finite tradition | same present stem | _hæfþ_ type evidence | hæfþ | genuine later OE finite form, but not the normalized target used here |

### heaven — OE heofon

Derivation: citation reconstruction _\*xémenaz_; selected input _\*xémonų_ $\rightarrow$ _heofon_ (late analogy).

#### Derivation trace

Proto input: _\*xémonų_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc Unstressed O Raising & \emph{*xémunų} \\
NWGmc Mn Dissimilation & \emph{*xéβunų} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Med Unstressed U Lowering & \emph{*xéβonų} \\
OE Velar Fricative Palatalization & \emph{*çéβonų} \\
OE Back Mutation & \emph{*çéoβonų} \\
OE High Vowel Apocope & \emph{*çéoβon} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _heofon_

#### Reconstruction and comparative evidence

The inherited noun belongs to the mn-stem family cited by Kroonen as
_\*hemina-\* ~ \*hemna-\*_ [@Kroonen2013]. The selected input _\*xémonų_ is an
oblique singular form within that paradigm rather than the lexeme-level
citation form _\*xémenaz_.

That difference matters for the West Saxon target. The back-vocalic oblique stem
provides the environment for the diphthong seen in _heofon_, whereas a
front-vocalic stem yields Anglian or Mercian _hefen_ / _heofen_
[@Campbell1959; @RingeTaylor2014].

#### Old English evidence

Old English dictionaries record the standard West Saxon noun as _heofon_,
alongside Anglian or Mercian _hefen_ material [@ClarkHall1960;
@BosworthToller1898, 43]. Campbell also cites an earlier stage _hefzen_ in the
history of the word [@Campbell1959].

The target of this entry is the West Saxon citation form _heofon_. Its vowel
history points toward the oblique stem rather than the front-vocalic nominative
line.

#### Development to Old English

From _\*xémonų_, the relevant pathway includes early _o_-raising before _u_,
dissimilation in the m/n cluster, and later lowering of unstressed _u_
[@Fulk2018; @Campbell1959]. Back mutation then yields _heo-_ before the labial
plus back-vowel sequence, and loss of the final high vowel gives _heofon_.

The front-vocalic nominative line remains important as background because it
explains the dialectal _hefen_ type. West Saxon _heofon_ reflects the oblique
stem that was generalized into the nominative position.

#### Paradigm comparison

The comparison below is manual. It distinguishes the front-vocalic nominative
line from the oblique stem selected for West Saxon _heofon_.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | *xémenaz | front-vocalic _hefen_ type outcome | hefen / heofen | useful control, but not the selected West Saxon target |
| selected oblique singular | *xémonų | compact-trace output: _heofon_ | heofon | exact match between input, output, and target |
| older pre-OE stage | inherited oblique line | earlier _hefzen_ stage | hefzen | historical background for the same West Saxon development |

### live — OE lifeþ

Derivation: citation reconstruction _\*libēną_; selected input _\*líbēθi_ $\rightarrow$ _lifeþ_ (late analogy).

#### Derivation trace

Proto input: _\*líbēθi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Early I Apocope & \emph{*líbēθ} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc Long E Lowering & \emph{*líbǣθ} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc B Allophony & \emph{*líβǣθ} \\
OE Unstressed Long Vowel Shortening & \emph{*líβæθ} \\
OE Unstressed AE Merger & \emph{*líβeθ} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _lifeþ_

#### Reconstruction and comparative evidence

The inherited verb belongs to the class-III weak family cited by Kroonen under
_\*libēn-_, reflected in Old English _libban_ [@Kroonen2013]. Ringe and Taylor
show that the paradigm also contained a separate 3sg present stem, continued in
late Northumbrian _lifed_, which they treat as an archaism
[@RingeTaylor2014].

The selected input _\*líbēθi_ therefore represents a finite present cell rather
than the citation infinitive. That distinction matters because the ordinary
later lemma tradition also includes remodeled forms such as _lifian_.

#### Old English evidence

The ordinary dictionary headwords are _libban_ and, in later remodeling,
_lifian_ [@BosworthToller1898; @ClarkHall1960]. For this entry, however, the
relevant comparison form is the archaic 3sg present attested as _lifed_, here
normalized as _lifeþ_ [@RingeTaylor2014; @Campbell1959].

The target is thus a normalized finite form, not the ordinary dictionary lemma.
Its value lies in preserving the older present-stem history more clearly than
the remodeled lemma tradition does.

#### Development to Old English

From _\*líbēθi_, regular reduction of the final syllable and later weakening of
the unstressed vowel yield _lifeþ_. The attested spelling _lifed_ belongs to the
same finite form in late Northumbrian orthography [@Campbell1959;
@RingeTaylor2014].

#### Paradigm comparison

The comparison below is manual. It separates the archaic finite cell from the
ordinary infinitival and later remodeled lemma lines.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation infinitive line | *libēną | OE _libban_ headword tradition | libban | establishes the lexeme, but not the selected target |
| selected 3sg present | *líbēθi | compact-trace output: _lifeþ_; attested _lifed_ | lifed, normalized here as lifeþ | selected archaic finite cell |
| later remodeled present tradition | later class-II-type forms | _lifian_ and related finite remodeling | lifian | genuine OE development, but secondary to the selected cell |

### man — OE mannes

Derivation: citation reconstruction _\*mánnaz_; selected input _\*mánnas_ $\rightarrow$ _mannes_ (late analogy).

#### Derivation trace

Proto input: _\*mánnas_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*mánnæs} \\
OE Unstressed AE Merger & \emph{*mánnes} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _mannes_

#### Reconstruction and comparative evidence

The lexeme-level reconstruction is not uniform. Kroonen cites _\*mannan-_, Orel
has _\*mannz_, and Ringe and Taylor summarize the inherited noun as _\*mann-_
[@Kroonen2013; @Orel2003, 299; @RingeTaylor2014]. The selected input _\*mánnas_
belongs to a different level: it is the genitive-singular cell chosen for the
Old English comparison.

That distinction matters because the target of this entry is not the ordinary
citation form. The selected cell is the one that keeps the geminate medial
before the ending.

#### Old English evidence

Campbell gives the paradigm _mann, man / mannes / menn_ [@Campbell1959].
Sievers-Brunner likewise cites _man mannes_ and explains that word-final
simplification underlies forms such as _man_ beside inflected _monnes_
[@SieversBrunner1965]. Clark Hall keeps the dictionary headword under _mann_
[@ClarkHall1960].

The relevant comparison form is therefore the attested genitive singular
_mannes_, not the citation lemma _mann_.

#### Development to Old English

From _\*mánnas_, Anglo-Frisian brightening yields _\*mánnæs_, and the later
unstressed merger gives _\*mánnes_, hence _mannes_ [@Campbell1959]. In this
cell the geminate remains medial before _-es_. The citation form behaves
differently because word-final gemination was simplified in Old English
[@SieversBrunner1965].

#### Paradigm comparison

The comparison below is manual. It separates the citation-form line from the
selected genitive singular.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | *mannăz | expected citation-form outcome _man_ | mann / monn | establishes the lexeme, but not the selected target |
| accusative singular | *manną | expected _man_ | man | same word-final simplification as the nominative |
| dative singular | *mannăi | expected _manne_ | manne | preserves medial _nn_, but not the chosen cell |
| selected genitive singular | *mánnas | compact-trace output: _mannes_ | mannes | exact match between input, output, and attested comparator |

### meed — OE meorde

Derivation: citation reconstruction _\*mizdō_; selected input _\*mízdai_ $\rightarrow$ _meorde_ (late analogy).

#### Derivation trace

Proto input: _\*mízdai_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Ai Monophthongization & \emph{*mírdē} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc I Lowering & \emph{*mérdē} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Breaking & \emph{*méordē} \\
OE Unstressed Long Vowel Shortening & \emph{*méorde} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _meorde_

#### Reconstruction and comparative evidence

The lexeme-level reconstruction is _\*mizdō_, but the selected input _\*mízdai_
is a dative-singular cell rather than the citation form. That distinction is
important because the Old English evidence for the _meord_ side is oblique.

The wider history of competing _mēd_ remains disputed. Crist, Kroonen, Ringe and
Taylor, and Fulk explain it through some form of _z_-loss and compensatory
lengthening [@Crist2002; @Kroonen2013; @RingeTaylor2014; @Fulk2018], Orel keeps
a doublet analysis [@Orel2003], and Kilday instead argues that West Saxon _mēd_
is a Saxono-Frisian loan [@Kilday2024]. The comparison here concerns the
attested oblique line _meorde_.

#### Old English evidence

The directly attested forms are obliques: _meorde_ as a dative singular and
_meorda_ as a genitive plural [@BrightCassidyRingler1971; @BosworthToller1898].
Lexicographers reconstruct a bare nominative _meord_ from those obliques, while
West Saxon prose more commonly shows the competing doublet _mēd_
[@ClarkHall1960; @BosworthToller1898].

The target of this entry is therefore the attested oblique _meorde_, not the
reconstructed lemma _meord_ and not the better-known West Saxon citation form
_mēd_.

#### Development to Old English

From _\*mízdai_, rhotacism gives _\*mírdai_. Proto-West-Germanic monophthongization
then yields _\*mírdē_, Northwest-Germanic lowering gives _\*mérdē_, Old English
breaking yields _\*méordē_, and unstressed shortening gives _\*méorde_, hence
_meorde_ [@RingeTaylor2014].

This is the regular oblique-cell path modeled by the current trace. The entry
therefore depends on the attested oblique line rather than on a full decision
about the history of the competing _mēd_ tradition.

#### Paradigm comparison

The comparison below is manual. It distinguishes the attested oblique target from
the broader lemma history.

| PGmc cell / interpretation | Candidate input | Expected or documented OE outcome | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | *mizdō | inferred lemma outcome _meord_ | meord | useful background, but the bare lemma is reconstructed rather than directly attested |
| selected dative singular | *mízdai | compact-trace output: _meorde_ | meorde | exact match between selected input and attested target |
| genitive singular | *mizdōz | compact-trace output: _meorde_ | meorde | converges on the same attested string, but the dat.sg. has the clearest direct support |
| genitive plural control | plural oblique line | attested _meorda_ | meorda | confirms the broader oblique tradition, but not the chosen singular target |

### night — OE niht

Derivation: citation reconstruction _\*náxtz_; selected input _\*náxti_ $\rightarrow$ _niht_ (late analogy).

#### Derivation trace

Proto input: _\*náxti_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*næxti} \\
OE Breaking & \emph{*neaxti} \\
OE I Umlaut & \emph{*niexti} \\
OE Ws Palatal Umlaut & \emph{*nixti} \\
OE High Vowel Apocope & \emph{*nixt} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _niht_

#### Reconstruction and comparative evidence

Ringe and Taylor distinguish the high-vowel oblique and plural side of the word
from the nominative citation form: they cite _gen.sg. \*nahtiz_, _dat.sg. \*nahti_, and _nom.pl. \*nahtiz_, and derive West Saxon _niht_ from that side of
the paradigm [@RingeTaylor2014]. The citation reconstruction _\*náxtz_ therefore
belongs to the nominative-like headword, while the selected input _\*náxti_
represents the dative-singular cell.

That distinction matters because the word later became the model for endingless
datives. Ringe and Taylor explicitly explain forms such as _dæg_ by analogy with
_dat. sg. niht < \*nahti_ [@RingeTaylor2014].

#### Old English evidence

Clark Hall lemmatizes _niht_ and records the spelling range _æ, e, ea, ie, y_,
while cross-referencing forms such as _neaht_, _neht_, and _nieht_
[@ClarkHall1960]. Campbell likewise preserves the fluctuation between _neaht_
and _niht_, giving genitive _nihte, nihtes_, dative _niht, nihte_, nominative
plural _niht_, and the contrasting plural-side forms represented by _neahtas_
[@Campbell1959].

The comparison form used here is therefore an attested Old English _niht_, not a
reconstructed substitute. The broader lexical record still preserves the
non-umlauted side of the paradigm in _neaht_-type forms.

#### Development to Old English

From _\*náxti_, Anglo-Frisian brightening first fronts the root vowel, and the
following high vowel then triggers i-umlaut. In West Saxon, the sequence before
_ht_ yields _niht_, whereas plural forms with a following back vowel preserve the
non-umlauted _neahtas_ type [@RingeTaylor2014; @Campbell1959;
@SieversBrunner1965].

The modeled path is therefore _\*náxti > \*næxti > \*neaxti > \*niexti > \*nixti > niht_.

#### Paradigm comparison

The comparison below is manual. It identifies the inherited cell that matches the
attested Old English form.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | *náxtz | expected non-umlauted outcome _neaht_ | neaht | useful background, but not the selected comparison for _niht_ |
| selected dative singular | *náxti | compact-trace output: _niht_ | niht | exact match between input, output, and paradigm cell |

### rest — OE ræste

Derivation: citation reconstruction _\*rastō_; selected input _\*rástōz_ $\rightarrow$ _ræste_ (late analogy).

#### Derivation trace

Proto input: _\*rástōz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*rástō} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Surviving Bimoric O Unrounding & \emph{*rástā} \\
Anglo Frisian Brightening & \emph{*ræstǣ} \\
OE Unstressed Long Vowel Shortening & \emph{*ræstæ} \\
OE Unstressed AE Merger & \emph{*ræste} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _ræste_

#### Reconstruction and comparative evidence

Kroonen treats the noun as a feminine ō-stem _\*rastō-_, continued by Old English
_ræst_ [@Kroonen2013]. The selected input _\*rástōz_ therefore does not replace
the lexeme-level headword. It identifies one oblique singular cell on the side of
the paradigm that yields _ræste_.

The source tradition used here labels that cell specifically as genitive
singular, but the broader local synthesis of the ō-stem paradigm shows that the
oblique singulars converge on the same front-vocalic _ræste_ side, in contrast
to a nominative singular that would remain _rast_.

#### Old English evidence

The ordinary Old English citation form is _ræst_ [@Kroonen2013; @ClarkHall1960].
Bosworth-Toller also preserves oblique uses of _ræste_, including prepositional
examples such as _on ræste_ and _tó ræste_ [@BosworthToller1898, 121].

The comparison form used here is therefore an attested oblique _ræste_, not a
reconstructed surrogate. The dictionary headword _ræst_ remains an equally real
part of the Old English record.

#### Development to Old English

Once final _\*z_ is lost, the selected input moves through the front-vocalic
oblique side of the paradigm rather than the back-vocalic nominative side. In
the modeled derivation, the surviving final long vowel is first exposed,
unrounded, fronted, shortened, and then reduced to the final _-e_ of _ræste_.

The key point is the paradigm split. Nominative _\*rastō_ yields a regular _rast_,
whereas the selected oblique input yields _ræste_. The later citation form _ræst_
is best explained as leveling from that oblique _ræst-_ stem.

#### Paradigm comparison

The comparison below is manual. It distinguishes the nominative citation form
from the oblique singular chosen here.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | *rastō | expected regular outcome _rast_ | ræst | useful background, but not the cell that matches attested oblique _ræste_ |
| selected oblique singular | *rástōz | compact-trace output: _ræste_ | ræste | exact match between selected input and attested OE oblique form |

### shoulder — OE sċuldrum

Derivation: citation reconstruction _\*skuldrō_; selected input _\*skúldramiz_ $\rightarrow$ _sċuldrum_ (late analogy).

#### Derivation trace

Proto input: _\*skúldramiz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc A To U Before M & \emph{*skúldrumiz} \\
PWGmc Early I Apocope & \emph{*skúldrumz} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*skúldrum} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Sk Palatalization & \emph{*ʃúldrum} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _sċuldrum_

#### Reconstruction and comparative evidence

The handbooks do not agree on the reconstruction of the Germanic word. Orel gives _\*skuldr(j)ō_, a feminine ō-/jō-stem, and explicitly notes that Old English _sculdor_ is masculine beside OFrisian _skulder_, Middle Low German _schulder_, and Old High German _scultra, scultirra_ [@Orel2003, p. 345]. Kroonen reconstructs _\*skuldra-_, a masculine a-stem, and derives the Old High German feminine forms from _\*skuldrjōn-_ [@Kroonen2013, p. 478]. Ringe and Taylor cite PWGmc _\*skuldru_ for the Old English branch [@RingeTaylor2014, p. 142].

These forms imply different stem classes and different expectations for the Old English inflection. The question is which inflectional cell best aligns with the Old English evidence.

A dative/instrumental plural form _\*skúldramiz_ aligns with the inherited plural ending that later yields Old English _-um_, and it corresponds directly to the attested dative plural discussed below.

#### Old English evidence

The ordinary Old English headword is _sculdor_. Bosworth-Toller and Clark Hall both lemmatize _sculdor_ as the normal dictionary form, and the Bosworth-Toller material also preserves plural and oblique forms such as _sculdru_, _sculdra_, and _sculdrum_ [@BosworthToller1898; @ClarkHall1960]. The dative plural _sculdrum_ is directly attested in the dictionary material [@BosworthToller1898].

Bosworth-Toller's Supplement records a weak-feminine _sculdra, an_, so _sculdra_ belongs to the Old English record beside the stronger masculine paradigm headed by _sculdor_ [@BosworthToller1898]. Brunner and Luick also record later spellings such as _sceoldor_ and the i-mutated dative plural _scyldrum_, which reflect secondary phonological and analogical reshaping within Old English [@SieversBrunner1965, §92.2.a; @Luick1914, p. 230].

The singular and plural evidence point to different parts of the paradigm. The relevant comparison form here is the attested dative plural _sċuldrum_. The spelling with _sċ-_ is a normalized representation of the same Old English initial cluster.

#### Development to Old English

Proto-Germanic _\*skúldramiz_ can be interpreted as a dative/instrumental plural form. In this environment the post-tonic _a_ before _m_ is raised to _u_, giving a form of the _\*skúldrumiz_ type. Unstressed _u_ is regularly preserved before _m_, especially in the dative plural ending _-um_: Campbell states this explicitly, and Hogg formulates the same condition for the dative plural inflexion [@Campbell1959, §373; @Hogg1992, §3.3.1.3]. Brunner points in the same direction by excluding _m_ from the environments in which medial _o_ became general in West Saxon [@SieversBrunner1965, §44 Anm. 7].

Subsequent reduction of the ending removes the final _\*i_ and _\*z_, so that the inflectional ending appears in Old English as _-um_. The initial cluster is written here as _sċ-_, and the development is _\*skúldramiz > \*skúldrumiz > \*skúldrum > sċuldrum_.

#### Paradigm comparison

A paradigm comparison identifies the Proto-Germanic inflectional cell that corresponds to an established Old English paradigm form. The comparison below is manual; no full automatic paradigm-generation run is presented here.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| singular-oriented citation input | *skúldrō | probe output: _sċoldor_ | sculdor | fails: the singular output has root _o_, not the attested _u_ |
| serious plural-based singular alternative | *skúldru | probe output: _sċuldor_ | sculdor | close formally, but it compares a plural-stage input with a singular form |
| dat./inst.pl. input | *skúldramiz | compact-trace output: _sċuldrum_ | sculdrum | matches both the output and the dative plural comparison form |
| later weak-feminine singular | — | OE _sculdra_ | sculdra | secondary doublet, useful as a control rather than the inherited target |

The dative plural line is decisive because it matches both the output and the paradigm cell of Old English _sculdrum_. Singular-oriented candidates either lower the root vowel or compare unlike cells.

### shove — OE sċēaf

Derivation: citation reconstruction _\*skéubaną_; selected input _\*skáub_ $\rightarrow$ _sċēaf_ (late analogy).

#### Derivation trace

Proto input: _\*skáub_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Au Fronting & \emph{*skáeub} \\
OE Diphthong Leveling & \emph{*skēab} \\
PGmc B Allophony & \emph{*skēaβ} \\
OE Sk Palatalization & \emph{*ʃēaβ} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _sċēaf_

#### Reconstruction and comparative evidence

Kroonen reconstructs the strong verb as _\*skeuban- ~ \*skūban-_ and cites Old
English present forms _scēofan, scūfan_ [@Kroonen2013]. Ringe and Taylor also
show that the English present system belongs to a wider class-II split that is
not identical with the preterite grade [@RingeTaylor2014]. The selected input
_\*skáub_ is therefore not a spelling variant of the infinitive but the singular
preterite cell.

#### Old English evidence

The ordinary dictionary verb is _scūfan/scēofan_, but the preterite itself is
well attested. Bright gives the principal parts _scufan, sceaf, scufon, scofen_
and also quotes _he sceaf þa mid þam scylde_; Sweet gives the same paradigm
[@BrightCassidyRingler1971; @Sweet1953]. The normalized form here is _sċēaf_,
regularizing the attested spellings _sceaf_ and prefixed _āsceaf_.

#### Development to Old English

From _\*skáub_, the documented trace is straightforward. _\*au_ fronts and levels
to _ēa_, final _\*b_ becomes a fricative and is written _f_, and initial _\*sk-_
undergoes the usual Old English palatalized spelling in this environment. The
trace therefore gives _\*skáub > \*skáeub > \*skēab > \*skēaβ > sċēaf_.

#### Paradigm comparison

A paradigm comparison is required here because the ordinary citation verb and
the selected Old English target belong to different cells of the same strong
paradigm. The comparison below is manual.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation infinitive | *skéubaną | inherited infinitive line _sċēofan_; present system also leveled _scūfan_ | scēofan / scūfan | necessary background, but not the selected comparison for _sċēaf_ |
| 1/3 sg. preterite | *skáub | documented trace output: _sċēaf_ | sċēaf | exact match between selected input and Old English target |
| preterite plural | *skúbun | later leveled plural _scufon_ beside expected _sċufun_ under the corrected cascade | scufon | poorer comparison for the singular-preterite target |
| past participle | *skúbanaz | attested participial line _scofen_ | scofen | valid clean cell, but not the chosen one |

### span — OE spanne

Derivation: citation reconstruction _\*spannō_; selected input _\*spánnai_ $\rightarrow$ _spanne_ (late analogy).

#### Derivation trace

Proto input: _\*spánnai_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Ai Monophthongization & \emph{*spánnē} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Unstressed Long Vowel Shortening & \emph{*spánne} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _spanne_

#### Reconstruction and comparative evidence

Orel reconstructs the noun as _\*spannō_, and Seebold likewise gives Old English
_spann_ under the same noun family [@Orel2003; @Seebold1970, 450]. The selected input
_\*spánnai_ is therefore not a rival headword, but a specific dative singular
cell of the feminine ō-stem paradigm [@SieversBrunner1965].

#### Old English evidence

The reviewed lexicographic evidence more directly supports the citation noun
_spann_ than the exact form _spanne_. Clark Hall gives _spann_, and _spanne_ is
accordingly treated as the selected regular dative singular comparison form
rather than as a dictionary headword [@ClarkHall1960].

#### Development to Old English

Citation _\*spannō_ yields _span_. The oblique cell _\*spánnai_ therefore
supplies the conservative comparison form: it preserves the medial geminate and
yields _spanne_, while citation _\*spannō_ gives the nominative background form.

#### Paradigm comparison

The comparison below is manual. It shows the contrast between the citation form
and the selected dative singular cell.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | *spannō | compact-trace output: _span_ | spann | useful citation-form background, but not the selected target |
| selected dative singular | *spánnai | compact-trace output: _spanne_ | spanne | exact match for the chosen conservative cell |

### thistle — OE þistles

Derivation: citation reconstruction _\*θéstilaz_; selected input _\*θístilas_ $\rightarrow$ _þistles_ (late analogy).

#### Derivation trace

Proto input: _\*θístilas_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*θístilæs} \\
OE L Adjacent Syncope & \emph{*θístlæs} \\
OE Unstressed AE Merger & \emph{*θístles} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _þistles_

#### Reconstruction and comparative evidence

The comparative tradition is divided. Orel prints _\*þe(x)stilaz_, while
Kluge-Seebold gives _\*þistila-_ [@Orel2003, 458; @KlugeSeebold2011]. The comparative
label _\*θéstilaz_ therefore remains in view as the lexeme-level headword, while
the selected input _\*θístilas_ is a specific genitive singular cell.

#### Old English evidence

The ordinary simplex headword tradition is broken _þistel_ / _ðistel_. Clark
Hall gives _ðistel_ as the noun headword [@ClarkHall1960, 326]. The selected target
here is the genitive singular _þistles_, which preserves the same stem in an
oblique form where the cluster is medial.

#### Development to Old English

Campbell's discussion of cluster nouns shows the contrast clearly. Simplex forms
often develop a parasite vowel in word-final obstruent + sonorant clusters,
while comparable medial clusters remain unbroken; his examples include _hrefn_,
_tacn_, _wépn_, and _botm_ beside forms with parasitic vowels elsewhere in the
same lexical class [@Campbell1959, 151]. The selected genitive singular _\*θístilas_
therefore supplies the conservative comparison form: the cluster is medial and
the regular development yields _þistles_, while the simplex nominative belongs
to the broken headword tradition _þistel_.

#### Paradigm comparison

The comparison below is manual. It shows the contrast between the citation form
and the selected genitive singular cell.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| citation nominative singular | *θéstilaz | computed output: _þistl_ | þistel | useful citation-form background, but not the selected target |
| selected genitive singular | *θístilas | computed output: _þistles_ | þistles | exact match for the chosen conservative cell |

### make (iptv.2sg) — OE maca

Derivation: citation reconstruction _\*makōną_; selected input _\*mákô_ $\rightarrow$ _maca_ (late analogy).

#### Derivation trace

Proto input: _\*mákô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*mækô} \\
OE A Restoration & \emph{*makô} \\
OE Unstressed Long Vowel Shortening & \emph{*maka} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _maca_

#### Reconstruction and comparative evidence

The make-family belongs to the Old English class-II weak verbs. Campbell cites
_macian_ beside _lapian_ and similar verbs with restored _a_, and Ringe and
Taylor place the Germanic verb in the same class, comparing West Germanic
continuants such as Old Frisian _makia_, Old Saxon _makon_, and Old High German
_mahhon_ [@Campbell1959; @RingeTaylor2014].

The selected input _\*mákô_ is not the citation form of the lexeme but a finite
paradigm cell. Ringe and Taylor's account of the class-II weak paradigm is the
reason for choosing it: the imperative singular belongs to the small set of
finite cells that preserve the trimoric _\*ō_ directly, whereas the ordinary
infinitive continues the remodelled _\*-ōja-_ formation behind _macian_
[@RingeTaylor2014].

#### Old English evidence

The dictionary headword is _macian_ [@ClarkHall1960]. The selected form in this
entry is therefore not the lemma but the imperative singular _maca_, chosen as a
paradigm form beside the headword _macian_ and the related finite form _macaþ_.

That distinction matters for the comparison. The lexical history of the verb is
still the history of _macian_, but the finite cell isolates the regular outcome
of trimoric _\*ō_ more cleanly than the citation form does.

#### Development to Old English

From _\*mákô_, Anglo-Frisian brightening first gives _\*mækô_. In this class-II
environment A-restoration returns the stem vowel to _a_, and unstressed long
vowel shortening then gives _\*maka_, whence _maca_ [@Campbell1959;
@RingeTaylor2014].

The same development explains why earlier fronted forms of the _mæċa_ type do
not control the entry. Once trimoric _\*ô_ is treated as a back-vocalic trigger
for restoration, the imperative singular falls into line with the broader
_macian_ family.

#### Paradigm comparison

A paradigm comparison identifies which finite cell of the make-family matches
the Old English form chosen here. The comparison below is manual.

| PGmc cell / interpretation | Candidate input | Old English outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | _\*mákōjaną_ | comparative continuation _macian_ | macian | ordinary headword of the verb, but not the selected finite cell |
| selected imperative singular | _\*mákô_ | compact-trace output: _maca_ | maca | exact match between input, output, and selected paradigm form |
| present third singular companion | _\*mákōθi_ | comparative companion _macaþ_ | macaþ | useful family control, but not the target of this entry |

### make (3sg) — OE macaþ

Derivation: citation reconstruction _\*makōną_; selected input _\*mákōθi_ $\rightarrow$ _macaþ_ (late analogy).

#### Derivation trace

Proto input: _\*mákōθi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Early I Apocope & \emph{*mákōθ} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*mækōθ} \\
OE A Restoration & \emph{*makōθ} \\
OE Late O Shortening & \emph{*makaθ} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _macaþ_

#### Reconstruction and comparative evidence

Kroonen derives the Old English verb from _\*makōjan-_ on the make-family base _\*maka-_ [@Kroonen2013]. Ringe and Taylor likewise place the verb among the class-II weak verbs and note that the present 2sg, 3sg, and imperative singular preserve suffixal _\*ō_ rather than the remodelled infinitival formation [@RingeTaylor2014].

The selected input _\*mákōθi_ is therefore a finite 3sg cell of the same family, not the citation form of the verb.

#### Old English evidence

Clark Hall lemmatizes the verb as _macian_ [@ClarkHall1960]. The relevant comparison form here is the normalized present-third-singular _macaþ_, set beside the dictionary headword and the related imperative singular _maca_.

Campbell's class-II paradigm makes the ordinary 3sg ending _-aþ_, while his dialect survey allows secondary _-e-_ spellings in some traditions [@Campbell1959, §355.4; @Campbell1959, §757]. _Macaþ_ is thus the regular comparison form for the non-_j_ 3sg cell.

#### Development to Old English

After early loss of final _-i_, _\*mákōθi_ yields _\*mákōθ_. Anglo-Frisian brightening gives _\*mækōθ_, but Campbell lists _macian_ among the class-II verbs with restored _a_, so the stem returns to _mak-_ before the ending is reduced [@Campbell1959, §159].

The ending then follows the ordinary class-II 3sg development. Campbell's _lufas, -aþ (< -ōsi, -ōþi)_ and Ringe and Taylor's discussion of stable _a_ in the finite non-_j_ cells point to _\*makōθ > \*makaθ > macaþ_ [@Campbell1959, §355.4; @RingeTaylor2014].

#### Paradigm comparison

The comparison below is manual. It distinguishes the selected 3sg cell from the make-family lemma and from the companion imperative form.

| PGmc cell / interpretation | Candidate input | OE outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | _\*makōjaną_ | dictionary headword _macian_ | macian | family background, but not the selected cell |
| selected 3sg present | _\*mákōθi_ | trace output _macaþ_ | macaþ | exact match |
| imperative singular companion | _\*mákô_ | related finite form _maca_ | maca | useful control, but not the target |

### bore (iptv.2sg) — OE bora

Derivation: citation reconstruction _\*burōną_; selected input _\*búrô_ $\rightarrow$ _bora_ (late analogy).

#### Derivation trace

Proto input: _\*búrô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc U Lowering & \emph{*bórô} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Unstressed Long Vowel Shortening & \emph{*bóra} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _bora_

#### Reconstruction and comparative evidence

Kroonen reconstructs the bore-family verb as _\*burojan-_ and cites Old English _borian_ among its continuants [@Kroonen2013]. In Ringe and Taylor's account of class-II weak verbs, the imperative singular belongs to the finite cells that preserve inherited suffixal _\*ō_, unlike the remodelled infinitive [@RingeTaylor2014].

The selected input _\*búrô_ is therefore an imperative cell of the same family, not the citation form of the verb.

#### Old English evidence

Clark Hall lemmatizes the verb as _borian_ [@ClarkHall1960]. The comparison form here is the normalized imperative singular _bora_, used beside the headword and the related 3sg form _boraþ_.

The imperative is thus a paradigm form rather than a replacement for the dictionary lemma. It is the most direct Old English comparator for the non-_j_ finite cell represented by _\*búrô_.

#### Development to Old English

Northwest Germanic lowering first gives _\*bórô_ from _\*búrô_, and late shortening of the unstressed long vowel then yields _\*bóra_, whence _bora_.

Ringe and Taylor's class-II imperative singular _-a < \*-ō_ points to exactly this type of outcome [@RingeTaylor2014]. The selected form therefore isolates the regular finite-cell development more cleanly than the remodelled infinitive does.

#### Paradigm comparison

The comparison below is manual. It distinguishes the selected imperative cell from the bore-family lemma and from the companion 3sg form.

| PGmc cell / interpretation | Candidate input | OE outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | _\*burōjaną_ | dictionary headword _borian_ | borian | family background, but not the selected cell |
| selected imperative singular | _\*búrô_ | trace output _bora_ | bora | exact match |
| 3sg present companion | _\*búrōθi_ | related finite form _boraþ_ | boraþ | useful control, but not the target |

### bore (3sg) — OE boraþ

Derivation: citation reconstruction _\*burōną_; selected input _\*búrōθi_ $\rightarrow$ _boraþ_ (late analogy).

#### Derivation trace

Proto input: _\*búrōθi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Early I Apocope & \emph{*búrōθ} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc U Lowering & \emph{*bórōθ} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Late O Shortening & \emph{*bóraθ} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _boraþ_

#### Reconstruction and comparative evidence

Kroonen reconstructs the bore-family verb as _\*burojan-_ and cites Old English _borian_ among its reflexes [@Kroonen2013]. The selected form isolates the finite 3sg cell _\*búrōθi_ rather than the infinitive.

Campbell's class-II pattern _lufas, -aþ (< -ōsi, -ōþi)_ and Ringe and Taylor's account of stable _a_ in the class-II 2sg and 3sg make this finite cell the relevant comparison form for the ending [@Campbell1959, §355.4; @RingeTaylor2014].

#### Old English evidence

Clark Hall lemmatizes the verb as _borian_ [@ClarkHall1960]. The relevant comparison form here is the normalized present-third-singular _boraþ_, used beside the headword and the imperative singular _bora_.

Campbell's dialect survey allows secondary _-e-_ and _-o-_ spellings in 2sg and 3sg class-II forms, but the basic ending remains _-aþ_ [@Campbell1959, §757]. _Boraþ_ is therefore the regular comparison form for this non-_j_ 3sg cell.

#### Development to Old English

Early loss of final _-i_ first gives _\*búrōθ_ from _\*búrōθi_. Northwest Germanic lowering then produces _\*bórōθ_, and late shortening of unstressed _ō_ yields _\*bóraθ_, whence _boraþ_.

Campbell's class-II ending evidence and Ringe and Taylor's discussion of stable _a_ in the finite non-_j_ cells support exactly this sequence [@Campbell1959, §355.4; @RingeTaylor2014].

#### Paradigm comparison

The comparison below is manual. It distinguishes the selected 3sg cell from the bore-family lemma and from the companion imperative form.

| PGmc cell / interpretation | Candidate input | OE outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | _\*burōjaną_ | dictionary headword _borian_ | borian | family background, but not the selected cell |
| selected 3sg present | _\*búrōθi_ | trace output _boraþ_ | boraþ | exact match |
| imperative singular companion | _\*búrô_ | related finite form _bora_ | bora | useful control, but not the target |

### learn (iptv.2sg) — OE liorna

Derivation: citation reconstruction _\*liznōjaną_; selected input _\*líznô_ $\rightarrow$ _liorna_ (late analogy).

#### Derivation trace

Proto input: _\*líznô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Breaking & \emph{*líornô} \\
OE Unstressed Long Vowel Shortening & \emph{*líorna} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _liorna_

#### Reconstruction and comparative evidence

Ringe and Taylor give Old English _liornian ~ leornian_ from a learn-family base of the _\*lizn-_ type, and Kroonen likewise keeps the weak verb as _\*liznōn-_ [@RingeTaylor2014; @Kroonen2013, 380]. Fulk cites the same Old English family from _\*liznō-_ [@Fulk2018].

The selected input _\*líznô_ is a finite imperative cell of that family, not the citation form of the verb.

#### Old English evidence

Clark Hall gives the ordinary headword as _leornian_ [@ClarkHall1960]. Brunner, however, explicitly records _leornian, nordh. auch liorna_, and Campbell notes that beside _leornian_ Northumbrian forms with _io_ occur where original _eo_ and _io_ remain distinct [@SieversBrunner1965; @Campbell1959, §123 n. 2].

_Liorna_ can therefore be treated as an attested Northumbrian finite form, while _leornian_ remains the better-known dictionary headword.

#### Development to Old English

The selected form develops regularly as _\*líznô > \*lírnô_ by rhotacism, then _\*líornô_ by breaking before _rn_, and finally _\*líorna_ by late shortening of the unstressed long vowel.

Campbell's Northumbrian _io_ evidence and Ringe and Taylor's explicit statement that no form of _liornian_ stood in an i-umlauting environment support this stem shape [@Campbell1959, §123 n. 2; @RingeTaylor2014]. The West-Saxon-looking _eo_ forms belong to a different dialectal presentation of the same family.

#### Paradigm comparison

The comparison below is manual. It distinguishes the selected imperative cell from the learn-family infinitive and from the companion 3sg form.

| PGmc cell / interpretation | Candidate input | OE outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | _\*liznōjaną_ | Northumbrian _liornian_; dictionary headword often _leornian_ | liornian / leornian | family background, but not the selected cell |
| selected imperative singular | _\*líznô_ | trace output and Brunner's Northumbrian _liorna_ | liorna | exact match |
| 3sg present companion | _\*líznōθi_ | related finite form _liornaþ_ | liornaþ | useful control, but not the target |

### learn (3sg) — OE liornaþ

Derivation: citation reconstruction _\*liznōjaną_; selected input _\*líznōθi_ $\rightarrow$ _liornaþ_ (late analogy).

#### Derivation trace

Proto input: _\*líznōθi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Early I Apocope & \emph{*lírnōθ} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Breaking & \emph{*líornōθ} \\
OE Late O Shortening & \emph{*líornaθ} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _liornaþ_

#### Reconstruction and comparative evidence

Ringe and Taylor give Old English _liornian ~ leornian_ from a learn-family base of the _\*lizn-_ type, and Kroonen likewise keeps the weak verb as _\*liznōn-_ [@RingeTaylor2014; @Kroonen2013, 380]. The selected input _\*líznōθi_ is the finite 3sg cell of that family, not the citation form of the verb.

For the ending, Campbell's _lufas, -aþ (< -ōsi, -ōþi)_ and Ringe and Taylor's discussion of stable _a_ in the class-II 2sg and 3sg make the non-_j_ 3sg cell the relevant comparison point [@Campbell1959, §355.4; @RingeTaylor2014].

#### Old English evidence

Clark Hall gives the ordinary headword as _leornian_ [@ClarkHall1960]. Brunner records Northumbrian finite forms in _liorn-_, including _liorna_ and the 3sg _liornes_, beside the West-Saxon-looking _leornian_ tradition [@SieversBrunner1965]. Campbell likewise notes Northumbrian forms with _io_ beside _leornian_ [@Campbell1959, §123 n. 2].

The relevant comparison form here is the normalized 3sg _liornaþ_. The directly cited Old English evidence supports the finite stem _liorn-_; the exact _-aþ_ ending follows the regular class-II 3sg pattern.

#### Development to Old English

The selected form develops as _\*líznōθi > \*lírnōθi_ by rhotacism, then _\*lírnōθ_ after early apocope of final _-i_, then _\*líornōθ_ by breaking before _rn_, and finally _\*líornaθ > liornaþ_ by late shortening of the unstressed long vowel.

Campbell's Northumbrian _io_ evidence and Ringe and Taylor's statement that no form of _liornian_ stood in an i-umlauting environment support the stem, while Campbell's class-II ending evidence supports the final _-aþ_ [@Campbell1959, §123 n. 2; @Campbell1959, §355.4; @RingeTaylor2014].

#### Paradigm comparison

The comparison below is manual. It distinguishes the selected 3sg cell from the learn-family infinitive and from the companion imperative form.

| PGmc cell / interpretation | Candidate input | OE outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | _\*liznōjaną_ | Northumbrian _liornian_; dictionary headword often _leornian_ | liornian / leornian | family background, but not the selected cell |
| selected 3sg present | _\*líznōθi_ | trace output _liornaþ_ | liornaþ | exact match |
| imperative singular companion | _\*líznô_ | trace output and Brunner's Northumbrian _liorna_ | liorna | useful control, but not the target |

### lick (iptv.2sg) — OE licca

Derivation: citation reconstruction _\*likkōną_; selected input _\*líkkô_ $\rightarrow$ _licca_ (late analogy).

#### Derivation trace

Proto input: _\*líkkô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Unstressed Long Vowel Shortening & \emph{*líkka} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _licca_

#### Reconstruction and comparative evidence

Ringe and Taylor place the verb among the West Germanic class-II weak verbs, with PWGmc _\*li/ekkōn_ continuing as Old English _liccian_, Old Saxon _likkon_, and Old High German _lecchon_ [@RingeTaylor2014]. Orel gives the fuller weak-verb reconstruction _\*likkōjanan_ with the same Old English continuation [@Orel2003].

The form treated here is not that remodeled infinitive but a finite cell in bare trimoric _\*-ō_. Campbell's weak class-II discussion and Ringe and Taylor's account of the paradigm both distinguish those finite singular cells from the ordinary _\*-ōja-_ citation formation [@Campbell1959; @RingeTaylor2014].

#### Old English evidence

Bosworth-Toller lemmatizes the verb as _liccian_, and Campbell and Brunner likewise cite _liccian_ with preserved geminate _cc_ [@BosworthToller1898; @Campbell1959; @SieversBrunner1965]. The Old English evidence therefore establishes the verbal headword and its consonantal frame securely.

The selected target in this entry is the imperative singular _licca_. It is a paradigm form chosen beside the headword _liccian_ and the related present _liccaþ_, not a separately lemmatized citation word.

#### Development to Old English

With the stem _licc-_ established, the remaining development is brief. Trimoric _\*-ô_ shortens late to _-a_ in this finite class-II cell, so _\*líkkô_ yields _\*líkka_ and then _licca_ [@Campbell1959; @RingeTaylor2014]. The same stem consonantism that appears in _liccian_ is preserved here, giving _cc_ throughout the finite form.

#### Paradigm comparison

The comparison below is manual.

| PGmc cell / interpretation | Candidate input | Old English outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | _\*líkkōjaną_ | manual probe output _liccian_ | liccian | ordinary dictionary headword of the verb, but not the selected finite cell |
| selected imperative singular | _\*líkkô_ | manual probe output _licca_ | licca | exact match between the chosen input and the selected target |
| present third singular companion | _\*líkkōθi_ | manual probe output _liccaþ_ | liccaþ | useful family control, but not the target of this entry |

### lick (3sg) — OE liccaþ

Derivation: citation reconstruction _\*likkōną_; selected input _\*líkkōθi_ $\rightarrow$ _liccaþ_ (late analogy).

#### Derivation trace

Proto input: _\*líkkōθi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Early I Apocope & \emph{*líkkōθ} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Late O Shortening & \emph{*líkkaθ} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _liccaþ_

#### Reconstruction and comparative evidence

Ringe and Taylor place the verb among the West Germanic class-II weak verbs, with PWGmc _\*li/ekkōn_ continuing as Old English _liccian_, Old Saxon _likkon_, and Old High German _lecchon_ [@RingeTaylor2014]. Orel gives the fuller weak-verb reconstruction _\*likkōjanan_ with the same Old English continuation [@Orel2003].

The selected form in this entry is the non-_j_ present third singular _\*líkkōθi_, not the remodeled infinitive. Campbell states the class-II present endings as _lufas, -aþ (< -ōsi, -ōþi)_, and Ringe and Taylor likewise treat the class-II 2sg and 3sg as forms with stable _-a-_ [@Campbell1959; @RingeTaylor2014].

#### Old English evidence

Bosworth-Toller lemmatizes the verb as _liccian_, and the same consonantal frame appears in Campbell and Brunner's grammatical citations of _liccian_ [@BosworthToller1898; @Campbell1959; @SieversBrunner1965]. The Old English headword is therefore clear even though the entry here is not about the citation form.

The form treated here is the present third singular _liccaþ_. It is a selected paradigm form beside the lemma _liccian_ and the related imperative _licca_, not a separately lemmatized headword.

#### Development to Old English

_\*líkkōθi_ first loses final _-i_, giving _\*líkkōθ_. Late shortening of unstressed _\*ō_ then yields _\*líkkaθ_, written _liccaþ_ [@Campbell1959; @RingeTaylor2014]. Because this ending never contains _-j-_, the form does not pass through an i-umlauted _-eþ_ stage; the regular class-II outcome is _-aþ_.

#### Paradigm comparison

The comparison below is manual.

| PGmc cell / interpretation | Candidate input | Old English outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | _\*líkkōjaną_ | manual probe output _liccian_ | liccian | ordinary dictionary headword of the verb, but not the selected finite cell |
| imperative singular companion | _\*líkkô_ | manual probe output _licca_ | licca | useful family control, but not the target of this entry |
| selected present third singular | _\*líkkōθi_ | manual probe output _liccaþ_ | liccaþ | exact match between the chosen input and the selected target |

### show (iptv.2sg) — OE sċēawa

Derivation: citation reconstruction _\*skawōną_; selected input _\*skáwô_ $\rightarrow$ _sċēawa_ (late analogy).

#### Derivation trace

Proto input: _\*skáwô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Aw Long Diphthong & \emph{*skḗawô} \\
OE Sk Palatalization & \emph{*ʃḗawô} \\
OE Unstressed Long Vowel Shortening & \emph{*ʃḗawa} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _sċēawa_

#### Reconstruction and comparative evidence

Orel reconstructs the verb as _\*skawōjanan_ and cites Old English _sceáwian_ beside Old Frisian _skawia_, Old Saxon _skawōn_, and Old High German _scouwōn_ [@Orel2003]. The selected input in this entry is not that infinitive but the imperative singular _\*skáwô_, a finite class-II cell that preserves bare _\*-ō_ rather than the remodeled _\*-ōja-_ formation [@RingeTaylor2014].

That distinction matters because the imperative singular provides the direct comparison for the Old English form treated here. The lexical history still belongs to the _sceáwian_ verb, but the selected cell isolates the finite _-a_ outcome more clearly than the citation form does.

#### Old English evidence

Bright lists _scēawian_ and explicitly gives the imperative singular _scēawa_ under that headword [@BrightCassidyRingler1971]. The form treated here is therefore an attested finite paradigm form, not a reconstructed convenience form.

The spelling used in this entry is normalized _sċēawa_, while Bright's glossary gives source spelling _scēawa_. The ordinary Old English headword remains _scēawian_; _sċēawa_ is the imperative singular chosen beside it.

#### Development to Old English

From _\*skáwô_, Old English _\*aw_ before vocalic material yields _\*skḗawô_, initial _sk_ palatalizes, and late shortening of trimoric _\*-ô_ gives _\*ʃḗawa_, written _sċēawa_ [@Campbell1959]. The result is therefore the expected finite singular form of the _scēawian_ family rather than an analogical replacement of the headword.

#### Paradigm comparison

The comparison below is manual.

| PGmc cell / interpretation | Candidate input | Old English outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | _\*skáwōjaną_ | manual probe output _sċēawian_ | scēawian | ordinary dictionary headword of the verb, but not the selected finite cell |
| selected imperative singular | _\*skáwô_ | manual probe output _sċēawa_ | scēawa / normalized sċēawa | exact match between the chosen input and the selected target |
| present third singular companion | _\*skáwōθi_ | manual probe output _sċēawaþ_ | sċēawaþ | useful family control, but not the target of this entry |

### show (3sg) — OE sċēawaþ

Derivation: citation reconstruction _\*skawōną_; selected input _\*skáwōθi_ $\rightarrow$ _sċēawaþ_ (late analogy).

#### Derivation trace

Proto input: _\*skáwōθi_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Early I Apocope & \emph{*skáwōθ} \\
\end{tabularx}
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Aw Long Diphthong & \emph{*skḗawōθ} \\
OE Sk Palatalization & \emph{*ʃḗawōθ} \\
OE Late O Shortening & \emph{*ʃḗawaθ} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _sċēawaþ_

#### Reconstruction and comparative evidence

Orel reconstructs the verb as _\*skawōjanan_ and cites Old English _sceáwian_ beside Old Frisian _skawia_, Old Saxon _skawōn_, and Old High German _scouwōn_ [@Orel2003]. The selected input in this entry is the present third singular _\*skáwōθi_, a finite class-II cell rather than the remodeled infinitive [@RingeTaylor2014].

Campbell states the class-II present endings as _lufas, -aþ (< -ōsi, -ōþi)_, and Ringe and Taylor likewise treat the class-II 2sg and 3sg as forms with stable _-a-_ [@Campbell1959; @RingeTaylor2014]. The relevant comparison is therefore the 3sg cell itself, not an i-umlauted alternative.

#### Old English evidence

Bright lists the simplex headword _scēawian_ and the imperative _scēawa_, and under _geond-scēawian_ also records a third singular _-sceawað_ [@BrightCassidyRingler1971]. The evidence thus establishes the _scēaw- / -awað_ finite-cell pattern directly.

The form written here as _sċēawaþ_ is the normalized simplex comparison form for that weak class-II pattern. It is therefore not a dictionary headword but a selected finite form aligned with the attested _scēaw-_ evidence and the directly cited _-sceawað_ ending pattern.

#### Development to Old English

_\*skáwōθi_ first loses final _-i_, giving _\*skáwōθ_. Old English _\*aw_ before vocalic material yields _\*skḗawōθ_, initial _sk_ palatalizes, and late shortening of unstressed _\*ō_ gives _\*ʃḗawaθ_, written _sċēawaþ_ [@Campbell1959]. Campbell's chronology matters here: late-shortened _ō_ yields _a_ too late for Anglo-Frisian fronting, and the class-II 3sg ending therefore gives _-aþ_ rather than _-eþ_ [@Campbell1959; @RingeTaylor2014]. Because the ending never contains _-j-_, no i-umlaut applies.

#### Paradigm comparison

The comparison below is manual.

| PGmc cell / interpretation | Candidate input | Old English outcome or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level infinitive | _\*skáwōjaną_ | manual probe output _sċēawian_ | scēawian | ordinary dictionary headword of the verb, but not the selected finite cell |
| imperative singular companion | _\*skáwô_ | manual probe output _sċēawa_ | scēawa | useful family control, but not the target of this entry |
| selected present third singular | _\*skáwōθi_ | manual probe output _sċēawaþ_ | normalized sċēawaþ; source-side pattern _-sceawað_ | exact match for the selected cell |

\clearpage

## Part V. Reconstructed Old English comparators

These entries use an explicitly reconstructed Old English-stage comparator for
the branch being modelled. The relevant comparison is therefore later than the
Proto-Germanic citation form but still belongs to the lexical derivation layer.

### knob — OE cnobba

Derivation: citation reconstruction _\*knúppaz_; selected input _\*knúbbô_ $\rightarrow$ _cnobba_ (reconstructed Old English comparator).

#### Derivation trace

Proto input: _\*knúbbô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc U Lowering & \emph{*knóbbô} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Unstressed Long Vowel Shortening & \emph{*knóbba} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _cnobba_

#### Reconstruction and comparative evidence

The wider knob-family is not uniform. Kroonen's discussion of the Germanic
n-stems points to related voiced and voiceless branches within this group
[@Kroonen2011]. The citation reconstruction _\*knúppaz_ represents the broader
cognate-set headword, while the selected input _\*knúbbô_ represents the voiced
weak-noun branch treated here.

That distinction matters because the Old English record is uneven. The better
attested OE material belongs to the voiceless branch, but the present entry
represents the reconstructed OE form that would continue the voiced branch
behind later English **knob**.

#### Old English evidence

Bosworth-Toller and Clark Hall preserve Old English evidence of the
_cnopp / cnoppa_ type [@BosworthToller1898; @ClarkHall1960]. Those forms are
genuine Old English evidence, but they belong to the voiceless branch of the
family.

The target _cnobba_ is different in status. It is a **reconstructed Old
English form**, not a directly attested one. The point of using it here is to
give the voiced branch an explicit OE-stage representation instead of allowing
the attested _cnoppa_ branch to stand in for a different prehistory. The choice
of _cnobba_ is therefore a modeling and comparative decision rather than a
settled point of Old English philology.

#### Development to Old English

From the selected weak-noun input _\*knúbbô_, the regular Old English outcome is
_cnobba_, with Proto-Germanic _kn-_ represented in Old English as _cn-_ and
with the expected weak-noun ending.

The entry therefore does not claim that _cnobba_ is attested. Its claim is
different: if the voiced weak-noun branch is the one to be represented, then
_cnobba_ is the regular Old English form corresponding to that branch.

#### Reconstruction status

The comparison below is manual. It keeps apart the reconstructed target and the
better-attested neighboring forms.

| Form | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _\*knúbbô -> cnobba_ | reconstructed OE form; trace-supported | selected target |
| _cnopp / cnoppa_ | attested OE branch | important control form, but belongs to the voiceless branch |
| _cnæp_ | attested OE form from another family | not part of the present lexeme line |

This remains the most review-sensitive item in the present pilot batch, because
the choice between reconstructed _cnobba_ and attested _cnoppa_ is still a
comparator-policy question rather than a settled point of OE attestation.

### reek — OE rēac

Derivation: citation reconstruction _\*ráukiz_; selected input _\*ráukaz_ $\rightarrow$ _rēac_ (reconstructed Old English comparator).

#### Derivation trace

Proto input: _\*ráukaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PGmc Final Z Deletion & \emph{*ráuka} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Au Fronting & \emph{*ráeuka} \\
OE Diphthong Leveling & \emph{*rēaka} \\
PWGmc Final Bare A Loss & \emph{*rēak} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _rēac_

#### Reconstruction and comparative evidence

The wider noun family is represented by _\*ráukiz_ / _\*rauki-_, with Old English
_rēc_ as the attested noun reflex in the comparative dictionaries
[@Kroonen2013, 446; @Orel2003, 338]. The selected input _\*ráukaz_ is therefore not the
lexeme-level headword, but the form used here for the Old English derivation.

#### Old English evidence

The attested noun is _rēc_, not _rēac_. Clark Hall records _rēc_ as the noun
and also preserves related forms such as _rēcels_; Kroonen likewise gives OE
_rēc_ under the noun family [@ClarkHall1960, 255; @Kroonen2013, 446]. Clark
Hall and Seebold also record verbal _rēac_ as the preterite of _rēocan_, but
that verbal form is separate from the noun treated here [@ClarkHall1960, 254;
@Seebold1970, 380].

The selected target _rēac_ is therefore a reconstructed West Saxon noun form,
not a directly attested manuscript headword.

#### Development to Old English

From _\*ráukaz_, the regular West Saxon development gives _rēac_. The attested
noun _rēc_ belongs to the same lexical family, but reflects a later smoothed
surface form rather than the regular noun target represented here.

#### Form note

The distinction here is between an attested noun headword _rēc_ and a
reconstructed regular West Saxon target _rēac_. The latter is treated as the
modelling target, while the former remains philological background.

### strew — OE strīeġan

Derivation: _\*stráwjaną_ $\rightarrow$ _strīeġan_ (reconstructed Old English comparator).

#### Derivation trace

Proto input: _\*stráwjaną_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE Awj Glide Formation & \emph{*stráujaną} \\
OE Au Fronting & \emph{*stráeujaną} \\
OE Diphthong Leveling & \emph{*strēajaną} \\
OE Heavy Syllable Nasal Apocope & \emph{*strēajan} \\
OE Secondary Nasalization & \emph{*strēająn} \\
OE I Umlaut & \emph{*strīejąn} \\
OE Weak Tail Reduction & \emph{*strīejan} \\
OE J Strengthening After Front Diphthong & \emph{*strīeʒan} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Outcome: _strīeġan_

#### Reconstruction and comparative evidence

Kroonen cites the inherited weak verb as _\*straujan-_ and gives Old English
_streowian_ as its dictionary continuation [@Kroonen2013, p. 483]. Ringe and
Taylor make the split within Old English explicit: the inherited class-I verb is
continued by Anglian _strēgan_, while West Saxon _streowian_ is a
remodelled class-II verb [@RingeTaylor2014, §6.1 n. 27].

The aw-series comparison is important here. Luick groups _\*strauwjan_ with the
same set as _\*hauwja-_ and _\*kauwjan_, yielding Anglian _strēzan_ beside West
Saxon forms of the _hīez, ciezan_ type [@Luick1914, §98]. Fulk likewise allows
an early West Saxon _\*striegan_ directly from Proto-Germanic _\*straujana_
[@Fulk2018, §4.10 n. 1].

#### Old English evidence

The attested inherited Old English form is _strēgan_ in Anglian. The
attested West Saxon citation forms are _strewian_, _streowian_, and
_strēawian_, which belong to the remodelled class-II branch
[@RingeTaylor2014, §6.1 n. 27; @Campbell1959, §753.7].

The target _strīeġan_ is therefore a **reconstructed Old English form**, not
an attested manuscript lemma. It is the reconstructed West Saxon reflex of the
inherited class-I verb, chosen to keep the inherited branch distinct from the
better-attested remodelled West Saxon lemma.

#### Development to Old English

From _\*stráwjaną_, the inherited West Saxon development passes through
_\*straujaną_, fronting and leveling to a _\*strēajan-_ stage, i-umlaut to
_\*strīejan_, and retention or strengthening of the glide after the front
diphthong, written here as _ġ_. The resulting form is _strīeġan_.

This differs from Anglian _strēgan_, where smoothing removes the diphthongal
sequence, and from West Saxon _strewian / streowian / strēawian_, where the
verb has already been remodelled into class II [@Fulk2018, §4.10 n. 1;
@Campbell1959, §753.7].

#### Reconstruction status

The comparison below is manual. It keeps apart the attested inherited branch,
the attested remodelled branch, and the reconstructed West Saxon comparator.

| Form or branch | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _strēgan_ | attested Anglian inherited class-I form | proves that the inherited verb survived into Old English |
| _strīeġan_ | reconstructed West Saxon inherited class-I form; trace-supported | selected target |
| _strewian / streowian / strēawian_ | attested remodelled West Saxon class-II forms | genuine OE evidence, but not the inherited branch modeled here |

\clearpage

## Part VI. Known but unmodelled remodellings

These entries preserve cases where the historical remodelling is broadly
understood, but the current deterministic transducer does not model that later
reshaping directly.

### fire — OE fȳre

Derivation: _\*fūri_ yields regular _fȳr_; the selected target is _fȳre_ (known but unmodelled remodelling).

#### Derivation trace

Proto input: _\*fūri_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE I Umlaut & \emph{*fȳri} \\
OE High Vowel Apocope & \emph{*fȳr} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Transducer outcome: _fȳr_

Selected target: _fȳre_

#### Reconstruction and comparative evidence

Kroonen places the lexeme in a heteroclitic family _\*fōr ~ \*fun-_ and explains
the front-mutated West Germanic forms from an oblique form of the
_\*fu(w)eri_ type [@Kroonen2013]. The selected input _\*fūri_ therefore does not
function as an arbitrary substitute for the headword: it represents the
specific inherited cell that supplies the _i_ needed for i-umlaut.

That distinction matters because the Old English target combines a regular
inherited form _fȳr_ with an attested analogical surface form _fȳre_.

#### Old English evidence

Bosworth-Toller records _fyr_ as the noun 'fire' and also preserves oblique
_fyre_ in the Old English record [@BosworthToller1898, 288]. The first is the
regular inherited outcome of the phonological development from the selected
input; the second shows the later restoration of a final _-e_ within the
paradigm.

The entry therefore concerns the relation between a regular inherited oblique
input and an attested Old English surface form that has undergone later
morphological remodeling.

#### Development to Old English

From _\*fūri_, i-umlaut changes _ū_ to _ȳ_, and subsequent loss of the final high
vowel after a heavy syllable yields _fȳr_ [@RingeTaylor2014; @Hogg1992;
@Campbell1959]. The inherited phonology is complete at that point.

_fȳre_ is later than that inherited output. Its final _-e_ belongs to
analogical restoration in the Old English paradigm rather than to the original
Proto-Germanic ending. The form therefore remains _known_unmodelled_: the
deterministic phonology is regular, but the attested surface form includes
later morphological rebuilding.

#### Paradigm comparison

The comparison below is manual. It distinguishes the lexeme-level etymological
background from the inherited cell that actually produces the front-mutated
form and from the later analogical surface result.

| PGmc cell / interpretation | Candidate input | OE output or comparison | OE comparison form | Result |
| :--- | :--- | :--- | :--- | :--- |
| lexeme-level heteroclitic headword | _\*fōr ~ \*fun-_ | comparative background only | fire family | explains the wider lexeme, but not the selected oblique input |
| inherited oblique cell | *fūri | compact-trace output: _fȳr_ | fȳr | regular inherited output from the selected input |
| later analogical surface form | — | attested _fȳre_ with restored _-e_ | fȳre | genuine OE target, but not the direct phonological output |

### tap — OE tæppa

Derivation: _\*táppô_ yields regular _tappa_; the selected target is _tæppa_ (known but unmodelled remodelling).

#### Derivation trace

Proto input: _\*táppô_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
Anglo Frisian Brightening & \emph{*tæppô} \\
OE A Restoration & \emph{*tappô} \\
OE Unstressed Long Vowel Shortening & \emph{*tappa} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Transducer outcome: _tappa_

Selected target: _tæppa_

#### Reconstruction and comparative evidence

Orel gives the noun under _\*tappòn_ and already connects it with Old English
_tæppa_ [@Orel2003]. The selected input is therefore the inherited noun itself;
the entry does not depend on a different lexeme-level proto or a different
inherited noun cell.

#### Old English evidence

The Old English noun family is well attested. Orel gives _tæppa_, and Clark
Hall records _tæppa_ together with derivatives _tæppere_ and _tæppestre_
[@Orel2003; @ClarkHall1960, 305]. The target is therefore a real Old English noun
form, not a reconstructed convenience spelling.

#### Development to Old English

From _\*táppô_, the regular inherited noun path gives _tappa_. The attested
target _tæppa_ therefore stands outside that regular phonological development.

The mismatch is historically intelligible, but it is not solved here by a new
inherited input. A related j-verb pathway would give _teppan_, not the noun
target _tæppa_. The entry accordingly remains _known_unmodelled_.

#### Form comparison

| Form type | Input or form | OE output or comparison | Result |
| :--- | :--- | :--- | :--- |
| regular inherited noun path | *táppô | compact-trace output: _tappa_ | regular output, but not the target |
| attested OE target | — | _tæppa_ | genuine target form, but analogically remodelled in the present classification |
| related j-verb background | *táppjaną | _teppan_ | related formation, but not the noun target |

\clearpage

## Part VII. Unexplained or deliberately unmodelled exceptions

These entries preserve a mismatch between the regular transducer output and the
selected Old English target. They are retained as documented lexical exceptions
rather than treated as evidence for further sound-change repair.

### buck — OE bucc

Derivation: _\*búkkaz_ yields regular _bocc_; the selected target is _bucc_ (unexplained exception).

#### Derivation trace

Proto input: _\*búkkaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc U Lowering & \emph{*bókkaz} \\
PGmc Final Z Deletion & \emph{*bókka} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Final Bare A Loss & \emph{*bókk} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Transducer outcome: _bocc_

Selected target: _bucc_

#### Reconstruction and comparative evidence

Kroonen and Orel both reconstruct the word with a geminate stop, _\*bukkaz_, and
both also preserve parallel n-stem material behind Old English _bucca_
[@Kroonen2013; @Orel2003]. The selected input therefore remains identical with
the lexeme label: no alternative inherited cell accounts for the form.

#### Old English evidence

Old English preserves a mixed lexical picture. Campbell cites _bucca_ in the
exception set for this phonological environment, while Clark Hall and
Bosworth-Toller show that Old English has both _bucca_ and _bucc_
[@Campbell1959; @ClarkHall1960; @BosworthToller1898, 122]. The a-stem citation form
_bucc_ is the target treated here, with _bucca_ kept as genuine philological
background from the same lexical family.

#### Development to Old English

From _\*búkkaz_, the regular inherited path gives _bocc_. That is the form
expected under the ordinary lowering pattern in this environment. _bucc_
therefore remains outside the deterministic phonology.

No accepted inherited cell repairs the mismatch. A high-vowel alternative would
introduce i-umlaut and produce a _byċċ_-type form rather than the target.
_bucc_ is therefore best treated as a documented exception, not as a regular
paradigm-cell survival.

#### Form comparison

| Form type | Input or form | OE output or comparison | Result |
| :--- | :--- | :--- | :--- |
| regular inherited noun path | *búkkaz | compact-trace output: _bocc_ | regular output, but not the target |
| attested OE target | — | _bucc_ | genuine target form, but unexplained in the present classification |
| parallel OE lexical background | — | _bucca_ | related n-stem form, not the present target |

### fowl — OE fugol

Derivation: _\*fúglaz_ yields regular _fogol_; the selected target is _fugol_ (unexplained exception).

#### Derivation trace

Proto input: _\*fúglaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc U Lowering & \emph{*fóglaz} \\
PGmc Final Z Deletion & \emph{*fógla} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Final Bare A Loss & \emph{*fógl} \\
OE Epenthetic Vowel & \emph{*fógol} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Transducer outcome: _fogol_

Selected target: _fugol_

#### Reconstruction and comparative evidence

The noun is the ordinary Germanic a-stem _\*fúglaz_, continued by forms such as
Old Norse _fugl_ and Old High German _fogal_ [@Kroonen2013, 197; @Orel2003,
155]. There
is no stem-class or paradigm-cell dispute behind this entry. The comparative
headword and the selected input are the same.

The difficulty lies instead in the stressed root vowel. Under the regular West
Germanic and Old English development, that _u_ should lower before the following
non-high vowel, yielding an _o_-vocalism
[@RingeTaylor2014, 42–43; @Campbell1959, 43].

#### Old English evidence

Old English dictionaries record the noun as _fugol_, with variant spelling
_fugel_ [@BosworthToller1898, 282; @ClarkHall1960, 138]. The target is therefore an
attested ordinary Old English noun, not a reconstructed or selectively chosen
paradigm form.

The attested word already contains the crucial problem. Its medial _-o-_ is the
ordinary parasite vowel of Old English cluster phonology, but the root _fu-_
retains _u_ where the regular history predicts _fo-_ [@Campbell1959, 150].

#### Development to Old English

From _\*fúglaz_, the regular cascade yields _fogol_: the root vowel lowers before
the following non-high vowel [@RingeTaylor2014, 42–43; @Campbell1959, 43],
final _z_ is lost, and the cluster is resolved by the usual medial vowel
[@RingeTaylor2014, 345; @Campbell1959, 150]. That is the expected inherited
outcome.

The attested Old English noun is _fugol_, not _fogol_. Luick and later
handbooks treat this preservation of _u_ as a small inherited residue, not as a
categorical sound law [@Luick1914, 148; @RingeTaylor2014, 47]. The item
therefore remains a genuine lexical exception rather than
the output of a recoverable regular mechanism.

#### Expected and attested forms

The comparison below is manual. It distinguishes the regular prediction from the
attested Old English noun.

| Form | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _fogol_ | computed regular output from _\*fúglaz_ | establishes the expected inherited outcome |
| _fugol_ | attested Old English form | selected target; preserves unexplained root _u_ |
| _fugel_ | attested variant spelling | secondary spelling variant of the attested noun |

The unresolved point lies only in the root vowel. The medial _-o-_ is regular,
but no accepted lautgesetzlich pathway has been found from _\*fúglaz_ to
attested _fugol_.

### rust — OE rust

Derivation: _\*rústō_ yields regular _rost_; the selected target is _rust_ (unexplained exception).

#### Derivation trace

Proto input: _\*rústō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc U Lowering & \emph{*róstō} \\
NWGmc Final Long O Raising & \emph{*róstu} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE High Vowel Apocope & \emph{*róst} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Transducer outcome: _rost_

Selected target: _rust_

#### Reconstruction and comparative evidence

The comparative dictionaries do not support a single citation reconstruction
uniformly. Orel cites _\*rustaz sb.m./f._ with Old English _rust_ and Old Saxon
and Old High German _rost_ [@Orel2003]. The form _\*rústō_ therefore stands here
as a competing citation reconstruction rather than as the best-supported
inherited headword.

That disagreement does not remove the central problem. Whether one starts from
_\*rústō_ or from source-supported _\*rustaz_, the regular citation-form history
points toward _rost_, not toward the attested Old English noun.

#### Old English evidence

The Old English noun is attested, not reconstructed. Clark Hall gives _rūst m._
[@ClarkHall1960], and Bosworth-Toller records _rúst (? and rust)_
[@BosworthToller1898, 677]. The form is normalized here as _rust_ from that attested
record.

Those dictionary entries also matter morphologically. They support a masculine
noun, which aligns better with Orel's _\*rustaz_ than with the competing _\*rústō_
preserved in the header.

#### Development to Old English

Under the regular lowering of stressed _u_ before a following non-high vowel,
the citation-form input gives _rost_, not _rust_ [@Campbell1959;
@RingeTaylor2014]. The same regular result follows from the comparative
citation-form reconstruction _\*rustaz_.

A high-vowel comparator such as instrumental-type _\*rústu_ would yield _rust_
regularly, but that does not explain the attested citation form of the noun. No
accepted regular pathway from the citation form to attested _rust_ has been
established.

#### Expected and attested forms

The comparison below is manual. It separates the regular inherited outcomes from
the attested Old English noun.

| Form / interpretation | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _\*rústō -> rost_ | computed regular output from one competing citation reconstruction | shows that this citation reconstruction does not reach attested _rust_ |
| _\*rustaz -> rost_ | expected regular output from the source-supported citation reconstruction | shows that correcting the stem class does not solve the vowel problem |
| _\*rústu -> rust_ | regular high-vowel comparator | useful negative control, but not a defensible citation-form solution |
| _rust_ | attested Old English noun, normalized from _rūst / rúst / rust_ | selected target; the citation-form development remains unexplained |

### wolf — OE wulf

Derivation: _\*wúlfaz_ yields regular _wolf_; the selected target is _wulf_ (unexplained exception).

#### Derivation trace

Proto input: _\*wúlfaz_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc U Lowering & \emph{*wólfaz} \\
PGmc Final Z Deletion & \emph{*wólfa} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
PWGmc Final Bare A Loss & \emph{*wólf} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Transducer outcome: _wolf_

Selected target: _wulf_

#### Reconstruction and comparative evidence

The inherited noun is an a-stem: Kroonen gives _\*wulfa-_, and the regular Old
English development of that citation form is the same one reflected by Old High
German _wolf_ [@Kroonen2013; @RingeTaylor2014]. Campbell accordingly names Old
English _wulf_ as an exception to the regular lowering of stressed _u_ before a
following non-high vowel [@Campbell1959].

The older literature often notices that the exceptional words cluster near
labials. Bülbring lists _full_, _wulle_, and _wulf_ together, but he also says
that the ordinary rule still gives _o_ in comparable forms such as _folc_ and
_bolt_ [@Bulbring1902]. Luick rejects a categorical labial blocker on the same
grounds and prefers a lexical or analogical account instead [@Luick1914, 148].

#### Old English evidence

Old English _wulf_ is an attested noun, and the handbook tradition treats it as
the ordinary lexical form while simultaneously recognizing its exceptional vowel
[@Campbell1959; @SieversBrunner1965]. The oblique form _wulfe_ also belongs to
the record, but Sievers-Brunner warns that this type continues _wulfi_ only with
i-umlaut later abandoned across the paradigm [@SieversBrunner1965].

That warning matters because the surviving oblique forms do not supply a clean
regular route back to bare _wulf_. They belong to the same lexeme, but they do
not remove the explanatory problem presented by the citation form.

#### Development to Old English

Under the regular lowering of stressed _u_, the citation-form input gives
_wolf_, not _wulf_ [@Campbell1959; @RingeTaylor2014]. The compact trace shows
exactly that path: _\*wúlfaz > \*wólfaz > \*wólfa > wolf_.

A high-vowel oblique input would behave differently. The following high vowel
would block the lowering of _u_, but the same environment would trigger
i-umlaut, so the regular result would be _wylf_ or _wylfe_, not bare _wulf_
[@SieversBrunner1965]. The attested noun therefore remains unexplained at the
citation-form level.

#### Expected and attested forms

The comparison below is manual. It separates the regular inherited outcomes from
the attested Old English noun.

| Form / interpretation | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _\*wúlfaz -> wolf_ | computed regular output from the citation form | shows the regular development expected from the inherited a-stem |
| _OHG wolf_ | comparative regular cognate | confirms that the _o_-vocalism is the ordinary outcome |
| _\*wúlfi / \*wúlfis -> wylf / wylfe_ | expected high-vowel control forms | shows why oblique high-vowel cells do not solve the noun's vowel history |
| _wulf_ | attested Old English noun | selected target; the preservation of _u_ remains unexplained |

### wool — OE wull

Derivation: _\*wúllō_ yields regular _woll_; the selected target is _wull_ (unexplained exception).

#### Derivation trace

Proto input: _\*wúllō_

\begingroup
\setlength{\fboxsep}{6pt}
\noindent\fbox{%
\begin{minipage}{0.97\linewidth}
\small
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Earlier Germanic changes}\par
\vspace{0.35em}
\raggedright
\centering\textbf{West Germanic}\par
\raggedright
\vspace{0.2em}
\raggedright [no change]\par
\vspace{0.6em}
\centering\textbf{Northwest Germanic}\par
\raggedright
\vspace{0.2em}
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
NWGmc U Lowering & \emph{*wóllō} \\
NWGmc Final Long O Raising & \emph{*wóllu} \\
\end{tabularx}
\end{minipage}\hfill
\begin{minipage}[t]{0.485\linewidth}
\centering\textbf{Old English changes}\par
\vspace{0.35em}
\raggedright
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}X>{\raggedleft\arraybackslash}p{0.34\linewidth}@{}}
OE High Vowel Apocope & \emph{*wóll} \\
\end{tabularx}
\end{minipage}
\end{minipage}%
}
\endgroup

Transducer outcome: _woll_

Selected target: _wull_

#### Reconstruction and comparative evidence

The inherited form is a feminine ō-stem _\*wúllō_. In the ordinary phonological
history of West Germanic, stressed _u_ lowers before a following non-high vowel,
so the regular Old English outcome is an _o_-form. Campbell's discussion of the
parallel adjective _full_, with OHG _foll_ as the regular comparator, shows that
the handbooks treat this as a genuine exception cluster rather than as a place
where the rule itself is doubtful [@Campbell1959, §115].

Bülbring likewise lists _wulle_ among the traditional _u_-preserving
exceptions [@Bulbring1902, §116]. The comparative evidence therefore establishes
two things at once: the regular result should be _woll_, and Old English still
has a lexical exception of the _wull / wulle_ type.

#### Old English evidence

The Old English target is given here as _wull_, a normalized lexeme form.
Handbook discussion often cites _wulle_, the feminine weak form of the noun
[@Bulbring1902, §116]. Both point to the same lexical item and to the same
exceptional preservation of root _u_.

The OE evidence therefore does not remove the problem. It confirms that the
language has a _u_-form where the regular phonology would have produced _o_.

#### Development to Old English

From _\*wúllō_, the regular sequence is lowering of stressed _u_ before a
non-high vowel, followed by the ordinary later reductions of the ending. The
regular outcome is therefore _woll_.

That regular derivation is not the attested Old English form. Luick rejects a
simple phonological rule that would protect this word alone, and Ringe and
Taylor state the larger problem plainly: we do not really know why _\*u_ failed
to lower in forms of this sort [@Luick1914, 148; @RingeTaylor2014, §2.3.1].

#### What remains unexplained

The comparison below is manual. It separates the regular trace result from the
attested lexical exception.

| Form | Status | Relevance to this entry |
| :--- | :--- | :--- |
| _\*wúllō -> woll_ | regular trace output | shows what the deterministic sound laws produce |
| _wull / wulle_ | attested OE exception | selected target and philological fact to be recorded |
| high-vowel escape from another paradigm cell | unsupported for this noun | rejected because the feminine ō-stem paradigm supplies no suitable escape cell |
