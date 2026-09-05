"""Academic Schedule practice question.

Implement one part at a time, then run its focused tests through
``run_tests.py``.
"""

from __future__ import annotations
import collections


def find_pairs(enrollments: list[list[str]]) -> dict[str, list[str]]:
    """Return shared courses for every unordered pair of students.

    Each enrollment is ``[student_id, course_name]``. Include every possible
    pair of students, even when they share no courses.

    Use a pair key in ``"smaller_id,larger_id"`` format, where student IDs are
    ordered lexicographically. Shared-course lists may be returned in any
    order and must not contain duplicates.

    Example:
        [
            ["1", "Math"],
            ["1", "Art"],
            ["2", "Math"],
            ["3", "Biology"],
        ]

        returns:
        {
            "1,2": ["Math"],
            "1,3": [],
            "2,3": [],
        }

    Complexity variables:
        n: number of enrollment pairs
        s: number of students
        c: number of distinct courses
    """

    course_map = collections.defaultdict(set)
    all_students = set()

    for student, course in enrollments:
        course_map[course].add(student)
        all_students.add(student)

    students = sorted(all_students)
    result = {}

    # Create every student pair, including pairs with no shared courses.
    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            key = students[i] + "," + students[j]
            result[key] = []

    # Add each course to all pairs of students enrolled in that course.
    for course, enrolled_students in course_map.items():
        course_students = sorted(enrolled_students)

        for i in range(len(course_students)):
            for j in range(i + 1, len(course_students)):
                key = course_students[i] + "," + course_students[j]
                result[key].append(course)

    return result



def curriculum_midpoints(prerequisites: list[list[str]]) -> list[str]:
    """Return every possible midpoint course in the curriculum.

    Each pair is ``[course, next_course]`` and forms a directed edge. The
    curriculum is a directed acyclic graph. A track starts at a course with no
    incoming edge and ends at a course with no outgoing edge.

    Find every root-to-leaf track and return the midpoint course from each
    track. For a track with an even number of courses, use the earlier of its
    two middle courses. Return unique course names in any order.

    Example:
        A -> B -> C -> D

        The midpoint is B because the track has an even number of courses and
        B is the earlier of the two middle courses.

    Complexity variables:
        n: number of prerequisite pairs
        c: number of distinct courses
    """
    graph = collections.defaultdict(list)
    all_courses = set()
    destinations = set()

    for source, destination in prerequisites:
        graph[source].append(destination)
        all_courses.add(source)
        all_courses.add(destination)
        destinations.add(destination)

    roots = all_courses - destinations
    midpoints = set()

    def dfs(course: str, path: list[str]) -> None:
        path.append(course)

        if course not in graph:
            midpoint_index = (len(path) - 1) // 2
            midpoints.add(path[midpoint_index])
        else:
            for next_course in graph[course]:
                dfs(next_course, path)

        path.pop()

    for root in roots:
        dfs(root, [])

    return list(midpoints)
