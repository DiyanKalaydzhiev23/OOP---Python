from project.player.player import Player


class Advanced(Player):
    HEALTH_POINTS = 250

    def __init__(self, username):
        super().__init__(username, Advanced.HEALTH_POINTS)
