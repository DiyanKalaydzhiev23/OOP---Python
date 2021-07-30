def reverse_text(text):
    text = list(text)
    index = len(text) - 1
    while index >= 0:
        yield text[index]
        index -= 1


for char in reverse_text("step"):
    print(char, end='')
