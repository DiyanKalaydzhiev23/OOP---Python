from project.rooms.room import Room


class AloneOld(Room):

    def __init__(self, family_name, pension):
        self.room_cost = 10
        super().__init__(family_name, pension, 1)
