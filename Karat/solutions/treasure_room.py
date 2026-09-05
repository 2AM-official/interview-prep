"""Treasure Room reference solutions."""

from __future__ import annotations

from collections import defaultdict, deque


def filter_treasure_leading_rooms(
    treasure_rooms: list[str], instructions: list[list[str]]
) -> list[str]:
    """Return rooms with two incoming rooms that immediately lead to treasure.

    Self-loops do not count toward the two *other* incoming rooms. Sort output.
    """
    incoming: dict[str, set[str]] = defaultdict(set)
    for source, destination in instructions:
        if source != destination:
            incoming[destination].add(source)

    return sorted(
        room for room in set(treasure_rooms) if len(incoming[room]) >= 2
    )


def minimum_instructions(instructions: list[int], money: int) -> int | None:
    """Find the fewest moves from room zero to the final room.

    At each room, either follow its positive jump for free or spend one dollar
    to change that jump by exactly -1 or +1. Jumps must remain positive and
    land within the room list. Spending less than the budget is allowed.
    """
    if not instructions or money < 0:
        return None

    final_room = len(instructions) - 1
    if final_room == 0:
        return 0

    budget = min(money, final_room)
    queue = deque([(0, 0, 0)])
    visited = {(0, 0)}

    while queue:
        room, spent, moves = queue.popleft()
        jump = instructions[room]
        choices = [(jump, 0), (jump - 1, 1), (jump + 1, 1)]

        for distance, cost in choices:
            new_spent = spent + cost
            destination = room + distance
            if (
                distance <= 0
                or destination > final_room
                or new_spent > budget
            ):
                continue
            if destination == final_room:
                return moves + 1

            state = (destination, new_spent)
            if state not in visited:
                visited.add(state)
                queue.append((destination, new_spent, moves + 1))

    return None
