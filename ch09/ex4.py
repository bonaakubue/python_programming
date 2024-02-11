# Deleting items in a dictionary

# The del statement
subjects = {1: 'agriculture', 2: 'history', 3: 'government', 4: 'geography', 5: 'mathematics'}

del subjects[5]
print(subjects)

# The pop() method
subjects = {1: 'agriculture', 2: 'history', 3: 'government', 4: 'geography', 5: 'mathematics'}

subject = subjects.pop(2)
print(subject)
print(subjects)

# The popitem() method
subjects = {1: 'agriculture', 2: 'history', 3: 'government', 4: 'geography', 5: 'mathematics'}

item = subjects.popitem()
print(item)
print(subjects)
