class Shortner:
    def __init__(self, items):
        self.items = items

    def print_original_items(self):
        print(self.items)


class ListAndCharShortner(Shortner):
    def print_shortened_items(self):
        print(self.items[0:3])


class DictionaryShortner(Shortner):
    def print_shortened_items(self):
        keys = list(self.items.keys())
        newdict = {}
        for i in range(3):
            key = keys[i]
            value = self.items[key]
            newdict[key] = value
        print(newdict)


print("-> Importing from utils.py (bad practise !)") # bad practise
print("__name__:"+__name__)
