# Frozen sets
numbers = (1,2,3)
colors = {'red', 'blue', 'green', 'gray'}
fruits = ['apple', 'grape', 'orange']
frozen_numbers = frozenset(numbers)
frozen_colors = frozenset(colors)
frozen_fruits = frozenset(fruits)
print(frozen_numbers)
print(frozen_colors)
print(frozen_fruits)

# converting frozen sets to lists and tuples
print(list(frozen_numbers))
print(tuple(frozen_numbers))

#frozen sets are immutable
F = frozenset({1,2,3})
F.discard(1)

