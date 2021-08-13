class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        consumption = sum([r.expenses + r.room_cost for r in self.rooms])
        return f"Monthly consumptions: {consumption:.2f}$."

    def pay(self):
        info = []
        for room in self.rooms:
            consumption = room.expenses + room.room_cost
            if consumption <= room.budget:
                room.budget -= consumption
                info.append(f"{room.family_name} paid {consumption:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                info.append(f"{room.family_name} does not have enough budget and must leave hotel.")
                self.rooms.remove(room)
        return '\n'.join(info)

    def status(self):
        result = []
        people = sum([r.members_count for r in self.rooms])
        result.append(f"Total population: {people}")
        for room in self.rooms:
            result.append(f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, "
                          f"Expenses: {room.expenses:.2f}$")
            for child in room.children:
                result.append(f"--- Child {room.children.index(child)+1} monthly cost: {child.cost * 30:.2f}$")
            if hasattr(room, "appliances"):
                result.append(f"--- Appliances monthly cost: {sum([a.get_monthly_expense() for a in room.appliances]):.2f}$")
        return '\n'.join(result)
