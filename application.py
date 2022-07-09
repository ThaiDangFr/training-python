#!/usr/bin/env python3

#from machines.vehicle_stuff import Vehicle,Truck
#print(__name__)

#truck1 = Truck("4x4","Toyota")
#truck2 = Truck("4x4","Honda")
#truck1.drive()
#print(truck1.get_vehicle_count())

#from animals.animal_stuff import *
#monkey = Monkey("jojo")
#monkey.eat()
#bird = Bird("piou")
#bird.fly()

#from utils.utility_stuff import *

#myshortner = ListAndCharShortner("this is a sentnce")
#myshortner.print_shortened_items()

#ms2 = DictionaryShortner({1: 'mike', 2: 'tom', 3: 'rebeca', 4: 'mike', 5: 'paul'})
#ms2.print_shortened_items()

#from main_package import main_module

#main_module.main_func()

def sum(n1,n2):
    try:
        print(n1+n2)
    except:
        print("error")

number1 = input("enter a number:")

sum(number1, 12)
