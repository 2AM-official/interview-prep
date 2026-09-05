# Words, Grids, Games, and Formatting

## `find_scrambled_word`

### Question

Given candidate words and a bag of letters, return the candidate that can be
built without using any letter more times than it appears. Return `None` if no
candidate works.

### Example and clarification

`["cat", "baby"], "tcabnihjs"` returns `"cat"`. Letter order and adjacency do
not matter. The prompt guarantees at most one answer.

### Approach

Count the available letters once. For each word, count its letters and check
whether any required count exceeds the available count.

### Complete Python solution

```python
from collections import Counter

def find_scrambled_word(words: list[str], letters: str) -> str | None:
    available = Counter(letters)
    for word in words:
        if not (Counter(word) - available):
            return word
    return None
```

### Complexity

Time: `O(L + C)`, where `L` is the number of supplied letters and `C` is the
total number of characters in all words. Space: `O(A)`, where `A` is the number
of distinct characters.

## `find_word_location`

### Question

Find a path that spells a word in a character grid. A path may begin anywhere
and move only right or down.

### Example and clarification

In `[['c', 'a'], ['x', 't']]`, `"cat"` uses
`[(0, 0), (0, 1), (1, 1)]`. Return coordinates in letter order, or `None`.

### Approach

Try every cell as a start. Depth-first search first to the right and then down,
backtracking when a letter does not match.

### Complete Python solution

```python
def find_word_location(grid, word):
    if not word:
        return []

    def dfs(row, column, index, path):
        if (row >= len(grid) or column >= len(grid[row])
                or grid[row][column] != word[index]):
            return None
        path.append((row, column))
        if index == len(word) - 1:
            return path.copy()
        for next_cell in ((row, column + 1), (row + 1, column)):
            result = dfs(*next_cell, index + 1, path)
            if result is not None:
                return result
        path.pop()
        return None

    for row, cells in enumerate(grid):
        for column in range(len(cells)):
            result = dfs(row, column, 0, [])
            if result is not None:
                return result
    return None
```

### Complexity

Time: `O(R * C * 2^W)` in the worst case for an `R` by `C` grid and a
`W`-letter word. Space: `O(W)` for recursion and the path.

## `find_word_locations`

### Question

Find right/down paths for several words while ensuring that no grid cell is
used by two words.

### Example and clarification

For `["by", "bat"]`, a locally valid path for `"by"` may block every path for
`"bat"`. Choices therefore need global backtracking. Return paths in input
order, or `None`.

### Approach

For the current word, enumerate every path that avoids occupied cells. Reserve
one path, recurse on the next word, and undo the choice if the remaining words
cannot be assigned.

### Complete Python solution

```python
def find_word_locations(grid, words):
    def paths(word, used):
        if not word:
            return [[]]
        found = []

        def dfs(row, column, index, path):
            cell = (row, column)
            if (row >= len(grid) or column >= len(grid[row])
                    or cell in used or grid[row][column] != word[index]):
                return
            path.append(cell)
            if index == len(word) - 1:
                found.append(path.copy())
            else:
                dfs(row, column + 1, index + 1, path)
                dfs(row + 1, column, index + 1, path)
            path.pop()

        for row, cells in enumerate(grid):
            for column in range(len(cells)):
                dfs(row, column, 0, [])
        return found

    answer = []

    def assign(index, used):
        if index == len(words):
            return True
        for path in paths(words[index], used):
            answer.append(path)
            if assign(index + 1, used | set(path)):
                return True
            answer.pop()
        return False

    return answer if assign(0, set()) else None
```

### Complexity

Time is exponential in the number and lengths of the words because all
compatible path combinations may be explored. Space is the total path length
plus recursion and generated candidate paths.

## `is_complete_hand`

### Question

Determine whether all digit tiles can be divided into zero or more triples and
exactly one pair.

### Example and clarification

`"55555"` is valid: one triple and one pair of fives. `"888"` is invalid
because it has no pair.

### Approach

For each digit count, divide by three. Exactly one digit must leave remainder
two; every other digit must leave remainder zero.

### Complete Python solution

