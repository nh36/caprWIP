#!/usr/bin/env python3
"""Regenerate FARMAN_ACCENTS.tsv: a calibration census of every acute-accented
token in Farman's portion of the Rushworth gloss (Mt 1:1 - Mk 2:15), as printed
by Tamoto (2013).

Source text (private, Git-ignored):
    docs/references/local/scholarly-2026-11-23/tamoto2013.txt
Farman's stint occupies file lines 5908-11738 of that extraction
(Mt begins at the edition's fol. 1r = file line 5908 "boéc sindun ...";
Mk 2:15 "ł hleonadun", Farman's last word, is at file line 11738).

Method:
  * A token counts as accented if its NFD normalization contains U+0301.
  * Latin lemmata of the gospel text also carry acutes in Tamoto's print
    (mostly -ís ablatives); these are excluded by an explicit verified list.
  * Loci are given by manuscript folio, tracked from Tamoto's inline
    "[folio Nr/v]" markers, plus the file line for audit.
  * Each Old English type is classified for etymological vowel quantity
    (long / short / short-HL / uncertain / target), with grounds.
    "short-HL" = etymologically short vowel standing before a homorganic
    cluster (ld, nd, rd, ng), i.e. in the environment of pre-cluster
    lengthening; such accents are compatible with a lengthened nucleus
    in Farman's late tenth-century speech.

The two hóeg tokens (Mt 6:30, Mt 14:19) are the forms under investigation
and are excluded from the calibration statistics ("target").

Run from the repository root:
    python3 Germanic/articles/hay/extract_farman_accents.py
"""

import collections
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "docs/references/local/scholarly-2026-11-23/tamoto2013.txt"
OUT = Path(__file__).resolve().parent / "FARMAN_ACCENTS.tsv"

START, END = 5907, 11738  # 0-based slice bounds of Farman's stint

def nfc(s):
    return unicodedata.normalize("NFC", s)

# Latin tokens of the gospel text (and letter-names) verified in context.
LATIN = set(nfc(t) for t in """
acceptís agriculís alís ámen ámore apertís bulís caelís cælís cenís conseruís
conuocatís cóinquinant cór dá demissís dextrís discipulís ebrís és ét? excelsís
falsís filís fragmentís fulgebánt hierusolimís hippochritís híc hís illís istís
isác íít iudicí lís loquí mandatís ministrís monumentís mortuís multís né
nostrís ó ós parabulís paruulís pillís profétis proiectís puerís pussillís
relictís scopís scribís scripturís sepulchrís sí síc Síc sinagogís sól somnís
suís súis testé té thesaurís turbís túis tú túmultuantem uarís uassís uerbís
uestimentís uestrís uobís uís í
""".split())

