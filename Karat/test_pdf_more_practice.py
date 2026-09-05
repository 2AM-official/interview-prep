import unittest

from pdf_more_practice import (
    ad_conversion_rates,
    best_day_to_cross,
    build_transition_graph,
    buildable_robots,
    carpool,
    catch_speeders,
    count_journeys,
    delivery_destinations,
    encrypt_with_key,
    filter_treasure_leading_rooms,
    find_earliest_ancestor,
    find_good_story_endings,
    find_nodes_with_zero_or_one_parent,
    find_word_location,
    find_word_locations,
    group_users_by_follow_count,
    has_common_ancestor,
    is_advanced_complete_hand,
    is_finishable,
    minimum_instructions,
    minimum_sphere_distance,
    most_powerful_card,
    most_requested_resource,
    nest_entrance_counts,
    parse_log_entry,
    possible_decryptions,
    recommend_movies,
    recommend_restaurant,
    reflow_and_justify,
    transpose_cipher,
    user_access_ranges,
    validate_nonogram,
)


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


class GoodStoryEndingsTest(unittest.TestCase):
    good = [10, 15, 25, 34]
    bad = [21, 30, 40]

    def test_finds_reachable_good_ending(self):
        self.assertEqual(
            [25],
            find_good_story_endings(self.good, self.bad, [[3, 16, 24]]),
        )

    def test_handles_loops_and_no_choices(self):
        self.assertEqual(
            [],
            find_good_story_endings(self.good, self.bad, [[3, 16, 20]]),
        )
        self.assertEqual(
            [34],
            find_good_story_endings(
                self.good,
                self.bad,
                [[3, 2, 19], [20, 21, 34]],
            ),
        )
        self.assertEqual(
            [10],
            find_good_story_endings(self.good, self.bad, []),
        )


class WordLocationTest(unittest.TestCase):
    grid = [
        list("ccxtib"),
        list("ccatni"),
        list("acnntt"),
        list("tcsipt"),
        list("aoooaa"),
        list("oaaaoo"),
        list("kaicki"),
    ]

    def test_finds_word_path(self):
        self.assertEqual(
            [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4)],
            find_word_location(self.grid, "catnip"),
        )

    def test_single_letter_and_no_match(self):
        self.assertEqual([(3, 2)], find_word_location(self.grid, "s"))
        self.assertIsNone(find_word_location(self.grid, "zebra"))


class MultipleWordLocationsTest(unittest.TestCase):
    def test_finds_disjoint_paths(self):
        grid = [list("bab"), list("yta"), list("xxt")]
        self.assertEqual(
            [
                [(0, 0), (1, 0)],
                [(0, 2), (1, 2), (2, 2)],
            ],
            find_word_locations(grid, ["by", "bat"]),
        )


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


class DeliveryDestinationsTest(unittest.TestCase):
    def test_maps_origins_to_terminal_locations(self):
        paths = [
            ["B", "K"],
            ["C", "K"],
            ["E", "L"],
            ["F", "G"],
            ["J", "M"],
            ["E", "F"],
            ["C", "G"],
            ["A", "B"],
            ["A", "C"],
            ["G", "H"],
            ["G", "I"],
        ]
        self.assertEqual(
            {"A": ["H", "I", "K"], "E": ["H", "I", "L"], "J": ["M"]},
            delivery_destinations(paths),
        )


class BuildableRobotsTest(unittest.TestCase):
    def test_filters_by_available_parts(self):
        required = [
            ["courier", ["wheel", "motor"]],
            ["scanner", ["sensor"]],
            ["drone", ["motor", "propeller"]],
        ]
        self.assertEqual(
            ["courier", "scanner"],
            buildable_robots(["wheel", "motor", "sensor"], required),
        )


class AdConversionTest(unittest.TestCase):
    def test_counts_purchasing_clicks_and_all_clicks(self):
        purchasers = ["3123122444", "234111110", "8321125440", "99911063"]
        clicks = [
            "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
            "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
            "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
            "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
            "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
            "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
        ]
        user_ips = [
            "2339985511,122.121.0.155",
            "234111110,122.121.0.1",
            "3123122444,92.130.6.145",
            "8321125440,82.1.106.8",
            "99911063,92.130.6.144",
        ]
        self.assertEqual(
            {
                "2017 Pet Mittens": (1, 2),
                "The Best Hollywood Coats": (0, 1),
                "Buy wool coats for your pets": (3, 3),
            },
            ad_conversion_rates(purchasers, clicks, user_ips),
        )


class ParentCountsTest(unittest.TestCase):
    def test_finds_zero_and_one_parent_nodes(self):
        pairs = [(1, 3), (2, 3), (4, 2), (4, 7)]
        self.assertEqual(
            ([1, 4], [2, 7]),
            find_nodes_with_zero_or_one_parent(pairs),
        )


class CommonAncestorTest(unittest.TestCase):
    pairs = [
        (1, 3),
        (2, 3),
        (3, 6),
        (5, 6),
        (5, 7),
        (4, 5),
        (4, 8),
    ]

    def test_detects_common_transitive_ancestor(self):
        self.assertTrue(has_common_ancestor(self.pairs, 5, 8))
        self.assertTrue(has_common_ancestor(self.pairs, 6, 5))
        self.assertFalse(has_common_ancestor(self.pairs, 3, 8))


class EarliestAncestorTest(unittest.TestCase):
    pairs = [
        (2, 3),
        (3, 15),
        (3, 6),
        (5, 6),
        (5, 7),
        (4, 5),
        (4, 8),
        (4, 9),
        (9, 11),
        (14, 4),
    ]

    def test_finds_farthest_ancestor(self):
        self.assertEqual(14, find_earliest_ancestor(self.pairs, 8))
        self.assertEqual(2, find_earliest_ancestor(self.pairs, 15))
        self.assertIsNone(find_earliest_ancestor(self.pairs, 14))


