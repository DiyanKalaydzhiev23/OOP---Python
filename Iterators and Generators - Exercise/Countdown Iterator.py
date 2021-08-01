class countdown_iterator:

    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.number < 0:
            raise StopIteration
        result = self.number
        self.number -= 1
        return result


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
