"""Tests for the Picking Restaurant interview question."""

import unittest

from exercise.picking_restaurant import recommend_restaurant


class RestaurantRecommendationTest(unittest.TestCase):
    def test_uses_mutual_friends_and_excludes_existing_likes(self):
        friendships = [
            ["Ted", "Lily"],
            ["Ted", "Robin"],
            ["Lily", "Robin"],
            ["Ted", "Marshall"],
            ["Marshall", "Lily"],
        ]
        likes = [
            ["Lily", "Restaurant_1", "Restaurant_17", "Restaurant_3"],
            ["Ted", "Restaurant_17", "Restaurant_1"],
            ["Robin", "Restaurant_5"],
            ["Marshall", "Restaurant_17", "Restaurant_5", "Restaurant_4"],
        ]
        self.assertEqual(
            "Restaurant_5",
            recommend_restaurant(friendships, likes, "Ted", "Lily"),
        )


if __name__ == "__main__":
    unittest.main()
