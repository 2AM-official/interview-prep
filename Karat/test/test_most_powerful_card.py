"""Tests for the Most Powerful Card interview question."""

import unittest

from exercise.most_powerful_card import most_powerful_card


class MostPowerfulCardTest(unittest.TestCase):
    def test_counts_transitive_wins(self):
        matchups = [
            ["giant", "wizard"],
            ["giant", "nymph"],
            ["wizard", "elf"],
            ["nymph", "muse"],
            ["orc", "elf"],
            ["orc", "goblin"],
            ["orc", "snake"],
        ]
        self.assertEqual("giant", most_powerful_card(matchups))


if __name__ == "__main__":
    unittest.main()
