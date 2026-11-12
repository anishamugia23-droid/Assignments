# 1
number = int(input('enter the number:'))

if number % 2 == 0:
    print('even number')
else:
    print('odd number')


# 2
age = int(input('Please enter your age:'))

if age <= 0:
    print('invalid age')
elif age <= 12:
    print('child')
elif age <= 17:
    print('teenager')
elif age <= 64:
    print('adult')
else:
    print('senior')


# 3
grade = int(input('Please enter your grade:'))

if grade <= 0 or grade > 100:
    print('invalid number')
if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
elif grade >= 50:
    print('E')
else:
    print('F')


# 4
answer = input('Do you like Python?').strip().upper()

if answer == 'YES':
    print('Great!')
elif answer == 'NO':
    print('Maybe you will like it later')
else:
    print('please answer yes or no')


# 5
num1 = float(input('Please enter your first number:'))
operation = input('Please enter your operation:').strip()
num2 = float(input('Please enter your second number:'))

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    if num1 != 0:
        print('cannot divide by zero')
else:
    print('invalid operation')






