# Rules of Operator Precedence

result = 2 + 2 - 2 * 2 / 2 ** 2 % 2
print(result)
#using parenthesis to confirm precedence
result = 2 + 2 - ((2 * (2 / (2 ** 2))) % 2)
print(result)
