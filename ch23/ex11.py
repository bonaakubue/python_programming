# Broadcasting

import numpy as np

num_array1 = np.array([1, 2])
num_array2 = np.array([[10, 20], [30, 40]])
result = num_array1 + num_array2
print(result)

num_array3 = np.array([10, 20, 30])
num_array4 = np.array([[[1], [2]], [[3], [4]]])
result = num_array3 + num_array4
print(result)
