# Looping a dictionary

#looping through the keys
subjects = {1: 'agriculture', 2: 'history', 3: 'government', 4: 'geography'}

for subject in subjects:
    print(subject)

#looping through the keys
for subject in subjects.keys():
    print(subject)

# Looping through value
subjects = {1: 'agriculture', 2: 'history', 3: 'government', 4: 'geography'}
for subject in subjects.values():
    print(subject)

#looping through the items
subjects = {1: 'agriculture', 2: 'history', 3: 'government', 4: 'geography'}

for subject in subjects.items():
    print(subject)

