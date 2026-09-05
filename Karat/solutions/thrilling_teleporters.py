"""Reference solutions for the Thrilling Teleporters practice questions."""

from __future__ import annotations

from collections import deque


def _parse_teleporters(teleporters: list[str]) -> dict[int, int]:
    result: dict[int, int] = {}
    for teleporter in teleporters:
        source, destination = teleporter.split(",")
        result[int(source)] = int(destination)
    return result


def _destinations(
    teleporter_map: dict[int, int],
    die_sides: int,
    start: int,
    last_square: int,
) -> list[int]:
    destinations: list[int] = []
    seen: set[int] = set()
    for roll in range(1, die_sides + 1):
        landed = min(start + roll, last_square)
        if landed < last_square:
            landed = min(teleporter_map.get(landed, landed), last_square)
        if landed not in seen:
            seen.add(landed)
            destinations.append(landed)
    return destinations


def teleporter_destinations(
    teleporters: list[str],
    die_sides: int,
    start: int,
    last_square: int,
) -> list[int]:
    """Return unique destinations possible after one die roll.

    Teleporters use ``"source,destination"`` format. Stop at ``last_square``
    when a roll reaches or passes it, and follow at most one teleporter per
    turn. Preserve first occurrence in die-roll order.

    Complexity variable: ``b`` board size.
    """
    if die_sides <= 0:
        return []
    return _destinations(
        _parse_teleporters(teleporters), die_sides, start, last_square
    )


def is_finishable(
    teleporters: list[str],
    die_sides: int,
    start: int,
    last_square: int,
) -> bool:
    """Return whether some sequence of die rolls reaches ``last_square``.

    Reaching or passing the last square stops there. Follow at most one
    teleporter after each roll.
    """
    if start >= last_square:
        return True
    if die_sides <= 0:
        return False

    teleporter_map = _parse_teleporters(teleporters)
    queue = deque([start])
    visited = {start}

    while queue:
        square = queue.popleft()
        for destination in _destinations(
            teleporter_map, die_sides, square, last_square
        ):
            if destination >= last_square:
                return True
            if destination not in visited:
                visited.add(destination)
                queue.append(destination)
    return False
