"""Reference solutions for the Catch Cheaters practice questions."""

from __future__ import annotations

from collections import Counter


def find_scrambled_word(words: list[str], letters: str) -> str | None:
    """Return the one word whose letter multiset is contained in ``letters``.

    Letter order and adjacency do not matter, but each character occurrence
    may be used only once. At most one candidate matches. Return ``None`` when
    no word matches.

    Complexity variables: number of words and total characters.
    """
    available = Counter(letters)
    for word in words:
        if not (Counter(word) - available):
            return word
    return None


def find_word_location(
    grid: list[list[str]], word: str
) -> list[tuple[int, int]] | None:
    """Find one path spelling ``word`` using only right and down moves.

    The word may start anywhere. Return its coordinates in letter order, or
    ``None`` when no path exists. A single path cannot reuse a cell.
    """
    if not word:
        return []

    def search(
        row: int, column: int, index: int, path: list[tuple[int, int]]
    ) -> list[tuple[int, int]] | None:
        if (
            row < 0
            or row >= len(grid)
            or column < 0
            or column >= len(grid[row])
            or grid[row][column] != word[index]
        ):
            return None

        path.append((row, column))
        if index == len(word) - 1:
            return path.copy()

        for next_row, next_column in ((row, column + 1), (row + 1, column)):
            result = search(next_row, next_column, index + 1, path)
            if result is not None:
                return result
        path.pop()
        return None

    for row, cells in enumerate(grid):
        for column in range(len(cells)):
            result = search(row, column, 0, [])
            if result is not None:
                return result
    return None


def find_word_locations(
    grid: list[list[str]], words: list[str]
) -> list[list[tuple[int, int]]] | None:
    """Find right/down paths for all words without sharing cells.

    Return paths in input-word order. Choices must be globally compatible;
    return ``None`` if no complete assignment exists.
    """
    def candidate_paths(
        word: str, unavailable: set[tuple[int, int]]
    ) -> list[list[tuple[int, int]]]:
        if not word:
            return [[]]

        candidates: list[list[tuple[int, int]]] = []

        def search(
            row: int,
            column: int,
            index: int,
            path: list[tuple[int, int]],
        ) -> None:
            coordinate = (row, column)
            if (
                row < 0
                or row >= len(grid)
                or column < 0
                or column >= len(grid[row])
                or coordinate in unavailable
                or grid[row][column] != word[index]
            ):
                return

            path.append(coordinate)
            if index == len(word) - 1:
                candidates.append(path.copy())
            else:
                search(row, column + 1, index + 1, path)
                search(row + 1, column, index + 1, path)
            path.pop()

        for row, cells in enumerate(grid):
            for column in range(len(cells)):
                search(row, column, 0, [])
        return candidates

    assignment: list[list[tuple[int, int]]] = []

    def assign(index: int, used: set[tuple[int, int]]) -> bool:
        if index == len(words):
            return True
        for path in candidate_paths(words[index], used):
            assignment.append(path)
            if assign(index + 1, used | set(path)):
                return True
            assignment.pop()
        return False

    return assignment if assign(0, set()) else None
