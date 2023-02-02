# password generator without using random.choice
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '?', '~']

print("Welcome to the Password Generator!")
n_letters = int(input('How many letters would you like in your password?'))
n_symbols = int(input('How many symbols would you like in your password?'))
n_numbers = int(input('How many numbers would you like in your password?'))

pw = []
for i in range(0, n_letters):
    pw.append(letters[random.randint(0, len(letters) - 1)])
for i in range(0, n_numbers):
    pw.append(numbers[random.randint(0, len(numbers) - 1)])
for i in range(0, n_symbols):
    pw.append(symbols[random.randint(0, len(symbols) - 1)])

final_pw = ""
for i in range(0, len(pw)):
    final_pw += pw[random.randint(0, len(pw) - 1)]

print("".join(pw))
print(final_pw)
