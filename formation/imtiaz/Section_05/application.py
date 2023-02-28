
# version import de classe
#from machine.vehicle_stuff import Car, Truck, Motorcycle
#from machine.tools.utils import ListAndCharShortner, DictionaryShortner

# version import de module
from machine import vehicle_stuff
from machine.tools import utils
        
# autre syntaxe
#import machine.vehicle_stuff
#import machine.tools.utils

car = vehicle_stuff.Car('jeep', 'toyota')
truck = vehicle_stuff.Truck("Big Rig", "Mercedes")
moto = vehicle_stuff.Motorcycle("Sport", "Honda")

for v in [car, truck, moto]:
    print(v.drive())

myshortner = utils.ListAndCharShortner("hello world")
myshortner.print_original_items()
myshortner.print_shortened_items()


myshortner2 = utils.ListAndCharShortner([1,2,3,4,5])
myshortner2.print_original_items()
myshortner2.print_shortened_items()

dictshortner = utils.DictionaryShortner({1:'mike', 2:'tom', 3:'rebeca', 4:'mike', 5:'paul'})
dictshortner.print_original_items()
dictshortner.print_shortened_items()
