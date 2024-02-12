#name mangling
class Shape:
    def __init__(self, length, width):
        #define and assign instance variables as private
        self.__length = length
        self.__width =  width

    def change_length(self, new_length):
        #change the value of an instance variable
        if new_length > 0:
            self.__length = new_length
        else:
            print('enter value greater than 0')
    def change_width(self, new_width):
        #change the value of an instance variable
        if new_width > 0:
            self.__width = new_width
        else:
            print('enter value greater than 0')

    def area(self):
        result = self.__length * self.__width
        return result

obj = Shape(3,4)
# print(obj.__length)