class AdvancedHandTest(unittest.TestCase):
    def test_valid_hands(self):
        for hand in ["11123", "12131", "11123455", "11122334", "99"]:
            with self.subTest(hand=hand):
                self.assertTrue(is_advanced_complete_hand(hand))

    def test_invalid_hands(self):
        for hand in ["123456", "1123456789", "00123457", "11890"]:
            with self.subTest(hand=hand):
                self.assertFalse(is_advanced_complete_hand(hand))


class MostPowerfulCardTest(unittest.TestCase):
    def test_counts_transitive_wins(self):
        matchups = [
            ["giant", "wizard"],
            ["giant", "nymph"],
            ["wizard", "elf"],
            ["nymph", "muse"],
            ["orc", "elf"],
            ["orc", "goblin"],
            ["orc", "snake"],
        ]
        self.assertEqual("giant", most_powerful_card(matchups))


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


class NonogramTest(unittest.TestCase):
    def test_validates_ordered_zero_runs(self):
        matrix = [
            [1, 1, 1, 1],
            [0, 1, 1, 1],
            [0, 1, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 1, 1],
        ]
        rows = [[], [1], [1, 2], [1], [2]]
        columns = [[2, 1], [1], [2], [1]]
        self.assertTrue(validate_nonogram(matrix, rows, columns))
        self.assertFalse(
            validate_nonogram(matrix, [[], [], [1], [1], [1, 1]], columns)
        )


class AccessRangesTest(unittest.TestCase):
    def test_finds_minimum_and_maximum_per_user(self):
        logs = [
            ["100", "u1", "r1"],
            ["50", "u1", "r2"],
            ["75", "u2", "r1"],
        ]
        self.assertEqual(
            {"u1": (50, 100), "u2": (75, 75)},
            user_access_ranges(logs),
        )


class MostRequestedResourceTest(unittest.TestCase):
    def test_finds_busiest_five_minute_window(self):
        logs = [
            ["53760", "user_3", "resource_3"],
            ["54001", "user_1", "resource_3"],
            ["54060", "user_2", "resource_3"],
            ["62314", "user_2", "resource_2"],
        ]
        self.assertEqual(
            ("resource_3", 3),
            most_requested_resource(logs),
        )


class TransitionGraphTest(unittest.TestCase):
    def test_adds_start_self_transitions_and_end(self):
        logs = [
            [str(time), "user_1", "resource_3"]
            for time in [300, 599, 900, 1199, 1200, 1201, 1202]
        ]
        graph = build_transition_graph(logs)
        self.assertEqual({"resource_3": 1.0}, graph["START"])
        self.assertAlmostEqual(6 / 7, graph["resource_3"]["resource_3"])
        self.assertAlmostEqual(1 / 7, graph["resource_3"]["END"])


class NestEntrancesTest(unittest.TestCase):
    def test_enclosed_open_component(self):
        board = [list("+++"), list("+0+"), list("+++")]
        self.assertEqual([0], nest_entrance_counts(board))

    def test_all_open_and_all_blocked(self):
        self.assertEqual([4], nest_entrance_counts([list("00"), list("00")]))
        self.assertEqual([], nest_entrance_counts([["+"]]))


class SnowyMountainTest(unittest.TestCase):
    def test_finds_best_forecast_day(self):
        altitudes = [0, 1, 2, 1]
        snow = [[1, 0, 1, 0], [0, 0, 0, 0], [1, 1, 0, 2]]
        self.assertEqual([2, 1], best_day_to_cross(altitudes, snow))


class FinishableTeleportersTest(unittest.TestCase):
    def test_detects_barrier_and_escape(self):
        blocked = ["10,8", "11,5", "12,7", "13,9"]
        self.assertFalse(is_finishable(blocked, 4, 0, 20))
        self.assertTrue(is_finishable(blocked + ["2,15"], 4, 0, 20))
        self.assertFalse(is_finishable(blocked + ["2,15"], 4, 9, 20))


class SphereDistanceTest(unittest.TestCase):
    def test_sums_nearest_matching_holes(self):
        self.assertEqual(6, minimum_sphere_distance("..b.r..r.R.B...b"))
        self.assertEqual(16, minimum_sphere_distance("RBGYygbr"))
        self.assertEqual(0, minimum_sphere_distance(".........."))


class TreasureLeadingRoomsTest(unittest.TestCase):
    def test_filters_rooms(self):
        instructions = [
            ["jasmin", "tulip"],
            ["lily", "tulip"],
            ["tulip", "tulip"],
            ["rose", "rose"],
            ["violet", "rose"],
            ["sunflower", "violet"],
            ["daisy", "violet"],
            ["iris", "violet"],
        ]
        treasures = ["lily", "tulip", "violet", "rose"]
        self.assertEqual(
            ["tulip", "violet"],
            filter_treasure_leading_rooms(treasures, instructions),
        )


class MinimumInstructionsTest(unittest.TestCase):
    def test_follows_instructions_without_money(self):
        self.assertEqual(3, minimum_instructions([1, 1, 1, 9], 0))

    def test_can_pay_to_take_shorter_route(self):
        self.assertEqual(1, minimum_instructions([2, 1, 9], 1))


class ReflowAndJustifyTest(unittest.TestCase):
    lines = [
        "The day began as still as the",
        "night abruptly lighted with",
        "brilliant flame",
    ]

    def test_reflows_and_justifies(self):
        self.assertEqual(
            [
                "The--day--began-as-still",
                "as--the--night--abruptly",
                "lighted--with--brilliant",
                "flame",
            ],
            reflow_and_justify(self.lines, 24),
        )


if __name__ == "__main__":
    unittest.main()
