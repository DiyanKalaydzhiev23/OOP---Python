from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("Ivan")
        self.student_with_course = Student("Ivan", {"math": ["some notes"]})

    def test_initializing(self):
        self.assertEqual("Ivan", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({"math": ["some notes"]}, self.student_with_course.courses)

    def test_course_already_in(self):
        result = self.student_with_course.enroll("math", ["more notes"])
        self.assertEqual("Course already added. Notes have been updated.", result)
        expected_notes = ["some notes", "more notes"]
        actual_notes = self.student_with_course.courses['math']
        self.assertEqual(expected_notes, actual_notes)

    def test_add_course_notes(self):
        result1 = self.student_with_course.enroll("physics", ["new notes"], "Y")
        result2 = self.student_with_course.enroll("biology", ["new notes"])
        self.assertEqual("Course and course notes have been added.", result1)
        self.assertEqual("Course and course notes have been added.", result2)
        self.assertEqual(["new notes"], self.student_with_course.courses["physics"])
        self.assertEqual(["new notes"], self.student_with_course.courses["biology"])

    def test_without_adding_notes(self):
        result = self.student.enroll("math", "", "no notes")
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student.courses["math"])

    def test_add_notes_on_existing_course(self):
        result = self.student_with_course.add_notes("math", "a+b=c")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["some notes", "a+b=c"], self.student_with_course.courses["math"])

    def test_add_notes_to_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("math", "a+b=c")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leaving_existing_course(self):
        result = self.student_with_course.leave_course("math")
        self.assertEqual("Course has been removed", result)

        with self.assertRaises(KeyError):
            result = self.student_with_course.courses["math"]

    def test_leaving_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("math")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()
