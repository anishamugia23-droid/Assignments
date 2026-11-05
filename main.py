# 1. Data Type ()
age = 22
print(age)
print(type(age))

height = 1.68
print(height)
print(type(height))

name = 'Ani'
print(name)
print(type(name))

is_Female = True
print(is_Female)
print(type(is_Female))


# 2. Math Operations
print(12 + 3)
print(12 - 3)
print(12 * 3)
print(12 / 3)
print(13 // 3)
print(13 % 3)


# 3. String Manipulation
first_name = input('please enter  your name:')
last_name = input('please enter yor last name:')
full_name = first_name + ' ' + last_name

print(full_name)
print(full_name.lower())
print(full_name.upper())
print(full_name.capitalize())
print(full_name.title())


# 4. sep/end
print('Jan', 'Feb', 'Mar', 'Apr', sep = '/')
print('111', '222', '333', '444', sep = '<')
print('Ani', '22', 'Georgian', sep = '\t')

print('Ani', end = ' ')
print('is Georgian')
print('Ani', end = ' ')
print('is Georgian')


# 5. Comparison and Logical Operations
age = 22
print(age >= 20)
print(age, '> 18 =', age > 18)

height = 1.68
print(height >= 1.70)
print(height, '!= 1.68', height != 1.68)

print('height > 1.65 and age == 21 =', height > 1.65 and age == 21)
print('height > 1.65 and age < 25 =', height >1.65 and age <25)


# 6. input()
name = input('please enter your name:')
print('Hello', name + '!')
age = int(input('please enter your age:'))
print('Hello', name + '!' 'You are', age, 'years old' + '!')

















