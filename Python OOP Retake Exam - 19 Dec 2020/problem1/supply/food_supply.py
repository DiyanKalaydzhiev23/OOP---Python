from problem1.supply.supply import Supply


class FoodSupply(Supply):

    def __init__(self):
        self.needs_increase = 20
        super().__init__(self.needs_increase)
