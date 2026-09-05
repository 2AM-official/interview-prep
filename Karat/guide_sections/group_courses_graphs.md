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
