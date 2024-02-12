#try-except block
try:
    file =  open('data.txt')
    result = file.read()
    print(result)
except:
    print('something went wrong!')

#catching a specific exception
try:
    result = input()
    print(result)
except ValueError as e:
    print(e)

# Handling multiple exceptions
try:
    result = input()
    print(result)
except ValueError:
    print('Invalid input')
except ZeroDivisionError:
    print('Division by zero not allowed.')

# else block
try:
    result = 6 * 3
    print(result)
except:
    print('an exception occurred!')
else:
    print("No exceptions occurred!")


#finally block
try:
    file =  open('data.txt')
    result = file.read()
    print(result)
except:
    print('an exception occurred!')
finally:
    file.close()
