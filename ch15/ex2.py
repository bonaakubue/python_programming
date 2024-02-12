#raise an exception
num = int(input())
if num < 0:
        raise ValueError("You cannot use a negative number.")

try:
    num = -2
    if num < 0:
        raise ValueError("You cannot use a negative number.")
except ValueError as e:
    print(e)
