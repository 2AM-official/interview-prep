"""Tests for the Resource Access Log interview question."""

import unittest

from exercise.resource_access_log import (
    build_transition_graph,
    most_requested_resource,
    user_access_ranges,
)


class AccessRangesTest(unittest.TestCase):
    def test_finds_minimum_and_maximum_per_user(self):
        logs = [
            ["100", "u1", "r1"],
            ["50", "u1", "r2"],
            ["75", "u2", "r1"],
        ]
        self.assertEqual(
            {"u1": (50, 100), "u2": (75, 75)},
            user_access_ranges(logs),
        )


class MostRequestedResourceTest(unittest.TestCase):
    def test_finds_busiest_five_minute_window(self):
        logs = [
            ["53760", "user_3", "resource_3"],
            ["54001", "user_1", "resource_3"],
            ["54060", "user_2", "resource_3"],
            ["62314", "user_2", "resource_2"],
        ]
        self.assertEqual(
            ("resource_3", 3),
            most_requested_resource(logs),
        )


class TransitionGraphTest(unittest.TestCase):
    def test_adds_start_self_transitions_and_end(self):
        logs = [
            [str(time), "user_1", "resource_3"]
            for time in [300, 599, 900, 1199, 1200, 1201, 1202]
        ]
        graph = build_transition_graph(logs)
        self.assertEqual({"resource_3": 1.0}, graph["START"])
        self.assertAlmostEqual(6 / 7, graph["resource_3"]["resource_3"])
        self.assertAlmostEqual(1 / 7, graph["resource_3"]["END"])


if __name__ == "__main__":
    unittest.main()
