# property as a decorator

def decorator_func(func):
    result = f'Output: {func()}'
    return result
@decorator_func
def func():
    return 'this is a function'

my_func = func
print(my_func)
