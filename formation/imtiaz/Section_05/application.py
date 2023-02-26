class Vehicle:
    color = "black"
    
    def __init__(self, model, company):
        self.model = model
        self.company = company

          
car1 = Vehicle('jeep', 'toyota')
car2 = Vehicle('truck', 'mercedes')

Vehicle.color = "red"
car2.color = "purple"

print(car1.color)
print(car2.color)
