class Vehicle:
    color = "black"

    counter = 0
    
    def __init__(self, model, company):
        self.model = model
        self.company = company
        Vehicle.counter += 1

    def getColor(self):
        return self.color

    def drive(self):
        raise NotImplementedError("Child class should be implementing this")

class Car(Vehicle):
    def drive(self):
        return "car driving"
    
class Truck(Vehicle):
    def drive(self):
        return "truck driving"

class Motorcycle(Vehicle):
    def drive(self):
        return "motorcycle driving"    
