from project.card.card import Card


class TrapCard(Card):
    DAMAGE_POINTS = 120
    HEALTH_POINTS = 5

    def __init__(self, name):
        super().__init__(name, TrapCard.DAMAGE_POINTS, TrapCard.HEALTH_POINTS)