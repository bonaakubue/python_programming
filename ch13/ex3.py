#writing to a file
file = open('data.txt', 'w')

for num in range(1,6):
    content = f'line {num}\n'
    file.write(content)

#appending to a file
file = open('data.txt', 'a')
content =  'line 6'
file.write(content)

#closing the file
file.close()

#file operations using with statement
with open('data.txt', 'w') as file:
    content = 'hello there!'
    file.write(content)
