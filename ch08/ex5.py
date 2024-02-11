# Built-in functions on tuples

# len() function
T1 = (1,2,3)
T2 = ('green', 'yellow', 'blue', 'red', 'purple')
print(len(T1))
print(len(T2))

# count() function
num = (1,2,3,4,4,3,1,2,5,7,2,5,2,1)
print(num.count(1))
print(num.count(2))
print(num.count(4))


# min() and max() function
L = (1,2,3,4,4,3,1,2,5,7,2,5,2,1)
min_value = min(L)
max_value = max(L)
print(min_value)
print(max_value)

# tuple() function
str_value = 'hello'
list_value = ['orange', 'banana', 'grape']
print(tuple(str_value))
print(tuple(list_value))

# index() function
L = (1,2,3,4,4,3,1,2,5,7,2,5,2,1)
print(L.index(1))
print(L.index(2))
print(L.index(3))
print(L.index(7))

