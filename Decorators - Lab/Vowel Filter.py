import functools


def vowel_filter(function):
    vowels = "aeiou"

    @functools.wraps(function)
    def wrapper():
        result = [l for l in function() if l in vowels]
        return result

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
