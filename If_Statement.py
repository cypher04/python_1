# if statements example

is_male = True
is_Tall = False

if is_male:
    print('you are male')
else:
    print('you are a female')

if is_male and not is_Tall:
    print('you are a male and not tall')
elif is_male and is_Tall:
    print('you are a correct human')