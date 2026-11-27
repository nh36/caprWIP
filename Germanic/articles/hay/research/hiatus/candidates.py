"""Research-only definitions and predeclared placement comparisons."""

CLASSES = {
    "stop": "p b t d k g",
    "dental_stop": "t d",
    "dental_obstruent": "t d θ ð",
    "coronal": "t d θ ð s z n l r",
    "attested_loss": "d θ ð n",
}


def segment(symbol):
    return "{*" + symbol + "}"


def sequence(symbols):
    return " ".join(map(segment, symbols))


def right_context(scope):
    if scope == "all":
        return ""
    if scope == "final":
        return ".#."
    if scope == "consonant":
        return "OEAnyConsonant"
    return "[" + " | ".join(map(segment, CLASSES[scope].split())) + "]"


def rewrite(before, after, scope="all", stress="foot"):
    clauses = []
    for acute in (True, False) if stress == "foot" else (True,):
        src, dst = before, after
        if acute:
            accents = {"e": "é", "ē": "ḗ"}
            src = accents[src[0]] + src[1:]
            dst = accents[dst[0]] + dst[1:]
        left = "" if acute else "HiHeadContext "
        right = right_context(scope)
        context = f" || {left}_{' ' + right if right else ''}" if left or right else ""
        clauses.append(f"[{sequence(src)} -> {sequence(dst)}{context}]")
    return " .o. ".join(clauses)


PREFIX = """define HiHeadContext .#. [{*ᵘ}|{*ᶜ}|0] [
    OEAnyConsonant* |
    {*ᶠ} OEAnyConsonant* EnglishStarVocalic OEAnyConsonant+
];
"""

RULES = {}


def rule(name, before, after, scope="all", stress="foot"):
    RULES[name] = rewrite(before, after, scope, stress)
    return name


CONTRACT = rule("HiContract", "ei", "ē")
ACUTE = rule("HiAcute", "ei", "ē", stress="acute")
GLIDE = rule("HiGlide", "ei", "ej")
FINAL_GLIDE = rule("HiEdgeGlide", "ei", "ej", "final")
C_GLIDE = rule("HiCGlide", "ei", "ej", "consonant")
LOSS = rule("HiLoss", "ej", "ē", "attested_loss")
LENGTH_FIRST = rule("HiPreLength", "ei", "ēi")
LONG_GLIDE = rule("HiLongGlide", "ēi", "ēj")
LENGTH_LAST = rule("HiPostLength", "ej", "ēj")

EARLY = "SC047FinalIi"  # Use OELatePalatalDiphthong in canonical.
ORDERINGS = {
    "early": EARLY,
    "pre-hvd": "OEHighVowelApocope",
    "post-hvd": "OEMedialSyncope",
    "pre-lowering": "OEMedUnstressedILowering1",
    "post-lowering": "OEMedUnstressedULowering",
    "late": "OEContraction",
}

# Each step is placed before a frozen component; steps sharing an anchor
# run in tuple order. These are placements to test, not historical dates.
ARMS = {
    "H0": (),
    "H1-acute": ((EARLY, ACUTE),),
    "H2-early": ((EARLY, GLIDE),),
    "H2-late": (("OEContraction", GLIDE),),
    "H4-pre-loss": ((EARLY, GLIDE), ("OEJLossAfterHeavy", LOSS)),
    "H4-post-loss": ((EARLY, GLIDE), ("OEFinalGeminateSimplification", LOSS)),
    "H4-post-merger": ((EARLY, GLIDE), ("OECjCleanup", LOSS)),
    "H5-length-first": ((EARLY, LENGTH_FIRST), ("OEFinalGeminateSimplification", LONG_GLIDE)),
    "H5-glide-first": ((EARLY, GLIDE), ("OEFinalGeminateSimplification", LENGTH_LAST)),
    "H6-final-only": ((EARLY, FINAL_GLIDE),),
    "H6-nonfinal-only": ((EARLY, C_GLIDE),),
}
for position, anchor in ORDERINGS.items():
    ARMS[f"H1-{position}"] = ((anchor, CONTRACT),)
for scope in ("stop", "dental_stop", "dental_obstruent", "coronal", "consonant"):
    component = rule("Hi" + scope.title().replace("_", ""), "ei", "ē", scope)
    ARMS[f"H3-{scope}-retain"] = ((EARLY, component),)
    ARMS[f"H3-{scope}-glide"] = ((EARLY, component), (EARLY, FINAL_GLIDE))


def placements(arm, model):
    return tuple(("OELatePalatalDiphthong" if anchor == EARLY and model == "canonical"
                  else anchor, component) for anchor, component in ARMS[arm])


def definitions():
    return PREFIX + "".join(f"define {name} {body};\n" for name, body in RULES.items())
