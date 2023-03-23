class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v
 
 
for x in I():
    print(x,end='')


mylist = [1,2]
myiter = iter(mylist)

print(next(myiter))
print(next(myiter))
print(next(myiter))
