# Descriptors
class Movement:
    def __get__(self, instance, owner=None):
        return 'moves'
class Animal:
    movement = Movement()

    def __init__(self, name):
        self.name = name


animal = Animal('Fish')
print(animal.movement)
