class EncryptionGenerator:

    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError("You must add a number.")

        result = []

        for letter in self.text:
            letter_value = ord(letter)
            while letter_value + other < 32:
                letter_value += 95
            while letter_value + other > 126:
                letter_value -= 95
            letter_value += other
            result.append(letter_value)

        return ''.join([chr(letter_value) for letter_value in result])


example = EncryptionGenerator('Super-Secret Message')
print(example + 20)
print(example + (-52))
