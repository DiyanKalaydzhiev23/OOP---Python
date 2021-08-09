class BattleField:

    def fight(self, attacker, enemy):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")
        if attacker.__class__.__name__ == "Beginner":
            self.increase_beginner(attacker)
        self.get_bonus_points(attacker)
        self.get_bonus_points(enemy)
        for c in attacker.card_repository.cards:
            if enemy.is_dead or attacker.is_dead:
                return
            enemy.take_damage(c.damage_points)

        for c in enemy.card_repository.cards:
            if enemy.is_dead or attacker.is_dead:
                return
            attacker.take_damage(c.damage_points)

    @staticmethod
    def increase_beginner(player):
        player.health += 40
        for card in player.card_repository.cards:
            card.damage_points += 30

    @staticmethod
    def get_bonus_points(player):
        player.health += sum([card.health_points for card in player.card_repository.cards])
