"""Tests for the Catch Cheaters interview questions."""

import unittest

from solutions.catch_cheaters import (
    find_scrambled_word,
    find_word_location,
    find_word_locations,
)


class ScrambledWordTest(unittest.TestCase):
    words = ["cat", "baby", "dog", "bird", "car", "ax"]

    def test_finds_word_without_order_or_adjacency(self):
        self.assertEqual("cat", find_scrambled_word(self.words, "tcabnihjs"))
        self.assertEqual("baby", find_scrambled_word(self.words, "bbabylkkj"))

    def test_does_not_reuse_letters(self):
        self.assertIsNone(find_scrambled_word(self.words, "baykkjl"))
        self.assertIsNone(find_scrambled_word(self.words, "ccc"))


class WordLocationTest(unittest.TestCase):
    grid = [
        list("ccxtib"),
        list("ccatni"),
        list("acnntt"),
        list("tcsipt"),
        list("aoooaa"),
        list("oaaaoo"),
        list("kaicki"),
    ]

    def test_finds_word_path(self):
        self.assertEqual(
            [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4)],
            find_word_location(self.grid, "catnip"),
        )

    def test_single_letter_and_no_match(self):
        self.assertEqual([(3, 2)], find_word_location(self.grid, "s"))
        self.assertIsNone(find_word_location(self.grid, "zebra"))


class MultipleWordLocationsTest(unittest.TestCase):
    def test_finds_disjoint_paths(self):
        grid = [list("bab"), list("yta"), list("xxt")]
        self.assertEqual(
            [
                [(0, 0), (1, 0)],
                [(0, 2), (1, 2), (2, 2)],
            ],
            find_word_locations(grid, ["by", "bat"]),
        )


if __name__ == "__main__":
    unittest.main()
