from problem1.supply.supply import Supply


class WaterSupply(Supply):

    def __init__(self):
        self.needs_increase = 40
        super().__init__(self.needs_increase)