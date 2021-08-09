from unittest import TestCase, main
from project.card.trap_card import TrapCard


class TestTrapCard(TestCase):

    def setUp(self):
        self.trap_card = TrapCard("boom")

    def test_initializing(self):
        self.assertEqual('boom', self.trap_card.name)
        self.assertEqual(5, self.trap_card.health_points)
        self.assertEqual(120, self.trap_card.damage_points)

    def test_name_error(self):
        with self.assertRaises(ValueError) as ve:
            TrapCard("")

        expected = "Card's name cannot be an empty string."
        self.assertEqual(expected, str(ve.exception))

    def test_damage_points_error(self):
        with self.assertRaises(ValueError) as ve:
            self.trap_card.damage_points = -1

        expected = "Card's damage points cannot be less than zero."
        self.assertEqual(expected, str(ve.exception))

    def test_health_error(self):
        with self.assertRaises(ValueError) as ve:
            self.trap_card.health_points = -1

        expected = "Card's HP cannot be less than zero."
        self.assertEqual(expected, str(ve.exception))


if __name__ == '__main__':
    main()