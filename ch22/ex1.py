#accessing or modifying attributes directly
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

#instantiating object
animal = Animal('Dog', 'bark')

#accessing attributes
print(animal.name)
print(animal.sound)

#modifying attributes
animal.name = 'Elephant'
animal.sound = 'snort'

#accessing attributes
print(animal.name)
print(animal.sound)
print(animal.name)
print(animal.sound)
