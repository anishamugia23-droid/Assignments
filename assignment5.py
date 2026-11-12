age = int(input('please enter your age:'))
money = int(input('please enter your amount:'))
ticket_price = 15

if age >= 12 and money >= ticket_price:
    print('Enjoy the movie!')
else:
    print('Access denied')


# 2
year = int(input('please enter the year:'))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('leap year')
else:
    print('not a leap year')


# 3
correct_PIN = 1234
balance = 500

PIN = int(input('please enter your PIN:'))
amount = int(input('please enter the Amount:'))

if PIN == correct_PIN:
    if amount <= 0:
        print("Invalid amount")
    elif amount > balance:
        print("Not enough money")
    else:
        balance -= amount
        print(f"Take your money: {amount}")
        print(f"New balance: {balance}")
else:
    print("Wrong PIN")


# 4
try:
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    number = int(input("Enter a number to divide 100 by: "))
    print("100 /", number, "=", 100 / number)
    print(f"Hello, {name}! Next year you will be {age + 1} years old.")
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
except TypeError:
    print("Cannot join text and number")
except Exception as e:
    print(e)
