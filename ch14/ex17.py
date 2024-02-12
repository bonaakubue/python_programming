# Comparing values
class Square:
    def __init__(self, num):
        self.num = num**2

    def __gt__(self, val):
        #greater than
        result = False
        if self.num > val:
            result = True
        return result

    def __lt__(self, val):
        #less than
        result = False
        if self.num < val:
            result = True
        return result

#instantiating object
obj = Square(3)

print(obj > 5)
print(obj < 5)
