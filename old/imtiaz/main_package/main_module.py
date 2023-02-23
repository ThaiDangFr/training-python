#!/usr/bin/env python3
#from utils.utility_stuff import *
from main_package.sub_package import another_module

def main_func():
    another_module.greet_user()
    
    # ms2 = DictionaryShortner({1: 'mike', 2: 'tom', 3: 'rebeca', 4: 'mike', 5: 'paul'})
    # ms2.print_shortened_items()

print(__name__)
