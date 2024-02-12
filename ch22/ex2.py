# Getter and setter methods
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def get_name(self):
        #getter method for name attribute
        return self.name

    def set_name(self, name):
        #setter method for name attribute
        print(f'setting name to {name}')
        self.name = name

    def get_sound(self):
        #getter method for sound attribute
        return self.sound

    def set_sound(self, sound):
        #setter method for sound attribute
        print(f'setting sound to {sound}')
        self.sound = sound

animal = Animal('Dog', 'bark')

print(animal.get_name())
print(animal.get_sound())

animal.set_name('Elephant')
animal.set_sound('snort')

print(animal.get_name())
print(animal.get_sound())
