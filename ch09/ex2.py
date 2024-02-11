#accessing items in a dictionary
subjects = {1:'chemistry', 2:'history', 3:'government', 
4:'geography', 5:'mathematics' }

#using slicing operator
subject = subjects[1]
print(subject)

#using get method
subject = subjects.get(3)
print(subject)

#updating items in a dictionary
subjects[1] = 'agriculture'
print(subjects)
