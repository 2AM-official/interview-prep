"""Tests for the camping-trip interview exercises."""

import unittest

from exercise.camping import carpool, shopping_savings


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


class CarpoolTest(unittest.TestCase):
    def test_assigns_people_to_first_car(self):
        roads = [
            ["Bridgewater", "Caledonia", "30"],
            ["Caledonia", "New Grafton", "15"],
            ["New Grafton", "Campground", "5"],
            ["Liverpool", "Milton", "10"],
            ["Milton", "New Grafton", "30"],
        ]
        starts = ["Bridgewater", "Liverpool"]
        people = [
            ["Jessie", "Bridgewater"],
            ["Travis", "Caledonia"],
            ["Jeremy", "New Grafton"],
            ["Katie", "Liverpool"],
        ]
        self.assertEqual(
            [["Jessie", "Travis"], ["Jeremy", "Katie"]],
            carpool(roads, starts, people),
        )


if __name__ == "__main__":
    unittest.main()
