"""Picking Restaurant reference solution."""

from __future__ import annotations

from collections import defaultdict


def recommend_restaurant(
    friendships: list[list[str]],
    likes: list[list[str]],
    person_a: str,
    person_b: str,
) -> str | None:
    """Choose the restaurant liked by the most mutual friends.

    Friendships are undirected. Exclude restaurants already liked by either
    diner. Break support-count ties lexicographically and return ``None`` when
    no candidate exists.
    """
    friends: dict[str, set[str]] = defaultdict(set)
    for left, right in friendships:
        friends[left].add(right)
        friends[right].add(left)

    restaurants_by_person: dict[str, set[str]] = defaultdict(set)
    for row in likes:
        if row:
            restaurants_by_person[row[0]].update(row[1:])

    mutual_friends = friends[person_a] & friends[person_b]
    excluded = restaurants_by_person[person_a] | restaurants_by_person[person_b]

    support: dict[str, int] = defaultdict(int)
    for friend in mutual_friends:
        for restaurant in restaurants_by_person[friend] - excluded:
            support[restaurant] += 1

    if not support:
        return None
    return min(support, key=lambda restaurant: (-support[restaurant], restaurant))
