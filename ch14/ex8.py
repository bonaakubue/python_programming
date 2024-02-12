#encapsulation
class Shape:
    def __init__(self, length, width):
        #define and assign values to instance variables
        self.length = length
        self.width =  width

    def change_length(self, new_length):
        #change the value 
        if self.length > 0:
            self.length = new_length
        else:
            print('enter value greater than 0')
    def change_width(self, new_width):
        #change the value of self.width
        if new_width > 0:
            self.width = new_width
        else:
            print('enter value greater than 0')

    def area(self):
        #calculate and return the area of a shape
        result = self.length * self.width
        return result
obj = Shape(2,3)
print(obj.area())

#changing a value directly
obj.length =  -3
print(obj.area())

#changing a value through an interface
obj.change_length(-3)
