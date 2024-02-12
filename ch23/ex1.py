import numpy as np

# create a basic array
num = [1, 2, 3, 4, 5]
num_array = np.array(num)

print(num_array)

# linspace() function
num_array = np.linspace(1, 5, 5)
print(num_array)

# arange() function
num_array = np.arange(1,10)
print(num_array)

# with step
num_array = np.arange(1,10,2)
print(num_array)

num_array = np.arange(1,10,3)
print(num_array)
