import math

# math.comb(n,p)
# math.factorial(n)

"""
A drawer contains marbles of three different colors, red, blue and green, given the amounts of each color of marble, if three marbles are selected at random, figure out the probability (as a percentage, rounded down), that there will be one of each color in the selection.
Entrée
Line 1: An integer R for the number of red marbles.
Line 2:An integer B for the number of blue marbles.
Line 3An integer G for the number of green marbles.
Sortie
The probability of selecting one marble of each color as a percentage (rounded down) outputted as a string
Contraintes
0≤R,B,G≤1000
"""

r = 2
b = 3
g = 4

# http://www.panamaths.net/Documents/Exercices/SolutionsHTML/19/PROBA00010.htm

#fact = lambda n: n * fact(n-1) if n != 0 else 1
#combin = lambda n,k: fact(n)//(fact(k)*fact(n-k))
#print(combin(r+g+b, 3)) # 84

total_ways = math.comb(r+b+g, 3)
one_each_color = r*g*b
prob = one_each_color*100//total_ways
print(prob,"%", sep="")