# (lemma, quantity_class, grounds) keyed by NFC surface form.
CLASSIFICATION = {nfc(k): v for k, v in {
 'á': ('ā “ever”', 'long', 'BT ā'),
 'áe': ('ǣ “law”', 'long', 'BT ǣ'), 'ǽ': ('ǣ “law”', 'long', 'BT ǣ'),
 'ǽfter': ('æfter', 'short', 'BT æfter, short æ'),
 'ǽlde': ('ǣlan “kindle” pret.', 'long', 'BT ǣlan (Mt 25:7, lamps)'),
 'abíd': ('ābīdan imp.', 'long', 'bīdan, long ī'),
 'abít': ('ābītan 3sg', 'long', 'bītan, long ī'),
 'afróefrede': ('ā-frēfran pret.', 'long', 'frēfran, long ē; ⟨oe⟩ spelling'),
 'áhæfæþ': ('ā-hebban (accent on prefix)', 'long', 'ā- prefix long; stem short'),
 'áhæfen': ('ā-hebban pp. (prefix)', 'long', 'ā- prefix long'),
 'áhæfgad': ('ā-hefigian pp. (prefix)', 'long', 'ā- prefix long'),
 'áhengon': ('ā-hōn pret.pl. (prefix)', 'long', 'ā- prefix long; -hēngon also long'),
 'áhongen': ('ā-hōn pp. (prefix)', 'long', 'ā- prefix long'),
 'ahélde': ('ā-heldan “incline” pret.', 'uncertain', 'heldan/hyldan < *hulþjan, short stem; accent on stem é'),
 'ahýded': ('ā-hȳdan pp.', 'long', 'hȳdan, long ȳ'),
 'aléfed': ('ā-lēfan “permit” pp.', 'long', 'Angl. lēfan = WS līefan, long'),
 'án': ('ān “one”', 'long', 'BT ān'),
 'áras': ('ā-rīsan pret. (prefix)', 'long', 'ā- prefix long; -rās also long'),
 'áre': ('ār “honour” dat.', 'long', 'BT ār'),
 'árefrendlicre': ('ā-rēfnendlic (prefix)', 'long', 'ā- prefix long; cf. ārǣfnan'),
 'arísaþ': ('ā-rīsan pl.', 'long', 'rīsan, long ī'),
 'áriseþ': ('ā-rīsan 3sg (prefix)', 'long', 'ā- prefix long'),
 'ascákeþ': ('ā-sceacan 3sg', 'short', 'sceacan, short a; accent on stem'),
 'astág': ('ā-stīgan pret.', 'long', 'stāg, long ā'),
 'ástág': ('ā-stīgan pret. (prefix)', 'long', 'ā- prefix long; stāg also long'),
 'áþiostraþ': ('ā-þīostrian (prefix)', 'long', 'ā- prefix long; þīostor long diphthong'),
 'áweorpnisse': ('ā-worpennes (prefix)', 'long', 'ā- prefix long; stem short'),
 'awóested': ('ā-wēstan pp.', 'long', 'wēstan, long ē; ⟨oe⟩ spelling'),
 'æt-hrán': ('æt-hrīnan pret.', 'long', 'hrān, long ā'),
 'áld': ('ald “old”', 'short-HL', 'short a + ld (Angl. unbroken); HL environment'),
 'beháldeþ': ('be-haldan 3sg', 'short-HL', 'short a + ld; HL environment'),
 'béod': ('bēod “table”', 'long', 'BT bēod, long ēo'),
 'bére': ('bēr “bier”', 'long', 'BT bēr, long ē'),
 'blód': ('blōd', 'long', 'BT blōd'),
 'blóde': ('blōd dat.', 'long', 'BT blōd'),
 'blódes': ('blōd gen.', 'long', 'BT blōd'),
 'blód-gyte': ('blōd-gyte', 'long', 'blōd long; accent on blód'),
 'boéc': ('bēc “book(s)”', 'long', 'i-umlaut of ō, long; ⟨oe⟩ spelling'),
 'bóec': ('bēc', 'long', 'as boéc'),
 'brýd-guma': ('brȳd-guma', 'long', 'brȳd, long ȳ'),
 'brýde': ('brȳd dat.', 'long', 'BT brȳd'),
 'cild-fóedendum': ('cild-fēdende dat.pl.', 'long', 'fēdan, long ē; ⟨oe⟩'),
 'crǽd': ('crāwan pret. “crew”', 'uncertain', 'Angl. contracted pret. crǣd; quantity of contracted pret. debated'),
 'dǽle': ('dǣl “part” dat.', 'long', 'BT dǣl'),
 'dégles': ('dēgol “secret” gen.', 'long', 'Angl. dēgol = WS dīegol, long'),
 'deoful-sóece': ('dēofol-sēoc', 'long', 'sēoc, long ēo; ⟨oe⟩ spelling'),
 'dóa': ('dōn subj.', 'long', 'dōn, long ō'),
 'dóeþ': ('dōn 3sg/imp.pl.', 'long', 'dōn'),
 'dóþ': ('dōn pl.', 'long', 'dōn'),
 'dónde': ('dōn pres.part.', 'long', 'dōn'),
 'gedóan': ('ge-dōn pp.', 'long', 'dōn'),
 'gedóen': ('ge-dōn pp.', 'long', 'dōn'),
 'dóm': ('dōm', 'long', 'BT dōm'),
 'dúne': ('dūn dat.', 'long', 'BT dūn'),
 'eáé': ('ēa “flood”', 'long', 'BT ēa, long'),
 'éc': ('ēc “also”', 'long', 'Angl. ēc = WS ēac'),
 'ége': ('ege “fear”', 'short', 'BT ege, short e'),
 'éode': ('ēode “went”', 'long', 'BT ēode'),
 'ét': ('ēt “ate”', 'long', 'pret. of etan, Angl. ēt = WS ǣt'),
 'ét‘o’n': ('ēton “ate” pl.', 'long', 'pret.pl. of etan, Angl. ē'),
 'fíc': ('fīc “fig(-tree)”', 'long', 'BT fīc, long ī'),
 'físcæs': ('fisc gen.', 'short', 'BT fisc, short i'),
 'fóedel-fuglas': ('fēdels-fuglas', 'long', 'fēdan, long ē; ⟨oe⟩'),
 'fóeran': ('fēran', 'long', 'fēran, long ē; ⟨oe⟩'),
 'foérde': ('fēran pret.', 'long', 'fēran; ⟨oe⟩'),
 'infoérde': ('in-fēran pret.', 'long', 'fēran; ⟨oe⟩'),
 'fóne': ('fōn infl.inf.', 'long', 'fōn, long ō'),
 'gá': ('gān imp./subj.', 'long', 'gān, long ā'),
 'gáð': ('gān pl.', 'long', 'gān'),
 'gáþ': ('gān pl.', 'long', 'gān'),
 'gǽþ': ('gǣþ 3sg', 'long', 'gān'),
 'gáeþ': ('gāeþ 3sg', 'long', 'gān'),
 'utgáeþ': ('ūt-gāeþ 3sg', 'long', 'gān'),
 'gángan': ('gangan', 'short-HL', 'short a + ng; HL environment'),
 'gánge': ('gangan 1sg', 'short-HL', 'short a + ng'),
 'gæfel-geróefe': ('gafol-gerēfa', 'long', 'gerēfa, long ē; ⟨oe⟩'),
 'geróefum': ('gerēfa dat.pl.', 'long', 'gerēfa; ⟨oe⟩'),
 'gehróefa': ('gerēfa (h-spelling)', 'long', 'gerēfa; ⟨oe⟩'),
 'gæfel-hróefe': ('gafol-gerēfa', 'long', 'gerēfa; ⟨oe⟩'),
 'gé': ('gē “ye”', 'long', 'BT gē'),
 'ge-hǽl': ('hǣlan imp.', 'long', 'hǣlan, long ǣ'),
 'gehǽl': ('hǣl/hǣlan', 'long', 'hǣlan'),
 'gehǽlde': ('hǣlan pret.', 'long', 'hǣlan'),
 'hǽl': ('hǣlan imp.', 'long', 'hǣlan'),
 'hǽlon': ('hǣlan pret.pl.', 'long', 'hǣlan'),
 'ge-héreð': ('hēran 3sg', 'long', 'Angl. hēran = WS hīeran'),
 'ge-héreþ': ('hēran 3sg', 'long', 'hēran'),
 'gehérde': ('hēran pret.', 'long', 'hēran'),
 'gehóerde': ('hēran pret.', 'long', 'hēran; ⟨oe⟩'),
 'gehoérde': ('hēran pret.', 'long', 'hēran; ⟨oe⟩'),
 'gehóerað': ('hēran pl.', 'long', 'hēran; ⟨oe⟩'),
 'gehóære': ('hēran subj.', 'long', 'hēran; ⟨oe⟩'),
 'gehýrde': ('hȳran pret.', 'long', 'hȳran, long ȳ'),
 'héred': ('hēran/herian pp.?', 'uncertain', 'if hēred (hēran) long; if hered (herian) short'),
 'gedróefed': ('ge-drēfan pp.', 'long', 'drēfan, long ē; ⟨oe⟩'),
 'gehroéred': ('ge-hrēran pp.', 'long', 'hrēran, long ē; ⟨oe⟩'),
 'gelóme': ('gelōme', 'long', 'BT gelōme, long ō'),
 'gemérdon': ('ge-mǣran pret.pl. “made known”', 'long', 'mǣre, long; Angl. ē'),
 'gemoéted': ('ge-mētan pp.', 'long', 'mētan, long ē; ⟨oe⟩'),
 'gemótum': ('gemōt dat.pl.', 'long', 'BT gemōt'),
 'geseáeþ': ('gesēon pl.', 'long', 'contracted sēon, long nucleus'),
 'geséaeþ': ('gesēon pl.', 'long', 'as geseáeþ'),
 'geséáeþ': ('gesēon pl.', 'long', 'as geseáeþ'),
 'geséanae': ('gesēne “visible”', 'long', 'Angl. gesēne, long ē'),
 'geségon': ('sēon pret.pl.', 'long', 'Angl. sēgon, long ē'),
 'geségun': ('sēon pret.pl.', 'long', 'sēgon'),
 'gestód': ('ge-standan pret.', 'long', 'stōd, long ō'),
 'stód': ('standan pret.', 'long', 'stōd'),
 'gód': ('gōd “good”', 'long', 'BT gōd, long ō (≠ god “God”)'),
 'góde': ('gōd infl.', 'long', 'gōd'),
 'gódne': ('gōd acc.', 'long', 'gōd'),
 'góld': ('gold', 'short-HL', 'short o + ld; HL environment'),
 'gólde': ('gold dat.', 'short-HL', 'short o + ld'),
 'gú-monnum': ('iū-/gū-monnum “men of old”', 'long', 'iū/gēo, long'),
 'gúmonnum': ('iū-monnum', 'long', 'iū'),
 'hǽtu': ('hǣtu “heat”', 'long', 'BT hǣtu, long ǣ'),
 'hí': ('hī “they”', 'long', 'BT hī'),
 'hóanne': ('hōn infl.inf. “crucify”', 'long', 'hōn, long ō'),
 'hóaþ': ('hōn pl.', 'long', 'hōn'),
 'hóeg': ('hēg “hay” (TARGET)', 'target', 'the form under investigation; excluded from calibration'),
 'hóehtnisse': ('ēhtnes “persecution”', 'long', 'ēhtan, long ē; ⟨oe⟩ + inorganic h'),
 'hónd': ('hond', 'short-HL', 'short o + nd; HL environment'),
 'hórd': ('hord', 'short-HL', 'short o + rd; HL environment'),
 'hrán': ('hrīnan pret.', 'long', 'hrān, long ā'),
 'hrǽþe': ('hraþe/hrǣþe “quickly”', 'uncertain', 'both short hraþe and long hrǣþe attested (BT)'),
 'hú': ('hū', 'long', 'BT hū'),
 'ínn': ('inn “in(side)”', 'short', 'BT inn, short i'),
 'lác': ('lāc “gift”', 'long', 'BT lāc'),
 'lánge': ('lange adv.', 'short-HL', 'short a + ng; HL environment'),
 'láre': ('lār dat.', 'long', 'BT lār'),
 'lǽdeþ': ('lǣdan 3sg', 'long', 'lǣdan, long ǣ'),
 'lét': ('lǣtan pret.', 'long', 'Angl. lēt, long ē'),
 'líc': ('līc “body”', 'long', 'BT līc'),
 'lónd': ('lond', 'short-HL', 'short o + nd; HL environment'),
 'lónde': ('lond dat.', 'short-HL', 'short o + nd (one token quoted in Tamoto fn.)'),
 'mín': ('mīn', 'long', 'BT mīn'),
 'mónige': ('monige “many”', 'short', 'monig, short o; clearest counterexample'),
 'mót': ('mōtan 3sg “may”', 'long', 'mōt, long ō'),
 'nǽfræ': ('nǣfre', 'long', 'ne + ǣfre, long ǣ'),
 'nú': ('nū', 'long', 'BT nū'),
 'ofslǽan': ('of-slēan', 'long', 'contracted slēan, long nucleus'),
 'ón': ('on prep.', 'short', 'short o; anomalous accent'),
 'ond-fóþ': ('ond-fōn pl.', 'long', 'fōn, long ō'),
 'onfóeð': ('on-fōn 3sg', 'long', 'fōn; ⟨oe⟩'),
 'onfóeþ': ('on-fōn 3sg', 'long', 'fōn; ⟨oe⟩'),
 'ondréd': ('on-drǣdan pret./imp.', 'long', 'Angl. ondrēd, long ē'),
 'ongǽgn': ('ongægn/ongēan “against”', 'uncertain', 'WS ongēan long; gegn- forms short'),
 'onsóc': ('on-sacan pret.', 'long', 'onsōc, long ō'),
 'rás': ('rīsan pret.', 'long', 'rās, long ā'),
 'róde': ('rōd dat. “cross”', 'long', 'BT rōd'),
 'rúm': ('rūm “broad”', 'long', 'BT rūm'),
 'sáe': ('sǣ', 'long', 'BT sǣ'),
 'sáé': ('sǣ', 'long', 'BT sǣ'),
 'sǽ': ('sǣ', 'long', 'BT sǣ'),
 'sæé': ('sǣ', 'long', 'BT sǣ'),
 'saés': ('sǣ gen.', 'long', 'BT sǣ'),
 'scán': ('scīnan pret.', 'long', 'scān, long ā'),
 'scép': ('scēp “sheep”', 'long', 'Angl. scēp = WS scēap, long'),
 'scépa': ('scēp gen.pl.', 'long', 'scēp'),
 'scípa': ('scip gen.pl.', 'short', 'BT scip, short i'),
 'scýnde': ('(ge)scyndan? “shortened”', 'uncertain', 'scyndan short y; lemma uncertain (Mt 24:22)'),
 'sé': ('sē dem.', 'long', 'BT sē, long ē'),
 'séd': ('sēd “seed”', 'long', 'Angl. sēd = WS sǣd, long'),
 'séǽd': ('sēd (double accent)', 'long', 'as séd'),
 'sláe': ('slēan subj.', 'long', 'contracted slēan'),
 'slán': ('slēan', 'long', 'contracted slēan'),
 'slógun': ('slēan pret.pl.', 'long', 'slōgon, long ō'),
 'sónde': ('sond dat. “sand”', 'short-HL', 'short o + nd; HL environment'),
 'stán': ('stān', 'long', 'BT stān'),
 'stáne': ('stān dat.', 'long', 'BT stān'),
 'stéfn': ('stefn “voice”', 'short', 'BT stefn, short e; clearest counterexample'),
 'stígas': ('stīg acc.pl. “paths”', 'long', 'BT stīg, long ī'),
 'swǽr': ('swǣr “heavy/hard”', 'long', 'BT swǣr, long ǣ'),
 'tán': ('tān “lot(s)”', 'long', 'BT tān'),
 'tén': ('tēn “ten”', 'long', 'Angl. tēn = WS tīen, long'),
 'tíd': ('tīd', 'long', 'BT tīd'),
 'tóþ': ('tōþ', 'long', 'BT tōþ'),
 'tóþa': ('tōþ gen.pl.', 'long', 'BT tōþ'),
 'tún': ('tūn', 'long', 'BT tūn'),
 'únklene': ('unclǣne (accent on un-)', 'short', 'un- short prefix; anomalous placement'),
 'út': ('ūt', 'long', 'BT ūt'),
 'út-gangende': ('ūt-gangende', 'long', 'ūt'),
 'þær-úte': ('þǣr-ūte', 'long', 'ūte, long ū'),
 'wá': ('wā “woe”', 'long', 'BT wā'),
 'wéde': ('wǣde “garment”', 'long', 'Angl. wēde = WS wǣde, long'),
 'wég': ('weg “way”', 'short', 'BT weg, short e; clearest counterexample'),
 'wén': ('wēn “expectation”', 'long', 'BT wēn'),
 'wéod': ('wēod “weed”', 'long', 'BT wēod, long ēo'),
 'wépan': ('wēpan', 'long', 'BT wēpan, long ē'),
 'wépaþ': ('wēpan pl.', 'long', 'wēpan'),
 'wéstan': ('westan “from the west”', 'uncertain', 'westan usually short e; cf. wēst- forms'),
 'wíd': ('wīd', 'long', 'BT wīd'),
 'wíf': ('wīf', 'long', 'BT wīf'),
 'wínd': ('wind', 'short-HL', 'short i + nd; HL of i + nd irregular'),
 'wítga': ('witga “prophet”', 'short', 'witega, short i'),
 'wóp': ('wōp “weeping”', 'long', 'BT wōp'),
 'wórd': ('word', 'short-HL', 'short o + rd; HL environment'),
 'wýrhtu': ('wyrhta “workers”', 'short', 'wyrhta, short y'),
}.items()}


