"""Starter functions for Karat-style mock interviews."""
import collections


def frequent_badge_access(records: list[list[str]]) -> dict[str, list[int]]:
    """Find employees with at least three badge uses in a 60-minute window.

    Each record is ``[employee_name, time]``. Times are zero-padded 24-hour
    ``HHMM`` strings, and records are not ordered.

    For each qualifying employee, return every time in their first qualifying
    inclusive 60-minute window, sorted as integer HHMM values. Omit employees
    who do not qualify.

    Example:
        [["Paul", "1315"], ["Paul", "1355"], ["Paul", "1405"]]
        -> {"Paul": [1315, 1355, 1405]}

    State time and space complexity in terms of r, the number of records.
    """
    employee_times = collections.defaultdict(list)
    result = collections.defaultdict(list)

    for employee, time in records:
        employee_times[employee].append(int(time))
    for employee, times in employee_times.items():
        times.sort()
        for i in range(len(times)):
            if i + 2 < len(times) and times[i + 2] - times[i] <= 100:
                result[employee].append(times[i])
                result[employee].append(times[i + 1])
                result[employee].append(times[i + 2])
                j = i + 3
                while j < len(times) and times[j] - times[i] <= 100:
                    result[employee].append(times[j])
                    j += 1
                break
    return result



def aggregate_domain_visits(visits: list[str]) -> dict[str, int]:
    """Aggregate visits for each domain and all of its parent domains.

    Each input has the form ``"<count> <domain>"`` or the PDF's original
    ``"<count>,<domain>"``. For example, ``"900 discuss.leetcode.com"`` adds
    900 visits to
    ``discuss.leetcode.com``, ``leetcode.com``, and ``com``.

    State complexity in terms of n entries and p total domain components.
    """
    result = collections.defaultdict(int)
    for visit in visits:
        count, domain = visit.replace(",", " ", 1).split()
        count = int(count)
        domains = domain.split('.')
        for i in range(len(domains)):
            result['.'.join(domains[i:])] += count
    return result


def shared_courses(enrollments: list[list[str]]) -> dict[str, list[str]]:
    """Return shared courses for every unordered pair of students.

    Each enrollment is ``[student_id, course_name]``. Include pairs with no
    shared courses. A pair key is ``"smaller_id,larger_id"`` using
    lexicographic order. Course lists are sorted and contain no duplicates.

    State complexity in terms of s students and e enrollments.
    """
    student_courses = collections.defaultdict(set)

    for student, course in enrollments:
        student_courses[student].add(course)
    
    students = sorted(student_courses.keys())
    result = collections.defaultdict(list)

    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            result[students[i] + ',' + students[j]] = sorted(student_courses[students[i]] & student_courses[students[j]])
    return result


def find_zero_rectangle(matrix: list[list[int]]) -> list[int]:
    """Locate the one solid rectangle of zeroes in a binary matrix.

    Every cell outside the rectangle is 1. Return inclusive coordinates as
    ``[top_row, left_column, bottom_row, right_column]``.

    State complexity in terms of rows and columns.
    """
    if not matrix or not matrix[0]:
        return [-1, -1, -1, -1]

    rows = len(matrix)
    cols = len(matrix[0])
    
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                bottom = row
                right = col

                while bottom + 1 < rows and matrix[bottom + 1][col] == 0:
                    bottom += 1

                while right + 1 < cols and matrix[row][right + 1] == 0:
                    right += 1

                return [row, col, bottom, right]

    return [-1, -1, -1, -1]



def reachable_good_endings(
    choices: dict[int, list[int]],
    start_page: int,
    good_endings: set[int],
    bad_endings: set[int],
) -> set[int]:
    """Return all good terminal pages reachable from ``start_page``.

    ``choices`` maps a page to the pages a reader may choose next. The graph
    may branch, converge, and contain cycles. Good and bad endings are
    terminal, even if malformed input gives one of them outgoing choices.

    State complexity in terms of reachable pages and choices.
    """
    visited = set()

    queue = collections.deque([start_page])
    visited.add(start_page)

    while queue:
        page = queue.popleft()
        if page in good_endings or page in bad_endings:
            continue
            
        for next_page in choices[page]:
            if next_page in visited:
                continue
            visited.add(next_page)
            queue.append(next_page)
    
    return visited & good_endings
    


def nearest_exit(
    grid: list[list[str]], start_row: int, start_column: int
) -> list[int]:
    """Find the nearest passable boundary cell other than the start.

    ``"0"`` is passable and ``"+"`` is blocked. Movement is allowed up, down,
    left, and right. Return ``[row, column]``, or ``[-1, -1]`` when no exit is
    reachable. Break distance ties by lowest row, then lowest column.

    State complexity in terms of rows and columns.
    """
    if not grid or not grid[0] or grid[start_row][start_column] != "0":
        return [-1, -1]

    rows = len(grid)
    cols = len(grid[0])
    entrance_sides = set()
    if start_row == 0:
        entrance_sides.add("top")
    if start_row == rows - 1:
        entrance_sides.add("bottom")
    if start_column == 0:
        entrance_sides.add("left")
    if start_column == cols - 1:
        entrance_sides.add("right")

    def is_exit(row, col):
        return (
            (row == 0 and "top" not in entrance_sides)
            or (row == rows - 1 and "bottom" not in entrance_sides)
            or (col == 0 and "left" not in entrance_sides)
            or (col == cols - 1 and "right" not in entrance_sides)
        )

    queue = collections.deque([(start_row, start_column, 0)])
    visited = {(start_row, start_column)}
    best_distance = None
    exits = []

    while queue:
        row, col, distance = queue.popleft()
        if best_distance is not None and distance > best_distance:
            break
        if is_exit(row, col):
            best_distance = distance
            exits.append((row, col))
            continue

        for dr, dc in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            new_row = row + dr
            new_col = col + dc
            if (
                0 <= new_row < rows
                and 0 <= new_col < cols
                and (new_row, new_col) not in visited
                and grid[new_row][new_col] == "0"
            ):
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, distance + 1))

    return list(min(exits)) if exits else [-1, -1]
