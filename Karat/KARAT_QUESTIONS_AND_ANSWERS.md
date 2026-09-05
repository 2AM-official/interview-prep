# Karat Coding Interview Learning Guide

This guide organizes the supplied Karat practice questions by topic. Use it
to study the problem statement, explain an approach aloud, implement the
function, run focused tests, and review complexity.

## Project layout

- Implementations: `Karat/exercise/`
- Tests: `Karat/test/`
- Focused test runner: `Karat/run_tests.py`

Run one complete question family from the repository root:

```bash
python3 Karat/run_tests.py academic-schedule
python3 Karat/run_tests.py domain-analysis
python3 Karat/run_tests.py snake-exits
```

A failing `NotImplementedError` means that part is still a starter exercise.

## Recommended practice routine

For each question:

1. Restate the inputs and expected output in your own words.
2. Work through one sample manually.
3. State the data structures you plan to use.
4. Implement the simplest correct solution.
5. Run the focused tests.
6. Add an edge-case test.
7. Explain time and space complexity.
8. Discuss how the solution would change for much larger input.

## Interview checklist

Before coding, clarify:

- Can the input be empty?
- Can records be duplicated?
- Is output order important?
- Are identifiers strings or numbers?
- Can a graph contain cycles?
- Can there be multiple valid answers?
- Should malformed input be rejected or assumed valid?

While coding:

- Use descriptive names.
- Separate input parsing from the main algorithm.
- State invariants for loops and recursive functions.
- Test the smallest valid input and a no-result case.

## 1. Academic Schedule

Files:

- `exercise/academic_schedule.py`
- `test/test_academic_schedule.py`

Run:

```bash
python3 Karat/run_tests.py academic-schedule
```

Part 1 asks for shared courses for every pair of students. The main patterns
are hash maps, sets, pair generation, and set intersection.

Part 2 asks for midpoint courses on every root-to-leaf curriculum track. The
main patterns are directed graphs, root detection, depth-first search,
backtracking, and path indexing.

## 2. Book Endings

Files:

- `exercise/book_endings.py`
- `test/test_book_endings.py`

Run:

```bash
python3 Karat/run_tests.py book-endings
```

Part 1 follows one fixed choice through a book and must detect loops. Part 2
explores every choice and returns all reachable good endings. Practice graph
traversal, terminal states, and visited sets.

## 3. Camping

Files:

- `exercise/camping.py`
- `test/test_camping.py`

Run:

```bash
python3 Karat/run_tests.py camping
```

Part 1 counts department visits saved by grouping a shopping list. Practice
mapping products to departments, counting contiguous runs, and distinct sets.

Part 2 assigns passengers to cars based on arrival time. Practice graph route
traversal, cumulative time, and comparing candidates.

## 4. Catch Cheaters

Files:

- `exercise/catch_cheaters.py`
- `test/test_catch_cheaters.py`

Run:

```bash
python3 Karat/run_tests.py catch-cheaters
```

Part 1 finds a word that can be formed from available letters. Practice
frequency counters and repeated-character handling.

Parts 2 and 3 locate words in a grid using right/down paths. The final part
must assign non-overlapping paths to several words. Practice DFS,
backtracking, coordinate paths, and global state.

## 5. Cipher

Files:

- `exercise/cipher.py`
- `test/test_cipher.py`

Run:

```bash
python3 Karat/run_tests.py cipher
```

The parts cover matrix transposition, keyed substitution, and ambiguous
numeric decryption. Practice indexing, character mapping, case preservation,
tokenization, and backtracking.

## 6. Delivery Bot

Files:

- `exercise/delivery_bot.py`
- `test/test_delivery_bot.py`

Run:

```bash
python3 Karat/run_tests.py delivery-bot
```

Part 1 maps graph origins to reachable terminal destinations. Part 2 checks
which robots can be built from available parts. Practice graph traversal,
root/leaf detection, memoization, and subset checks.

## 7. Domain Analysis

Files:

- `exercise/domain_analysis.py`
- `test/test_domain_analysis.py`

Run:

```bash
python3 Karat/run_tests.py domain-analysis
```

Question 1 aggregates visits for full domains and parent domains. Practice
string parsing and hash-map aggregation.

Question 2 finds the longest contiguous sequence shared by two browsing
histories. This is the longest common substring pattern and uses dynamic
programming.

