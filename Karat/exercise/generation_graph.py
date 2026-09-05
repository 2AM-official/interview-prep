"""Complete reference solutions for the Generation Graph exercise family."""

from __future__ import annotations

from collections import defaultdict, deque


def find_nodes_with_zero_or_one_parent(
    parent_child_pairs: list[tuple[int, int]],
) -> tuple[list[int], list[int]]:
    """Return nodes with zero parents and exactly one distinct parent.

    Sort both output lists numerically and treat duplicate edges as one edge.
    """
    parents: dict[int, set[int]] = defaultdict(set)
    nodes: set[int] = set()
    for parent, child in parent_child_pairs:
        nodes.update((parent, child))
        parents[child].add(parent)

    zero_parents = sorted(node for node in nodes if not parents[node])
    one_parent = sorted(node for node in nodes if len(parents[node]) == 1)
    return zero_parents, one_parent


def has_common_ancestor(
    parent_child_pairs: list[tuple[int, int]], first: int, second: int
) -> bool:
    """Return whether two nodes have any transitive ancestor in common.

    A node is not considered its own ancestor.
    """
    parents: dict[int, set[int]] = defaultdict(set)
    for parent, child in set(parent_child_pairs):
        parents[child].add(parent)

    def all_ancestors(person: int) -> set[int]:
        ancestors: set[int] = set()
        pending = list(parents[person])
        while pending:
            ancestor = pending.pop()
            if ancestor in ancestors:
                continue
            ancestors.add(ancestor)
            pending.extend(parents[ancestor])
        ancestors.discard(person)
        return ancestors

    return bool(all_ancestors(first) & all_ancestors(second))


def find_earliest_ancestor(
    parent_child_pairs: list[tuple[int, int]], person: int
) -> int | None:
    """Return an ancestor at the greatest parent-edge distance.

    Return the numerically smallest ancestor when distances tie, or ``None``
    when ``person`` has no ancestor.
    """
    parents: dict[int, set[int]] = defaultdict(set)
    for parent, child in set(parent_child_pairs):
        parents[child].add(parent)

    if not parents[person]:
        return None

    greatest_distance: dict[int, int] = {}
    pending: deque[tuple[int, int]] = deque(
        (parent, 1) for parent in parents[person]
    )
    while pending:
        ancestor, distance = pending.popleft()
        if distance <= greatest_distance.get(ancestor, 0):
            continue
        greatest_distance[ancestor] = distance
        pending.extend(
            (parent, distance + 1) for parent in parents[ancestor]
        )

    maximum = max(greatest_distance.values())
    return min(
        ancestor
        for ancestor, distance in greatest_distance.items()
        if distance == maximum
    )
