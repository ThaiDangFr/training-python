"""
commentaires
multilignes
"""

glob = 10

def greet_person(jibberish):
    print("hello " + str(jibberish))

def remainder(x,y):
    return x % y


def mysum(*args):
    return args

def keyvalues(**kwargs):
    return kwargs

def test_global():
    global glob
    return glob


greet_person(4)
print(remainder(10,3))

print(mysum(1,2,3,4,5))
print(keyvalues(toto="12", titi=15))
print(test_global())
