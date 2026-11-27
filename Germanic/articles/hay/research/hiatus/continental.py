"""Private segmental diagnostics, not complete continental cascades."""

RULES = {
    "DaCopyLabial": "[{*j} -> {*w} || [{*au}|{*iu}] _ EnglishStarVocalic]",
    "DaGeminate": "[{*w} -> {*w}{*w} || EnglishStarShortVowel _ {*j}]",
    "DaLowLoss": "[{*ą} -> 0 || _ .#.]",
    "DaDiffer": "[{*au} -> {*ǣo}, {*iu} -> {*īo}]",
    "DaUnfuse": """[
        [{*au}{*j} -> {*a}{*w}{*i} || _ .#.]
        .o. [{*iu}{*j} -> {*i}{*w}{*i} || _ .#.]
    ]""",
    "DaLateDirect": "DaLowLoss .o. DaUnfuse",
    "DaEarlyDirect": "DaDiffer .o. DaLowLoss .o. DaUnfuse",
    "DaGemDirect": "DaGeminate .o. DaLowLoss",
}


def definitions():
    return "".join(f"define {name} {body};\n" for name, body in RULES.items())
