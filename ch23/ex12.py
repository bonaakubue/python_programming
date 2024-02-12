# Reshaping a NumPy array

import numpy as np

num_array = np.array([[1, 2, 3], [4, 5, 6], [7,8,9], [10,11,12]])
rsh_array = np.reshape(num_array, (3,4))
print(rsh_array)

# np.ndarray.flatten andnp.ravel methods
num_array = np.array([[1, 2, 3], [4, 5, 6], [7,8,9], [10,11,12]])
result = num_array.flatten()
print(result)
result = np.ravel(num_array)
print(result)
