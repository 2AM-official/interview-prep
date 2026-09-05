"""Reference solutions for the Puzzle Checker practice questions."""

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

    def zero_runs(line: list[int]) -> list[int]:
        runs: list[int] = []
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

    if any(zero_runs(row) != instruction for row, instruction in zip(matrix, row_instructions)):
        return False

    for column, instruction in enumerate(column_instructions):
        if zero_runs([matrix[row][column] for row in range(height)]) != instruction:
            return False
    return True
