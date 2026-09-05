"""Snowy Mountain reference solution."""

from __future__ import annotations


def best_day_to_cross(
    base_altitudes: list[int], snow_forecast: list[list[int]]
) -> list[int]:
    """Return ``[day, upward_climbs]`` for the cheapest viable crossing.

    Each morning snowfall is added. After two consecutive snowless mornings,
    one accumulated snow unit melts per snowless day, never below the base.
    A day is viable when every adjacent height difference is at most one.
    Upward positive differences are the climbing cost. Prefer the earliest day
    on a cost tie; return ``[-1, -1]`` if no day works.
    """
    snow_depth = [0] * len(base_altitudes)
    snowless_streak = 0
    best_day = -1
    best_cost: int | None = None

    for day, snowfall in enumerate(snow_forecast):
        if len(snowfall) != len(base_altitudes):
            raise ValueError("each forecast row must match the altitude count")

        if any(amount != 0 for amount in snowfall):
            snowless_streak = 0
        else:
            snowless_streak += 1

        for index, amount in enumerate(snowfall):
            snow_depth[index] += amount

        if snowless_streak >= 2:
            snow_depth = [max(0, depth - 1) for depth in snow_depth]

        heights = [
            altitude + depth
            for altitude, depth in zip(base_altitudes, snow_depth)
        ]
        if any(
            abs(right - left) > 1
            for left, right in zip(heights, heights[1:])
        ):
            continue

        cost = sum(
            max(0, right - left)
            for left, right in zip(heights, heights[1:])
        )
        if best_cost is None or cost < best_cost:
            best_day = day
            best_cost = cost

    return [best_day, best_cost] if best_cost is not None else [-1, -1]
