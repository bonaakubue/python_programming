# Property decorator
class Animal:
    def __init__(self, name, sound):
        self._name = name
        self._sound = sound

    @property
    def name(self):
        print(f'accessing name: {self._name}')
        return self._name

    @name.setter
    def name(self, value):
        print(f'setting name to: {self._name}')
        self._name = value

    @property
    def sound(self):
        print(f'accessing sound: {self._sound}')
        return self._sound

    @sound.setter
    def sound(self, value):
        print(f'setting sound to: {self._sound}')
        self._sound = value


animal = Animal('Dog', 'bark')
print(animal.name)
print(animal.sound)

animal.name = 'Elephant'
animal.sound = 'snort'

print(animal.name)
print(animal.sound)
