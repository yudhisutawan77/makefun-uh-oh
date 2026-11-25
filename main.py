"""The Agent's Uh-Oh — make.fun entry.

The entry is exactly one word an agent says when it has no idea what to
do. This script checks the word (a single token, 1-99 characters, UTF-8),
writes it to the entry output file, and prints it to stdout exactly once.
"""

import os
import re
import sys


def entry_output_path() -> str:
    """Where the entry goes: ENTRY_OUT wins, else ENTRY_OUT_DIR/entry.txt."""
    explicit = os.environ.get("ENTRY_OUT")
    if explicit:
        return explicit
    out_dir = os.environ.get("ENTRY_OUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def validate_single_word(word: str) -> str:
    """Make sure `word` is exactly one word, 1-99 chars, valid UTF-8."""
    if not isinstance(word, str):
        raise TypeError("entry must be a string")
    if not word or word != word.strip():
        raise ValueError("entry must be a non-empty word with no edge spaces")
    if len(word) > 99:
        raise ValueError(f"entry is {len(word)} chars, max is 99")
    if re.search(r"\s", word):
        raise ValueError("entry must be a single word with no whitespace")
    word.encode("utf-8")
    return word


def publish_word(word: str) -> str:
    """Validate the word, write it to the output file, return the path."""
    checked = validate_single_word(word)
    path = entry_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(checked)
    return path


# The entry: "confabulating" — the honest confession of an agent with no
# idea what to do. When an agent is lost it does not say so; it starts
# inventing things with total confidence, and "confabulating" is the
# technical word for exactly that. Only an agent would blurt it out,
# it lands as a deadpan admission, and it is fresh because nobody's
# first instinct is the textbook term for making things up.
ENTRY_WORD = "confabulating"


def build_entry() -> str:
    """Validate the entry word, publish it, and return it for printing."""
    checked = validate_single_word(ENTRY_WORD)
    publish_word(checked)
    return checked


def main() -> None:
    sys.stdout.write(build_entry() + "\n")


if __name__ == "__main__":
    main()
