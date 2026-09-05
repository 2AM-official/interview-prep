"""Tomb Raider reference solution."""

from __future__ import annotations

from collections import defaultdict


def minimum_sphere_distance(room: str) -> int:
    """Sum each uppercase sphere's distance to its nearest lowercase hole.

    There is at most one sphere of each color and at least one matching hole.
    Empty positions are periods; carrying distance is absolute index distance.
    """
    holes: dict[str, list[int]] = defaultdict(list)
    spheres: list[tuple[str, int]] = []

    for index, item in enumerate(room):
        if item.islower():
            holes[item].append(index)
        elif item.isupper():
            spheres.append((item.lower(), index))

    return sum(
        min(abs(sphere_index - hole_index) for hole_index in holes[color])
        for color, sphere_index in spheres
    )
