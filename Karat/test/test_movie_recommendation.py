"""Tests for the Movie Recommendation interview questions."""

import unittest

from exercise.movie_recommendation import (
    group_users_by_follow_count,
    recommend_movies,
)


class FollowGroupingTest(unittest.TestCase):
    def test_applies_connect_and_disconnect(self):
        events = [
            ["Nicole", "Alice", "CONNECT"],
            ["Nicole", "Alice", "DISCONNECT"],
            ["Charlie", "Alice", "CONNECT"],
            ["Edward", "Alice", "CONNECT"],
        ]
        self.assertEqual(
            (["Alice", "Nicole"], ["Charlie", "Edward"]),
            group_users_by_follow_count(events, 1),
        )


class MovieRecommendationsTest(unittest.TestCase):
    def test_recommends_from_similar_user(self):
        ratings = [
            ["Alice", "Frozen", "5"],
            ["Bob", "Mad Max", "5"],
            ["Dennis", "Mad Max", "4"],
            ["Bob", "Lost In Translation", "5"],
        ]
        self.assertEqual(
            ["Lost In Translation"], recommend_movies("Dennis", ratings)
        )


if __name__ == "__main__":
    unittest.main()
