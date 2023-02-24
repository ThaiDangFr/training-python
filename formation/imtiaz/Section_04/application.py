if 5 < 6:
    print("5<6")
else:
    print("5>6")


idx = 1
for i in ['goat', 'horse', 'chicken', 'cow', 'dog']:
    ph = str(idx) + "->" + i
    print(ph)
    idx = idx + 1

for i in ("abc", "def"):
    print(i)    


mydict = {'a':1, 'b':2}
for i in mydict.keys():
    p = str(i) + "->" + str(mydict[i])
    print(p)


for i in "toto":
    print(i)

for i in "not yet implemeted":
    pass

def not_implemeted():
    pass

not_implemeted()

x = 0
while x < 10:   
    if x == 6:
        x += 3
        continue
    else:
        print(x)
        x += 3
    
else:
    print("loop end")


employees_dict = {'tom':20, 'joe': 25}
employees_list = [('carl',21), ('max',26)]

for (name, age) in employees_dict.items():
    print(str(name) + "->" + str(age))
    
for (name, age) in employees_list:
    print(str(name) + "->" + str(age))