```python
from collections import Counter

def is_complete_hand(tiles: str) -> bool:
    if any(tile not in "0123456789" for tile in tiles):
        return False
    pair_found = False
    for count in Counter(tiles).values():
        remainder = count % 3
        if remainder == 2:
            if pair_found:
                return False
            pair_found = True
        elif remainder != 0:
            return False
    return pair_found
```

### Complexity

Time: `O(n)`. Space: `O(1)` because there are only ten possible digits.

## `is_advanced_complete_hand`

### Question

Use every tile as exactly one pair plus groups that are either three equal
digits or three consecutive digits.

### Example and clarification

`"11123"` is valid as pair `11` plus run `123`. Runs do not wrap, so `890` is
not a run.

### Approach

Try every possible pair. For the remaining counts, take the lowest available
digit and recursively try a triple or a run starting there. Memoize count
states.

### Complete Python solution

```python
from functools import lru_cache

def is_advanced_complete_hand(tiles: str) -> bool:
    if len(tiles) % 3 != 2 or any(c not in "0123456789" for c in tiles):
        return False
    counts = [0] * 10
    for tile in tiles:
        counts[int(tile)] += 1

    @lru_cache(None)
    def groups(state):
        first = next((i for i, count in enumerate(state) if count), None)
        if first is None:
            return True
        remaining = list(state)
        if remaining[first] >= 3:
            remaining[first] -= 3
            if groups(tuple(remaining)):
                return True
            remaining[first] += 3
        if first <= 7 and remaining[first + 1] and remaining[first + 2]:
            remaining[first] -= 1
            remaining[first + 1] -= 1
            remaining[first + 2] -= 1
            if groups(tuple(remaining)):
                return True
        return False

    for pair in range(10):
        if counts[pair] >= 2:
            counts[pair] -= 2
            if groups(tuple(counts)):
                return True
            counts[pair] += 2
    return False
```

### Complexity

There are at most `product(count[d] + 1)` memoized count states, each doing
constant work; this is exponential in the number of tiles in the general
bound. Space is the same number of states plus `O(n)` recursion depth.

## `is_valid_matrix`

### Question

Check that an `N x N` matrix has every value from `1` through `N` exactly once
in each row and each column.

### Example and clarification

`[[1, 2], [2, 1]]` is valid. Reject empty, non-square, duplicate, missing, and
out-of-range data.

### Approach

Build the expected set once. Compare every row and every constructed column to
that set.

### Complete Python solution

```python
def is_valid_matrix(matrix: list[list[int]]) -> bool:
    if not matrix:
        return False
    size = len(matrix)
    expected = set(range(1, size + 1))
    if any(len(row) != size or set(row) != expected for row in matrix):
        return False
    return all(
        {matrix[row][column] for row in range(size)} == expected
        for column in range(size)
    )
```

### Complexity

Time: `O(n^2)`. Space: `O(n)` for the sets.

## `validate_nonogram`

### Question

Validate that each row and column has the exact ordered lengths of contiguous
black-cell runs described by its instructions. Black cells are zero.

### Example and clarification

`[0, 0, 1, 0]` produces instructions `[2, 1]`. A line with no zeros produces
`[]`.

### Approach

Scan a line and record a run whenever zeros end. Compare all rows, then build
and compare all columns. Also reject mismatched dimensions.

### Complete Python solution

```python
def validate_nonogram(matrix, row_instructions, column_instructions):
    height = len(matrix)
    width = len(matrix[0]) if matrix else 0
    if (len(row_instructions) != height
            or len(column_instructions) != width
            or any(len(row) != width for row in matrix)):
        return False

    def runs(line):
        answer, length = [], 0
        for cell in line:
            if cell == 0:
                length += 1
            elif length:
                answer.append(length)
                length = 0
        if length:
            answer.append(length)
        return answer

    if any(runs(row) != clue for row, clue in zip(matrix, row_instructions)):
        return False
    return all(
        runs([matrix[row][column] for row in range(height)]) == clue
        for column, clue in enumerate(column_instructions)
    )
```

### Complexity

Time: `O(R * C)`. Space: `O(max(R, C))` for a line and its runs.

## `teleporter_destinations`

### Question

List the unique squares reachable after one die roll, applying at most one
teleporter and preserving die-roll order.

### Example and clarification

