# Reading files

#reading file contents
file = open('data.txt', 'r')

#read method
content = file.read()
print(content)

#readlines method
content = file.readlines()
print(content)

#readline method
content = file.readline()
for line in content:
    print(line)


