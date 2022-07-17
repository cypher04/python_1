
# Working with Dictionary
person = {
    'firstname':'Olumide',
    'lastname':'maintain',
}

# to get a value
print(person.get('firstname'))

# add key value
person ['phone'] = 90888444777

# to copy dict
person2 = person.copy()

# to delete items
del(person2['phone'])
person.pop('lastname')

print(person2)

print(person)

# Getting Dict Keys
print(dict.keys(person))

# list of dictionaries
people = [
             {'name':'martha','age':30},
    {'name': 'egbon','age':40}
]

print(people)

# function is a block of code which only runs when it is called. In python, identation with tabs or spaces is what is used
def same(name2='igok'):
    print(f'hello{name2}')

