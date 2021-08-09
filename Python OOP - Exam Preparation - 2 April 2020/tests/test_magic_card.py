from unittest import TestCase, main
from project.card.magic_card import MagicCard


class TestMagicCard(TestCase):

    def setUp(self):
        self.magic_card = MagicCard("boom")

    def test_initializing(self):
        self.assertEqual('boom', self.magic_card.name)
        self.assertEqual(80, self.magic_card.health_points)
        self.assertEqual(5, self.magic_card.damage_points)

    def test_name_error(self):
        with self.assertRaises(ValueError) as ve:
            MagicCard("")

        expected = "Card's name cannot be an empty string."
        self.assertEqual(expected, str(ve.exception))

    def test_damage_points_error(self):
        with self.assertRaises(ValueError) as ve:
            self.magic_card.damage_points = -1

        expected = "Card's damage points cannot be less than zero."
        self.assertEqual(expected, str(ve.exception))

    def test_health_error(self):
        with self.assertRaises(ValueError) as ve:
            self.magic_card.health_points = -1

        expected = "Card's HP cannot be less than zero."
        self.assertEqual(expected, str(ve.exception))


if __name__ == '__main__':
    main()
