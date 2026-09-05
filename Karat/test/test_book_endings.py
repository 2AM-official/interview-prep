"""Tests for choose-your-own-adventure ending exercises."""

import unittest

from exercise.book_endings import find_good_story_endings, find_story_ending


class StoryEndingTest(unittest.TestCase):
    def test_reaches_ending(self):
        endings = [6, 15, 21, 30]
        self.assertEqual(15, find_story_ending(endings, [[3, 14, 2]], 1))

    def test_detects_loop(self):
        endings = [6, 15, 21, 30]
        self.assertEqual(-1, find_story_ending(endings, [[3, 14, 2]], 2))

    def test_multiple_choices(self):
        choices = [
            [5, 11, 28],
            [9, 19, 29],
            [14, 16, 20],
            [18, 7, 22],
            [25, 6, 30],
        ]
        self.assertEqual(21, find_story_ending([6, 15, 21, 30], choices, 1))
        self.assertEqual(30, find_story_ending([6, 15, 21, 30], choices, 2))


class GoodStoryEndingsTest(unittest.TestCase):
    good = [10, 15, 25, 34]
    bad = [21, 30, 40]

    def test_finds_reachable_good_ending(self):
        self.assertEqual(
            [25],
            find_good_story_endings(self.good, self.bad, [[3, 16, 24]]),
        )

    def test_handles_loops_and_no_choices(self):
        self.assertEqual(
            [],
            find_good_story_endings(self.good, self.bad, [[3, 16, 20]]),
        )
        self.assertEqual(
            [34],
            find_good_story_endings(
                self.good,
                self.bad,
                [[3, 2, 19], [20, 21, 34]],
            ),
        )
        self.assertEqual(
            [10],
            find_good_story_endings(self.good, self.bad, []),
        )


if __name__ == "__main__":
    unittest.main()
