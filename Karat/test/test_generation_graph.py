"""Tests for the Generation Graph interview questions."""

import unittest

from exercise.generation_graph import (
    find_earliest_ancestor,
    find_nodes_with_zero_or_one_parent,
    has_common_ancestor,
)


class ParentCountsTest(unittest.TestCase):
    def test_finds_zero_and_one_parent_nodes(self):
        pairs = [(1, 3), (2, 3), (4, 2), (4, 7)]
        self.assertEqual(
            ([1, 4], [2, 7]),
            find_nodes_with_zero_or_one_parent(pairs),
        )


class CommonAncestorTest(unittest.TestCase):
    pairs = [
        (1, 3),
        (2, 3),
        (3, 6),
        (5, 6),
        (5, 7),
        (4, 5),
        (4, 8),
    ]

    def test_detects_common_transitive_ancestor(self):
        self.assertTrue(has_common_ancestor(self.pairs, 5, 8))
        self.assertTrue(has_common_ancestor(self.pairs, 6, 5))
        self.assertFalse(has_common_ancestor(self.pairs, 3, 8))


class EarliestAncestorTest(unittest.TestCase):
    pairs = [
        (2, 3),
        (3, 15),
        (3, 6),
        (5, 6),
        (5, 7),
        (4, 5),
        (4, 8),
        (4, 9),
        (9, 11),
        (14, 4),
    ]

    def test_finds_farthest_ancestor(self):
        self.assertEqual(14, find_earliest_ancestor(self.pairs, 8))
        self.assertEqual(2, find_earliest_ancestor(self.pairs, 15))
        self.assertIsNone(find_earliest_ancestor(self.pairs, 14))


if __name__ == "__main__":
    unittest.main()
