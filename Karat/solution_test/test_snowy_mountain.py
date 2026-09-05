"""Tests for the Snowy Mountain interview question."""

import unittest

from solutions.snowy_mountain import best_day_to_cross


class SnowyMountainTest(unittest.TestCase):
    def test_finds_best_forecast_day(self):
        altitudes = [0, 1, 2, 1]
        snow = [[1, 0, 1, 0], [0, 0, 0, 0], [1, 1, 0, 2]]
        self.assertEqual([2, 1], best_day_to_cross(altitudes, snow))


if __name__ == "__main__":
    unittest.main()
