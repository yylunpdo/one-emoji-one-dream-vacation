#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji to /output/entry.txt: the single most evocative
emoji for a dream vacation. Pure Python standard library, no dependencies.
"""

import os

# U+1F305 SUNRISE — the sun rising (or setting) over the sea: the golden-hour
# moment every dream vacation is really about. One codepoint, no text, no
# variation selector, no ZWJ sequence.
EMOJI = "\U0001F305"


def main() -> None:
    assert len(EMOJI) == 1, "entry must be exactly one emoji character"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)
    # Self-check: what was written must read back as exactly one character.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == EMOJI and len(written) == 1, "entry.txt is not one emoji"


if __name__ == "__main__":
    main()
