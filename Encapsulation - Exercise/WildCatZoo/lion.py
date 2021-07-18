from WildCatZoo.animal import Animal


class Lion(Animal):

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, 50)
