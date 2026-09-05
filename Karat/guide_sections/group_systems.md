# Group and Systems Reference Guide

Each answer is intentionally short enough to review on a phone. The code matches
the reference modules in `Karat/solutions`.

## Cipher

### `transpose_cipher`

**Question**

Fill a `rows × columns` matrix from left to right, top to bottom, then read it
top to bottom, left to right.

**Example / clarification**

For `"abcdef"`, 2 rows, and 3 columns, the rows are `abc` and `def`; reading
columns produces `"adbecf"`. Spaces and punctuation are ordinary characters.

**Approach**

For each column, visit every row. A row-major cell is at
`row * columns + column`.

**Complete Python solution**

```python
def transpose_cipher(message: str, rows: int, columns: int) -> str:
    return "".join(
        message[row * columns + column]
        for column in range(columns)
        for row in range(rows)
    )
```

**Complexity**

Time is `O(rows × columns)`. Output space is `O(rows × columns)`.

### `encrypt_with_key`

**Question**

Build a substitution alphabet from the first case-insensitive occurrence of
each letter in the key, then encrypt a message.

**Example / clarification**

If the deduplicated key starts `THE...`, then `A → T`, `B → H`, and `C → E`.
Preserve message case and leave non-ASCII letters, spaces, and punctuation
unchanged.

**Approach**

Deduplicate the key into 26 uppercase letters. Zip those letters against
`A-Z`, then substitute each message character.

**Complete Python solution**

```python
from string import ascii_uppercase


def encrypt_with_key(message: str, key: str) -> str:
    keyed_alphabet = []
    seen = set()
    for character in key:
        upper = character.upper()
        if upper in ascii_uppercase and upper not in seen:
            seen.add(upper)
            keyed_alphabet.append(upper)

    substitution = dict(zip(ascii_uppercase, keyed_alphabet))
    encrypted = []
    for character in message:
        replacement = substitution.get(character.upper())
        if replacement is None:
            encrypted.append(character)
        elif character.islower():
            encrypted.append(replacement.lower())
        else:
            encrypted.append(replacement)
    return "".join(encrypted)
```

**Complexity**

For key length `K` and message length `M`, time is `O(K + M)` and extra space
is `O(M)` including the output.

### `possible_decryptions`

**Question**

Return dictionary words that can map bijectively to a ciphertext split into
numbers `1..26`.

**Example / clarification**

`"122"` can represent a three-letter pattern such as `1,2,2`, so `"COO"`
matches. `"CAT"` does not because its last two different letters would both
map to `2`. Tokens cannot start with zero.

**Approach**

Try each dictionary word. Backtrack over one- and two-digit tokens while
maintaining both a letter-to-number map and a set of numbers already assigned
to other letters.

**Complete Python solution**

```python
def possible_decryptions(dictionary: list[str], ciphertext: str) -> list[str]:
    def matches(word: str) -> bool:
        word = word.upper()

        def search(letter_i, digit_i, assignments, used):
            if letter_i == len(word):
                return digit_i == len(ciphertext)
            if digit_i >= len(ciphertext) or ciphertext[digit_i] == "0":
                return False

            letter = word[letter_i]
            for width in (1, 2):
                end = digit_i + width
                if end > len(ciphertext):
                    continue
                number = int(ciphertext[digit_i:end])
                if not 1 <= number <= 26:
                    continue
                assigned = assignments.get(letter)
                if assigned is not None and assigned != number:
                    continue
                if assigned is None and number in used:
                    continue

                if assigned is None:
                    assignments[letter] = number
                    used.add(number)
                if search(letter_i + 1, end, assignments, used):
                    return True
                if assigned is None:
                    del assignments[letter]
                    used.remove(number)
            return False

        return search(0, 0, {}, set())

    answer = []
    seen_words = set()
    for word in dictionary:
        if word not in seen_words and matches(word):
            seen_words.add(word)
            answer.append(word)
    return answer
```

**Complexity**

For `D` words of maximum length `L`, worst-case time is `O(D × 2^L)` because
each letter may consume one or two digits. Backtracking space is `O(L)`.

## Delivery Bot

### `delivery_destinations`

**Question**

For every origin in a directed acyclic graph, list every reachable terminal
destination.

**Example / clarification**

With `A → B`, `A → C`, `B → D`, and `C → D`, only `A` is an origin and `D` is
its only terminal. Duplicate paths do not duplicate results.

**Approach**

Origins have no incoming edge. Use memoized DFS to compute the set of terminal
nodes reachable from each node.

**Complete Python solution**

```python
from collections import defaultdict


def delivery_destinations(paths: list[list[str]]) -> dict[str, list[str]]:
    graph = defaultdict(set)
    nodes = set()
    has_incoming = set()
    for origin, destination in paths:
        graph[origin].add(destination)
        nodes.update((origin, destination))
        has_incoming.add(destination)

    cache = {}

    def terminals(node):
        if node in cache:
            return cache[node]
        if not graph[node]:
            cache[node] = {node}
        else:
            cache[node] = set()
            for neighbor in graph[node]:
                cache[node].update(terminals(neighbor))
        return cache[node]

    origins = sorted(nodes - has_incoming)
    return {origin: sorted(terminals(origin)) for origin in origins}
```

