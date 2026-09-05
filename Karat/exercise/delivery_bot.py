"""Complete reference solutions for the Delivery Bot exercise family."""

from __future__ import annotations

from collections import defaultdict


def delivery_destinations(paths: list[list[str]]) -> dict[str, list[str]]:
    """Map each DAG origin to all terminal destinations it can reach.

    Origins have no incoming edge; terminal locations have no outgoing edge.
    Return destinations sorted lexicographically.
    """
    graph: dict[str, set[str]] = defaultdict(set)
    nodes: set[str] = set()
    has_incoming: set[str] = set()
    for origin, destination in paths:
        graph[origin].add(destination)
        nodes.update((origin, destination))
        has_incoming.add(destination)

    cache: dict[str, set[str]] = {}

    def terminals(node: str) -> set[str]:
        if node in cache:
            return cache[node]
        if not graph[node]:
            cache[node] = {node}
            return cache[node]
        reachable: set[str] = set()
        for neighbor in graph[node]:
            reachable.update(terminals(neighbor))
        cache[node] = reachable
        return reachable

    origins = sorted(nodes - has_incoming)
    return {origin: sorted(terminals(origin)) for origin in origins}


def buildable_robots(
    all_parts: list[str], required_parts: list[list[object]]
) -> list[str]:
    """Return robots whose required-part set is available.

    Each requirement is ``[robot_name, list_of_parts]``. Parts are reusable
    across robots and quantities are not modeled. Preserve robot input order.
    """
    available = set(all_parts)
    result: list[str] = []
    for robot_name, parts in required_parts:
        if set(parts).issubset(available):
            result.append(str(robot_name))
    return result
