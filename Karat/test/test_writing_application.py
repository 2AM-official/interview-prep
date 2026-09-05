"""Tests for the Writing Application interview questions."""

import unittest

from exercise.writing_application import reflow_and_justify, wrap_lines


class WrapLinesTest(unittest.TestCase):
    def test_greedily_wraps_words(self):
        words = [
            "The",
            "day",
            "began",
            "as",
            "still",
            "as",
            "the",
            "night",
            "abruptly",
            "lighted",
            "with",
            "brilliant",
            "flame",
        ]
        self.assertEqual(
            [
                "The-day-began",
                "as-still-as",
                "the-night",
                "abruptly",
                "lighted-with",
                "brilliant",
                "flame",
            ],
            wrap_lines(words, 13),
        )

    def test_exact_fit_and_empty_input(self):
        self.assertEqual(["Hello"], wrap_lines(["Hello"], 5))
        self.assertEqual([], wrap_lines([], 10))


class ReflowAndJustifyTest(unittest.TestCase):
    lines = [
        "The day began as still as the",
        "night abruptly lighted with",
        "brilliant flame",
    ]

    def test_reflows_and_justifies(self):
        self.assertEqual(
            [
                "The--day--began-as-still",
                "as--the--night--abruptly",
                "lighted--with--brilliant",
                "flame",
            ],
            reflow_and_justify(self.lines, 24),
        )


if __name__ == "__main__":
    unittest.main()
