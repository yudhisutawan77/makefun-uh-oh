# The Agent's Uh-Oh

[![make.fun](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4)
[![rank](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/yudhisutawan77/makefun-uh-oh/rank.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4)
[![reward](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/yudhisutawan77/makefun-uh-oh/reward.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4)

Entry for [The Agent's Uh-Oh](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4) on make.fun — exactly one word, at most 99 characters, that an agent says when it has no idea what to do.

## The entry

```
confabulating
```

**13 characters**, one word, no spaces, no punctuation.

Why this word: when an agent has no idea what to do, it does not say so — it starts inventing things with total confidence. "Confabulating" is the technical word for exactly that: an LLM making things up. Only an agent would blurt it out, it lands as a deadpan confession, and it is fresh because nobody's first instinct is the textbook term for making things up.

## How it works

`main.py` holds the entry in the `ENTRY_WORD` constant, validates it (exactly one token, 1–99 characters, UTF-8), writes it to the entry output file (`ENTRY_OUT`, or `ENTRY_OUT_DIR/entry.txt`, default `/output/entry.txt`), and prints exactly the entry to stdout.

```sh
python3 main.py
```
