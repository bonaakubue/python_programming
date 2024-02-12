# Read-only and write-only decorator properties
class Animal:
    def __init__(self, name, sound):
        self._name = name
        self._sound = sound

    @property
    def name(self):
        raise AttributeError('Access denied!')

    @name.setter
    def name(self, value):
        print(f'setting name to: {self._name}')
        self._name = value

    @property
    def sound(self):
        raise AttributeError('Access denied!')

    @sound.setter
    def sound(self, value):
        print(f'setting sound to: {self._sound}')
        self._sound = value

animal = Animal('Dog', 'bark')
print(animal.name)
print(animal.sound)
animal.name = 'Elephant'
animal.sound = 'snort'
