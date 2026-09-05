"""Solution tests for the Academic Schedule exercises."""

import unittest

from solutions.academic_schedule import curriculum_midpoints, find_pairs


class AcademicSchedulePart1Test(unittest.TestCase):
    def assert_shared_courses(self, expected, enrollments):
        actual = find_pairs(enrollments)
        self.assertEqual(
            {pair: set(courses) for pair, courses in expected.items()},
            {pair: set(courses) for pair, courses in actual.items()},
        )

    def test_enrollments_1(self):
        enrollments = [
            ["58", "Linear Algebra"], ["94", "Art History"],
            ["94", "Operating Systems"], ["17", "Software Design"],
            ["58", "Mechanics"], ["58", "Economics"],
            ["17", "Linear Algebra"], ["17", "Political Science"],
            ["94", "Economics"], ["25", "Economics"],
            ["58", "Software Design"],
        ]
        expected = {
            "17,25": [], "17,58": ["Linear Algebra", "Software Design"],
            "17,94": [], "25,58": ["Economics"],
            "25,94": ["Economics"], "58,94": ["Economics"],
        }
        self.assert_shared_courses(expected, enrollments)

    def test_enrollments_2(self):
        enrollments = [
            ["0", "Advanced Mechanics"], ["0", "Art History"],
            ["1", "Course 1"], ["1", "Course 2"],
            ["2", "Computer Architecture"], ["3", "Course 1"],
            ["3", "Course 2"], ["4", "Algorithms"],
        ]
        expected = {
            "0,1": [], "0,2": [], "0,3": [], "0,4": [], "1,2": [],
            "1,3": ["Course 1", "Course 2"], "1,4": [], "2,3": [],
            "2,4": [], "3,4": [],
        }
        self.assert_shared_courses(expected, enrollments)

    def test_enrollments_3(self):
        enrollments = [
            ["23", "Software Design"], ["3", "Advanced Mechanics"],
            ["2", "Art History"], ["33", "Another"],
        ]
        expected = {
            "2,23": [], "2,3": [], "2,33": [],
            "23,3": [], "23,33": [], "3,33": [],
        }
        self.assert_shared_courses(expected, enrollments)


class AcademicSchedulePart2Test(unittest.TestCase):
    def test_branching_curriculum(self):
        courses = [
            ["Logic", "COBOL"], ["Data Structures", "Algorithms"],
            ["Creative Writing", "Data Structures"], ["Algorithms", "COBOL"],
            ["Intro to Computer Science", "Data Structures"],
            ["Logic", "Compilers"], ["Data Structures", "Logic"],
            ["Graphics", "Networking"], ["Networking", "Algorithms"],
            ["Creative Writing", "System Administration"],
            ["Databases", "System Administration"],
            ["Creative Writing", "Databases"],
            ["Intro to Computer Science", "Graphics"],
        ]
        self.assertEqual(
            {"Creative Writing", "Data Structures", "Databases", "Networking"},
            set(curriculum_midpoints(courses)),
        )

    def test_two_tracks_with_different_midpoints(self):
        courses = [
            ["Course_3", "Course_7"], ["Course_0", "Course_1"],
            ["Course_1", "Course_2"], ["Course_2", "Course_3"],
            ["Course_3", "Course_4"], ["Course_4", "Course_5"],
            ["Course_5", "Course_6"],
        ]
        self.assertEqual(
            {"Course_2", "Course_3"}, set(curriculum_midpoints(courses))
        )


if __name__ == "__main__":
    unittest.main()
