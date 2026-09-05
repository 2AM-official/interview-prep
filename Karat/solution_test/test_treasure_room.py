"""Tests for the Treasure Room interview question."""

import unittest

from solutions.treasure_room import (
    filter_treasure_leading_rooms,
    minimum_instructions,
)


class TreasureLeadingRoomsTest(unittest.TestCase):
    def test_filters_rooms(self):
        instructions = [
            ["jasmin", "tulip"],
            ["lily", "tulip"],
            ["tulip", "tulip"],
            ["rose", "rose"],
            ["violet", "rose"],
            ["sunflower", "violet"],
            ["daisy", "violet"],
            ["iris", "violet"],
        ]
        treasures = ["lily", "tulip", "violet", "rose"]
        self.assertEqual(
            ["tulip", "violet"],
            filter_treasure_leading_rooms(treasures, instructions),
        )


class MinimumInstructionsTest(unittest.TestCase):
    def test_follows_instructions_without_money(self):
        self.assertEqual(3, minimum_instructions([1, 1, 1, 9], 0))

    def test_can_pay_to_take_shorter_route(self):
        self.assertEqual(1, minimum_instructions([2, 1, 9], 1))


if __name__ == "__main__":
    unittest.main()
