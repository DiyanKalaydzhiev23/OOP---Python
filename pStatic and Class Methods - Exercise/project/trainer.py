class Trainer:
    id = 1

    def __init__(self, name):
        self.name = name
        self.id = __class__.id
        __class__.id += 1

    @staticmethod
    def get_next_id():
        return __class__.id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
