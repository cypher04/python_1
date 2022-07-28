# This is a program to tell random stories when run

import random

# we'll be using a list to contain the different data.

First_paragraph = ['Once upon a time there lived a man called Edet in Amsterdam', '20 years ago Edet lived in Amsterdam', 'Decades ago in Amsterdam, there was a man called Edet']
Second_paragraph = ['Edet loves to swim with his friends and family', 'The man prefer to play with his friends and family', 'The pool was all he would prefer to play in with his aquaintances']
Third_paragraph = ['I love Edet', 'He is a cool guy', 'Everyone loves him']

print(random.choice(First_paragraph) + random.choice(Second_paragraph) + random.choice(Third_paragraph))