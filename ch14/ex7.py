# Modifying the attributes in a class
class Car:
    def __init__(self, name):
        self.name = name

    def rename(self, new_name):
        self.name = new_name

#Accessing the value of an instance variable
obj = Car('Honda')
print(obj.name)
#modifying the instance variable through the instance
obj.name = 'BMW'
print(obj.name)

#modifying the instance variable through an interface
obj.rename('Toyota')
print(obj.name)
