"""Tests for the Passage Tracker interview questions."""

import unittest

from exercise.passage_tracker import catch_speeders, count_journeys, parse_log_entry


class ParseLogEntryTest(unittest.TestCase):
    def test_parses_fields(self):
        self.assertEqual(
            (44776.619, "KTB918", 310, "EAST", "MAINROAD"),
            parse_log_entry("44776.619 KTB918 310E MAINROAD"),
        )


class JourneyCountTest(unittest.TestCase):
    def test_counts_complete_journeys(self):
        logs = [
            "90750.191 JOX304 250E ENTRY",
            "91081.684 JOX304 260E MAINROAD",
            "91483.251 JOX304 270E MAINROAD",
            "91874.493 JOX304 280E EXIT",
            "1000.000 ABC123 100W ENTRY",
            "1100.000 ABC123 90W EXIT",
        ]
        self.assertEqual(2, count_journeys(logs))


class CatchSpeedersTest(unittest.TestCase):
    def test_flags_fast_ten_kilometer_segment(self):
        logs = [
            "1000.000 TST002 270W ENTRY",
            "1275.000 TST002 260W EXIT",
        ]
        self.assertEqual(["TST002"], catch_speeders(logs))


if __name__ == "__main__":
    unittest.main()
