#! /usr/bin/env python3

import re
import sys

print(sys.argv[-1])
text = open(sys.argv[-1], encoding="utf8").read()
list_text = list(text)

mathsections = [r.span() for r in re.finditer(r"\$(.\*)\$", text)]

for section in mathsections:
    for i in range(*section):
        if list_text[i] in ["*", "|"] and list_text[i-1] != "\\":
            list_text[i] = "\\"+list_text[i]

open(sys.argv[-1], "w").write("".join(list_text))

