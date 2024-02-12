# Methods

class Car:
    #class variable
    quantity = 10
    def __init__(self, name, manufacturer, colour):
        #assign values to instance variables
        self.name = name
        self.manufacturer = manufacturer
        self.colour = colour
    def __init(self, name, manufacturer, colour):
        #define and assign values to instance variables
        self.name = name
        self.manufacturer = manufacturer
        self.colour = colour
    def start(self):
        #method to start the car
        print('starting')
    def move(self):
        #method to move the car
        print('moving')
    def car_info(self):
        #method to get information about the car
        info = f'Car information: {self.colour} {self.name} by {self.manufacturer}'
        print(info)

#accessing attributes and methods
obj = Car('Sunny', 'Nissan', 'Black')
colour =  obj.colour
print(colour)
obj.car_info()
obj.start()
obj.move()

