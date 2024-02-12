# decorating the getter method and not specifying the setter method
class Animal:
    def __init__(self, name, sound):
        self._name = name
        self._sound = sound

    @property
    def name(self):
        print(f'accessing name: {self._name}')
        return self._name

    @property
    def sound(self):
        print(f'accessing sound: {self._sound}')
        return self._sound


animal = Animal('Dog', 'bark')
print(animal.name)
print(animal.sound)
animal.name = 'Elephant'
animal.sound = 'snort'
