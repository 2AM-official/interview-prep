"""Picking Restaurant practice question."""

from collections import defaultdict


def recommend_restaurant(friendships, likes, person_a, person_b):
    """Choose the restaurant liked by the most mutual friends.

    Friendships are undirected. Exclude restaurants already liked by either
    diner. Break support-count ties lexicographically and return ``None`` when
    no candidate exists.
    """
    friends = defaultdict(set)
    for left, right in friendships:
        friends[left].add(right)
        friends[right].add(left)

    liked = defaultdict(set)
    for row in likes:
        person = row[0]
        for restaurant in row[1:]:
            liked[person].add(restaurant)

    excluded = set()
    for restaurant in liked[person_a]:
        excluded.add(restaurant)
    for restaurant in liked[person_b]:
        excluded.add(restaurant)

    support = defaultdict(int)
    for friend in friends[person_a]:
        if friend not in friends[person_b]:
            continue
        for restaurant in liked[friend]:
            if restaurant not in excluded:
                support[restaurant] += 1

    best_restaurant = None
    best_count = 0
    for restaurant in support:
        count = support[restaurant]
        if best_restaurant is None or count > best_count or (
            count == best_count and restaurant < best_restaurant
        ):
            best_restaurant = restaurant
            best_count = count
    return best_restaurant
