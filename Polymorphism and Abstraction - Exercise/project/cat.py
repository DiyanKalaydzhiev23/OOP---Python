from project.animal import Animal


class Cat(Animal):

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.sound = "Meow meow!"

    def make_sound(self):
        return self.sound
