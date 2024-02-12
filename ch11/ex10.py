# Generator Expressions
squares = (x ** 2 for x in range(1, 5))
for square in squares:
    print(square)


#Generating odd numbers using a generator expression
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_nums = (num for num in numbers if num % 2 != 0)
for num in odd_nums:
    print(num)
