import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(abs(x-self.__x), abs(y-self.__y))
    
    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__points = [vertice1, vertice2, vertice3]

    def perimeter(self):
        a = self.__points[0]
        b = self.__points[1]
        c = self.__points[2]
        ab = a.distance_from_point(b)
        bc = b.distance_from_point(c)
        ac = a.distance_from_point(c)
        return ab + bc + ac

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
    



