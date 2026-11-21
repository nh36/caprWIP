"""Run only the additional, unscored SC047 lexical-cell probes in Docker."""

import json
import os
from pathlib import Path
import tempfile
from unittest.mock import patch

import run_parallel as parallel

CELLS = {
    "hedge.f.nom.sg": "xágjō",
    "hedge.f.acc.sg": "xágjǭ",
    "rest.nom.sg": "rástō",
    "rest.gen.sg.control": "rástōz",
    "rest.dat.sg": "rástōi",
    "rest.acc.sg": "rástǭ",
    "hay.dat.sg": "xáwjai",
    "hue.dat.sg": "xíwjai",
    "net.direct.control": "nátją",
}
# Dahl's conditional ja-stem: these literal strings start after the
# input acceptor, where accepted forms are normally encoded.
ENCODED = {
    "hyse.nom.sg.component": "*x*ú*s*j*a*z",
    "hyse.dat.sg.component": "*x*ú*s*j*ai",
    "hyse.acc.sg.component_control": "*x*ú*s*j*ą",
    "net.direct.component_control": "*n*á*t*j*ą",
}
CHECKPOINTS = {
    "EnglishProtoInput", "PNWGmcFinalLongORaising", "EAFFinalZDeletion",
    "PWGmcFinalBareALoss", "PWGmcJGemination", "OEHeavySyllableNasalApocope",
    "FON", "FNU", "OEHighVowelApocope", parallel.LAST,
}


def run():
    import anglo_frisian_experiments as compiler
    from capr_runtime import layout
    from oe_pipeline import CITATION_CONTEXT, stages
    from sound_change_order_sensitivity import batch_apply_down

    source = layout().germanic_fst
    variants, additions, _ = parallel.recipe()
    names = [stage.foma_identifier for stage in stages()]
    assert names[0] == "EnglishProtoInput"
    orders = {"identity": names, **{
        key: parallel.order_for(names, variant) for key, variant in variants.items()
    }}
    inputs = {
        "full": {key: CITATION_CONTEXT.encode(form) for key, form in CELLS.items()},
        "component": ENCODED,
    }
    definitions = list(additions.values())
    queries = {}
    for arm, order in orders.items():
        for mode, forms in inputs.items():
            start = int(mode == "component")
            for stop in range(start, len(order)):
                stage = order[stop]
                if stage not in CHECKPOINTS:
                    continue
                symbol = f"CLX{len(queries)}"
                domain = compiler.foma_domain(forms.values())
                definitions.append(f"define {symbol} {domain} .o. "
                                   + " .o. ".join(order[start:stop + 1]) + ";")
                queries[arm, mode, stage] = symbol
    with tempfile.TemporaryDirectory(prefix="capr-sc047-cells-") as tmp:
        work = Path(tmp)
        image = compiler.prepare_definition_image(source, work)
        if image is None:
            raise RuntimeError("Source does not support isolated definition images")
        with patch.dict(os.environ, {"CAPR_FOMA_DEFINITION_IMAGE": str(image)}):
            bins = compiler.compile_isolated(source, {
                "definitions": "\n".join(definitions), "replace": {},
                "insert_rule": None, "insert_after": None,
                "component_checks": [{"component": symbol} for symbol in queries.values()],
            }, [], work, components_only=True)
        traces = {
            ":".join(key): dict(zip(inputs[key[1]], batch_apply_down(
                bins[f"component:{symbol}"], list(inputs[key[1]].values()))))
            for key, symbol in queries.items()
        }
    for arm in orders:
        for stage in CHECKPOINTS - {"EnglishProtoInput"}:
            key = f"{arm}:full:{stage}"
            if key in traces:
                assert traces[key]["net.direct.control"] == \
                    traces[f"{arm}:component:{stage}"]["net.direct.component_control"]
    return {"sha256": {p.name: parallel.digest(p) for p in (
                source, parallel.CONTROL, Path(parallel.__file__), Path(__file__))},
            "inputs": inputs, "traces": traces}


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))
