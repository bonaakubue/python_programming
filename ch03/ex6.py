# Bitwise operators

#bitwise and

num1 = 0b1101
num2 = 0b1011

result1 = bin(num1 & num2)
print(result1)

num3 = 0b100
num4 = 0b101

result2 = bin(num3 & num4)
print(result2)


#bitwise or

num5 = 0b1101
num6 = 0b1001

result3 = bin(num5 | num6)
print(result3)

num7 = 0b100
num8 = 0b101

result4 = bin(num7 | num8)
print(result4)


#bitwise xor

num9 = 0b1101
num10 = 0b1011

result5 = bin(num9 ^ num10)
print(result5)

num11 = 0b110111
num12 = 0b101011

result6 = bin(num11 ^ num12)
print(result6)


#bitwise not

num13 = 0b10
result7 = bin(~num13)
print(result7)


#bitwise leftshift

num14 = 0b1001

result8 = bin(num14 << 1)
print(result8)

result9 = bin(num14 << 2)
print(result9)

result10 = bin(num14 << 3)
print(result10)

#bitwise right shift

num15 = 0b1001

result11 = bin(num15 >> 1)
print(result11)

result12 = bin(num15 >> 2)
print(result12)

result13 = bin(num15 >> 3)
print(result13)

result14 = bin(num15 >> 4)
print(result14)
