# multiple inheritance

class Shape:
    def __init__(self):
        #define and assign value to the instance variable
        self.sides = 1
    def get_name(self, sides):
        #return the name of a shape
        self.sides = sides
        if self.sides == 3:
            return 'Triangle'
        elif self.sides == 4:
            return 'Rectangle'
        elif self.sides == 5:
            return 'Pentagon'
        else:
            return 'shape'

class Colour:
    def __init__(self):
        self.colour = 'colour'

    def get_black(self):
        #return black
        self.colour = 'black'
        return self.colour

    def get_blue(self):
        #return blue
        self.colour = 'blue'
        return self.colour

    def get_green(self):
        #return green
        self.colour = 'green'
        return self.colour

class Drawing(Shape, Colour):
    def __init__(self, name):
        self.name = name

#instantiating the object
obj = Drawing('Tree')

#Acessing methods of the Colour class
result = obj.get_black()
print(result)

result = obj.get_green()
print(result)

#Accessing a method in the Shape class
result = obj.get_name(3)
print(result)