With teleporters `["3,1", "4,2", "5,10"]`, a six-sided die, start `0`, and
finish `20`, the result is `[1, 2, 10, 6]`. Any roll reaching or passing the
finish stops at the finish.

### Approach

Parse teleporters into a source-to-destination map. Simulate every roll, clamp
to the finish, apply one lookup, and append destinations not seen before.

### Complete Python solution

```python
def teleporter_destinations(teleporters, die_sides, start, last_square):
    links = {}
    for item in teleporters:
        source, destination = map(int, item.split(","))
        links[source] = destination
    answer, seen = [], set()
    for roll in range(1, die_sides + 1):
        landed = min(start + roll, last_square)
        if landed < last_square:
            landed = min(links.get(landed, landed), last_square)
        if landed not in seen:
            seen.add(landed)
            answer.append(landed)
    return answer
```

### Complexity

Time: `O(T + D)` for `T` teleporters and `D` die sides. Space: `O(T + D)`.

## `is_finishable`

### Question

Determine whether some sequence of rolls can reach the final square when one
teleporter may be followed after each roll.

### Example and clarification

Backward teleporters can create a barrier. This is reachability, not a request
for the minimum number of rolls.

### Approach

Treat board squares as graph nodes. Breadth-first search all one-roll
destinations and use a visited set so cycles terminate.

### Complete Python solution

```python
from collections import deque

def is_finishable(teleporters, die_sides, start, last_square):
    if start >= last_square:
        return True
    if die_sides <= 0:
        return False
    links = {}
    for item in teleporters:
        source, destination = map(int, item.split(","))
        links[source] = destination
    queue, visited = deque([start]), {start}
    while queue:
        square = queue.popleft()
        for roll in range(1, die_sides + 1):
            landed = min(square + roll, last_square)
            if landed < last_square:
                landed = min(links.get(landed, landed), last_square)
            if landed >= last_square:
                return True
            if landed not in visited:
                visited.add(landed)
                queue.append(landed)
    return False
```

### Complexity

Time: `O(B * D + T)` for `B` reachable board states, `D` die sides, and `T`
teleporters. Space: `O(B + T)`.

## `wrap_lines`

### Question

Greedily place as many words as possible on each line without exceeding a
maximum width, rendering spaces as hyphens.

### Example and clarification

`["The", "day", "began"]` at width `7` becomes `["The-day", "began"]`.
Individual words are guaranteed to fit.

### Approach

Track the current words and visible width. Before adding each word, account for
one separator; flush the current line if the new word would overflow.

### Complete Python solution

```python
def wrap_lines(words: list[str], max_width: int) -> list[str]:
    answer, current, width = [], [], 0
    for word in words:
        added = len(word) + (1 if current else 0)
        if current and width + added > max_width:
            answer.append("-".join(current))
            current, width = [word], len(word)
        else:
            current.append(word)
            width += added
    if current:
        answer.append("-".join(current))
    return answer
```

### Complexity

Time: `O(C)` and space: `O(C)`, where `C` is the total number of characters in
the output.

## `reflow_and_justify`

### Question

Reflow words to a maximum width and fully justify every multiword line with
hyphens. Earlier gaps receive extra hyphens first.

### Example and clarification

For three words requiring eight total hyphens, two gaps receive four hyphens
each. Single-word lines are not padded.

### Approach

Split all input lines into words and greedily wrap them. For each multiword
line, subtract letter count from the target width, divide the hyphens evenly
across gaps, and give one extra to each earliest remainder gap.

### Complete Python solution

```python
def reflow_and_justify(lines: list[str], max_width: int) -> list[str]:
    words = [word for line in lines for word in line.split()]
    wrapped = wrap_lines(words, max_width)
    answer = []
    for line in wrapped:
        line_words = line.split("-")
        if len(line_words) == 1:
            answer.append(line)
            continue
        hyphens = max_width - sum(map(len, line_words))
        gaps = len(line_words) - 1
        base, extra = divmod(hyphens, gaps)
        pieces = [line_words[0]]
        for index, word in enumerate(line_words[1:]):
            pieces += ["-" * (base + (index < extra)), word]
        answer.append("".join(pieces))
    return answer
```

### Complexity

Time: `O(C)` and space: `O(C)`, where `C` is the total input/output character
count.
