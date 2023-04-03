class A:
    def __init__(self):
        #self.i = 1
        print("constructeur A appelé")
 
    def func(self):
        self.i = 10
 
 
class B(A):
    #def __init__(self):
    #    print("constructeur B appelé")
    def func(self):
        pass
        #self.i += 1
        #return self.i
 
 
b = B()
#print(b.func())
#b.func()
