"""Additional Karat-style exercises adapted from the supplied PDF.

Every function intentionally starts unimplemented. Pick one topic, implement
it, and run only its focused tests through ``run_tests.py``.
"""

from __future__ import annotations

import collections


def curriculum_midpoints(prerequisites: list[list[str]]) -> list[str]:
    """Return every possible midpoint course on a root-to-leaf curriculum path.

    Each pair is ``[course, next_course]`` and the graph is a DAG. For a path
    with an even number of courses, use the earlier of the two middle courses.
    Return unique course names in any order.

    Complexity variables: ``n`` pairs and ``c`` distinct courses.
    """
    graph = collections.defaultdict(list)
    all_courses = set()
    destinations = set()

    for source, destination in prerequisites:
        graph[source].append(destination)
        all_courses.add(source)
        all_courses.add(destination)
        destinations.add(destination)

    roots = all_courses - destinations
    midpoints = set()

    def dfs(course, path):
        path.append(course)

        if course not in graph:
            midpoint_index = (len(path) - 1) // 2
            midpoints.add(path[midpoint_index])
        else:
            for next_course in graph[course]:
                dfs(next_course, path)

        path.pop()

    for root in roots:
        dfs(root, [])

    return list(midpoints)


def find_story_ending(
    endings: list[int], choices: list[list[int]], option: int
) -> int:
    """Follow one fixed option through a choose-your-own-adventure book.

    Reading starts at page 1. Normally the next page is ``page + 1``. Each
    choice is ``[page, option_1, option_2]``. Always select ``option`` (1 or 2).
    Return the ending reached, or ``-1`` if reading enters a loop.

    Complexity variable: ``n`` pages represented by endings and choices.
    """

    endings_set = set(endings)
    choices_dict = collections.defaultdict(list)

    for page, option_1, option_2 in choices:
        choices_dict[page].append(option_1)
        choices_dict[page].append(option_2)

    visited = set()
    page = 1

    while page not in endings_set:
        if page in visited: return -1

        visited.add(page)

        if page in choices_dict:
            page = choices_dict[page][option - 1]
        else:
            page += 1

    return page


def shopping_savings(
    products: list[list[str]], shopping_list: list[str]
) -> int:
    """Return department visits saved by grouping items by department.

    ``products`` contains ``[product, department]`` pairs. The original visit
    count is the number of contiguous department runs in ``shopping_list``.
    The optimized count is the number of distinct departments represented.

    Complexity variable: ``n`` products.
    """
    grouped = set()
    regular_visit = 0

    product_map = collections.defaultdict(str)

    for product, department in products:
        product_map[product] = department
    
    prev = ""
    
    for product in shopping_list:
        department = product_map[product]
        grouped.add(department)

        if regular_visit == 0:
            prev = department
            regular_visit += 1
        else:
            if department == prev:
                continue
            else:
                prev = department
                regular_visit += 1
        
    
    return regular_visit - len(grouped)
    


def find_scrambled_word(words: list[str], letters: str) -> str | None:
    """Return the one word whose letter multiset is contained in ``letters``.

    Letter order and adjacency do not matter, but each character occurrence
    may be used only once. At most one candidate matches. Return ``None`` when
    no word matches.

    Complexity variables: number of words and total characters.
    """
    bucket = [0]*26
    for l in letters:
        bucket[ord(l)-ord('a')] += 1
    
    for word in words:
        bucket_copy = bucket.copy()
        idx = 0
        while idx != len(word):
            if bucket_copy[ord(word[idx]) - ord('a')] == 0:
                break
            else:
                bucket_copy[ord(word[idx]) - ord('a')] -= 1
            idx += 1
        if idx == len(word):
            return word


