from project.animal import Animal


class Dog(Animal):

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.sound = "Woof!"

    def make_sound(self):
        return self.sound
