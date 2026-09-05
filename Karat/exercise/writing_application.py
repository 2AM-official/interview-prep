"""Reference solutions for the Writing Application practice questions."""

from __future__ import annotations


def wrap_lines(words: list[str], max_width: int) -> list[str]:
    """Greedily wrap words using hyphens as visible spaces.

    Put as many words as possible on each line without exceeding
    ``max_width``. Input words individually fit within the width.

    Complexity variable: total number of characters.
    """
    wrapped: list[str] = []
    current: list[str] = []
    current_width = 0

    for word in words:
        added_width = len(word) + (1 if current else 0)
        if current and current_width + added_width > max_width:
            wrapped.append("-".join(current))
            current = [word]
            current_width = len(word)
        else:
            current.append(word)
            current_width += added_width

    if current:
        wrapped.append("-".join(current))
    return wrapped


def reflow_and_justify(lines: list[str], max_width: int) -> list[str]:
    """Reflow words and fully justify lines using hyphens.

    Greedily fit words with at least one hyphen per gap. Multiword lines are
    padded to exactly ``max_width`` with extras assigned to earlier gaps.
    Single-word lines are not padded.
    """
    words = [word for line in lines for word in line.split()]
    wrapped = wrap_lines(words, max_width)
    justified: list[str] = []

    for line in wrapped:
        line_words = line.split("-")
        if len(line_words) == 1:
            justified.append(line)
            continue

        letters = sum(map(len, line_words))
        total_hyphens = max_width - letters
        gaps = len(line_words) - 1
        base, extra = divmod(total_hyphens, gaps)

        pieces = [line_words[0]]
        for index, word in enumerate(line_words[1:]):
            pieces.append("-" * (base + (index < extra)))
            pieces.append(word)
        justified.append("".join(pieces))

    return justified
