# Dynamic Attribute Retrieval
class Movement:
    def __get__(self, instance, owner=None):
        moves = {'Bird':'flies', 'Fish':'swims', 'Dog': 'walks or runs'}
        if instance.name in moves:
            return moves[instance.name]
        return 'moves'

class Animal:
    movement = Movement()

    def __init__(self, name):
        self.name = name

animal = Animal('Dog')
print(animal.movement)