def longest_contiguous_history(first: list[str], second: list[str]) -> list[str]:
    """Return the longest contiguous sequence shared by two browsing histories.

    If several sequences have the same maximum length, return the one that
    starts earliest in ``first``. Return an empty list when there is no match.

    Complexity variables: ``n`` and ``m`` history lengths.
    """
    
    dp = [[0] * (len(second)+1) for _ in range(len(first)+1)]

    best_length = 0
    best_start = 0

    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            if first[i-1] == second[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                current_length = dp[i][j]
                current_start = i - current_length

                if (
                    current_length > best_length
                    or (
                        current_length == best_length
                        and current_start < best_start
                    )
                ):
                    best_length = current_length
                    best_start = current_start
    
    return first[best_start : best_start + best_length]


def longest_common_subsequence(first: list[str], second: list[str]) -> list[str]:
    """Return one longest sequence that appears in order in both histories.

    Unlike a contiguous history, a subsequence may skip elements. If either
    history is empty or there are no shared elements, return an empty list.

    Complexity variables: ``n`` and ``m`` history lengths.
    """
    n, m = len(first), len(second)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if first[i - 1] == second[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    result = []
    i, j = n, m

    while i > 0 and j > 0:
        if first[i - 1] == second[j - 1]:
            result.append(first[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return result[::-1]



def is_complete_hand(tiles: str) -> bool:
    """Return whether all tiles form triples plus exactly one pair.

    Tiles are digits 0-9. There may be zero or more triples, and the pair may
    have the same digit as one of the triples. Every tile must be used.

    Complexity variable: ``n`` tiles.
    """
    counts = collections.Counter(tiles)
    found = False

    for count in counts.values():
        remain = count % 3

        if remain == 2:
            if found:
                return False
            found = True
        elif remain != 0:
            return False
    
    return found


def is_valid_matrix(matrix: list[list[int]]) -> bool:
    """Check whether every row and column contains exactly 1 through N.

    The input must be an ``N x N`` matrix. Duplicates, missing values,
    out-of-range values, and non-square input are invalid.

    Complexity variable: ``n`` rows and columns.
    """
    if not matrix: return False

    n = len(matrix)
    expected = set(range(1, n+1))

    for row in matrix:
        if len(row) != n or set(row) != expected:
            return False
    
    for col in range(n):
        values = [matrix[row][col] for row in range(n)]
        if set(values) != expected:
            return False
    return True


def passable_lanes(board: list[list[str]]) -> tuple[list[int], list[int]]:
    """Return completely passable rows and columns in a snake board.

    ``"0"`` is passable and ``"+"`` is blocked. Return
    ``(passable_rows, passable_columns)`` in increasing index order.

    Complexity variables: ``r`` rows and ``c`` columns.
    """
    row = len(board)
    col = len(board[0])

    row_result = []
    col_result = []

    for r in range(row):
        c = 0
        while c < col:
            if board[r][c] == "+":
                break
            c += 1
        if c == col:
            row_result.append(r)
    
    for c in range(col):
        r = 0
        while r < row:
            if board[r][c] == "+":
                break
            r += 1
        if r == row:
            col_result.append(c)
    
    return (row_result, col_result)



def teleporter_destinations(
    teleporters: list[str],
    die_sides: int,
    start: int,
    last_square: int,
) -> list[int]:
    """Return unique destinations possible after one die roll.

    Teleporters use ``"source,destination"`` format. Stop at ``last_square``
    when a roll reaches or passes it, and follow at most one teleporter per
    turn. Preserve first occurrence in die-roll order.

    Complexity variable: ``b`` board size.
    """
    if die_sides <= 0:
        return []

    teleporter_map = {}
    for teleporter in teleporters:
        source, destination = teleporter.split(",")
        teleporter_map[int(source)] = int(destination)

    destinations = []
    seen = set()
    for roll in range(1, die_sides + 1):
        landed = min(start + roll, last_square)
        if landed < last_square:
            landed = min(teleporter_map.get(landed, landed), last_square)
        if landed not in seen:
            seen.add(landed)
            destinations.append(landed)
    return destinations


def wrap_lines(words: list[str], max_width: int) -> list[str]:
    """Greedily wrap words using hyphens as visible spaces.

    Put as many words as possible on each line without exceeding
    ``max_width``. Input words individually fit within the width.

    Complexity variable: total number of characters.
    """
    wrapped = []
    current = []
    current_width = 0

    for word in words:
        added_width = len(word) + (1 if current else 0)
        if current and current_width + added_width > max_width:
            wrapped.append("-".join(current))
            current = [word]
            current_width = len(word)
        else:
            current.append(word)
            current_width += added_width

    if current:
        wrapped.append("-".join(current))
    return wrapped

