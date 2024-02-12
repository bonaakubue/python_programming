# Getting, setting and deleting attributes
class Name:

    def __get__(self, instance, owner=None):
        print(f'accessing {instance._name}')
        return instance._name.upper()

    def __set__(self, instance, value):
        print(f'updating {instance._name} to {value}')
        instance._name = value

    def __delete__(self, instance):
        del instance._name
        print('deleting...')

class Animal:
    name = Name()
    def __init__(self, name):
        self._name = name


animal = Animal('Bird')
print(animal.name)
animal.name = 'Dog'
animal.name = 'Fish'
print(animal.name)
del animal.name
