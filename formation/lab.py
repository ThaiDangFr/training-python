
x = [1,2,3]
def func():
    print(x)
    x.pop()
    del x[1]

func()
print(x)
