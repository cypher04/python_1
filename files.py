# python has functions for creating, reading, updating and deleting files

#opening a file

with open('readmeeeeee.txt', 'w') as f:
    f.write('Create a new text file!')

# to append to the file

with open('readmeeeeee.txt', 'a') as f:
    f.write('Look at me now!')

#to handle file error exception

try:
    with open('docs/readme.txt', 'x') as f:
        f.write('Create a new text file!')
except FileNotFoundError:
    print("The 'docs' directory does not exist")

# to get some info
print('name:', f.name)
print('is closed: ', f.closed)
print('mode: ', f.mode)

# to read from a file
f = open('readmeeeeee.txt', 'r+')
all = f.read()
print(all)
