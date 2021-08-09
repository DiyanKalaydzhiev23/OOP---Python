from unittest import TestCase, main
from project.battle_field import BattleField
from project.controller import Controller


class TestBattleField(TestCase):

    def setUp(self):
        self.c = Controller()
        self.c.add_player("Beginner", "pesho")
        self.c.add_player("Advanced", "ivan")
        self.c.add_card("Magic", "boom")
        self.c.add_card("Trap", "oops")
        self.c.add_player_card("pesho", "boom")
        self.c.add_player_card("ivan", "oops")
        self.c.add_player_card("ivan", "boom")
        self.attacker = self.c.player_repository.find("pesho")
        self.enemy = self.c.player_repository.find("ivan")
        self.b = BattleField()

    def test_attacker_enemy_dead(self):
        self.attacker.health = 0
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.c.fight("pesho", "ivan")
        self.assertEqual("Player is dead!", str(ve.exception))

    def test_increase_beginner(self):
        self.b.increase_beginner(self.attacker)
        self.assertEqual(90, self.attacker.health)

    def test_getting_bonus_points(self):
        self.b.get_bonus_points(self.attacker)
        self.b.get_bonus_points(self.enemy)
        self.assertEqual(130, self.attacker.health)
        self.assertEqual(335, self.enemy.health)

    def test_attacker_is_dead_after_fight(self):
        self.c.fight("pesho", "ivan")
        self.c.fight("pesho", "ivan")
        self.assertTrue(self.attacker.is_dead)

    def test_enemy_is_dead_after_fight(self):
        self.c.fight("ivan", "pesho")
        self.c.fight("ivan", "pesho")
        self.assertTrue(self.attacker.is_dead)


if __name__ == '__main__':
    main()
