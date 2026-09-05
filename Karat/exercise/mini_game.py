"""Mini Game practice questions.

Implement one part at a time, then run its focused tests.
"""

from __future__ import annotations

import collections


def is_complete_hand(tiles: str) -> bool:
    """Return whether all tiles form triples plus exactly one pair.

    Tiles are digits 0-9. There may be zero or more triples, and the pair may
    have the same digit as one of the triples. Every tile must be used.

    Complexity variable: ``n`` tiles.
    """
    counts = collections.Counter(tiles)
    found = False

    for count in counts.values():
        remain = count % 3

        if remain == 2:
            if found:
                return False
            found = True
        elif remain != 0:
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

    memo = {}

    def can_form_groups(state):
        if state in memo:
            return memo[state]

        remaining = list(state)

        first = None
        for digit in range(10):
            if remaining[digit] > 0:
                first = digit
                break

        if first is None:
            return True

        # Try using the smallest remaining digit in a triple.
        if remaining[first] >= 3:
            remaining[first] -= 3

            if can_form_groups(tuple(remaining)):
                memo[state] = True
                return True

            remaining[first] += 3

        # Otherwise, try a consecutive run beginning with that digit.
        if (
            first <= 7
            and remaining[first + 1] > 0
            and remaining[first + 2] > 0
        ):
            remaining[first] -= 1
            remaining[first + 1] -= 1
            remaining[first + 2] -= 1

            if can_form_groups(tuple(remaining)):
                memo[state] = True
                return True

        memo[state] = False
        return False

    # Try every digit that could serve as the hand's one pair.
    for pair in range(10):
        if counts[pair] >= 2:
            counts[pair] -= 2

            if can_form_groups(tuple(counts)):
                counts[pair] += 2
                return True

            counts[pair] += 2

    return False