def main():
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    folio = "1r"
    rows = collections.defaultdict(list)
    for i in range(START, END):
        line = lines[i]
        m = re.search(r"\[folio\s+(\d+[rv])\]", line)
        if m:
            folio = m.group(1)
        for tok in re.findall(r"[^\s,.;:·‘’()\[\]0-9&=ˉ]+", line):
            if "\u0301" in unicodedata.normalize("NFD", tok):
                rows[nfc(tok)].append((i + 1, folio, line.strip()))

    stats = collections.Counter()
    tokstats = collections.Counter()
    unclassified = []
    with OUT.open("w", encoding="utf-8") as out:
        out.write("form\ttokens\tfolios\tfile_lines\tlemma\tquantity_class\tgrounds\tsample_context\n")
        for tok in sorted(rows, key=lambda t: unicodedata.normalize("NFD", t.lower())):
            occ = rows[tok]
            if tok in LATIN:
                stats["latin-excluded"] += 1
                tokstats["latin-excluded"] += len(occ)
                continue
            if tok not in CLASSIFICATION:
                unclassified.append((tok, occ[0]))
                continue
            lemma, qc, grounds = CLASSIFICATION[tok]
            stats[qc] += 1
            tokstats[qc] += len(occ)
            folios = " ".join(dict.fromkeys(f for _, f, _ in occ))
            fls = " ".join(str(n) for n, _, _ in occ)
            ctx = occ[0][2][:70].replace("\t", " ")
            out.write(f"{tok}\t{len(occ)}\t{folios}\t{fls}\t{lemma}\t{qc}\t{grounds}\t{ctx}\n")
    print("type stats:", dict(stats))
    print("token stats:", dict(tokstats))
    if unclassified:
        print("UNCLASSIFIED:")
        for tok, (ln, fol, ctx) in unclassified:
            print(f"  {tok}  line {ln}  fol. {fol}  {ctx[:60]}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
