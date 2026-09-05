"""Tests for the Delivery Bot interview questions."""

import unittest

from solutions.delivery_bot import buildable_robots, delivery_destinations


class DeliveryDestinationsTest(unittest.TestCase):
    def test_maps_origins_to_terminal_locations(self):
        paths = [
            ["B", "K"],
            ["C", "K"],
            ["E", "L"],
            ["F", "G"],
            ["J", "M"],
            ["E", "F"],
            ["C", "G"],
            ["A", "B"],
            ["A", "C"],
            ["G", "H"],
            ["G", "I"],
        ]
        self.assertEqual(
            {"A": ["H", "I", "K"], "E": ["H", "I", "L"], "J": ["M"]},
            delivery_destinations(paths),
        )


class BuildableRobotsTest(unittest.TestCase):
    def test_filters_by_available_parts(self):
        required = [
            ["courier", ["wheel", "motor"]],
            ["scanner", ["sensor"]],
            ["drone", ["motor", "propeller"]],
        ]
        self.assertEqual(
            ["courier", "scanner"],
            buildable_robots(["wheel", "motor", "sensor"], required),
        )


if __name__ == "__main__":
    unittest.main()
