#default parameters
def add(a=5, b=4):
    result = a + b
    return result

#providing arguments
result = add(1,2)
print(result)

#without providing arguments
result = add()
print(result)
