# Mathematical operations on arrays

import numpy as np

num_array1 = np.array([1, 2, 3])
num_array2 = np.array([4, 5, 6])

#addition
result = num_array1 + num_array2
print(result)

#subtraction
result = num_array1 - num_array2
print(result)

#multiplication
result = num_array1 * num_array2
print(result)

#division
result = num_array1 / num_array2
print(result)

# functions

num = [1,2,3,4,5,6,7,8,9,10]
num_array = np.array(num)

#square root
squared_array = np.sqrt(num_array)
print(squared_array)

#mean
mean = np.mean(num_array)
print(mean)

#median
median = np.median(num_array)
print(median)

#standard deviation
std_dev = np.std(num_array)
print(std_dev)
