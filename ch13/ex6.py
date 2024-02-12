# Writing binary data to file
data = b'hello'
file = open('data.txt', 'wb')
file.write(data)
file.close()
file = open('data.txt', 'rb')
output = file.read()
print(output)

