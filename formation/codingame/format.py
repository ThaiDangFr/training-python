hour = 4
minute = 5

# f-strings
# https://he-arc.github.io/livre-python/fstrings/index.html

print(f"{hour:02}:{minute:02}")  # en mettant 02 : 2 places et le vide est remplacé par zéro



# 40 decimal
from decimal import Decimal
from decimal import getcontext
getcontext().prec = 40
r = Decimal(2).sqrt()
print(2**0.5)            # 1.4142135623730951
format(2**0.5, '.40f')   # 1.4142135623730951454746218587388284504414  => valeur fausse
print(r)                 # 1.414213562373095048801688724209698078570   => c'est exact, j'ai vérifié sur wikipedia

i = 8
j = 9
k = i / j
d = Decimal(i) / Decimal(j)
print (k, type(k))
print (d, type(d))

