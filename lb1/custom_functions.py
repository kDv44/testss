def contains_object(array, obj):
    return obj in array


def contains_word(text, word):
    return word in text


def contains_field(obj, field):
    return hasattr(obj, field)


def apply_callback(array, callback):
    for item in array:
        callback(item)


def text_to_words(text, callback):
    words = text.split()
    callback(words)


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self):
        print(f"Hello, I'm {self.first_name} {self.last_name}")
