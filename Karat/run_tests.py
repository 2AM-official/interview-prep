#!/usr/bin/env python3
"""Run one Karat practice topic or the complete suite."""

import sys
import unittest


TOPICS = {
    "badge": "test_karat_practice.BadgeAccessTest",
    "domains": "test_domain_analysis.DomainVisitsTest",
    "courses": "test_academic_schedule.AcademicSchedulePart1Test",
    "rectangle": "test_karat_practice.ZeroRectangleTest",
    "story": "test_karat_practice.StorybookTest",
    "exit": "test_snake_exits.NearestExitTest",
    "academic-part1": "test_academic_schedule.AcademicSchedulePart1Test",
    "academic-part2": "test_academic_schedule.AcademicSchedulePart2Test",
    "academic-schedule": [
        "test_academic_schedule.AcademicSchedulePart1Test",
        "test_academic_schedule.AcademicSchedulePart2Test",
    ],
    "midpoints": "test_academic_schedule.AcademicSchedulePart2Test",
    "ending": "test_book_endings.StoryEndingTest",
    "shopping": "test_camping.ShoppingSavingsTest",
    "scramble": "test_catch_cheaters.ScrambledWordTest",
    "history": "test_domain_analysis.ContiguousHistoryTest",
    "subsequence": "test_pdf_practice.CommonSubsequenceTest",
    "hand": "test_mini_game.CompleteHandTest",
    "matrix": "test_puzzle_checker.ValidMatrixTest",
    "lanes": "test_snake_exits.PassableLanesTest",
    "teleporters": "test_thrilling_teleporters.TeleporterDestinationsTest",
    "wrap": "test_writing_application.WrapLinesTest",
    "carpool": "test_camping.CarpoolTest",
    "good-endings": "test_book_endings.GoodStoryEndingsTest",
    "word-location": "test_catch_cheaters.WordLocationTest",
    "word-locations": "test_catch_cheaters.MultipleWordLocationsTest",
    "transpose": "test_cipher.TransposeCipherTest",
    "encrypt": "test_cipher.KeyedEncryptionTest",
    "decrypt": "test_cipher.PossibleDecryptionsTest",
    "delivery": "test_delivery_bot.DeliveryDestinationsTest",
    "robots": "test_delivery_bot.BuildableRobotsTest",
    "ads": "test_domain_analysis.AdConversionTest",
    "parents": "test_generation_graph.ParentCountsTest",
    "ancestor": "test_generation_graph.CommonAncestorTest",
    "earliest": "test_generation_graph.EarliestAncestorTest",
    "advanced-hand": "test_mini_game.AdvancedHandTest",
    "card": "test_most_powerful_card.MostPowerfulCardTest",
    "follows": "test_movie_recommendation.FollowGroupingTest",
    "movies": "test_movie_recommendation.MovieRecommendationsTest",
    "parse-log": "test_passage_tracker.ParseLogEntryTest",
    "journeys": "test_passage_tracker.JourneyCountTest",
    "speeders": "test_passage_tracker.CatchSpeedersTest",
    "restaurant": "test_picking_restaurant.RestaurantRecommendationTest",
    "nonogram": "test_puzzle_checker.NonogramTest",
    "access": "test_resource_access_log.AccessRangesTest",
    "busiest": "test_resource_access_log.MostRequestedResourceTest",
    "transitions": "test_resource_access_log.TransitionGraphTest",
    "nests": "test_snake_exits.NestEntrancesTest",
    "snow": "test_snowy_mountain.SnowyMountainTest",
    "finishable": "test_thrilling_teleporters.FinishableTeleportersTest",
    "spheres": "test_tomb_raider.SphereDistanceTest",
    "treasure-rooms": "test_treasure_room.TreasureLeadingRoomsTest",
    "treasure-path": "test_treasure_room.MinimumInstructionsTest",
    "justify": "test_writing_application.ReflowAndJustifyTest",
    "domain-analysis": "test_domain_analysis",
    "snake-exits": "test_snake_exits",
    "book-endings": "test_book_endings",
    "camping": "test_camping",
    "catch-cheaters": "test_catch_cheaters",
    "mini-game": "test_mini_game",
    "puzzle-checker": "test_puzzle_checker",
    "thrilling-teleporters": "test_thrilling_teleporters",
    "writing-application": "test_writing_application",
    "cipher": "test_cipher",
    "delivery-bot": "test_delivery_bot",
    "generation-graph": "test_generation_graph",
    "movie-recommendation": "test_movie_recommendation",
    "passage-tracker": "test_passage_tracker",
    "most-powerful-card": "test_most_powerful_card",
    "picking-restaurant": "test_picking_restaurant",
    "resource-access-log": "test_resource_access_log",
    "snowy-mountain": "test_snowy_mountain",
    "tomb-raider": "test_tomb_raider",
    "treasure-room": "test_treasure_room",
    "all": [
        "test_karat_practice",
        "test_academic_schedule",
        "test_domain_analysis",
        "test_snake_exits",
        "test_book_endings",
        "test_camping",
        "test_catch_cheaters",
        "test_mini_game",
        "test_puzzle_checker",
        "test_thrilling_teleporters",
        "test_writing_application",
        "test_cipher",
        "test_delivery_bot",
        "test_generation_graph",
        "test_movie_recommendation",
        "test_passage_tracker",
        "test_most_powerful_card",
        "test_picking_restaurant",
        "test_resource_access_log",
        "test_snowy_mountain",
        "test_tomb_raider",
        "test_treasure_room",
    ],
    "pdf": [
        "test_academic_schedule",
        "test_domain_analysis",
        "test_snake_exits",
        "test_book_endings",
        "test_camping",
        "test_catch_cheaters",
        "test_mini_game",
        "test_puzzle_checker",
        "test_thrilling_teleporters",
        "test_writing_application",
        "test_cipher",
        "test_delivery_bot",
        "test_generation_graph",
        "test_movie_recommendation",
        "test_passage_tracker",
        "test_most_powerful_card",
        "test_picking_restaurant",
        "test_resource_access_log",
        "test_snowy_mountain",
        "test_tomb_raider",
        "test_treasure_room",
    ],
}


def resolve_test_target(target: str) -> str:
    """Point split exercise tests at the ``test`` package."""
    module = target.split(".", 1)[0]
    legacy_modules = {
        "test_karat_practice",
        "test_pdf_practice",
        "test_pdf_more_practice",
    }
    return target if module in legacy_modules else f"test.{target}"


def main() -> int:
    topic = sys.argv[1] if len(sys.argv) == 2 else "all"
    if topic not in TOPICS:
        options = "|".join(TOPICS)
        print(f"Usage: python3 run_tests.py {{{options}}}", file=sys.stderr)
        return 2

    targets = TOPICS[topic]
    if isinstance(targets, str):
        targets = [targets]

    suite = unittest.TestSuite(
        unittest.defaultTestLoader.loadTestsFromName(resolve_test_target(target))
        for target in targets
    )
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
