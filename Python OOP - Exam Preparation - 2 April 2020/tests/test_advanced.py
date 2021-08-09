from unittest import TestCase, main
from project.player.advanced import Advanced


class TestAdvanced(TestCase):

    def setUp(self):
        self.advanced = Advanced("pesho")

    def test_initializing(self):
        self.assertEqual("pesho", self.advanced.username)
        self.assertEqual(250, self.advanced.health)
        self.assertEqual(0, len(self.advanced.card_repository.cards))

    def test_is_dead(self):
        self.advanced.health = 0
        self.assertTrue(self.advanced.is_dead)

    def test_username_error(self):
        with self.assertRaises(ValueError) as ve:
            Advanced("")

        self.assertEqual("Player's username cannot be an empty string.", str(ve.exception))

    def test_health_error(self):
        with self.assertRaises(ValueError) as ve:
            self.advanced.health = -5

        expected = "Player's health bonus cannot be less than zero."
        self.assertEqual(expected, str(ve.exception))

    def test_take_damage_error(self):
        with self.assertRaises(ValueError) as ve:
            self.advanced.take_damage(-5)

        expected = "Damage points cannot be less than zero."
        self.assertEqual(expected, str(ve.exception))

    def test_remove_health(self):
        self.advanced.take_damage(5)
        self.assertEqual(245, self.advanced.health)


if __name__ == '__main__':
    main()
