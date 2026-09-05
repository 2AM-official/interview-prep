"""Tests for the Puzzle Checker interview questions."""

import unittest

from solutions.puzzle_checker import is_valid_matrix, validate_nonogram


class ValidMatrixTest(unittest.TestCase):
    def test_valid_matrix(self):
        matrix = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
        self.assertTrue(is_valid_matrix(matrix))

    def test_rejects_duplicates_and_non_square_input(self):
        self.assertFalse(is_valid_matrix([[1, 1], [2, 2]]))
        self.assertFalse(is_valid_matrix([[1, 2, 3], [2, 3, 1]]))


class NonogramTest(unittest.TestCase):
    def test_validates_ordered_zero_runs(self):
        matrix = [
            [1, 1, 1, 1],
            [0, 1, 1, 1],
            [0, 1, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 1, 1],
        ]
        rows = [[], [1], [1, 2], [1], [2]]
        columns = [[2, 1], [1], [2], [1]]
        self.assertTrue(validate_nonogram(matrix, rows, columns))
        self.assertFalse(
            validate_nonogram(matrix, [[], [], [1], [1], [1, 1]], columns)
        )


if __name__ == "__main__":
    unittest.main()
