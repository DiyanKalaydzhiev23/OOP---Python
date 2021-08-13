from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):

    def __init__(self, family_name, salary):
        self.room_cost = 10
        self.appliances = [TV()]
        self.calculate_expenses(self.appliances)
        super().__init__(family_name, salary, 1)
