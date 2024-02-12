# Working with CSV Files

# Reading CSV files
import csv
file = open('data.csv', 'r')
reader = csv.reader(file)
for row in reader:
	print(row)

# Writing CSV files
file = open('data.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow([1,2,3])
file.close()

# writerows() method
content = [['Fruit 1', 'Fruit 2', 'Fruit 3'], ['Apple', 'Orange', 'Mango']]

with open('data.csv', 'w', newline='') as file:
	writer = csv.writer(file, delimiter=',')
	writer.writerows(content)

# DictReader() method
file = open('data.csv', 'r')
reader = csv.DictReader(file)
for row in reader:
	print(row)


# DictWriter() method
labels = ['color1', 'color2']
file = open('data.csv', 'w', newline='')
writer = csv.DictWriter(file, fieldnames=labels)
writer.writeheader()

writer.writerow({'color1':'green', 'color2':'purple'})

writer.writerow({'color1':'orange', 'color2':'white'})
writer.writerow({'color1':'violet', 'color2':'red'})

file.close()

file = open('data.csv', 'r', newline='')
reader = csv.DictReader(file)

for row in reader:
	print(row)
