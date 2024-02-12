# Boolean Indexing
import numpy as np

num = [1,2,3,4,5]
num_array = np.array(num)
print(num_array[num_array > 2])
print(num_array[num_array < 5])
print(num_array[num_array % 2 == 0])
