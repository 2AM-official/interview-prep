"""Tests for the Thrilling Teleporters interview questions."""

import unittest

from solutions.thrilling_teleporters import is_finishable, teleporter_destinations


class TeleporterDestinationsTest(unittest.TestCase):
    def test_follows_one_teleporter_and_removes_duplicates(self):
        teleporters = ["3,1", "4,2", "5,10"]
        self.assertEqual(
            [1, 2, 10, 6],
            teleporter_destinations(teleporters, 6, 0, 20),
        )

    def test_stops_at_last_square(self):
        teleporters = ["6,18", "49,55", "92,85"]
        self.assertEqual(
            [96, 97, 98, 99, 100],
            teleporter_destinations(teleporters, 10, 95, 100),
        )


class FinishableTeleportersTest(unittest.TestCase):
    def test_detects_barrier_and_escape(self):
        blocked = ["10,8", "11,5", "12,7", "13,9"]
        self.assertFalse(is_finishable(blocked, 4, 0, 20))
        self.assertTrue(is_finishable(blocked + ["2,15"], 4, 0, 20))
        self.assertFalse(is_finishable(blocked + ["2,15"], 4, 9, 20))


if __name__ == "__main__":
    unittest.main()
