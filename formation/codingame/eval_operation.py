"""
You must evaluate given mathematical expression like a non scientific calc, meaning there is no operator precedence. For example, 1+2*3 will result in 9 ((1+2)*3) instead of 7.
Entrée
Input: One string containing an expression to evaluate.
Sortie
Output: Integer result of the expression
Contraintes
Input string contains only digits 0-9 or operators in +-*/
0 < Input string length < 30
-100000 < Output < +100000
Input string does not contain negative numbers (3*-4 is not a possible input, but 0-4 is possible).
Divisions always result in integer, no need to round or to use floats. No need to worry about dividing by zero, it won't happen.
Exemple
Entrée
1+2*3
Sortie
9
"""

import time
s= "1+2*3"
l = list(s)
i = 0

while True:
    if i >= len(l):
        break
    c = l[i]
    if c in ['+','-','/','*']:
        l.insert(i, ")")
        l.insert(0,"(")
        i += 3
    else:
        i += 1

print(eval("".join(l)))
