import sys
import math
import time

#e = float(input())
e = 10.0

pi4 = math.pi/4

def pi_leib(n):
    res = 0
    for i in range(n):
        if i % 2 == 0:
            res += 1/(2*i+1)
        else:
            res -= 1/(2*i+1)
    return res


n = 1
while True:
    aprox_pi = pi_leib(n)
    err = 100*abs((aprox_pi - pi4)/pi4)
    if  err <= e:
        break
    else:
        n += 1

print(n)



