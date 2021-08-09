from unittest import TestCase, main

from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(TestCase):

    def setUp(self):
        self.pr = PlayerRepository()
        self.player = Beginner("pesho")

    def test_initializing(self):
        self.assertEqual(0, self.pr.count)
        self.assertEqual([], self.pr.players)

    def test_add_error(self):
        self.pr.add(self.player)
        with self.assertRaises(ValueError) as ve:
            self.pr.add(self.player)

        expected = f"Player pesho already exists!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_player(self):
        self.pr.add(self.player)
        self.assertIn(self.player, self.pr.players)
        self.assertEqual(1, self.pr.count)

    def test_remove_error(self):
        with self.assertRaises(ValueError) as ve:
            self.pr.remove("")

        expected = "Player cannot be an empty string!"
        self.assertEqual(expected, str(ve.exception))

    def test_remove_player_working(self):
        self.pr.add(self.player)
        self.pr.remove("pesho")
        self.assertEqual(0, len(self.pr.players))
        self.assertEqual(0, self.pr.count)

    def test_find(self):
        self.pr.add(self.player)
        result = self.pr.find("pesho")
        self.assertEqual(result, self.player)


if __name__ == '__main__':
    main()
