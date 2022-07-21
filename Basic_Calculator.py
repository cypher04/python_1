# Creating a simple calculator

num1 = input ('Enter the first number:')
op = input ('Enter operator:')
num2 = input ('Enter the second number')

if op == '+':
    ans = float(num1) + float(num2)
    print ('your answer is:', ans)

if op == '-':
    ans = float(num1) - float(num2)
    print ('your answer is:', ans)

if op == '*':
    ans = float(num1) * float(num2)
    print ('your answer is:', ans)

if op == '/':
    ans = float(num1) / float(num2)
    print ('your answer is:', ans)

if op == '%':
    ans = float(num1) % float(num2)
    print ('your answer is:', ans)
