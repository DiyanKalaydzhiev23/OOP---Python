from project.cat import Cat


class Kitten(Cat):

    def __init__(self, name, age):
        super().__init__(name, age, "Female")
        self.sound = "Meow"
