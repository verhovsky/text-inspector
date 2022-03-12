#!/usr/bin/env python3

import requests
import re
import itertools

OUTFILE = "codepoint-names.js"

starts_with_number = re.compile("[0-9A-F]+")


def pairwise(iterable):
    "s -> (s0, s1), (s1, s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


with open(OUTFILE, "w") as f:
    f.write("const NAMES = {\n")
    result = requests.get("https://www.unicode.org/Public/UCD/latest/ucd/NamesList.txt")
    lines = iter(result.text.splitlines())
    for line, next_line in pairwise(lines):
        if re.match(starts_with_number, line):
            codepoint, name = line.split("\t")
            if name == "<control>" and next_line.lstrip().startswith("= "):
                name = next_line.lstrip(" \t=")
            f.write(f"0x{codepoint}:{name!r},\n")

    f.write("};\n")
