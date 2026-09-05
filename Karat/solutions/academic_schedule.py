"""Reference solutions for the Academic Schedule exercises."""

from __future__ import annotations

from collections import defaultdict


def find_pairs(enrollments: list[list[str]]) -> dict[str, list[str]]:
    """Return the shared courses for every unordered pair of students."""
    courses_by_student: dict[str, set[str]] = defaultdict(set)
    for student, course in enrollments:
        courses_by_student[student].add(course)

    students = sorted(courses_by_student)
    result: dict[str, list[str]] = {}
    for index, first in enumerate(students):
        for second in students[index + 1 :]:
            result[f"{first},{second}"] = sorted(
                courses_by_student[first] & courses_by_student[second]
            )
    return result


def curriculum_midpoints(prerequisites: list[list[str]]) -> list[str]:
    """Return the unique midpoint courses on all root-to-leaf tracks.

    For an even-length track, the earlier of the two middle courses is used.
    """
    graph: dict[str, list[str]] = defaultdict(list)
    courses: set[str] = set()
    destinations: set[str] = set()
    for source, destination in prerequisites:
        if destination not in graph[source]:
            graph[source].append(destination)
        courses.update((source, destination))
        destinations.add(destination)

    midpoints: set[str] = set()

    def visit(course: str, path: list[str]) -> None:
        path.append(course)
        if not graph[course]:
            midpoints.add(path[(len(path) - 1) // 2])
        else:
            for following_course in graph[course]:
                visit(following_course, path)
        path.pop()

    for root in courses - destinations:
        visit(root, [])
    return sorted(midpoints)
