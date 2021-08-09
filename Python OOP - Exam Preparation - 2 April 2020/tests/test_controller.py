from unittest import TestCase, main
from project.controller import Controller


class TestController(TestCase):

    def setUp(self):
        self.c = Controller()

    def test_initializing(self):
        self.assertEqual([], self.c.player_repository.players)
        self.assertEqual([], self.c.card_repository.cards)

    def test_adding_player(self):
        result_beginner = self.c.add_player("Beginner", "Someone")
        self.assertEqual(1, len(self.c.player_repository.players))
        result_advanced = self.c.add_player("Advanced", "Someone2")
        self.assertEqual(2, len(self.c.player_repository.players))
        self.assertEqual(result_beginner, f"Successfully added player of type Beginner with username: Someone")
        self.assertEqual(result_advanced, f"Successfully added player of type Advanced with username: Someone2")

    def test_adding_card(self):
        result_magic = self.c.add_card("Magic", "Someone")
        self.assertEqual(1, len(self.c.card_repository.cards))
        result_trap = self.c.add_card("Trap", "Someone2")
        self.assertEqual(2, len(self.c.card_repository.cards))
        self.assertEqual(result_magic, f"Successfully added card of type MagicCard with name: Someone")
        self.assertEqual(result_trap, f"Successfully added card of type TrapCard with name: Someone2")

    def test_add_player_card(self):
        self.c.add_player("Beginner", "pesho")
        self.c.add_card("Magic", "boom")
        result = self.c.add_player_card("pesho", "boom")
        # may have to check if card is in player repo
        self.assertEqual(result, f"Successfully added card: boom to user: pesho")

    def test_fight(self):
        self.c.add_player("Beginner", "pesho")
        self.c.add_player("Advanced", "ivan")
        self.c.add_card("Magic", "boom")
        self.c.add_player_card("pesho", "boom")
        self.c.add_player_card("ivan", "boom")
        result = self.c.fight("pesho", "ivan")
        self.assertEqual(result, f"Attack user health 135 - Enemy user health 295")

    def test_report(self):
        self.c.add_player("Beginner", "pesho")
        self.c.add_card("Magic", "boom")
        self.c.add_player_card("pesho", "boom")
        self.assertEqual(f"Username: pesho - Health: 50 - Cards 1\n### Card: boom - Damage: 5\n", self.c.report())


if __name__ == '__main__':
    main()
