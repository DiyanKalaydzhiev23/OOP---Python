from project.appliances.appliance import Appliance


class Laptop(Appliance):

    def __init__(self):
        self.cost = 1
        super().__init__(self.cost)
