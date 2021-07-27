from Wild.food import Meat, Fruit, Vegetable, Seed
from Wild.animals.animal import Bird


class Owl(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.food_that_eats = [Meat]
        self.weight_per_food = 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.food_that_eats = [Meat, Vegetable, Fruit, Seed]
        self.weight_per_food = 0.35

    def make_sound(self):
        return "Cluck"
