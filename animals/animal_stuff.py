class Animal:
    def __init__(self, name):
        self.animal_name = name

    def eat(self):
        raise NotImplementedError("Child class should be implementing this")

        
class Monkey(Animal):
    def eat(self):
        print("monkey eat bananas")

class Bird(Animal):
    def eat(self):
        print("bird eat seeds")

    def fly(self):
        print("bird soaring high")
        
