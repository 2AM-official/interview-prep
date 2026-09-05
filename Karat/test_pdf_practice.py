import unittest

from pdf_practice import (
    curriculum_midpoints,
    find_scrambled_word,
    find_story_ending,
    is_complete_hand,
    is_valid_matrix,
    longest_common_subsequence,
    longest_contiguous_history,
    passable_lanes,
    shopping_savings,
    teleporter_destinations,
    wrap_lines,
)


class CurriculumMidpointsTest(unittest.TestCase):
    def test_branching_curriculum(self):
        prerequisites = [
            ["Logic", "COBOL"],
            ["Data Structures", "Algorithms"],
            ["Creative Writing", "Data Structures"],
            ["Algorithms", "COBOL"],
            ["Intro to Computer Science", "Data Structures"],
            ["Logic", "Compilers"],
            ["Data Structures", "Logic"],
            ["Graphics", "Networking"],
            ["Networking", "Algorithms"],
            ["Creative Writing", "System Administration"],
            ["Databases", "System Administration"],
            ["Creative Writing", "Databases"],
            ["Intro to Computer Science", "Graphics"],
        ]
        self.assertEqual(
            {"Creative Writing", "Data Structures", "Databases", "Networking"},
            set(curriculum_midpoints(prerequisites)),
        )

    def test_even_path_uses_earlier_middle(self):
        prerequisites = [["A", "B"], ["B", "C"], ["C", "D"]]
        self.assertEqual({"B"}, set(curriculum_midpoints(prerequisites)))


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


class ShoppingSavingsTest(unittest.TestCase):
    products = [
        ["Cheese", "Dairy"],
        ["Carrots", "Produce"],
        ["Potatoes", "Produce"],
        ["Canned Tuna", "Pantry"],
        ["Romaine Lettuce", "Produce"],
        ["Chocolate Milk", "Dairy"],
        ["Flour", "Pantry"],
        ["Iceberg Lettuce", "Produce"],
        ["Coffee", "Pantry"],
        ["Pasta", "Pantry"],
        ["Milk", "Dairy"],
        ["Blueberries", "Produce"],
        ["Pasta Sauce", "Pantry"],
    ]

    def test_saves_repeated_department_visits(self):
        shopping_list = [
            "Blueberries",
            "Milk",
            "Coffee",
            "Flour",
            "Cheese",
            "Carrots",
        ]
        self.assertEqual(2, shopping_savings(self.products, shopping_list))

    def test_already_grouped(self):
        shopping_list = [
            "Cheese",
            "Potatoes",
            "Blueberries",
            "Canned Tuna",
        ]
        self.assertEqual(0, shopping_savings(self.products, shopping_list))


class ScrambledWordTest(unittest.TestCase):
    words = ["cat", "baby", "dog", "bird", "car", "ax"]

    def test_finds_word_without_order_or_adjacency(self):
        self.assertEqual("cat", find_scrambled_word(self.words, "tcabnihjs"))
        self.assertEqual("baby", find_scrambled_word(self.words, "bbabylkkj"))

    def test_does_not_reuse_letters(self):
        self.assertIsNone(find_scrambled_word(self.words, "baykkjl"))
        self.assertIsNone(find_scrambled_word(self.words, "ccc"))


class ContiguousHistoryTest(unittest.TestCase):
    def test_finds_longest_shared_run(self):
        first = [
            "/start",
            "/green",
            "/blue",
            "/pink",
            "/register",
            "/orange",
            "/one/two",
        ]
        second = ["/start", "/pink", "/register", "/orange", "/red", "a"]
        self.assertEqual(
            ["/pink", "/register", "/orange"],
            longest_contiguous_history(first, second),
        )

    def test_empty_and_single_item_matches(self):
        self.assertEqual(
            [], longest_contiguous_history(["/start"], ["/different"])
        )
        self.assertEqual(["a"], longest_contiguous_history(["a"], ["x", "a"]))


class CommonSubsequenceTest(unittest.TestCase):
    def test_allows_gaps(self):
        self.assertEqual(
            ["a", "b", "c"],
            longest_common_subsequence(
                ["a", "b", "c"], ["a", "x", "b", "c"]
            ),
        )

    def test_empty_and_no_match(self):
        self.assertEqual([], longest_common_subsequence([], ["a"]))
        self.assertEqual(
            [], longest_common_subsequence(["a"], ["different"])
        )


class CompleteHandTest(unittest.TestCase):
    def test_valid_hands(self):
        for hand in ["88844", "99", "55555", "22333333"]:
            with self.subTest(hand=hand):
                self.assertTrue(is_complete_hand(hand))

    def test_invalid_hands(self):
        for hand in ["111333555", "42", "888", "100100000", "776655", "7"]:
            with self.subTest(hand=hand):
                self.assertFalse(is_complete_hand(hand))


class ValidMatrixTest(unittest.TestCase):
    def test_valid_matrix(self):
        matrix = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
        self.assertTrue(is_valid_matrix(matrix))

    def test_rejects_duplicates_and_non_square_input(self):
        self.assertFalse(is_valid_matrix([[1, 1], [2, 2]]))
        self.assertFalse(is_valid_matrix([[1, 2, 3], [2, 3, 1]]))


class PassableLanesTest(unittest.TestCase):
    def test_finds_rows_and_columns(self):
        board = [
            list("+++0+00"),
            list("00+0000"),
            list("0000+00"),
            list("+++00+0"),
            list("0000000"),
        ]
        self.assertEqual(([4], [3, 6]), passable_lanes(board))

    def test_single_passable_and_blocked_cells(self):
        self.assertEqual(([0], [0]), passable_lanes([["0"]]))
        self.assertEqual(([], []), passable_lanes([["+"]]))


class TeleporterDestinationsTest(unittest.TestCase):
    def test_follows_one_teleporter_and_removes_duplicates(self):
        teleporters = ["3,1", "4,2", "5,10"]
        self.assertEqual(
            [1, 2, 10, 6],
            teleporter_destinations(teleporters, 6, 0, 20),
        )

    def test_stops_at_last_square(self):
        teleporters = ["6,18", "49,55", "92,85"]
        self.assertEqual(
            [96, 97, 98, 99, 100],
            teleporter_destinations(teleporters, 10, 95, 100),
        )


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


if __name__ == "__main__":
    unittest.main()
