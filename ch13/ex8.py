# Copy files
import shutil
shutil.copy('data.txt', 'newfolder/data1.txt')

#move files
shutil.move('data.txt', 'newfolder')

#rename a file
import os
os.rename('data.txt', 'data2.txt')

#remove a file
os.remove('data2.txt')
