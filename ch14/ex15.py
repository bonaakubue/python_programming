# Printing an instance of a class

class Car:
    def __init__(self, name):
        #initializing the instance variable
        self.name = name

    def get_name(self):
        #return the instance variable name
        return self.name

#instantiating the class
obj = Car('Tesla')
print(obj)

# using __str__() method

class Car:
    def __init__(self, name):
        #initialize the instance variable
        self.name = name

    def get_name(self):
        #return the instance variable
        return self.name

    def __str__(self):
        #result when the instance is printed
        return self.get_name()
#instantiating the class
obj = Car('Tesla')
#print object
print(obj)
