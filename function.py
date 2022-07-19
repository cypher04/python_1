# function is a block of code which only runs when it is called. In python, identation with tabs or spaces is what is used

#create function
def samehi(name):
    print(f'hello {name}')
samehi('igol')

# return values
numb1 = 87; numb2 = 22
def getSum():
    total = numb1 + numb2
    return total

print(getSum())

#lambda function is a small anonymous function
# A lambda function can take an number of arguments, but can only have one expression.

getSum = lambda num1, num2 : num1 + num2

print(getSum(10, 5))

#Conditionals
#if/else conditions are used to decide to do something based on something being true or false

x = 10
y = 20

# Comparison Operators (==, !=, >, <, >=, <=) are used to compare values
if x < y:
    print(f'{x} is less than {y}')
elif x > y :
    print(f'{x} is more than {y}')
elif x == y :
    print(f'{x} equals to {y}')
else:
    print(f'invalid expressionale')

# Using Logical operators (and, or not) - used to combine conditional statements

# and
if y > x and y > 3:
    print(f'this is the greatest {y}')

# or

if y < x or y <= 50:
    print(f'{y} is maddt')

# not
if not(x == y):
    print(f'{x} is not equal to {y}')

# membership operators (not, not in_ - membership operators are used to test if  a sequence is presented in an object
# With these operators you get aa boolean as a response
numbers = [1, 2, 3, 20]

if x not in numbers:
    print(x not in numbers)


if x in numbers:
    print(x in numbers)

# identity operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
# With these operators you get aa boolean as a response

if x is not numbers:
    print(x is not numbers)


# LOOPS
# for loops are used for iterating over a sequence (that s either a list, a tuple, a dictionary, a set, or a string.

# A simple for loop
people = ['john', 'Kate','tesse', 'agnes']

for person in people:
    print(f'Current in person:{person}')

# Break
for person in people:
    if person == 'tesse':
        break
    print(f'Current in person:{person}')

# Continue (this is also known as skip)
for person in people:
    if person == 'tesse':
        continue
    print(f'Current in person:{person}')

#range
for i in range(len(people)):
    print(people[i])

# Custom Range
for i in range(1,3):
    print(f'{i}')


# While Loops execute a set of statements as long as a condition is true

count = 0

while count < 20:
    print(f'count is:{count}')
    count +=1

# A module is basically a file containing a set of functions to include in you application.
# There are core python modules, modules you can install using the pip package manager

import time
from datetime import date

today = date.today()
print(today)

timestamp = time.time()
print(timestamp)

# creating custom modules
from mymodule import greeting

name = 'onyinye'
print(greeting(name))




