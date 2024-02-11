# Packing and unpacking of tuples
T = 1,2,3,4,5

# This is the same thing as:

T = (1,2,3,4,5)

a,b,c = 1,2,3

print(a)
print(b)
print(c)

# Unpacking when the list has more items than variables
T = (1,2,3)
num1, *num2 = T
print(num1)
print(num2)

T = (1,2,3)
*num1, num2 = T
print(num1)
print(num2)

# Dummy variables
_,a,b = (1,2,3)
print(a)
_,a,b,_ = (1,2,3,4)
print(a)
print(b)