Question 3 attributes ad clicks to purchasing users. Practice parsing,
joining records through IDs and IPs, and grouped counting.

## 8. Generation Graph

Files:

- `exercise/generation_graph.py`
- `test/test_generation_graph.py`

Run:

```bash
python3 Karat/run_tests.py generation-graph
```

The parts find nodes with zero or one parent, determine whether two nodes
share an ancestor, and find an earliest ancestor. Practice parent adjacency
maps, indegree counting, DFS/BFS, and ancestor depth.

## 9. Mini Game

Files:

- `exercise/mini_game.py`
- `test/test_mini_game.py`

Run:

```bash
python3 Karat/run_tests.py mini-game
```

Part 1 validates hands made of identical triples plus exactly one pair.
Frequency counts and modulo arithmetic are central.

Part 2 also allows runs. Practice recursive search, consuming/restoring
counts, and trying alternative valid groupings.

## 10. Most Powerful Card

Files:

- `exercise/most_powerful_card.py`
- `test/test_most_powerful_card.py`

Run:

```bash
python3 Karat/run_tests.py most-powerful-card
```

Matchup pairs describe which card defeats another. Practice directed graphs,
transitive reachability, and identifying a unique winner.

## 11. Movie Recommendation

Files:

- `exercise/movie_recommendation.py`
- `test/test_movie_recommendation.py`

Run:

```bash
python3 Karat/run_tests.py movie-recommendation
```

Part 1 groups users by follow count. Part 2 recommends movies through social
connections. Practice grouping, adjacency sets, deduplication, and excluding
already-seen items.

## 12. Passage Tracker

Files:

- `exercise/passage_tracker.py`
- `test/test_passage_tracker.py`

Run:

```bash
python3 Karat/run_tests.py passage-tracker
```

The parts parse access logs, count journeys, and detect speeding. Practice
structured parsing, grouping events by entity, sorting by time, and deriving
metrics from consecutive events.

## 13. Picking Restaurant

Files:

- `exercise/picking_restaurant.py`
- `test/test_picking_restaurant.py`

Run:

```bash
python3 Karat/run_tests.py picking-restaurant
```

The question recommends a restaurant through mutual friends. Practice graph
neighborhoods, intersections, candidate scoring, and deterministic
tie-breaking.

## 14. Puzzle Checker

Files:

- `exercise/puzzle_checker.py`
- `test/test_puzzle_checker.py`

Run:

```bash
python3 Karat/run_tests.py puzzle-checker
```

Part 1 verifies that every row and column contains exactly `1` through `N`.
Practice matrix validation, sets, and careful dimension checks.

Part 2 validates nonogram clues. Practice scanning rows/columns, converting
filled cells into run lengths, and comparing those runs with clues.

## 15. Resource Access Log

Files:

- `exercise/resource_access_log.py`
- `test/test_resource_access_log.py`

Run:

```bash
python3 Karat/run_tests.py resource-access-log
```

The questions calculate each user's access range, find the busiest
five-minute resource window, and build transition probabilities. Practice
time conversion, sorting, sliding windows, nested counters, and probability
normalization.

## 16. Snake Exits

Files:

- `exercise/snake_exits.py`
- `test/test_snake_exits.py`

Run:

```bash
python3 Karat/run_tests.py snake-exits
```

Part 1 finds rows and columns with no blocked cells. Practice matrix scanning.

Part 2 finds the nearest reachable boundary exit. Practice BFS and shortest
paths in an unweighted grid.

Part 3 counts connected nest entrances. Practice connected components,
boundary detection, and DFS/BFS.

## 17. Snowy Mountain

Files:

- `exercise/snowy_mountain.py`
- `test/test_snowy_mountain.py`

Run:

```bash
python3 Karat/run_tests.py snowy-mountain
```

The question chooses the cheapest day to cross changing terrain. Practice
evaluating candidate days, path costs, and dynamic programming or shortest
path reasoning.

## 18. Thrilling Teleporters

Files:

- `exercise/thrilling_teleporters.py`
- `test/test_thrilling_teleporters.py`

Run:

```bash
python3 Karat/run_tests.py thrilling-teleporters
```

Part 1 returns unique possible destinations after one die roll. Practice
simulation, lookup maps, deduplication, and preserving order.

