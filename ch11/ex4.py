#positional arguments
def add(a, b):
    result = a + b
    return result

result = add(10, 5)
print(result)

#keyword arguments
def add(a, b):
    result = a + b
    return result

result = add(b=2, a=7)
print(result)

# keyword and positional arguments
def add(a, b, c):
    result = a + b + c
    return result

result = add(1, c=3, b=5)
print(result)
