from project.card.card import Card


class MagicCard(Card):
    DAMAGE_POINTS = 5
    HEALTH_POINTS = 80

    def __init__(self, name):
        super().__init__(name, MagicCard.DAMAGE_POINTS, MagicCard.HEALTH_POINTS)
