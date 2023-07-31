import functools

print(functools.reduce(lambda a,b: a*b, range(1,n+1)))
print(sum(list(range(1,n+1))))


s = "ab?"
print(sum((ord(i.lower())-96)*i.isalpha() for i in s))
