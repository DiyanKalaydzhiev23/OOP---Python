from unittest import TestCase, main
from project.card.magic_card import MagicCard
from project.card.card_repository import CardRepository


class TestCardRepository(TestCase):

    def setUp(self):
        self.cr = CardRepository()
        self.magic_card = MagicCard("boom")

    def test_initializing(self):
        self.assertEqual(0, self.cr.count)
        self.assertEqual([], self.cr.cards)

    def test_add_error(self):
        self.cr.add(self.magic_card)
        with self.assertRaises(ValueError) as ve:
            self.cr.add(self.magic_card)

        expected = f"Card boom already exists!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_card(self):
        self.cr.add(self.magic_card)
        self.assertIn(self.magic_card, self.cr.cards)
        self.assertEqual(1, self.cr.count)

    def test_remove_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cr.remove("")

        expected = "Card cannot be an empty string!"
        self.assertEqual(expected, str(ve.exception))

    def test_remove_player_working(self):
        self.cr.add(self.magic_card)
        self.cr.remove("boom")
        self.assertEqual(0, len(self.cr.cards))
        self.assertEqual(0, self.cr.count)

    def test_find(self):
        self.cr.add(self.magic_card)
        result = self.cr.find("boom")
        self.assertEqual(result, self.magic_card)


if __name__ == '__main__':
    main()
