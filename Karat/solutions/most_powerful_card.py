"""Most Powerful Card reference solution."""

from __future__ import annotations

from collections import defaultdict


def most_powerful_card(matchups: list[list[str]]) -> str | None:
    """Return the card that transitively beats the most distinct cards.

    A matchup is ``[winner, loser]``. Break ties lexicographically and handle
    cycles without counting a card as beating itself.
    """
    if not matchups:
        return None

    cards: set[str] = set()
    defeated_by: dict[str, set[str]] = defaultdict(set)
    for winner, loser in matchups:
        cards.add(winner)
        cards.add(loser)
        defeated_by[winner].add(loser)

    best_card: str | None = None
    best_count = -1

    for card in sorted(cards):
        reachable: set[str] = set()
        stack = list(defeated_by[card])

        while stack:
            defeated = stack.pop()
            if defeated == card or defeated in reachable:
                continue
            reachable.add(defeated)
            stack.extend(defeated_by[defeated])

        if len(reachable) > best_count:
            best_card = card
            best_count = len(reachable)

    return best_card
