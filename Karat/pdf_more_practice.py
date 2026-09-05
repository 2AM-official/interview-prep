"""Remaining non-duplicate exercises from the supplied Karat PDF.

Implementations live in ``exercise/``; this module re-exports them so the
legacy combined tests keep working.
"""

from exercise.book_endings import find_good_story_endings
from exercise.camping import carpool
from exercise.catch_cheaters import find_word_location, find_word_locations
from exercise.cipher import encrypt_with_key, possible_decryptions, transpose_cipher
from exercise.delivery_bot import buildable_robots, delivery_destinations
from exercise.domain_analysis import ad_conversion_rates
from exercise.generation_graph import (
    find_earliest_ancestor,
    find_nodes_with_zero_or_one_parent,
    has_common_ancestor,
)
from exercise.mini_game import is_advanced_complete_hand
from exercise.most_powerful_card import most_powerful_card
from exercise.movie_recommendation import group_users_by_follow_count, recommend_movies
from exercise.passage_tracker import catch_speeders, count_journeys, parse_log_entry
from exercise.picking_restaurant import recommend_restaurant
from exercise.puzzle_checker import validate_nonogram
from exercise.resource_access_log import (
    build_transition_graph,
    most_requested_resource,
    user_access_ranges,
)
from exercise.snake_exits import nest_entrance_counts
from exercise.snowy_mountain import best_day_to_cross
from exercise.thrilling_teleporters import is_finishable
from exercise.tomb_raider import minimum_sphere_distance
from exercise.treasure_room import filter_treasure_leading_rooms, minimum_instructions
from exercise.writing_application import reflow_and_justify

__all__ = [
    "ad_conversion_rates",
    "best_day_to_cross",
    "build_transition_graph",
    "buildable_robots",
    "carpool",
    "catch_speeders",
    "count_journeys",
    "delivery_destinations",
    "encrypt_with_key",
    "filter_treasure_leading_rooms",
    "find_earliest_ancestor",
    "find_good_story_endings",
    "find_nodes_with_zero_or_one_parent",
    "find_word_location",
    "find_word_locations",
    "group_users_by_follow_count",
    "has_common_ancestor",
    "is_advanced_complete_hand",
    "is_finishable",
    "minimum_instructions",
    "minimum_sphere_distance",
    "most_powerful_card",
    "most_requested_resource",
    "nest_entrance_counts",
    "parse_log_entry",
    "possible_decryptions",
    "recommend_movies",
    "recommend_restaurant",
    "reflow_and_justify",
    "transpose_cipher",
    "user_access_ranges",
    "validate_nonogram",
]
