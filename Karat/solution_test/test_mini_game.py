"""Tests for the Mini Game interview questions."""

import unittest

from solutions.mini_game import is_advanced_complete_hand, is_complete_hand


class CompleteHandTest(unittest.TestCase):
    def test_valid_hands(self):
        for hand in ["88844", "99", "55555", "22333333"]:
            with self.subTest(hand=hand):
                self.assertTrue(is_complete_hand(hand))

    def test_invalid_hands(self):
        for hand in ["111333555", "42", "888", "100100000", "776655", "7"]:
            with self.subTest(hand=hand):
                self.assertFalse(is_complete_hand(hand))


class AdvancedHandTest(unittest.TestCase):
    def test_valid_hands(self):
        for hand in ["11123", "12131", "11123455", "11122334", "99"]:
            with self.subTest(hand=hand):
                self.assertTrue(is_advanced_complete_hand(hand))

    def test_invalid_hands(self):
        for hand in ["123456", "1123456789", "00123457", "11890"]:
            with self.subTest(hand=hand):
                self.assertFalse(is_advanced_complete_hand(hand))


if __name__ == "__main__":
    unittest.main()
