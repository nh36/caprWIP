"""Supplementary controls for Dahl's final consonant hypothesis."""

# Use the frozen vowel classes; quantities and atomic diphthongs are
# independent of the following consonant.
RULES = {
    "DaFinalJ": """[
        {*j} -> 0 || [EnglishStarLongVowel | EnglishStarDiphthong] _ .#.
    ]""",
}

POSITIONS = {
    "before-umlaut": "OEIUmlaut",
    "after-umlaut": "OEWLossBeforeI",
    "before-hvd": "OEHighVowelApocope",
    "after-hvd": "OEMedialSyncope",
    "before-merger": "OEPalatalFricativeMerger",
    "after-merger": "OECjCleanup",
}


def definitions():
    return "".join(f"define {name} {body};\n" for name, body in RULES.items())
