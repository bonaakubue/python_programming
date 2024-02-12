# Class variables

class Car:
    #class variable
    quantity = 10
    def __init__(self, name, manufacturer, colour):
        #assign values to instance variables
        self.name = name
        self.manufacturer = manufacturer
        self.colour = colour

#instances of the class
car1 = Car('Camry', 'Toyota', 'Black')
car2 = Car('Accord', 'Honda', 'White')
print(car1.quantity)
print(car2.quantity)
