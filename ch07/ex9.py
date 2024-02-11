# map() function
from math import trunc
L = [1.2,2.88,3.01,4.00,5.75]
num = map(trunc, L)
print(num)

num = map(abs, [-1,-2,-3,-4])
print(num)

# Map with user-defined functions
def square(num):
	return num**2
L = [1,2,3,4,5]
squares = map(square, L)
print(squares)

# lambda functions with map
L = [1,2,3,4,5]
squares = map(lambda num: num**2, L)
print(squares)

# Using map with list comprehensions
def square(num):
	return num**2
L = [1,2,3,4,5]
result = [num for num in map(square, L)]
print(result)

# zip() function
L1 = [1,2,3]
L2 = [4,5,6]
result = zip(L1, L2)
print(result)

# combine as many lists as possible
L1 = [1,2,3]
L2 = [4,5,6]
L3 = [7,8,9]
L4 = [10,11,12]

result = zip(L1, L2, L3, L4)
print(result)

# Combining lists of variable lengths 
L1 = [1,2,3]
L2 = [4,5]
L3 = [7,8,9]
result = zip(L1, L2, L3)
print(result)

# list comprehension and the zip() function
L1 = [1,2,3]
L2 = [4,5,6]
result = [x for x in zip(L1, L2)]
print(result)


# list of zip items instead of tuples
result = [[x,y] for [x,y] in zip(L1, L2)]
print(result)

# combining two lists together using the zip() and map() 
L1 = [1,2,3]
L2 = [4,5,6]
result = [num**2 for num in map(sum, zip([1,2,3], [2,3,4]))]
print(result)

# filter() function
L = [1,2,3,4,5,6,7,8,9,10]
def is_even(num):
	if num % 2 == 0:
	    return True
result = filter(is_even, L)
print(result)

# alternatively with lambda function
L = [1,2,3,4,5,6,7,8,9,10]
result = filter((lambda x: x % 2 == 0), L)
print(result)



