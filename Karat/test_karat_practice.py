import unittest

from karat_practice import (
    aggregate_domain_visits,
    find_zero_rectangle,
    frequent_badge_access,
    nearest_exit,
    reachable_good_endings,
    shared_courses,
)


class BadgeAccessTest(unittest.TestCase):
    def test_finds_first_qualifying_window_in_unsorted_input(self):
        records = [
            ["Paul", "1415"],
            ["John", "0830"],
            ["Paul", "1315"],
            ["Paul", "1355"],
            ["John", "0931"],
            ["Paul", "1405"],
            ["John", "0900"],
        ]
        self.assertEqual(
            {"Paul": [1315, 1355, 1405, 1415]},
            frequent_badge_access(records),
        )

    def test_sixty_minute_boundary_is_inclusive(self):
        records = [["Alex", "1000"], ["Alex", "1030"], ["Alex", "1100"]]
        self.assertEqual(
            {"Alex": [1000, 1030, 1100]},
            frequent_badge_access(records),
        )

    def test_converts_hhmm_before_comparing_minutes(self):
        records = [
            ["Maya", "0950"],
            ["Maya", "1010"],
            ["Maya", "1045"],
            ["Noah", "1200"],
            ["Noah", "1301"],
            ["Noah", "1402"],
        ]
        self.assertEqual(
            {"Maya": [950, 1010, 1045]},
            frequent_badge_access(records),
        )


class DomainVisitsTest(unittest.TestCase):
    def test_aggregates_all_parent_domains(self):
        visits = [
            "900 discuss.leetcode.com",
            "50 leetcode.com",
            "1 com",
            "5 mail.google.com",
        ]
        self.assertEqual(
            {
                "discuss.leetcode.com": 900,
                "leetcode.com": 950,
                "mail.google.com": 5,
                "google.com": 5,
                "com": 956,
            },
            aggregate_domain_visits(visits),
        )

    def test_supports_single_component_domain(self):
        self.assertEqual({"localhost": 7}, aggregate_domain_visits(["7 localhost"]))

    def test_supports_original_pdf_comma_format(self):
        self.assertEqual(
            {"mail.yahoo.com": 60, "yahoo.com": 60, "com": 60},
            aggregate_domain_visits(["60,mail.yahoo.com"]),
        )

    def test_empty_input(self):
        self.assertEqual({}, aggregate_domain_visits([]))


class SharedCoursesTest(unittest.TestCase):
    def test_includes_every_student_pair(self):
        enrollments = [
            ["58", "Software Design"],
            ["58", "Linear Algebra"],
            ["94", "Art History"],
            ["94", "Software Design"],
            ["17", "Software Design"],
            ["17", "Political Science"],
        ]
        self.assertEqual(
            {
                "17,58": ["Software Design"],
                "17,94": ["Software Design"],
                "58,94": ["Software Design"],
            },
            shared_courses(enrollments),
        )

    def test_includes_pairs_with_no_overlap_and_removes_duplicates(self):
        enrollments = [
            ["A", "Math"],
            ["A", "Math"],
            ["A", "Art"],
            ["B", "Math"],
            ["B", "Art"],
            ["C", "Biology"],
        ]
        self.assertEqual(
            {
                "A,B": ["Art", "Math"],
                "A,C": [],
                "B,C": [],
            },
            shared_courses(enrollments),
        )


class ZeroRectangleTest(unittest.TestCase):
    def test_rectangle_in_middle(self):
        matrix = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]
        self.assertEqual([1, 1, 2, 3], find_zero_rectangle(matrix))

    def test_single_cell_at_boundary(self):
        self.assertEqual([0, 2, 0, 2], find_zero_rectangle([[1, 1, 0]]))

    def test_rectangle_reaches_bottom_right(self):
        matrix = [[1, 1, 1], [1, 0, 0], [1, 0, 0]]
        self.assertEqual([1, 1, 2, 2], find_zero_rectangle(matrix))


class StorybookTest(unittest.TestCase):
    def test_returns_all_reachable_good_endings(self):
        choices = {
            1: [2, 3],
            2: [4],
            3: [5, 6],
            6: [3, 7],  # cycle back to 3
        }
        self.assertEqual(
            {4, 7},
            reachable_good_endings(choices, 1, {4, 7, 99}, {5}),
        )

    def test_start_page_can_be_an_ending(self):
        self.assertEqual(
            {8},
            reachable_good_endings({8: [9]}, 8, {8}, {9}),
        )

    def test_unreachable_good_endings_are_omitted(self):
        self.assertEqual(
            set(),
            reachable_good_endings({1: [2]}, 1, {10}, {2}),
        )


class NearestExitTest(unittest.TestCase):
    def test_finds_shortest_exit(self):
        grid = [
            list("0+++0"),
            list("000+0"),
            list("+0000"),
            list("++++0"),
        ]
        self.assertEqual([2, 4], nearest_exit(grid, 0, 0))

    def test_breaks_distance_tie_by_coordinate(self):
        grid = [
            list("+0+"),
            list("00+"),
            list("+0+"),
        ]
        self.assertEqual([0, 1], nearest_exit(grid, 1, 0))

    def test_returns_negative_one_when_trapped(self):
        grid = [
            list("0++"),
            list("+++"),
            list("++0"),
        ]
        self.assertEqual([-1, -1], nearest_exit(grid, 0, 0))


if __name__ == "__main__":
    unittest.main()
