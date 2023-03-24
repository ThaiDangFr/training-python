class A:
    def print(self):
        print("A")

class B(A):
    def __init__(self, name):
        self.name = name
        print(super)
        print(super())

    def print(self):
        print("B")


b = B("O")
b.print()
