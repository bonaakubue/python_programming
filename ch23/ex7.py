# Adding and removing

import numpy as np

# np.append() function
num = [1,2,3,4,5]
num_array = np.array(num)
print(num_array)
num_array = np.append(num_array, 6)
print(num_array)


# np.insert() function
num = [1,2,3,4,5]
num_array = np.array(num)
print(num_array)
num_array = np.insert(num_array, 0, 0)
print(num_array)
num_array = np.insert(num_array, 2, 99)
print(num_array)

# Removing Elements
num = [1,2,3,4,5]
num_array = np.array(num)
print(num_array)
num_array = np.delete(num_array, 0)
print(num_array)

num_array = np.delete(num_array, 3)
print(num_array)
