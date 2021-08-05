from project.hero import Hero
from unittest import TestCase, main


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("Slim Shady", 1, 100, 100)
        self.enemy_hero = Hero("Machine Gun Kelly", 1, 50, 50)

    def test_initializing(self):
        self.assertEqual("Slim Shady", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_fighting_yourself_error(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_not_positive_health_hero_error(self):
        self.hero.health = 0

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        expected = "Your health is lower than or equal to 0. You need to rest"
        self.assertEqual(expected, str(ex.exception))

    def test_not_positive_health_enemy_error(self):
        self.enemy_hero.health = 0

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        expected = f"You cannot fight {self.enemy_hero.username}. He needs to rest"
        self.assertEqual(expected, str(ex.exception))

    def test_damage_and_health_change_hero_win(self):
        expected_level = self.hero.level + 1
        expected_health = self.hero.health - self.enemy_hero.damage + 5
        expected_damage = self.hero.damage + 5

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)
        self.assertEqual("You win", result)

    def test_damage_and_health_change_hero_lose(self):
        enemy_hero = self.hero
        hero = self.enemy_hero
        expected_level = enemy_hero.level + 1
        expected_health = enemy_hero.health - hero.damage + 5
        expected_damage = enemy_hero.damage + 5

        result = hero.battle(enemy_hero)

        self.assertEqual(expected_level, enemy_hero.level)
        self.assertEqual(expected_health, enemy_hero.health)
        self.assertEqual(expected_damage, enemy_hero.damage)
        self.assertEqual("You lose", result)

    def test_string_representation(self):
        expected = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"

        self.assertEqual(expected, str(self.hero))

    def test_draw_result(self):
        enemy_hero = Hero("Machine Gun Kelly", 1, 100, 100)
        result = self.hero.battle(enemy_hero)
        self.assertEqual("Draw", result)


if __name__ == '__main__':
    main()