Part 2 checks whether the board is finishable. Practice graph reachability,
cycle detection, and reasoning about every possible move.

## 19. Tomb Raider

Files:

- `exercise/tomb_raider.py`
- `test/test_tomb_raider.py`

Run:

```bash
python3 Karat/run_tests.py tomb-raider
```

The question calculates the minimum distance between spheres and holes.
Practice three-dimensional Euclidean distance, radii, and clamping negative
surface distances to zero.

## 20. Treasure Room

Files:

- `exercise/treasure_room.py`
- `test/test_treasure_room.py`

Run:

```bash
python3 Karat/run_tests.py treasure-room
```

Question 1 filters rooms that lead to treasure under graph constraints.
Question 2 finds a route with the fewest paid instructions. Practice reverse
graphs, reachability, weighted shortest paths, and Dijkstra's algorithm.

## 21. Writing Application

Files:

- `exercise/writing_application.py`
- `test/test_writing_application.py`

Run:

```bash
python3 Karat/run_tests.py writing-application
```

Part 1 greedily wraps words within a line width. Part 2 reflows and justifies
text. Practice tokenization, greedy packing, distributing spaces, and edge
cases such as one-word lines.

## Pattern review

Hash maps and sets:

- Academic Schedule Part 1
- Domain Analysis Question 1
- Delivery Bot Part 2
- Mini Game

Graph traversal:

- Academic Schedule Part 2
- Book Endings
- Delivery Bot Part 1
- Generation Graph
- Snake Exits
- Treasure Room

Dynamic programming and backtracking:

- Catch Cheaters
- Cipher Part 3
- Domain Analysis Question 2
- Mini Game Part 2
- Snowy Mountain

Sorting and sliding windows:

- Passage Tracker
- Resource Access Log

Matrix and grid processing:

- Catch Cheaters
- Puzzle Checker
- Snake Exits
- Cipher Part 1

## Final review questions

For every completed solution, be ready to answer:

1. Why is your chosen data structure appropriate?
2. What are the time and space complexities?
3. Which input causes the worst-case runtime?
4. What edge cases did you test?
5. How would you handle malformed or extremely large input?
6. Could recursion exceed the call-stack limit?
7. Is output deterministic when sets or dictionaries are used?


---

# Grouping, Courses, and Graphs

Reference notes for the Academic Schedule, Domain Analysis, Snake Exits,
Book Endings, and Camping exercise families.

## `find_pairs`

### Question

Given student-course enrollments, list the shared courses for every pair of
students. Include pairs that share nothing.

### Example and clarification

`[["1", "Math"], ["1", "Art"], ["2", "Math"], ["3", "Art"]]` gives
`{"1,2": ["Math"], "1,3": ["Art"], "2,3": []}`. Student IDs are sorted as
strings, and duplicate enrollments do not duplicate a course.

### Approach

Build one set of courses per student. Generate every pair from the sorted
student IDs and intersect their sets.

### Complete Python solution

```python
from collections import defaultdict

def find_pairs(enrollments: list[list[str]]) -> dict[str, list[str]]:
    courses_by_student = defaultdict(set)
    for student, course in enrollments:
        courses_by_student[student].add(course)

    students = sorted(courses_by_student)
    result = {}
    for index, first in enumerate(students):
        for second in students[index + 1:]:
            result[f"{first},{second}"] = sorted(
                courses_by_student[first] & courses_by_student[second]
            )
    return result
```

### Complexity

For `n` enrollments, `s` students, and at most `c` courses per student: time is
`O(n + s²c)` and auxiliary space is `O(n + s²)` excluding returned course
lists.

## `curriculum_midpoints`

### Question

Find the midpoint course of every root-to-leaf path in a prerequisite DAG.
Return unique midpoint names.

### Example and clarification

For `A -> B -> C -> D`, return `B`: on an even-length path, choose the earlier
middle course. Branches create separate root-to-leaf paths.

### Approach

Build adjacency lists and find roots by subtracting destinations from all
courses. Depth-first search each complete path; at a leaf, select index
`(path_length - 1) // 2`.

### Complete Python solution

