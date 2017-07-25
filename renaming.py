###############################################
### Renaming Multiple PDFs according to CSV ###
###      Shaun Anderson - July, 2017        ###
###############################################

import os, glob

#store path to documents folder as a string
path = 'to rename'

students = []

#open file - student numbers should be in csv file called names in root directory
f = open('names.csv', 'r')

for line in f:
    students.append(line.strip())

f.close()

print(students)

files = os.listdir(path)
files.sort()

print(files)

x = 0

for i in students:
        os.rename(os.path.join(path, files[x]), os.path.join(path, i + '.pdf'))
        x = x + 1
