# Comprehension in dictionaries
result = {num:num**2 for num in [1,2,3,4]}
print(result)

# with zip() function
D = {x for x in zip([1,2,3], [4,5,6])}
print(D)
