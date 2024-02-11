# Standard string formatting specifiers
S = 'Hello there %s' % 5
print(S)

S = 'Hello there %s' % '5'
print(S)
S = 'Hello there %d' % 5
print(S)
S = 'Hello there %f' % 5
print(S)
S = 'Hello there %c' % '5'
print(S)

# Precision
S = 'Hello there %.2f' % 5
print(S)
S = 'Hello there %.5f' % 5
print(S)


# Width
S = '%d oranges' % 5
print(S)
S = '%5d oranges' % 5
print(S)
S = '%05d oranges' % 5
print(S)
S = '%10s oranges' % 'apple'
print(S)

# Fill
S = '%05d oranges' % 5
print(S)
