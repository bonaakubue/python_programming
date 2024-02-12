# Accessing arrays

import numpy as np

# indexing
num = [1,2,3,4,5]
num_array = np.array(num)
print(num_array[0])
print(num_array[1])
print(num_array[2])

# indexing in 2 dimensional arrays
num = [[1,2,3], [4,5,6], [7,8,9]]
num_array = np.array(num)
print(num_array[0, 0])
print(num_array[0, 1])
print(num_array[0, 2])

