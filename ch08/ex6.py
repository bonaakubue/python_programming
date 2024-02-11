# Named Tuples

from collections import namedtuple

numbers = namedtuple('number', ['a', 'b', 'c'])
even = numbers(2,4,6)
numbers(a=2, b=4, c=6)
for i in even: 
    print(i)


print(even.a)
print(even.b)
print(even.c)
print(even[2])
