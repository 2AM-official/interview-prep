"""Tests for the Cipher interview questions."""

import unittest

from exercise.cipher import encrypt_with_key, possible_decryptions, transpose_cipher


class TransposeCipherTest(unittest.TestCase):
    def test_transposes_message(self):
        self.assertEqual(
            "Oe y Mnss ioe iwnr nmatddoploootlk r",
            transpose_cipher("One does not simply walk into Mordor", 6, 6),
        )
        self.assertEqual(
            "11iwt. gas2gat!",
            transpose_cipher("1.21 gigawatts!", 5, 3),
        )


class KeyedEncryptionTest(unittest.TestCase):
    key = (
        "The quick onyx goblin, Grabbing his sword ==}-------- "
        "jumps over the 1st lazy dwarf!"
    )

    def test_preserves_case_and_punctuation(self):
        self.assertEqual(
            "Od ptw txx t qsutg.",
            encrypt_with_key("It was all a dream.", self.key),
        )
        self.assertEqual(
            "Pljxq zlj yobqxz?",
            encrypt_with_key("Would you kindly?", self.key),
        )


class PossibleDecryptionsTest(unittest.TestCase):
    dictionary = ["AXE", "CAT", "AT", "OR", "A", "COO", "CARD"]

    def test_matches_all_valid_tokenizations(self):
        self.assertEqual(
            {"AXE", "CAT", "AT", "OR"},
            set(possible_decryptions(self.dictionary, "123")),
        )
        self.assertEqual(
            {"COO", "AT", "OR"},
            set(possible_decryptions(self.dictionary, "122")),
        )
        self.assertEqual(
            {"AT", "OR"},
            set(possible_decryptions(self.dictionary, "102")),
        )


if __name__ == "__main__":
    unittest.main()
