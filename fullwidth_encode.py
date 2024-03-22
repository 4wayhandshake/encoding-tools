#!/bin/env python3

import sys, codecs

s = sys.argv[1]

# unescape special characters
escapes = {'\\n': '\n', '\\r': '\r', '\\t': '\t'}
for escape_seq, char in escapes.items():
    s = s.replace(escape_seq, char)

# UTF16-encode the string and store as hex
hex_encoded = codecs.encode(s.encode('utf-16le'), 'hex')

# Bytes are in wrong endianness; swap them
swapped_chunks = [chunk[2:] + chunk[:2] for chunk in [hex_encoded[i:i+4] for i in range(0, len(hex_encoded), 4)]]

# Add 0xFEE0 to each character to convert to fullwidth. Re-prefix as \\u
# Fullwidth only exists for characters 0x21 through 0x7e.
unicode_chunks = [hex(int(chunk,16) + 0xfee0).replace('0x','\\u') if (int(chunk,16) >= 0x21 and int(chunk,16) <= 0x7e) else '\\u'+hex(int(chunk,16))[2:].zfill(4) for chunk in swapped_chunks]

# Parse each character as unicode, using eval
#unicode_str = ''.join([eval('"'+chunk+'"') for chunk in unicode_chunks])
unicode_str = ''
for chunk in unicode_chunks:
    try:
        unicode_str += eval('"'+chunk+'"') 
    except SyntaxError as e:
        print(f'Failed to decode chunk: {chunk}')
        unicode_str += str(chunk)

print(unicode_str.rstrip())
