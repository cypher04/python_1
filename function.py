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

numbers = [1, 2, 3, 20]

if x not in numbers:
    print(x not in numbers)


if x in numbers:
    print(x in numbers)







