class PlayerRepository:

    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player):
        if player in self.players:
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player):
        if not player:
            raise ValueError("Player cannot be an empty string!")
        player_obj = [p for p in self.players if p.username == player][0]
        if player_obj:
            self.players.remove(player_obj)
            self.count -= 1

    def find(self, username):
        return [p for p in self.players if p.username == username][0]
