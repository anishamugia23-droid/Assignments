# 1. Index and Slicing
word = 'university'

print(word[0])
print(word[-1])
print(word[-3])
print(word[:4])
print(word[-4:])
print(word[::2])
print(word[::-1])


# 2. Split email

email = input('please enter your email:')
at_index = email.index('@')
username = email[:at_index]
domain = email[at_index + 1:]
dot_index = domain.index('.')
domain_part = domain[:dot_index]

print(username)
print(domain)
print(domain_part)


# 3

phone = input('please enter your phone number:')
clear_phone = phone.replace(' ', '').replace('-', '')
print (clear_phone)


# 4
title = input('please enter your title:')
title_lower = title.lower()
words = title_lower.split()
slug = '-'.join(words)
print(slug)



# 5
name = input('please enter your name:')
age = input('please enter your age:')
city = input('please enter your city:')
favorite_programming_language = input('please enter your favorite programming language:')

print('====================================')
print(f'name: {name.title()}')
print(f'age: {age}')
print(f'city: {city.title()}')
print(f'favorite_programming_language: {favorite_programming_language.upper()}')
print('====================================')
