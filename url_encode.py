#!/bin/env python3
import sys, urllib.parse as ul
s = sys.argv[1]
escapes = {'\\n': '\n', '\\r': '\r', '\\t': '\t'}
for escape_seq, char in escapes.items():
    s = s.replace(escape_seq, char)
print(ul.quote_plus(s))
