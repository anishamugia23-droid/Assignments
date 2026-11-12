# 1
number = 1

while number <= 50:
    if number % 2 == 0:
        print(number)
    number += 1


# 2
n = int(input('Enter N: '))

total = 0
i = 1

while i <= n:
    total += i
    i += 1

print(f'Sum: {total}')


# 3
n = int(input('Enter n: '))

factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print(f'{n}! = {factorial}')


# 4
count = 0
total = 0

while True:
    number = int(input('Enter a number: '))
    if number == 0:
        break
    total += number
    count += 1

print(f'Count: {count}')
print(f'Sum: {total}')

if count > 0:
    print(f'Average: {total / count}')
else:
    print('Average: 0')


# 5
secret = 7
attempts = 0
max_attempts = 5
guessed = False

while attempts < max_attempts and not guessed:
    guess = int(input('Guess: '))
    attempts += 1

    if guess > secret:
        print('Too high')
    elif guess < secret:
        print('Too low')
    else:
        print('You win!')
        guessed = True

if not guessed:
    print(f'You lose! The number was {secret}')
