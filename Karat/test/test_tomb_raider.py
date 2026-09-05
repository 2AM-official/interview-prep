"""Tests for the Tomb Raider interview question."""

import unittest

from exercise.tomb_raider import minimum_sphere_distance


class SphereDistanceTest(unittest.TestCase):
    def test_sums_nearest_matching_holes(self):
        self.assertEqual(6, minimum_sphere_distance("..b.r..r.R.B...b"))
        self.assertEqual(16, minimum_sphere_distance("RBGYygbr"))
        self.assertEqual(0, minimum_sphere_distance(".........."))


if __name__ == "__main__":
    unittest.main()
