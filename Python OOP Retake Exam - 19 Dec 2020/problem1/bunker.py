class Bunker:

    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_supplies = [f for f in self.supplies if f.__name__ == "FoodSupply"]
        if not food_supplies:
            raise IndexError("There are no food supplies left!")
        return food_supplies

    @property
    def water(self):
        water_supplies = [w for w in self.supplies if w.__name__ == "WaterSupply"]
        if not water_supplies:
            raise IndexError("There are no water supplies left!")
        return water_supplies

    @property
    def painkillers(self):
        painkillers_supplies = [p for p in self.medicine if p.__name__ == "Painkillers"]
        if not painkillers_supplies:
            raise IndexError("There are no painkillers left!")
        return painkillers_supplies

    @property
    def salves(self):
        salves_supplies = [s for s in self.medicine if s.__name__ == "Salves"]
        if not salves_supplies:
            raise IndexError("There are no salves left!")
        return salves_supplies

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if survivor.needs_healing:
            for med in self.medicine[::-1]:
                if type(med).__name__ == medicine_type:
                    med.apply(survivor)
                    self.medicine.remove(med)
                    return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            for sup in self.supplies[::-1]:
                if type(sup).__name__ == sustenance_type:
                    sup.apply(survivor)
                    self.supplies.remove(sup)
                    return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2

        for survivor in self.survivors:
            self.sustain(survivor, "FoodSupply")
            self.sustain(survivor, "WaterSupply")
