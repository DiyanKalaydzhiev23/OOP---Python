class Child:

    def __init__(self, food_cost, *toys_cost):
        self.food_cost = food_cost
        self.toys_cost = sum(toys_cost)
        self.cost = self.food_cost + self.toys_cost
