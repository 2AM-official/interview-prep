"""Puzzle Checker practice questions.

Implement one part at a time, then run its focused tests.
"""

from __future__ import annotations


def is_valid_matrix(matrix: list[list[int]]) -> bool:
    """Check whether every row and column contains exactly 1 through N.

    The input must be an ``N x N`` matrix. Duplicates, missing values,
    out-of-range values, and non-square input are invalid.

    Complexity variable: ``n`` rows and columns.
    """
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


def validate_nonogram(
    matrix: list[list[int]],
    row_instructions: list[list[int]],
    column_instructions: list[list[int]],
) -> bool:
    """Validate every ordered run of black (0) cells in rows and columns."""
    height = len(matrix)
    width = len(matrix[0]) if matrix else 0
    if (
        len(row_instructions) != height
        or len(column_instructions) != width
        or any(len(row) != width for row in matrix)
    ):
        return False

    def zero_runs(line):
        runs = []
        length = 0
        for cell in line:
            if cell == 0:
                length += 1
            elif length:
                runs.append(length)
                length = 0
        if length:
            runs.append(length)
        return runs

    for i in range(height):
        if zero_runs(matrix[i]) != row_instructions[i]:
            return False

    for column in range(width):
        column_cells = []
        for row in range(height):
            column_cells.append(matrix[row][column])
        if zero_runs(column_cells) != column_instructions[column]:
            return False
    return True
