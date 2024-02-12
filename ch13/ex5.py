# Bytearrays

data = b'hello'
b_data = bytearray(data)
print(b_data)

# Converting string to bytearray
b_data = bytearray('hello', 'utf-8')
print(b_data)

# to convert bytearray to string
data = bytearray('hello', 'utf-8').decode()
print(data)
