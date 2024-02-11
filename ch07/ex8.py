# List comprehension
nums = [1,2,3,4,5]
squares = [num**2 for num in nums]
print(squares)

# conditionals in a list comprehension

L = [1,2,3,4,5,6,7,8,9,10]
numbers = [num for num in L if num % 2 == 0]
print(numbers)

# odd numbers
numbers = [num for num in L if num % 2 != 0]
print(numbers)

# characters in a string
chars = [char for char in 'hello']
print(chars)

#filtering
result  = [num*2 for num in range(4) if num > 1]
print(result)

# Using list comprehension to create nested lists
L = [1,2,3,4,5]
squares = [[num, num**2] for num in L]
print(squares)

# nested comprehension
L = [[1,2], [3,4], [5,6]]
result = [[x[i] for x in L] for i in range(2)]
print(result)

