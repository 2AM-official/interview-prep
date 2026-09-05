"""Complete reference solutions for the Movie Recommendation exercise family."""

from __future__ import annotations

from collections import defaultdict


def group_users_by_follow_count(
    events: list[list[str]], threshold: int
) -> tuple[list[str], list[str]]:
    """Apply CONNECT/DISCONNECT events and group users by outgoing follows.

    Include every user appearing in either event position. Repeated CONNECT
    and missing DISCONNECT operations are idempotent. Sort both groups.
    """
    follows: dict[str, set[str]] = defaultdict(set)
    users: set[str] = set()
    for follower, followed, operation in events:
        users.update((follower, followed))
        if operation == "CONNECT":
            follows[follower].add(followed)
        elif operation == "DISCONNECT":
            follows[follower].discard(followed)
        else:
            raise ValueError(f"unknown operation: {operation}")

    below = sorted(user for user in users if len(follows[user]) < threshold)
    at_or_above = sorted(
        user for user in users if len(follows[user]) >= threshold
    )
    return below, at_or_above


def recommend_movies(user: str, ratings: list[list[str]]) -> list[str]:
    """Recommend unseen movies watched by users similar to ``user``.

    Users are similar when both rated at least one common movie above 3.
    Recommend every movie watched by a similar user but not by ``user``.
    Return unique movie names sorted lexicographically.
    """
    watched: dict[str, set[str]] = defaultdict(set)
    liked: dict[str, set[str]] = defaultdict(set)
    for rating_user, movie, rating_text in ratings:
        watched[rating_user].add(movie)
        if float(rating_text) > 3:
            liked[rating_user].add(movie)

    similar_users = {
        other
        for other in watched
        if other != user and liked[user] & liked[other]
    }
    recommendations: set[str] = set()
    for similar_user in similar_users:
        recommendations.update(watched[similar_user] - watched[user])
    return sorted(recommendations)
