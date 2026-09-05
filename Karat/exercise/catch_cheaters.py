"""Catch Cheaters practice questions.

Implement one part at a time, then run its focused tests.
"""

from __future__ import annotations


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

    def search(row, column, index, path):
        if (
            row >= len(grid)
            or column >= len(grid[row])
            or grid[row][column] != word[index]
        ):
            return None

        path.append((row, column))

        if index == len(word) - 1:
            return path[:]

        result = search(row, column + 1, index + 1, path)
        if result is not None:
            return result

        result = search(row + 1, column, index + 1, path)
        if result is not None:
            return result

        path.pop()
        return None

    for row in range(len(grid)):
        for column in range(len(grid[row])):
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
    def all_paths(word, used):
        found = []

        def search(row, column, index, path):
            cell = (row, column)
            if (
                row >= len(grid)
                or column >= len(grid[row])
                or cell in used
                or grid[row][column] != word[index]
            ):
                return

            path.append(cell)

            if index == len(word) - 1:
                found.append(path[:])
            else:
                search(row, column + 1, index + 1, path)
                search(row + 1, column, index + 1, path)

            path.pop()

        if not word:
            return [[]]

        for row in range(len(grid)):
            for column in range(len(grid[row])):
                search(row, column, 0, [])
        return found

    answer = []

    def assign(index, used):
        if index == len(words):
            return True

        for path in all_paths(words[index], used):
            answer.append(path)
            if assign(index + 1, used | set(path)):
                return True
            answer.pop()

        return False

    if assign(0, set()):
        return answer
    return None
