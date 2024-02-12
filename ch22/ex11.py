#validating names using set

# class Movement:
#     def __get__(self, instance, owner=None):
#         moves = {'Bird':'flies', 'Fish':'swims', 'Dog': 'walks or runs'}
#         return moves[instance.name]

#     def __set__(self, instance, value):
#         if instance.name not in moves:
#             raise ValueError('Incorrect name of animal')
#         instance.name = value

# class Animal:
#     movement = Movement()

#     def __init__(self, name):
#         self.name = name

# animal = Animal('Bird')
# print(animal.movement)
