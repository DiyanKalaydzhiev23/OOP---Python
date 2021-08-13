from problem1.medicine.medicine import Medicine


class Painkiller(Medicine):

    def __init__(self):
        self.health_increase = 20
        super().__init__(self.health_increase)
