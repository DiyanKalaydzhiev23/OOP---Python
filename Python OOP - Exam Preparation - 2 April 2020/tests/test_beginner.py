from unittest import TestCase, main
from project.player.beginner import Beginner


class TestBeginner(TestCase):

    def setUp(self):
        self.beginner = Beginner("pesho")

    def test_initializing(self):
        self.assertEqual("pesho", self.beginner.username)
        self.assertEqual(50, self.beginner.health)
        self.assertEqual(0, len(self.beginner.card_repository.cards))

    def test_is_dead(self):
        self.beginner.health = 0
        self.assertTrue(self.beginner.is_dead)

    def test_username_error(self):
        with self.assertRaises(ValueError) as ve:
            Beginner("")

        self.assertEqual("Player's username cannot be an empty string.", str(ve.exception))

    def test_health_error(self):
        with self.assertRaises(ValueError) as ve:
            self.beginner.health = -5

        expected = "Player's health bonus cannot be less than zero."
        self.assertEqual(expected, str(ve.exception))

    def test_take_damage_error(self):
        with self.assertRaises(ValueError) as ve:
            self.beginner.take_damage(-5)

        expected = "Damage points cannot be less than zero."
        self.assertEqual(expected, str(ve.exception))

    def test_remove_health(self):
        self.beginner.take_damage(5)
        self.assertEqual(45, self.beginner.health)


if __name__ == '__main__':
    main()
