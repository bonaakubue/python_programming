# Built-in methods for dictionaries

# clear() method
D = {'name':'Andrew', 'age':23, 'married':False, 'colors':['red', 'green']}

D.clear()
print(D)

# copy() method
D1 = {'name':'Andrew', 'age':23, 'married':False, 'colors':['red', 'green']}
D2 = D1.copy()
print(D2)

# fromkeys() method
D = dict.fromkeys(['name', 'age', 'gender'], '-')
print(D)
D = dict.fromkeys(['name', 'age', 'gender'])
print(D)

# get() method
student = {'age': 21, 'gender': 'male'}
age = student.get('age')
gender = student.get('gender')
print(age)
print(gender)

# items() method
student = {'age': 21, 'gender': 'male'}
print(student.items())

# keys() method
student = {'age': 21, 'gender': 'male'}
print(student.keys())

# values() method
student = {'age': 21, 'gender': 'male'}
print(student.values())

# pop() method
D =  {'name': 'Kenny', 'age': 21, 'gender': 'male'}
person = D.pop('name')
print(person)
print(D)
age = D.pop('age')
print(age)
print(D)

# popitem() method
D =  {'name': 'Kenny', 'age': 21, 'gender': 'male'}
person = D.popitem()
print(person)
print(D)
person = D.popitem()
print(person)
print(D)

# setdefault() method
D =  {'name': 'Kenny', 'age': 21, 'gender': 'male'}
name = D.setdefault('name')
print(name)

level = D.setdefault('level')
print(level)
print(D)

complexion = D.setdefault('complexion', 'black')
print(complexion)
print(D)

# update() method
student = {'name': 'kevin', 'age': 21, 'gender': 'male', 'major': 'engineering'}
level  = {'year':2}
student.update(level)
print(student)

# enumerate() method
D = {'name':'Kenny', 'age':21, 'phone':'0903-843-9234', 
'major':'engineering'}

print(enumerate(D))
print(list(enumerate(D)))

#looping and printing the items
for item in enumerate(D):
	print(item)



