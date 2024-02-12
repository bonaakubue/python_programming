# Overloading arithmetic operators

class Numbers:
    def __init__(self, num):
        #define and assign value to the instance variable
        self.num = num**2

    def __add__(self, val):
        #addition
        return self.num + val

    def __sub__(self, val):
        #subtraction
        return self.num - val

    def __mul__(self, val):
        #multiplication
        return self.num * val

    def __truediv__(self, val):
        #division
        return (float(self.num) / val)

#instantiating object
obj = Numbers(3)
num = 2

#addition
result = obj + num
print(result)

#subtraction
result = obj - num
print(result)
#multiplication
result = obj * num
print(result)

#division
result = obj / num
print(result)

#overloading in reverse order.
obj = Numbers(3)
result = 4 + obj
print(result)

class Numbers:
    def __init__(self, num):
        #define and assign value to the instance variable
        self.num = num**2

    def __add__(self, val):
        #left addition
        return self.num + val

    def __radd__(self, val):
        #right addition
        return val + self.num

    def __sub__(self, val):
        #left subtraction
        return self.num - val

    def __rsub__(self, val):
        #right subtraction
        return val - self.num

    def __mul__(self, val):
        #left multiplication
        return self.num * val

    def __rmul__(self, val):
        #right multiplication
        return val * self.num

    def __truediv__(self, val):
        #left division
        return (float(self.num) / val)

    def __rtruediv__(self, val):
        #right division
        return (val / float(self.num))

#instantiating object
obj = Numbers(3)
num = 2

#addition
result = obj + num
print(result)

result = num + obj
print(result)

#subtraction
result = obj - num
print(result)

result = num - obj
print(result)

#multiplication
result = obj * num
print(result)

result = num * obj
print(result)

#division
result = obj / num
print(result)

result = num / obj
print(result)
