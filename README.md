# encoding-tools
A small collection of tools I like to use for re-encoding text.



## Installation

This only applies to **url_encode** and **fullwidth_encode**

1. Clone this repo:
   ```bash
   https://github.com/4wayhandshake/encoding-tools.git
   cd encoding-tools
   ```

2. Copy `url_encode.py` and `fullwidth_encode.py` into `~/.local/share`
   ```bash
   cp *_encode.py ~/.local/share/
   ```

3. Copy `url_encode` and `fullwidth_encode` into your path somewhere
   ```bash
   cp *_encode ~/.local/bin/
   ```



## url_encode

### Usage:

Provide the text as an **argument**:
```bash
url_encode 'hello newline \n'
# hello+newline+%0A
```

Alternatively, **pipe** it in:
```bash
echo -n 'hello newline \n' | url_encode
# hello+newline+%0A
```

Pipe it twice to **double-encode**:

```bash
echo -n 'hello newline \n' | url_encode | url_encode
# hello%2Bnewline%2B%250A%0A
```



## fullwidth_encode

Please see [this wikipedia page](https://en.wikipedia.org/wiki/Halfwidth_and_Fullwidth_Forms_(Unicode_block)) for a description of fullwidth characters.

It's used for turning this strings like `4wayhandshake` into `４ｗａｙｈａｎｄｓｈａｋｅ`
### Usage:

Provide the text as an argument:

```bash
fullwidth_encode 'fullwidth!'
# ｆｕｌｌｗｉｄｔｈ！
```

Alternatively, **pipe** it in:

```bash
echo 'fullwidth!' | fullwidth_encode
# ｆｕｌｌｗｉｄｔｈ！
```



## Hex using Bash

Simple enough, but here's an example:

```bash
# encoding as hex
echo -n 'this is utf-8 text' | xxd -p
# decoding it
echo -n '74686973206973207574662d382074657874' | xxd -r -p
```

> Remember to use `-n` with `echo` to suppress the line ending character. 



## Unicode Encoding

To convert ascii text into UTF-8 unicode:

```bash
echo -n 'Special ch@r5 :)' | xxd -p | sed 's/../\\u&/g'
# \u53\u70\u65\u63\u69\u61\u6c\u20\u63\u68\u40\u72\u35\u20\u3a\u29
```

It's sometimes more useful to have UTF-16 unicode:

```bash
echo -n "Special ch@r5 :)" | iconv -t UTF-16LE | xxd -p -c 2 | sed 's/\(..\)\(..\)/\\u\2\1/g' | tr -d '\n'
#\u0053\u0070\u0065\u0063\u0069\u0061\u006c\u0020\u0063\u0068\u0040\u0072\u0035\u0020\u003a\u0029
```

