"""Complete reference solutions for the Passage Tracker exercise family."""

from __future__ import annotations

from collections import defaultdict
from typing import Optional

LogEntry = tuple[float, str, int, str, str]


def parse_log_entry(log_line: str) -> tuple[float, str, int, str, str]:
    """Parse ``timestamp plate locationDirection boothType``.

    Convert E/W to EAST/WEST and raise ``ValueError`` for another direction.
    """
    timestamp_text, plate, location_direction, booth_type = log_line.split()
    direction_code = location_direction[-1]
    directions = {"E": "EAST", "W": "WEST"}
    if direction_code not in directions:
        raise ValueError(f"invalid direction: {direction_code}")
    return (
        float(timestamp_text),
        plate,
        int(location_direction[:-1]),
        directions[direction_code],
        booth_type,
    )


def _complete_journeys(log_lines: list[str]) -> list[list[LogEntry]]:
    by_plate: dict[str, list[LogEntry]] = defaultdict(list)
    for log_line in log_lines:
        entry = parse_log_entry(log_line)
        by_plate[entry[1]].append(entry)

    journeys: list[list[LogEntry]] = []
    for entries in by_plate.values():
        entries.sort(key=lambda entry: entry[0])
        current: Optional[list[LogEntry]] = None
        for entry in entries:
            booth_type = entry[4]
            if booth_type == "ENTRY":
                current = [entry]
            elif current is not None:
                current.append(entry)
                if booth_type == "EXIT":
                    journeys.append(current)
                    current = None
    journeys.sort(key=lambda journey: journey[0][0])
    return journeys


def count_journeys(log_lines: list[str]) -> int:
    """Count complete ENTRY-to-EXIT journeys grouped by license plate.

    Input may be unsorted. The PDF guarantees complete, non-overlapping
    journeys for each plate.
    """
    return len(_complete_journeys(log_lines))


def catch_speeders(log_lines: list[str]) -> list[str]:
    """Return one plate entry per speeding journey.

    A journey speeds at >=130 km/h over a 10 km segment or >=120 km/h over
    two consecutive 10 km segments. Booth records are 10 km apart. Preserve
    chronological journey order; the same plate may appear more than once.
    """

    def at_least_speed(
        first: LogEntry, last: LogEntry, distance: int, speed: int
    ) -> bool:
        elapsed_seconds = last[0] - first[0]
        return (
            elapsed_seconds > 0
            and abs(last[2] - first[2]) == distance
            and distance * 3600 >= speed * elapsed_seconds
        )

    speeding_plates: list[str] = []
    for journey in _complete_journeys(log_lines):
        speeding = any(
            at_least_speed(journey[index], journey[index + 1], 10, 130)
            for index in range(len(journey) - 1)
        )
        if not speeding:
            speeding = any(
                abs(journey[index + 1][2] - journey[index][2]) == 10
                and abs(journey[index + 2][2] - journey[index + 1][2]) == 10
                and (
                    journey[index + 1][2] - journey[index][2]
                )
                == (
                    journey[index + 2][2] - journey[index + 1][2]
                )
                and at_least_speed(
                    journey[index], journey[index + 2], 20, 120
                )
                for index in range(len(journey) - 2)
            )
        if speeding:
            speeding_plates.append(journey[0][1])
    return speeding_plates
