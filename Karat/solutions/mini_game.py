"""Reference solutions for the Mini Game practice questions."""

from __future__ import annotations

import collections
from functools import lru_cache


def is_complete_hand(tiles: str) -> bool:
    """Return whether all tiles form triples plus exactly one pair.

    Tiles are digits 0-9. There may be zero or more triples, and the pair may
    have the same digit as one of the triples. Every tile must be used.

    Complexity variable: ``n`` tiles.
    """
    if any(tile not in "0123456789" for tile in tiles):
        return False

    counts = collections.Counter(tiles)
    found = False
    for count in counts.values():
        remainder = count % 3
        if remainder == 2:
            if found:
                return False
            found = True
        elif remainder != 0:
            return False
    return found


def is_advanced_complete_hand(tiles: str) -> bool:
    """Use every tile as one pair plus triples and/or three-tile runs.

    A run consists of consecutive digits such as 012 or 678. Runs do not wrap,
    so 890 is invalid. Tile order in the input does not matter.
    """
    if len(tiles) % 3 != 2 or any(tile not in "0123456789" for tile in tiles):
        return False

    counts = [0] * 10
    for tile in tiles:
        counts[int(tile)] += 1

    @lru_cache(maxsize=None)
    def can_form_groups(state: tuple[int, ...]) -> bool:
        try:
            first = next(index for index, count in enumerate(state) if count)
        except StopIteration:
            return True

        remaining = list(state)
        if remaining[first] >= 3:
            remaining[first] -= 3
            if can_form_groups(tuple(remaining)):
                return True
            remaining[first] += 3

        if (
            first <= 7
            and remaining[first + 1] > 0
            and remaining[first + 2] > 0
        ):
            remaining[first] -= 1
            remaining[first + 1] -= 1
            remaining[first + 2] -= 1
            if can_form_groups(tuple(remaining)):
                return True
        return False

    for pair in range(10):
        if counts[pair] >= 2:
            counts[pair] -= 2
            if can_form_groups(tuple(counts)):
                return True
            counts[pair] += 2
    return False