**Complexity**

Let `T` be the number of terminals. Set propagation takes
`O((V + E) × T)` time and `O(V × T + E)` space in the worst case.

### `buildable_robots`

**Question**

Return robots for which every required part is available.

**Example / clarification**

Available parts are reusable. If `"courier"` needs `wheel` and `motor`, one of
each in the available set is enough, regardless of other robots.

**Approach**

Put available parts in a set and use a subset check for each robot.

**Complete Python solution**

```python
def buildable_robots(
    all_parts: list[str], required_parts: list[list[object]]
) -> list[str]:
    available = set(all_parts)
    answer = []
    for robot_name, parts in required_parts:
        if set(parts).issubset(available):
            answer.append(str(robot_name))
    return answer
```

**Complexity**

Time is `O(P + R)`, where `P` is the available-part count and `R` is the total
number of required-part entries. Extra space is `O(P)`.

## Generation Graph

### `find_nodes_with_zero_or_one_parent`

**Question**

Find all nodes with zero distinct parents and all nodes with exactly one.

**Example / clarification**

For `(1,3), (2,3), (4,2)`, nodes `1` and `4` have zero parents, while `2` has
one. Duplicate edges count once.

**Approach**

Collect every node and a set of parents for each child, then filter and sort.

**Complete Python solution**

```python
from collections import defaultdict


def find_nodes_with_zero_or_one_parent(parent_child_pairs):
    parents = defaultdict(set)
    nodes = set()
    for parent, child in parent_child_pairs:
        nodes.update((parent, child))
        parents[child].add(parent)
    zero = sorted(node for node in nodes if not parents[node])
    one = sorted(node for node in nodes if len(parents[node]) == 1)
    return zero, one
```

**Complexity**

Building sets is `O(E)` average time. Sorting makes total time
`O(E + V log V)`; space is `O(V + E)`.

### `has_common_ancestor`

**Question**

Determine whether two nodes share any direct or transitive ancestor.

**Example / clarification**

If `1 → 3 → 6` and `1 → 4`, then `6` and `4` share ancestor `1`. A node does
not count as its own ancestor.

**Approach**

Traverse parent edges from each person, build two ancestor sets, and test their
intersection.

**Complete Python solution**

```python
from collections import defaultdict


def has_common_ancestor(parent_child_pairs, first, second):
    parents = defaultdict(set)
    for parent, child in set(parent_child_pairs):
        parents[child].add(parent)

    def all_ancestors(person):
        ancestors = set()
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
```

**Complexity**

Time and space are both `O(V + E)`.

### `find_earliest_ancestor`

**Question**

Find an ancestor at the greatest parent-edge distance, breaking distance ties
with the smaller numeric node.

**Example / clarification**

For `1 → 3 → 6` and `2 → 6`, person `6` returns `1`, which is two edges away.
A person with no parent returns `None`.

**Approach**

Walk upward while recording the greatest distance found for each ancestor.
After traversal, select the smallest ancestor at the maximum distance.

**Complete Python solution**

```python
from collections import defaultdict, deque


def find_earliest_ancestor(parent_child_pairs, person):
    parents = defaultdict(set)
    for parent, child in set(parent_child_pairs):
        parents[child].add(parent)
    if not parents[person]:
        return None

    greatest_distance = {}
    pending = deque((parent, 1) for parent in parents[person])
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
```

**Complexity**

On a DAG, distance relaxations take at most `O(V × E)` time in the worst case.
The graph, queue, and distance map use `O(V + E)` space.

## Movie Recommendation

### `group_users_by_follow_count`

**Question**

Apply connect/disconnect events, then split all users below a follow threshold
from users at or above it.

**Example / clarification**

Connections are outgoing from the first user to the second. Reconnecting the
same pair or disconnecting a missing pair changes nothing. Users who only
appear as targets still belong in the output.

**Approach**

Maintain each user's outgoing neighbors as a set. Sets make both event types
idempotent.

**Complete Python solution**

```python
from collections import defaultdict


def group_users_by_follow_count(events, threshold):
    follows = defaultdict(set)
    users = set()
    for follower, followed, operation in events:
        users.update((follower, followed))
        if operation == "CONNECT":
            follows[follower].add(followed)
        elif operation == "DISCONNECT":
            follows[follower].discard(followed)
        else:
            raise ValueError(f"unknown operation: {operation}")
    below = sorted(user for user in users if len(follows[user]) < threshold)
    above = sorted(user for user in users if len(follows[user]) >= threshold)
    return below, above
```

**Complexity**

For `E` events and `U` users, time is `O(E + U log U)` and space is
`O(U + E)`.

### `recommend_movies`

**Question**

Recommend unseen movies watched by users who share a movie rated above 3 with
the target user.

**Example / clarification**

