#!/usr/bin/env python3
# Assignment 1:

"""
Define a class hierarchy representing animals with a parent class Animal
and child classes such as dog, fish and bird. Each subclass animal should have
a name and an age and should have 2 methods defined in it: move(), eat().
The move method needs to be specific for a given animal where as the
eat() method should be generic for all animals. The methods don't need to
do anything except print information about who is doing what.

After creating the class hierarchy, create instances of each of the 3 animals
dog, fish and bird and make them eat and move.

"""
# Your Code Below:

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def move(self):
        raise NotImplementedError("TODO")
    def eat(self):
        print(self.name + " is eating...")
        
class Dog(Animal):
    def move(self):
        print(self.name + " is running...")
    
class Fish(Animal):
    def move(self):
        print(self.name + " is swimming...")

class Bird(Animal):
    def move(self):
        print(self.name + " is flying...")
        
if __name__ == '__main__' :
    dog = Dog("Chien",5)    
    fish = Fish("Poisson",3)
    bird = Bird("Oiseau",1)
    
    dog.eat()
    dog.move()
    fish.eat()
    fish.move()
    bird.eat()
    bird.move()

        

















































# Solution:
# class Animal:
#     def __init__(self):
#         print("Animal Constructed")
#
#     def move(self):
#         print("Animal Moving...")
#
#     def eat(self):
#         print("Animal Eating...")
#
#
#
# class Bird(Animal):
#
#     def __init__(self, bird_age, bird_name):
#         Animal.__init__(self)
#         self.age = bird_age
#         self.name = bird_name
#
#     def move(self):
#         print("Bird flying...")
#
#
#
# class Fish(Animal):
#
#     def __init__(self, bird_age, bird_name):
#         Animal.__init__(self)
#         self.age = bird_age
#         self.name = bird_name
#
#     def move(self):
#         print("Fish Swimming...")
#
#
# class Dog(Animal):
#
#     def __init__(self, bird_age, bird_name):
#         Animal.__init__(self)
#         self.age = bird_age
#         self.name = bird_name
#
#     def move(self):
#         print("Dog Running ...")
#
# mydog = Dog(3, "wolfy")
# mydog.move()
# mydog.eat()
#
# mydog = Fish(1, "nemo")
# mydog.move()
# mydog.eat()
#
# mydog = Bird(3, "jojo")
# mydog.move()
# mydog.eat()
