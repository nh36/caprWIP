"""Separate Jones's coda and nuclear hypotheses before surface serialization."""

import candidates
import palatal


def rewrite(before, after, scope=""):
    clauses = []
    for acute in (True, False):
        src = ("é", *before[1:]) if acute else before
        accents = {"e": "é", "ē": "ḗ"}
        dst = (accents.get(after[0], after[0]), *after[1:]) if acute else after
        left = "" if acute else "HiHeadContext "
        context = f" || {left}_{scope}" if left or scope else ""
        clauses.append(f"[{candidates.sequence(src)} -> {candidates.sequence(dst)}{context}]")
    return " .o. ".join(clauses)


CODA = "[OEAnyConsonant | .#.]"
PROBES = {
    "JoHiOff": rewrite(("e", "i"), ("ei",)),
    "JoHiOnset": rewrite(("e", "i"), ("e", "j"), " EnglishStarVocalic"),
    "JoFricOff": rewrite(("e", "ʝ"), ("ei",), " " + CODA),
    "JoApproxOff": rewrite(("e", "j"), ("ei",), " " + CODA),
    "JoFricAssim": rewrite(("e", "ʝ"), ("ē",), " " + CODA),
    "JoFricBreak": rewrite(("e", "ʝ"), ("ei", "ʝ"), " " + CODA),
    "JoMerge": "[{*ei} -> {*ē} || _ " + candidates.right_context("attested_loss") + "]",
}
RULES = candidates.RULES | palatal.RULES | PROBES

ANCHOR = "OEJLossAfterHeavy"
ARMS = {
    "J-offglide": ((ANCHOR, "JoHiOff"),),
    "J-onset": ((ANCHOR, "JoHiOnset"),),
    "J-fricative-direct": ((ANCHOR, "JoFricAssim"),),
    "J-fricative-serial": ((ANCHOR, "JoFricOff"), (ANCHOR, "JoMerge")),
    "J-approximant-serial": ((ANCHOR, "JoApproxOff"), (ANCHOR, "JoMerge")),
    "J-breaking": ((ANCHOR, "JoFricBreak"),),
    "Dahl-final": ((ANCHOR, "DaFinalJ"),),
}


def definitions():
    return (candidates.definitions() + palatal.definitions()
            + "".join(f"define {name} {body};\n" for name, body in PROBES.items()))
