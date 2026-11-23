# 1
for i in range (1, 11):
    print(f'{i} squared = {i ** 2}')

for i in range (10, 0, -1):
    print(i)
print('go!')

total = 0
for i in range (2, 101, 2):
    total += i
print(total)


# 2
text = input('Enter text:')
count = 0

for ch in text.lower():
    if ch in 'aeiou':
        count += 1
print(f'Vowels: {count}')


# 3
total = 0
count = 0

while True:
    user_input = input('enter a number:')
    if user_input == 'stop':
        break

    number = int(user_input)

    if number < 0:
        print('negative numbers are not allowed')
        continue

    total += number
    count += 1

print(f'Sum: {total}')
print(f'Count: {count}')


# 4
n = int(input('enter n:'))

for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print()

print ()

for i in range (n, 0, -1):
    for j in range(i):
        print('*', end='')
    print()




