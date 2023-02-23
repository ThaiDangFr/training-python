#!/usr/bin/env python

my_list = ['b','d','a','z','x']
another_list = [1,2,3,4,5]

part1 = my_list[:3]
part1.sort()
part1.reverse()

part2 = another_list[:3]
part2.sort()
part2.reverse()

result = part1 + part2
print(my_list)
print(another_list)
print(result)

x = ['a', 'b', ["hello","world"]]
print(x[2][1])

tuple = (1,2,3, ['a', 'b'])
tuple[3][1] = 'c'
print(tuple)

mydict = {'k1' : 'value1', 'k2' : 'value2'}
print(mydict.pop('k1'))
print(mydict)

print(5!=6)
