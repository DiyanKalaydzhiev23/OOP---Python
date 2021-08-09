from project.battle_field import BattleField
from project.player.player_repository import PlayerRepository
from project.card.card_repository import CardRepository
from project.player.beginner import Beginner
from project.player.advanced import Advanced
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard


class Controller:

    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type, username):
        if type == "Beginner":
            player = Beginner(username)
        else:
            player = Advanced(username)
        self.player_repository.add(player)
        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type, name):
        if type == "Magic":
            card = MagicCard(name)
        else:
            card = TrapCard(name)
        self.card_repository.add(card)
        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username, card_name):
        player = self.player_repository.find(username)
        card = self.card_repository.find(card_name)
        player.card_repository.add(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name, enemy_name):
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)
        battle_field = BattleField()
        battle_field.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        result = ""
        for p in self.player_repository.players:
            result += f"Username: {p.username} - Health: {p.health} - Cards {p.card_repository.count}\n"
            for c in p.card_repository.cards:
                result += f"### Card: {c.name} - Damage: {c.damage_points}\n"
        return result
