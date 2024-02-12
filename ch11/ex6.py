# *args and **kwargs

def func(*args):
    for arg in args:
        print(arg)
func('orange', 'purple', 'brown', 'red')

#**kwargs
def func(**kwargs):
    for key in kwargs:
        print(key, '=>', kwargs[key])
func(name='Eva', sex='male', age=9, nationality='France')
