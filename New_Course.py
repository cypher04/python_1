# Random examples

from math import *

# this will import all the functions in the math repo

my_num = -5
print(abs(my_num))

# Getting input from users

name = input ('Enter your name:')
print('hello' + name + 'welcome to this class, to confirm'
                       'you are not a robot, type yes')
confirm = input ('Yes/ No')
if confirm == 'yes':
    print('Welcome Human')
else:
    print('get out of here')
