from unittest import TestCase, main
from project.people.child import Child
from project.rooms.room import Room


class TestRoom(TestCase):

    def setUp(self):
        self.r = Room("ivanovi", 1000, 2)

    def test_initializing(self):
        self.assertEqual("ivanovi", self.r.family_name)
        self.assertEqual(1000, self.r.budget)
        self.assertEqual(2, self.r.members_count)
        self.assertEqual([], self.r.children)
        self.assertEqual(0, self.r.expenses)

    def test_expenses_error(self):
        with self.assertRaises(ValueError) as ve:
            self.r.expenses = -1

        expected = "Expenses cannot be negative"
        self.assertEqual(expected, str(ve.exception))

    def test_expenses_set_value(self):
        self.r.expenses = 5
        self.assertEqual(5, self.r.expenses)

    def test_calculate_expenses(self):
        self.r.calculate_expenses([Child(5, 5)])
        self.assertEqual(300, self.r.expenses)


if __name__ == '__main__':
    main()