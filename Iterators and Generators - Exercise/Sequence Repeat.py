class sequence_repeat:

    def __init__(self, text, times):
        self.text = list(text)
        self.times = times
        self.current_repeat = 0
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_repeat == self.times:
            raise StopIteration
        if self.index == len(self.text):
            self.index = 0
        self.current_repeat += 1
        result = self.text[self.index]
        self.index += 1
        return result


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