```python
from collections import defaultdict

def curriculum_midpoints(prerequisites: list[list[str]]) -> list[str]:
    graph = defaultdict(list)
    courses, destinations = set(), set()
    for source, destination in prerequisites:
        if destination not in graph[source]:
            graph[source].append(destination)
        courses.update((source, destination))
        destinations.add(destination)

    midpoints = set()

    def visit(course, path):
        path.append(course)
        if not graph[course]:
            midpoints.add(path[(len(path) - 1) // 2])
        else:
            for following_course in graph[course]:
                visit(following_course, path)
        path.pop()

    for root in courses - destinations:
        visit(root, [])
    return sorted(midpoints)
```

### Complexity

Building the graph costs `O(e + v)`. Traversal costs the total size of all
root-to-leaf paths, which can be exponential in a branching DAG. The active
path uses `O(v)` space, plus graph and output storage.

## `aggregate_domain_visits`

### Question

Add each domain's visits to that domain and every parent domain.

### Example and clarification

`"900 discuss.leetcode.com"` contributes 900 to `discuss.leetcode.com`,
`leetcode.com`, and `com`. Both space-separated and comma-separated inputs are
accepted.

### Approach

Parse each count and domain, split the domain into components, and join every
suffix while adding the count.

### Complete Python solution

```python
from collections import defaultdict

def aggregate_domain_visits(visits: list[str]) -> dict[str, int]:
    totals = defaultdict(int)
    for visit in visits:
        count_text, domain = visit.replace(",", " ", 1).split(maxsplit=1)
        components = domain.split(".")
        for index in range(len(components)):
            totals[".".join(components[index:])] += int(count_text)
    return dict(totals)
```

### Complexity

With `p` total domain components, time is `O(p)` ignoring string-copy cost and
space is `O(p)` for distinct suffixes.

## `longest_contiguous_history`

### Question

Find the longest contiguous run of pages shared by two browsing histories.

### Example and clarification

`["a", "b", "c"]` and `["x", "b", "c"]` return `["b", "c"]`. For equal
lengths, choose the match starting earliest in the first history.

### Approach

Use longest-common-substring dynamic programming. A matching pair extends the
diagonal value from the preceding row. Only two rows are needed.

### Complete Python solution

```python
def longest_contiguous_history(first: list[str], second: list[str]) -> list[str]:
    previous = [0] * (len(second) + 1)
    best_length = best_start = 0

    for first_index, first_page in enumerate(first, start=1):
        current = [0] * (len(second) + 1)
        for second_index, second_page in enumerate(second, start=1):
            if first_page == second_page:
                current[second_index] = previous[second_index - 1] + 1
                length = current[second_index]
                start = first_index - length
                if length > best_length or (
                    length == best_length and start < best_start
                ):
                    best_length, best_start = length, start
        previous = current
    return first[best_start:best_start + best_length]
```

### Complexity

For history lengths `n` and `m`, time is `O(nm)` and auxiliary space is
`O(m)`.

## `ad_conversion_rates`

### Question

For each ad, count all clicks and the clicks made by users who later bought.

### Example and clarification

Map user IDs to IP addresses first. A click from an unknown IP still increases
the total, but not the purchasing count. Each click counts separately.

### Approach

Put completed IDs in a set, derive a set of purchaser IPs, then aggregate two
counters for each ad while scanning clicks.

### Complete Python solution

```python
def ad_conversion_rates(completed_user_ids, ad_clicks, user_ips):
    purchasers = set(completed_user_ids)
    purchaser_ips = {
        ip
        for user_id, ip in (entry.split(",", 1) for entry in user_ips)
        if user_id in purchasers
    }
    counts = {}
    for click in ad_clicks:
        ip, _timestamp, ad = click.split(",", 2)
        purchasing, total = counts.setdefault(ad, [0, 0])
        counts[ad] = [purchasing + (ip in purchaser_ips), total + 1]
    return {ad: tuple(values) for ad, values in counts.items()}
```

### Complexity

For `u` user-IP records and `k` clicks, time is `O(u + k)` and space is
`O(u + a)`, where `a` is the number of ads.

## `passable_lanes`

### Question

Return every row and column containing only open (`"0"`) cells.

### Example and clarification

For a one-cell board, `[["0"]]` returns `([0], [0])`; `[["+"]]` returns
`([], [])`. Indices must be increasing.

### Approach

Scan each row with `all`, then scan each column by checking that coordinate in
every row.

### Complete Python solution

