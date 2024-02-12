# binary data

print(type(b'hello'))

# looping unicode points of characters
data = b'hello'
for num in data:
	print(num)

# Decode Function
data = b'hello'
print(data.decode())

# using str() method
data = b'hello'
print(str(data, encoding='utf-8'))

