from project.appliances.appliance import Appliance


class Fridge(Appliance):

    def __init__(self):
        self.cost = 1.2
        super().__init__(self.cost)