```python
def passable_lanes(board: list[list[str]]) -> tuple[list[int], list[int]]:
    if not board or not board[0]:
        return ([], [])
    rows = [
        index for index, row in enumerate(board)
        if all(cell == "0" for cell in row)
    ]
    columns = [
        column
        for column in range(len(board[0]))
        if all(board[row][column] == "0" for row in range(len(board)))
    ]
    return rows, columns
```

### Complexity

For `r` rows and `c` columns, time is `O(rc)` and auxiliary space is
`O(r + c)` for the returned indices.

## `nearest_exit`

### Question

From a starting open cell, find the closest reachable open cell on a different
boundary side.

### Example and clarification

Move only up, down, left, or right. The side containing the entrance is not an
exit side; a corner entrance excludes both of its sides. If two exits have the
same distance, choose the lower row, then lower column.

### Approach

Record the entrance's boundary sides. Breadth-first search visits cells by
shortest distance. Gather valid exits at the first exit distance, then choose
the smallest coordinate.

### Complete Python solution

```python
from collections import deque

def nearest_exit(grid, start_row, start_column):
    if not grid or not grid[0] or grid[start_row][start_column] != "0":
        return [-1, -1]
    rows, columns = len(grid), len(grid[0])
    entrance_sides = set()
    if start_row == 0:
        entrance_sides.add("top")
    if start_row == rows - 1:
        entrance_sides.add("bottom")
    if start_column == 0:
        entrance_sides.add("left")
    if start_column == columns - 1:
        entrance_sides.add("right")

    def is_exit(row, column):
        return (
            (row == 0 and "top" not in entrance_sides)
            or (row == rows - 1 and "bottom" not in entrance_sides)
            or (column == 0 and "left" not in entrance_sides)
            or (column == columns - 1 and "right" not in entrance_sides)
        )

    queue = deque([(start_row, start_column, 0)])
    visited = {(start_row, start_column)}
    best_distance, exits = None, []

    while queue:
        row, column, distance = queue.popleft()
        if best_distance is not None and distance > best_distance:
            break
        if is_exit(row, column):
            best_distance = distance
            exits.append((row, column))
            continue
        for row_delta, column_delta in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            next_cell = (row + row_delta, column + column_delta)
            next_row, next_column = next_cell
            if (
                0 <= next_row < rows
                and 0 <= next_column < columns
                and next_cell not in visited
                and grid[next_row][next_column] == "0"
            ):
                visited.add(next_cell)
                queue.append((next_row, next_column, distance + 1))
    return list(min(exits)) if exits else [-1, -1]
```

### Complexity

Time and space are both `O(rc)` because each cell enters the queue at most
once.

## `nest_entrance_counts`

### Question

For each connected region of open cells, count how many of its cells touch the
board boundary.

### Example and clarification

An enclosed open region has count zero and must still be returned. A fully
open 2-by-2 board is one region with four boundary cells, so it returns `[4]`.

### Approach

Start a DFS whenever an unvisited open cell is found. Count cells on the
boundary during that component traversal, then sort all component counts.

### Complete Python solution

```python
def nest_entrance_counts(board: list[list[str]]) -> list[int]:
    if not board or not board[0]:
        return []
    rows, columns = len(board), len(board[0])
    visited, counts = set(), []

    for start_row in range(rows):
        for start_column in range(columns):
            start = (start_row, start_column)
            if board[start_row][start_column] != "0" or start in visited:
                continue
            entrances, stack = 0, [start]
            visited.add(start)
            while stack:
                row, column = stack.pop()
                if row in (0, rows - 1) or column in (0, columns - 1):
                    entrances += 1
                for row_delta, column_delta in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                    next_cell = (row + row_delta, column + column_delta)
                    next_row, next_column = next_cell
                    if (
                        0 <= next_row < rows
                        and 0 <= next_column < columns
                        and next_cell not in visited
                        and board[next_row][next_column] == "0"
                    ):
                        visited.add(next_cell)
                        stack.append(next_cell)
            counts.append(entrances)
    return sorted(counts)
```

### Complexity

Traversal takes `O(rc)` time and `O(rc)` space. Sorting `q` component counts
adds `O(q log q)` time.

## `find_story_ending`

### Question

Starting at page 1, repeatedly choose one fixed option at every choice page.
Return the ending reached.

