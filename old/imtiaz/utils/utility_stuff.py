class Shortner:
    def __init__(self, items):
        self.original_items = items

    def print_original_items(self):
        print(self.original_items)

class ListAndCharShortner(Shortner):
    def print_shortened_items(self):
        print(self.original_items[0:3])

class DictionaryShortner(Shortner):
    def print_shortened_items(self):
        adict = self.original_items
        ndict = {}
        counter = 0
        for k,v in adict.items():
            if counter < 3:
                ndict.update({k:v})
                counter += 1
        print(ndict)
