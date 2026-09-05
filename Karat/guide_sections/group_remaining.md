# Remaining Reference Solutions

## `most_powerful_card`

### Question

Given directed matchup pairs `[winner, loser]`, return the card that can beat
the most distinct cards directly or transitively. A card does not beat itself,
even through a cycle. Break ties lexicographically. Return `None` when there
are no cards.

### Example and clarification

If `giant` beats `wizard` and `wizard` beats `elf`, then `giant` beats both
cards. Duplicate matchups do not add extra wins.

### Approach

Build a directed adjacency set. From every card, run a graph traversal and
count distinct reachable cards. Seed the answer by checking cards in sorted
order, so replacing it only for a strictly larger count preserves the required
lexicographic tie-break.

### Complete Python solution

```python
from collections import defaultdict


def most_powerful_card(matchups: list[list[str]]) -> str | None:
    """Return the card that transitively beats the most distinct cards.

    A matchup is ``[winner, loser]``. Break ties lexicographically and handle
    cycles without counting a card as beating itself.
    """
    if not matchups:
        return None

    cards = set()
    defeated_by = defaultdict(set)
    for winner, loser in matchups:
        cards.add(winner)
        cards.add(loser)
        defeated_by[winner].add(loser)

    best_card = None
    best_count = -1
    for card in sorted(cards):
        reachable = set()
        stack = list(defeated_by[card])
        while stack:
            defeated = stack.pop()
            if defeated == card or defeated in reachable:
                continue
            reachable.add(defeated)
            stack.extend(defeated_by[defeated])

        if len(reachable) > best_count:
            best_card = card
            best_count = len(reachable)

    return best_card
```

### Complexity

With `V` cards and `E` matchups, time is `O(V(V + E))` and space is
`O(V + E)`.

## `recommend_restaurant`

### Question

Friendships are undirected. Recommend the restaurant liked by the largest
number of the two diners' mutual friends. Exclude anything either diner
already likes. Break support ties lexicographically and return `None` if no
candidate remains.

### Example and clarification

If both Robin and Marshall are friends with Ted and Lily, and both like
`Restaurant_5`, that restaurant has support two. A repeated restaurant in one
friend's data still counts as only one person's support.

### Approach

Build each person's friend set and restaurant set. Intersect the two diners'
friend sets, then count each mutual friend's unseen restaurant likes. Select
by descending support and then ascending name.

### Complete Python solution

```python
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
    friends = defaultdict(set)
    for left, right in friendships:
        friends[left].add(right)
        friends[right].add(left)

    restaurants_by_person = defaultdict(set)
    for row in likes:
        if row:
            restaurants_by_person[row[0]].update(row[1:])

    mutual_friends = friends[person_a] & friends[person_b]
    excluded = restaurants_by_person[person_a] | restaurants_by_person[person_b]

    support = defaultdict(int)
    for friend in mutual_friends:
        for restaurant in restaurants_by_person[friend] - excluded:
            support[restaurant] += 1

    if not support:
        return None
    return min(support, key=lambda restaurant: (-support[restaurant], restaurant))
```

### Complexity

Let `F` be the friendship entries and `L` the total restaurant-like entries.
Time is `O(F + L + C)`, where `C` is the number of candidate likes scanned.
Space is `O(F + L)`.

## `user_access_ranges`

### Question

For unsorted `[timestamp, user, resource]` records, return each user's earliest
and latest timestamps as integers.

### Example and clarification

Records at times `100` and `50` for `u1` produce `u1: (50, 100)`. A user with
one record has the same minimum and maximum.

### Approach

Scan once. Initialize a pair for a new user; otherwise update both endpoints.

### Complete Python solution

```python
def user_access_ranges(
    logs: list[list[str]],
) -> dict[str, tuple[int, int]]:
    """Return each user's minimum and maximum timestamp from unsorted logs."""
    ranges = {}
    for timestamp_text, user, _resource in logs:
        timestamp = int(timestamp_text)
        if user not in ranges:
            ranges[user] = (timestamp, timestamp)
        else:
            earliest, latest = ranges[user]
            ranges[user] = (min(earliest, timestamp), max(latest, timestamp))
    return ranges
```

### Complexity

For `N` records, time is `O(N)` and space is `O(U)` for `U` users.

## `most_requested_resource`

### Question

Find the resource with the most accesses inside any inclusive 300-second
window. Break equal maximum counts lexicographically. Return `None` for no
logs.

### Example and clarification

Timestamps `100` and `400` can share a window because their difference is
exactly 300. Timestamps `100` and `401` cannot.

### Approach

Group timestamps by resource. Sort each group and use two pointers. Move the
left pointer until the current interval spans at most 300 seconds. Track each
resource's largest window, processing names in sorted order for tie-breaking.

### Complete Python solution

```python
from collections import defaultdict


def most_requested_resource(
    logs: list[list[str]],
) -> tuple[str, int] | None:
    """Find the resource with most accesses in an inclusive 300-second window.

    Break equal maximum counts lexicographically. Return ``None`` for no logs.
    """
    if not logs:
        return None

    timestamps_by_resource = defaultdict(list)
    for timestamp, _user, resource in logs:
        timestamps_by_resource[resource].append(int(timestamp))

    best_resource = None
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

    return (best_resource, best_count)
```

### Complexity

For `N` logs, sorting costs `O(N log N)` time and grouping costs `O(N)` space.
The sliding-window scans are linear after sorting.

## `build_transition_graph`

### Question

Order every user's accesses by time. Count `START` to first resource, each
consecutive resource transition, and final resource to `END`. Return outgoing
probabilities. Include `START`; never use `END` as a source.

### Example and clarification

