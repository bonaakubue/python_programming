# Generating random numbers
import numpy as np

# Generating Random Integers
rand_num = np.random.randint(1,10)
print(rand_num)

# Creating Random Arrays
rand_array = np.random.rand(5)
print(rand_array)

rand_array = np.random.rand(2,4)
print(rand_array)

# Setting the Random Seed
np.random.seed(12)
rand_array = np.random.rand(5)
print(rand_array)
