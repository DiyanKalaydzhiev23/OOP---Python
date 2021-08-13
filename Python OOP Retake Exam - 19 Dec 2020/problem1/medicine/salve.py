from problem1.medicine.medicine import Medicine


class Salve(Medicine):

    def __init__(self):
        self.health_increase = 50
        super().__init__(self.health_increase)
