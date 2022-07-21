# JSON is commonly used with data APIS. here is how we can parse JSON into a python Dictionary

import json

userJSON = '{"first_name":"abey", "Last_name":"alinco", "age": 32}'
user = json.loads(userJSON)

print(user)

# printing as dictionary
print(user['first_name'])

# printing back to json from dictionary
car = {'make':'toyota', 'model':'camry', 'year':2022}
motor = json.dumps(car)
print(motor)