A user visiting `A, A, B` contributes `START -> A`, `A -> A`, `A -> B`, and
`B -> END`. Repeated resource visits are real self-transitions.

### Approach

Group timestamped resources by user while retaining input order to break equal
timestamps stably. Sort each user's sequence, count all edges, then divide
each edge count by its source's total outgoing count.

### Complete Python solution

```python
from collections import Counter, defaultdict


def build_transition_graph(
    logs: list[list[str]],
) -> dict[str, dict[str, float]]:
    """Build per-user resource transition probabilities.

    Sort accesses by timestamp per user. Count START to first resource,
    consecutive resource transitions, and last resource to END. Include START
    but do not include END as a source key.
    """
    accesses_by_user = defaultdict(list)
    for order, (timestamp, user, resource) in enumerate(logs):
        accesses_by_user[user].append((int(timestamp), order, resource))

    transitions = defaultdict(Counter)
    for accesses in accesses_by_user.values():
        accesses.sort()
        resources = [resource for _timestamp, _order, resource in accesses]
        transitions["START"][resources[0]] += 1
        for source, destination in zip(resources, resources[1:]):
            transitions[source][destination] += 1
        transitions[resources[-1]]["END"] += 1

    graph = {}
    for source, destinations in transitions.items():
        total = sum(destinations.values())
        graph[source] = {
            destination: count / total
            for destination, count in destinations.items()
        }
    return graph
```

### Complexity

For `N` logs, time is `O(N log N)` in the worst case and space is `O(N + E)`,
where `E` is the number of distinct transition pairs.

## `best_day_to_cross`

### Question

Add each morning's snow to the base terrain. After two consecutive mornings
with no snowfall anywhere, melt one accumulated unit per location on that and
each later snowless day. A crossing is viable when every adjacent absolute
height difference is at most one. Its cost is the sum of upward differences.
Return the cheapest `[zero_based_day, cost]`, preferring the earliest day, or
`[-1, -1]`.

### Example and clarification

For bases `[0, 1]`, final heights `[1, 2]` are viable with one upward climb.
Snow depth never goes below zero, so melting never lowers the base terrain.

### Approach

Maintain snow depth and a global snowless-day streak. For each day, update the
depth, apply melting when appropriate, test every adjacent pair, and compute
the upward-only cost. Replace the answer only for a strictly smaller cost.

### Complete Python solution

```python
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
    best_cost = None

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
```

### Complexity

For `D` days and `P` positions, time is `O(DP)` and space is `O(P)`.

## `minimum_sphere_distance`

### Question

Uppercase letters are colored spheres and matching lowercase letters are
holes. Sum the distance from every sphere to its nearest matching hole.
Periods are empty positions.

### Example and clarification

For `R...r.r`, the sphere at index zero chooses the hole at index four, so its
distance is four. Different spheres are handled independently.

### Approach

Record all hole indices by lowercase color and every sphere's index. For each
sphere, find the smallest absolute difference to its matching hole indices.

### Complete Python solution

```python
from collections import defaultdict


def minimum_sphere_distance(room: str) -> int:
    """Sum each uppercase sphere's distance to its nearest lowercase hole.

    There is at most one sphere of each color and at least one matching hole.
    Empty positions are periods; carrying distance is absolute index distance.
    """
    holes = defaultdict(list)
    spheres = []
    for index, item in enumerate(room):
        if item.islower():
            holes[item].append(index)
        elif item.isupper():
            spheres.append((item.lower(), index))

    return sum(
        min(abs(sphere_index - hole_index) for hole_index in holes[color])
        for color, sphere_index in spheres
    )
```

### Complexity

For room length `N`, time is `O(N)` under the guarantee of at most one sphere
per color: each matching hole list is scanned at most once. Space is `O(N)`.

## `filter_treasure_leading_rooms`

### Question

Return every treasure room reached directly from at least two distinct other
rooms. A self-loop does not count. Sort the result.

### Example and clarification

Edges `A -> T`, `B -> T`, and `T -> T` qualify treasure room `T` because its
two qualifying sources are `A` and `B`. Duplicate `A -> T` edges count once.

### Approach

Build a reverse adjacency set while skipping self-loops. Keep treasure rooms
whose reverse set has size at least two, then sort.

### Complete Python solution

```python
from collections import defaultdict


def filter_treasure_leading_rooms(
    treasure_rooms: list[str], instructions: list[list[str]]
) -> list[str]:
    """Return rooms with two incoming rooms that immediately lead to treasure.

    Self-loops do not count toward the two *other* incoming rooms. Sort output.
    """
    incoming = defaultdict(set)
    for source, destination in instructions:
        if source != destination:
            incoming[destination].add(source)

    return sorted(
        room for room in set(treasure_rooms) if len(incoming[room]) >= 2
    )
```

### Complexity

For `E` instructions and `T` treasure rooms, time is
`O(E + T log T)` and space is `O(E)`.

## `minimum_instructions`

### Question

Start in room zero and reach the final room in the fewest moves. Normally a
room jumps forward by its instruction for free. For one dollar, that move may
instead use exactly one less or one more. Distances must stay positive and
land in bounds. Spending less than the budget is allowed.

### Example and clarification

With `[2, 1, 9]` and one dollar, the free jump of two already reaches the final
room in one move, so spending is unnecessary. More generally, each state must
remember both the room and dollars spent because the remaining budget affects
later choices.

### Approach

Run breadth-first search over `(room, dollars_spent)`. Every legal transition
is one move, so the first final-room transition has the minimum move count.
Positive jumps mean no successful path can spend more than the number of
non-final rooms, allowing the budget to be safely capped.

### Complete Python solution

```python
from collections import deque


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
```

### Complexity

With `N` rooms and budget `M`, time and space are
`O(N * min(M, N))`.