### Example and clarification

Ordinary pages advance to the next number. If following the selected option
revisits a page, return `-1` because the story loops.

### Approach

Map choice pages to their two targets. Simulate reading while storing visited
pages, stopping at either an ending or a repeated page.

### Complete Python solution

```python
def find_story_ending(endings, choices, option):
    terminal = set(endings)
    choice_by_page = {
        page: (option_one, option_two)
        for page, option_one, option_two in choices
    }
    visited, page = set(), 1
    while page not in terminal:
        if page in visited:
            return -1
        visited.add(page)
        page = choice_by_page.get(page, (page + 1, page + 1))[option - 1]
    return page
```

### Complexity

For `n` represented pages, time and space are `O(n)`.

## `find_good_story_endings`

### Question

Find every good ending reachable from page 1 when both options may be taken.

### Example and clarification

Good and bad endings are terminal. A branch entering a loop must not prevent
other branches from reaching good endings. Return sorted unique page numbers.

### Approach

Treat pages as graph nodes. DFS from page 1, expanding a choice into two
targets and an ordinary page into `page + 1`. A visited set handles cycles.

### Complete Python solution

```python
def find_good_story_endings(good_endings, bad_endings, choices):
    good = set(good_endings)
    terminal = good | set(bad_endings)
    choice_by_page = {
        page: (option_one, option_two)
        for page, option_one, option_two in choices
    }
    all_targets = {
        target for targets in choice_by_page.values() for target in targets
    }
    highest_known = max(terminal | set(choice_by_page) | all_targets, default=1)
    reachable_good, visited, stack = set(), set(), [1]

    while stack:
        page = stack.pop()
        if page in visited:
            continue
        visited.add(page)
        if page in good:
            reachable_good.add(page)
        elif page in terminal or page > highest_known:
            continue
        elif page in choice_by_page:
            stack.extend(choice_by_page[page])
        else:
            stack.append(page + 1)
    return sorted(reachable_good)
```

### Complexity

For `n` relevant pages and choice edges, time and space are `O(n)`.

## `shopping_savings`

### Question

How many department visits are saved by regrouping a shopping list by
department?

### Example and clarification

The original visit count is the number of contiguous department runs. The
grouped count is the number of distinct departments. An empty list saves zero.

### Approach

Map products to departments, count transitions in shopping-list order, and
subtract the number of unique departments.

### Complete Python solution

```python
def shopping_savings(products, shopping_list):
    if not shopping_list:
        return 0
    department_by_product = {
        product: department for product, department in products
    }
    departments = [
        department_by_product[product] for product in shopping_list
    ]
    original_visits = 1 + sum(
        current != previous
        for previous, current in zip(departments, departments[1:])
    )
    return original_visits - len(set(departments))
```

### Complexity

For `p` products and `n` shopping-list items, time is `O(p + n)` and space is
`O(p + n)`.

## `carpool`

### Question

Two cars follow fixed road chains. Assign each person to the car that reaches
their location first.

### Example and clarification

Cars leave together. Road times are strings but represent minutes. Preserve
car order and person order; omit unreachable people. Either car is valid for
a tie, and this solution consistently picks the earlier car.

### Approach

For each car, walk its route once and record cumulative arrival times. For
each person, compare the available arrival times and append the name to the
best car's list.

### Complete Python solution

```python
def carpool(roads, starts, people):
    next_road = {
        origin: (destination, int(minutes))
        for origin, destination, minutes in roads
    }
    arrival_times = []
    for start in starts:
        times, location, elapsed, visited = {start: 0}, start, 0, {start}
        while location in next_road:
            destination, minutes = next_road[location]
            if destination in visited:
                break
            elapsed += minutes
            times[destination] = elapsed
            visited.add(destination)
            location = destination
        arrival_times.append(times)

    assignments = [[] for _ in starts]
    for person, location in people:
        candidates = [
            (times[location], car_index)
            for car_index, times in enumerate(arrival_times)
            if location in times
        ]
        if candidates:
            _arrival, car_index = min(candidates)
            assignments[car_index].append(person)
    return assignments
```

### Complexity

For `r` reachable road steps across cars, `p` people, and `k` cars, time is
`O(r + pk)` and space is `O(r + p)`.


---

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


---

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


---

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
