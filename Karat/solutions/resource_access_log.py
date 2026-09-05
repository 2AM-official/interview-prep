"""Resource Access Log reference solutions."""

from __future__ import annotations

from collections import Counter, defaultdict


def user_access_ranges(
    logs: list[list[str]],
) -> dict[str, tuple[int, int]]:
    """Return each user's minimum and maximum timestamp from unsorted logs."""
    ranges: dict[str, tuple[int, int]] = {}
    for timestamp_text, user, _resource in logs:
        timestamp = int(timestamp_text)
        if user not in ranges:
            ranges[user] = (timestamp, timestamp)
        else:
            earliest, latest = ranges[user]
            ranges[user] = (min(earliest, timestamp), max(latest, timestamp))
    return ranges


def most_requested_resource(
    logs: list[list[str]],
) -> tuple[str, int] | None:
    """Find the resource with most accesses in an inclusive 300-second window.

    Break equal maximum counts lexicographically. Return ``None`` for no logs.
    """
    if not logs:
        return None

    timestamps_by_resource: dict[str, list[int]] = defaultdict(list)
    for timestamp, _user, resource in logs:
        timestamps_by_resource[resource].append(int(timestamp))

    best_resource: str | None = None
    best_count = 0

    for resource in sorted(timestamps_by_resource):
        timestamps = sorted(timestamps_by_resource[resource])
        left = 0
        resource_best = 0

        for right, timestamp in enumerate(timestamps):
            while timestamp - timestamps[left] > 300:
                left += 1
            resource_best = max(resource_best, right - left + 1)

        if resource_best > best_count:
            best_resource = resource
            best_count = resource_best

    return (best_resource, best_count) if best_resource is not None else None


def build_transition_graph(
    logs: list[list[str]],
) -> dict[str, dict[str, float]]:
    """Build per-user resource transition probabilities.

    Sort accesses by timestamp per user. Count START to first resource,
    consecutive resource transitions, and last resource to END. Include START
    but do not include END as a source key.
    """
    accesses_by_user: dict[str, list[tuple[int, int, str]]] = defaultdict(list)
    for order, (timestamp, user, resource) in enumerate(logs):
        accesses_by_user[user].append((int(timestamp), order, resource))

    transitions: dict[str, Counter[str]] = defaultdict(Counter)
    for accesses in accesses_by_user.values():
        accesses.sort()
        resources = [resource for _timestamp, _order, resource in accesses]
        transitions["START"][resources[0]] += 1
        for source, destination in zip(resources, resources[1:]):
            transitions[source][destination] += 1
        transitions[resources[-1]]["END"] += 1

    graph: dict[str, dict[str, float]] = {}
    for source, destinations in transitions.items():
        total = sum(destinations.values())
        graph[source] = {
            destination: count / total
            for destination, count in destinations.items()
        }
    return graph
