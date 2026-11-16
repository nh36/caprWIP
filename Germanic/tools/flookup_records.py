"""Raw single-input flookup records, before evaluator-specific output policy."""


def parse_records(stdout, form):
    outputs = []
    seen = False
    for line in stdout.splitlines():
        if not line:
            continue
        if line.count("\t") != 1:
            raise ValueError("malformed flookup record")
        head, output = line.split("\t")
        if head != form:
            raise ValueError("wrong-input flookup record")
        seen = True
        if output != "+?" and output not in outputs:
            outputs.append(output)
    if not seen:
        raise ValueError("missing flookup record")
    return outputs
