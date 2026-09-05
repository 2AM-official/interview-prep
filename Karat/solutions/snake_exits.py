"""Reference solutions for the snake-board exit exercises."""

from __future__ import annotations

from collections import deque


def passable_lanes(board: list[list[str]]) -> tuple[list[int], list[int]]:
    """Return the indices of completely passable rows and columns."""
    if not board or not board[0]:
        return ([], [])

    rows = [
        row_index
        for row_index, row in enumerate(board)
        if all(cell == "0" for cell in row)
    ]
    columns = [
        column
        for column in range(len(board[0]))
        if all(board[row][column] == "0" for row in range(len(board)))
    ]
    return rows, columns


def nearest_exit(
    grid: list[list[str]], start_row: int, start_column: int
) -> list[int]:
    """Return the nearest reachable exit on a different boundary side.

    A boundary side containing the entrance is excluded; a corner entrance
    therefore excludes both of its sides. Distance ties are broken by row and
    then column.
    """
    if not grid or not grid[0] or grid[start_row][start_column] != "0":
        return [-1, -1]

    row_count, column_count = len(grid), len(grid[0])
    entrance_sides = set()
    if start_row == 0:
        entrance_sides.add("top")
    if start_row == row_count - 1:
        entrance_sides.add("bottom")
    if start_column == 0:
        entrance_sides.add("left")
    if start_column == column_count - 1:
        entrance_sides.add("right")

    def is_exit(row: int, column: int) -> bool:
        return (
            (row == 0 and "top" not in entrance_sides)
            or (row == row_count - 1 and "bottom" not in entrance_sides)
            or (column == 0 and "left" not in entrance_sides)
            or (column == column_count - 1 and "right" not in entrance_sides)
        )

    queue = deque([(start_row, start_column, 0)])
    visited = {(start_row, start_column)}
    best_distance: int | None = None
    exits: list[tuple[int, int]] = []

    while queue:
        row, column, distance = queue.popleft()
        if best_distance is not None and distance > best_distance:
            break
        if is_exit(row, column):
            best_distance = distance
            exits.append((row, column))
            continue

        for row_delta, column_delta in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            next_row = row + row_delta
            next_column = column + column_delta
            next_cell = (next_row, next_column)
            if (
                0 <= next_row < row_count
                and 0 <= next_column < column_count
                and next_cell not in visited
                and grid[next_row][next_column] == "0"
            ):
                visited.add(next_cell)
                queue.append((next_row, next_column, distance + 1))

    return list(min(exits)) if exits else [-1, -1]


def nest_entrance_counts(board: list[list[str]]) -> list[int]:
    """Return sorted boundary-cell counts for all open components."""
    if not board or not board[0]:
        return []

    row_count, column_count = len(board), len(board[0])
    visited: set[tuple[int, int]] = set()
    counts: list[int] = []

    for start_row in range(row_count):
        for start_column in range(column_count):
            start = (start_row, start_column)
            if board[start_row][start_column] != "0" or start in visited:
                continue

            entrances = 0
            stack = [start]
            visited.add(start)
            while stack:
                row, column = stack.pop()
                if row in (0, row_count - 1) or column in (0, column_count - 1):
                    entrances += 1
                for row_delta, column_delta in ((-1, 0), (0, -1), (0, 1), (1, 0)):
                    next_row = row + row_delta
                    next_column = column + column_delta
                    next_cell = (next_row, next_column)
                    if (
                        0 <= next_row < row_count
                        and 0 <= next_column < column_count
                        and next_cell not in visited
                        and board[next_row][next_column] == "0"
                    ):
                        visited.add(next_cell)
                        stack.append(next_cell)
            counts.append(entrances)

    return sorted(counts)
