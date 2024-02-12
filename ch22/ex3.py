# properties

class Animal:
    def __init__(self, name, sound):
        self._name = name
        self._sound = sound

    def _get_name(self):
        print(f'accessing name: {self._name}')
        return self._name

    def _set_name(self, value):
        print(f'setting name to: {self._name}')
        self._name = value
    def _get_sound(self):
        print(f'accessing sound: {self._sound}')
        return self._sound

    def _set_sound(self, value):
        print(f'setting sound to: {self._sound}')
        self._sound = value

    name = property(fget=_get_name, fset=_set_name, fdel=None, doc='name of animal')
    sound = property(fget=_get_sound, fset=_set_sound, fdel=None, doc='sound of animal')

animal = Animal('Dog', 'bark')
print(animal.name)
print(animal.sound)

animal.name = 'Elephant'
animal.sound = 'snort'

print(animal.name)
print(animal.sound)