Similarity is direct, not transitive. A similar user's low-rated movie is still
a recommendation because the shared high rating establishes similarity while
all watched movies are candidates.

**Approach**

Build watched and liked sets per user. Find users whose liked set intersects
the target's, then union their unseen watched movies.

**Complete Python solution**

```python
from collections import defaultdict


def recommend_movies(user, ratings):
    watched = defaultdict(set)
    liked = defaultdict(set)
    for rating_user, movie, rating_text in ratings:
        watched[rating_user].add(movie)
        if float(rating_text) > 3:
            liked[rating_user].add(movie)

    similar = {
        other
        for other in watched
        if other != user and liked[user] & liked[other]
    }
    answer = set()
    for other in similar:
        answer.update(watched[other] - watched[user])
    return sorted(answer)
```

**Complexity**

Building indexes is `O(R)`. Similarity checks and unions are `O(R)` total in
typical set accounting, plus `O(M log M)` to sort `M` recommendations. Space
is `O(R)`.

## Passage Tracker

### `parse_log_entry`

**Question**

Parse a log line into typed fields and expand `E/W` directions.

**Example / clarification**

`"44776.619 KTB918 310E MAINROAD"` becomes
`(44776.619, "KTB918", 310, "EAST", "MAINROAD")`. Any direction other than
`E` or `W` raises `ValueError`.

**Approach**

Split four whitespace-separated fields. The last character of the location
field is its direction; the preceding characters form the integer location.

**Complete Python solution**

```python
def parse_log_entry(log_line: str):
    timestamp_text, plate, location_direction, booth_type = log_line.split()
    direction_code = location_direction[-1]
    directions = {"E": "EAST", "W": "WEST"}
    if direction_code not in directions:
        raise ValueError(f"invalid direction: {direction_code}")
    return (
        float(timestamp_text),
        plate,
        int(location_direction[:-1]),
        directions[direction_code],
        booth_type,
    )
```

**Complexity**

Time and returned storage are `O(L)` for line length `L`.

### Shared journey grouping

Both remaining functions use this helper. It groups by plate, sorts each
plate's records, pairs each `ENTRY` with its `EXIT`, then globally sorts
journeys by entry time.

```python
from collections import defaultdict


def _complete_journeys(log_lines):
    by_plate = defaultdict(list)
    for line in log_lines:
        entry = parse_log_entry(line)
        by_plate[entry[1]].append(entry)

    journeys = []
    for entries in by_plate.values():
        entries.sort(key=lambda entry: entry[0])
        current = None
        for entry in entries:
            if entry[4] == "ENTRY":
                current = [entry]
            elif current is not None:
                current.append(entry)
                if entry[4] == "EXIT":
                    journeys.append(current)
                    current = None
    journeys.sort(key=lambda journey: journey[0][0])
    return journeys
```

### `count_journeys`

**Question**

Count complete entry-to-exit journeys even when logs arrive unsorted.

**Example / clarification**

Two plates with one complete `ENTRY ... EXIT` sequence each produce `2`.
Journeys for the same plate are guaranteed not to overlap.

**Approach**

Use `_complete_journeys` above and count the resulting groups.

**Complete Python solution**

```python
def count_journeys(log_lines: list[str]) -> int:
    return len(_complete_journeys(log_lines))
```

**Complexity**

Sorting dominates: time is `O(N log N)` and space is `O(N)`.

### `catch_speeders`

**Question**

Return one plate for each journey averaging at least 130 km/h over one 10 km
segment or at least 120 km/h over two consecutive segments.

**Example / clarification**

Ten kilometers in 275 seconds is about 130.9 km/h and is flagged. Compare
using multiplication, not rounded speeds. The same plate can appear for
multiple speeding journeys.

**Approach**

Group journeys chronologically. Check adjacent records for the one-segment
rule and triples moving consistently through two 10 km segments for the
two-segment rule.

**Complete Python solution**

```python
def catch_speeders(log_lines: list[str]) -> list[str]:
    def fast_enough(first, last, distance, speed):
        elapsed = last[0] - first[0]
        return (
            elapsed > 0
            and abs(last[2] - first[2]) == distance
            and distance * 3600 >= speed * elapsed
        )

    answer = []
    for journey in _complete_journeys(log_lines):
        speeding = any(
            fast_enough(journey[i], journey[i + 1], 10, 130)
            for i in range(len(journey) - 1)
        )
        if not speeding:
            speeding = any(
                abs(journey[i + 1][2] - journey[i][2]) == 10
                and abs(journey[i + 2][2] - journey[i + 1][2]) == 10
                and journey[i + 1][2] - journey[i][2]
                == journey[i + 2][2] - journey[i + 1][2]
                and fast_enough(journey[i], journey[i + 2], 20, 120)
                for i in range(len(journey) - 2)
            )
        if speeding:
            answer.append(journey[0][1])
    return answer
```

**Complexity**

Grouping and sorting take `O(N log N)` time; scanning takes `O(N)`. Stored
records require `O(N)` space.
