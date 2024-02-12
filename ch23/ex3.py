# Attributes of an array
import numpy as np

# shape
num = [1,2,3,4,5,6,7,8,9]
num_array = np.array(num)
print(num_array.shape)

num = [[1,2,3], [4,5,6], [7,8,9]]
num_array = np.array(num)
print(num_array.shape)

#dimension
num = [1,2,3,4,5,6,7,8,9]
num_array = np.array(num)
print(num_array.ndim)

num = [[1,2,3], [4,5,6], [7,8,9]]
num_array = np.array(num)
print(num_array.ndim)

# size
num = [1,2,3,4,5,6,7,8,9]
num_array = np.array(num)
print(num_array.size)

num = [[1,2,3], [4,5,6], [7,8,9]]
num_array = np.array(num)
print(num_array.size)

# type
num = [1,2,3,4,5,6,7,8,9]
num_array = np.array(num)
print(num_array.dtype)


