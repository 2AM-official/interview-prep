"""Solution tests for the snake-board exit exercises."""

import unittest

from solutions.snake_exits import nearest_exit, nest_entrance_counts, passable_lanes


class PassableLanesTest(unittest.TestCase):
    def test_finds_rows_and_columns(self):
        board = [
            list("+++0+00"),
            list("00+0000"),
            list("0000+00"),
            list("+++00+0"),
            list("0000000"),
        ]
        self.assertEqual(([4], [3, 6]), passable_lanes(board))

    def test_single_passable_and_blocked_cells(self):
        self.assertEqual(([0], [0]), passable_lanes([["0"]]))
        self.assertEqual(([], []), passable_lanes([["+"]]))


class NearestExitTest(unittest.TestCase):
    def test_finds_shortest_exit(self):
        grid = [
            list("0+++0"),
            list("000+0"),
            list("+0000"),
            list("++++0"),
        ]
        self.assertEqual([2, 4], nearest_exit(grid, 0, 0))

    def test_breaks_distance_tie_by_coordinate(self):
        grid = [list("+0+"), list("00+"), list("+0+")]
        self.assertEqual([0, 1], nearest_exit(grid, 1, 0))

    def test_returns_negative_one_when_trapped(self):
        grid = [list("0++"), list("+++"), list("++0")]
        self.assertEqual([-1, -1], nearest_exit(grid, 0, 0))


class NestEntrancesTest(unittest.TestCase):
    def test_enclosed_open_component(self):
        board = [list("+++"), list("+0+"), list("+++")]
        self.assertEqual([0], nest_entrance_counts(board))

    def test_all_open_and_all_blocked(self):
        self.assertEqual([4], nest_entrance_counts([list("00"), list("00")]))
        self.assertEqual([], nest_entrance_counts([["+"]]))


if __name__ == "__main__":
    unittest.main()
