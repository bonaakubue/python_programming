# testing
class Number:
    def __init__(self, val):
        #define and assign values to the instance variable
        self.value = val

    def add(self, val):
        #perform addition and result result
        result = self.value + val
        return result

    def subtract(self, val):
        #perform subtraction and return result
        result =  self.value - val
        return result

    def multiply(self, val):
        #perform multiplication and return result
        result = self.value * val
        return result

    def divide(self, val):
        #perform division and return result
        result = self.value / val
        return result


import unittest
class NumberTestCase(unittest.TestCase):
    def test_add(self):
        #testing the add method
        number =  Number(10)
        val = 10
        output = 20
        result = number.add(val)
        self.assertEqual(result, output)

    def test_subtract(self):
        #testing the subtract method
        number =  Number(10)
        val = 10
        output = 0
        result = number.subtract(val)
        self.assertEqual(result, output)

    def test_multiply(self):
        #testing the multiply method
        number =  Number(10)
        val = 10
        output = 100
        result = number.multiply(val)
        self.assertEqual(result, output)

    def test_divide(self):
        #testing the divide method
        number =  Number(10)
        val = 10
        output = 1
        result = number.divide(val)
        self.assertEqual(result, output)

#running the unit tests
unittest.main()
